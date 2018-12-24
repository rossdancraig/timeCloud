# timeCloud
Django-based website and Android app to record and visualise 
how users spend their time.

## Installing Tools and Packages
1) First make sure you have Python and pip3 installed:
```
sudo apt-get update
sudo apt-get install python3.6
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1
sudo apt-get -y install python3-pip
```
Verify that they were installed correctly:
```
python --version 
pip3 --version 
```


2) Create a virtual environment to keep consistent environment
variables and tool versions:
```
sudo apt install virtualenv
virtualenv --python=`which python3` [VIRTUAL_ENV_NAME]
source [VIRTUAL_ENV_NAME]/bin/activate
```
To get out of virtualenv simply type `deactivate` in terminal.


3) Once inside your virtualenv, install Django (web framework) and 
Postgres (database mananger) and Python packages:
[Postgres Installation Instructions](https://www.postgresql.org/download/)

```
sudo apt-get install postgresql libpq-dev postgresql-client postgresql-client-common postgresql-contrib
pip install psycopg2 psycopg2-binary
pip install Django
```
Check that Django was installed correctly:
```
python -m django --version
```

## Configuring a new App and Database
The following is a summary of steps taken from the 
[Official Django Beginner Tutorial](https://docs.djangoproject.com/en/2.1/intro/).
Be sure to first enter into your virtual environment from earlier.

```
django-admin startproject [PROJECT_NAME]
```

From the `PROJECT_NAME` dir you can run `python manage.py runserver` and view the 
result on your browser (see terminal result for instructions).



```
python manage.py startapp [APP_NAME]
```

[Configure Postgres and create a database](https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-DATABASES)
[Configure the  `PROJECT_NAME/settings.py`](https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-DATABASES) 
file to use this database and update `TIME_ZONE` (ex: `America/Toronto`)
Also add this line to the `INSTALLED_APPS` paths 
(see `APP_NAME/apps.py` file for exact auto-generated Config class name):
```
'APP_NAME.apps.AppNameConfig',
```

```
python manage.py migrate
```

## Models and Migrations
### Models
I will talk more about models in the next section, but for now just know 
that the `mysite/event_recorder/models.py` file includes the following:

* Category([ID], name, parent)
* Relation([ID], name)
* Person([ID], first_name, last_name, relations, approx_DOB, gender)
* Event([ID], start_time, end_time, description, categories, people, notes)
* Rating([ID], event, enjoyment, productivity)

### Migrations
At each update to the model, run updates onto Django migration edit files, then migrate
them to the databse:
```
python manage.py makemigrations event_recorder
python manage.py sqlmigrate event_recorder [NUMBER]
python manage.py migrate
```

The second command doesn't make any actual changes it's just optional if you want
to check what the SQL command code would look like in updating the database.

## Admin
Create a bunch of model instances and save it onto your database by
entering `python manage.py shell`. 

Create a superuser:
```
python manage.py createsuperuser
Username: [ADMIN_NAME]
Email address: [ADMIN_EMAIL]
Password: [ADMIN_PASSWORD]
```

Add models to `[APP_NAME]/admin.py`
Play around however you like using the default Django admin site by
running the server and going to whatever the admin path is in the 
`mysite/urls.py` file.

## How files all work together: Model-View-Template 
### Overview
In the `[APP_NAME]` directory, you will see the following files/dirs:
```
models.py
urls.py
views.py
templates/\*.html
static/\*
```
The basic idea is a user accesses a new URL on our website either directly
(typing an internet address) or indirectly (ex: clicking on a button). 
When this happens, the `urls.py` file parsing the URL to an API function
from the `views.py` file. Depending on the function, the `views.py` 
sends an HTTP request to the associated `template/*` file along with 
any relevant database objects defined in the `models.py` file. The template
file dynamically renders the HTML page based on the model object and 
relevant `static/*` file that helps define the look of the webpage.
Once this HTML file is rendered, it sends it as a response back to the 
view function which returns it to your browser (that's why it's called a 
view file - your browser is 'viewing' the returned contents). 

### models.py
We've already defined our models in the `models.py` file. It tells our
database how each object should be stored (ie: what fields it owns, which
fields are required, the default value of fields, etc) as well as how
each object is connected to other object. 

Ex: The `Event` model has a `people` field defined as a
`ManyToManyField` with the `Person` model. This means that any event 
object can have an unlimited number of person objects associated with it
while any person object can also have an unlimited number number of 
associated events. 

For more details on OneToMany (ForeignKey), OneToOne and ManyToMany 
relationships, I found 
[this Stack Overflow
](https://stackoverflow.com/questions/19641841/django-difference-between-one-to-one-many-to-one-and-many-to-many)
answer pretty useful.


### urls.py
This is where we define the 'links' between a URL that a user types 
into a browser and the subsequent API call invoked to our server.

Ex: For this line:
```
path('events/', views.EventIndexView.as_view(), name='events-index')
```
if a user enters `[ROOT_WEBSITE_PATH_DEFINED_IN_MYSITE/URLS.PY]/events/`
this tells our server that it needs to run the
`EventIndexView.as_view()` command found in the `views.py` file. The 
extra parameter `name='events-index` will be useful for referencing this
browser link later in our `template/*` files without explicitly having
to refer back to the URL string. This is good because in the future we
might want to change the URL string and as long as the name remains the 
same we won't need to edit every single reference to it in all the
template files.

### views.py
Yea there's a bunch of stuff "under the hood" that Django takes care
of you here with it's 5 different classes of generic views (I've also
included the typical template file name which you would call to when
using each specific view class):

1) **ListView**: `index.html` - seeing many (or all) model instances 
2) **DetailView**: `detail.html` - seeing one specific model instance
3) **CreateView**: `create.html` - creating a new model instance
4) **UpdateView**: `update.html` - editing an existing model instance
4) **DeleteView**: `delete.html` - deleting an existing model instance

There are a few more but those are the most commonly used. To see more
check out the [official documentation](https://docs.djangoproject.com/en/2.1/ref/class-based-views/)

By the way, you don't _HAVE_ to name the template files `index.html` or
`detail.html` like I did (you define the template name in the view 
class) but it's pretty intuitive if you do and everyone
will know what you're talking about.

In most cases, you will need to define these parameters in each
class:
1) `model`
2) `template_name`
3) `context_object_name` (optional but recommended for index views)

it's pretty straightforward: `model` tells the template defined in the 
`[APP_NAME]/template/[template_name]` file which model to use. 

The `context_object_name` tells the template the "name" of the variable.
For webpages dealing with individual model instances (ie: non-index views)
the default context_object_name is just the model name itself (ex: if you 
said `Model = Event` then you can just call `event` in special squiggly
brackets in the template view and it knows what you're talking about since
the detail view also passes in an `id` in the URL. For index views, the 
default context_object_name is `[MODEL_NAME]_list`.

### templates/\*.html
Lol pretty tired not I'll talk about this later but it's probably the
least difficulty part to understand. Basically just dynamically
renders an HTML 'script' into final static HTML that you see whenever
you click 'Inspect Element' on a website.

### static/\*
Can include anything from .css files defining the main look of the website
to image files, sound recordings, etc. It's called 'static' because in 
contrast to 'dynamic' components of a web page, these files are all 
pre-built and never change or get updated based on the user's web session.
They might appear altered or used differently by the template files,
but the content itself that is stored here always remains the same. 

Again, you don't _HAVE_ to follow this convention (you could store your
template files here if you really wanted to and just call them from the 
views function) but that would just be confusing to everyone trying
to understand the website design so don't do that.

### One last thing I haven't talked about is .forms but I'll do that another time
