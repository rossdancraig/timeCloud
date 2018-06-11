#Basic PostgreSQL Instructions

#Background for more info: 
Setting up database: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04
Moving database to git directory: https://www.digitalocean.com/community/tutorials/how-to-move-a-postgresql-data-directory-to-a-new-location-on-ubuntu-16-04

#1) Creating a database on your computer
Ubuntu: 
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib

Windows:
Don't know Adam please install and fill this in.

Essentially this installs postgres and creates the default user "postgres".
To access the database, type:

sudo -i -u postgres psql

When inside the postgres environment, you can type the follwing commands:

\d (describe): see the description of all tables in the database
\i (import) [FILE_NAME]: execute a file that typically runs postgres commands
\q (quit): exit the postgres environment

Also, you can type in the basic commands directly on postgres (similar to Python):
Example:

CREATE TABLE playground (
    equip_id serial PRIMARY KEY,
    type varchar (50) NOT NULL,
    color varchar (25) NOT NULL,
    location varchar(25) check (location in ('north', 'south', 'west', 'east', 'northeast', 'southeast', 'southwest', 'northwest')),
    install_date date
);

or 

SELECT [columns]
FROM [table]
WHERE [condition on data to include row in table in result];

##Actually just ignore the rest of this part it's just extra and unnecessary
##Key takeaway, as long as you have postgres installed on your system you can
##just run the sql scripts and get the same result

#2) Moving data directory to git folder
Login to postgres (sudo -u postgres psql) and type:

SHOW data_directory; (1)

Remember the result and quit (\q). In my case, I get the result 
"/var/lib/postgresql/10/main". If you have data in your postgres data_directory,
you need to shut down postgres for data integrity purposes:

sudo systemctl stop postgresql

Check that the shut down succeeded by typing this and seeing if server has stopped:

sudo systemctl status postgresql

Copy existing database directory to wherever you want to mount it. 
IMPORTANT: Be sure there is no trailing slash on the directory, 
which may be added if you use tab completion. When there’s a trailing slash, 
"rsync" command will dump the contents of the directory into the mount point 
instead of transferring it into a containing PostgreSQL directory. After this is
done, create a backup of the database in the old default directory:

sudo rsync -av /var/lib/postgresql ~/baller_boys/postgres
sudo mv /var/lib/postgresql/10/main /var/lib/postgresql/10/main.bak

Now we need to edit the postgres configuration file to change the data 
directory to point to the new place we moved it to:

data_directory = '~/baller_boys/postgres'

Finally, you need to restart postgres to apply the changes:

sudo systemctl start postgresql
sudo systemctl status postgresql

Log into postgres (sudo -u postgres psql) and check the data directory:

SHOW data_directory;

If everything is good, you can delete the backup dir and restart:

sudo rm -Rf /var/lib/postgresql/10/main.bak
sudo systemctl restart postgresql
sudo systemctl status postgresql
