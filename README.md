Start here if you are a new developer on the team and want to setup your local development environment.

### Technologies and Tools Used

#### Back-End
- Python = 3.4
- Django = 1.10
- PostgreSQL = 9.4

#### Front-End
- HTML
- CSS
- Javascript

#### IDE of preference
- PyCharm
- Sublime

#### Server Side
- Ubuntu 14.0.4
- Vagrant
- Virtual Box
- GIT
- Nginx/Gunicorn

### Installing required software

1. Install Vagrant (Go to: http://www.vagrantup.com/downloads.html)
2. Install Virtual Box (Go to: https://www.virtualbox.org/wiki/Downloads)
3. Install GIT, including command line options. (Go to: http://git-scm.com/downloads)
4. Install Python 3.4 (Go to: https://www.python.org/)


### Cloning the code

1. Clone the GIT Repository using the following command:
    `git clone https://github.com/humbertomn/wannamigrate.git ~/wannamigrate`

    PS: If you want to install anywhere on your system, change the path: "~/wannamigrate"

2. To start up your virtual environment, run the following command:
    ```
    cd ~/wannamigrate/infra
    vagrant up
    ```
    Vagrant is configured to use the ports 2222, 8085, 8181 and 4443, so make sure they are free to be used.

3. If you see an error message that starts with 'Failed to mount folders in Linux guest' run the following commands:
    ```
    vagrant ssh
    sudo groupadd wannamigrate-dev
    sudo usermod -a -G wannamigrate-dev vagrant
    sudo usermod -a -G wannamigrate-dev www-data
    exit
    vagrant reload
    ```

4. Run the following command to configure your environment (Make sure you're still in the 'infra' folder).
    `python helper.py config site on local with database`

    The helper.py script will install all needed packages on your local environment, such as apache, git and also a local postgresql database. It will ask to you the root's password for the database (Choose one that is good to you. We will use "88uhGLua19UOSAmav" for the initial setup).


### Installing the database
1. Connect to the virtual machine via SSH:
    `python helper.py connect local` or `vagrant ssh`

2. Start the service and connect to the PSQL command interface
     ```
    sudo service postgresql start
    sudo su - postgres
    psql
    ```
    
3. Create the database 'wannamigrate' and the user 'wannamigrate':
    ```
    CREATE DATABASE wannamigrate;
    CREATE USER wannamigrate WITH PASSWORD 'uhaRYush72ogHau37iO920';
    ALTER ROLE wannamigrate SET client_encoding TO 'utf8';
    ALTER ROLE wannamigrate SET default_transaction_isolation TO 'read committed';
    ALTER ROLE wannamigrate SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE wannamigrate TO wannamigrate;
    ALTER USER postgres WITH PASSWORD 'Ujs82Z81kIeB27Haaao82jdI90O3u333';
    \quit
    exit
    ```

4. Adjust pgsql pg_hba settings
    ```
    sudo vi /etc/postgresql/9.3/main/pg_hba.conf

    # 1- Change values ‘ident’ and ‘peer’ to ‘md5’

    # 2- If on local, change line with IP 127.0.0.1/32 to IP 0.0.0.0/0

    sudo service postgresql restart
    ```

5. Activate your python virtualenv and run a 'migrate' inside your django application:
    ```
    source /wannamigrate/src/wannamigratevenv/bin/activate
    python /wannamigrate/src/manage.py migrate
    ```

6. Create a superuser to be able to access the admin area
    ```
    source /wannamigrate/src/wannamigratevenv/bin/activate
    python /wannamigrate/src/manage.py createsuperuser
    ```


### Testing
To make sure it works open up [http://localhost:8087/]
