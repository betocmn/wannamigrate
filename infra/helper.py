#!/usr/bin/python
import sys, getopt, os, subprocess, re, time, datetime


##############################
# Configurations
##############################

# Servers' info
SERVERS = {
    # Local server
    "local": {
        "IP": "localhost",
        "DOMAIN": "localhost",
        "KEYPAIR": "",
        "DEFAULT_USER": "vagrant",
        "HTTP_PORT": 80,
        "HTTPS_PORT": 443,
        "HTTP_FORWARDED_PORT": 8087,
        "HTTPS_FORWARDED_PORT": 4443,
        "BRANCH": "master",
    },

    "prod": {
        "IP": "54.179.156.171",
        "DOMAIN": "wannamigrate.com",
        "KEYPAIR": "wanna-singapore-production.pem",
        "DEFAULT_USER": "ubuntu",
        "HTTP_PORT": 80,
        "HTTPS_PORT": 443,
        "HTTP_FORWARDED_PORT": 80,
        "HTTPS_FORWARDED_PORT": 443,
        "BRANCH": "master",
    },

    "staging": {
        "IP": "",
        "DOMAIN": "",
        "KEYPAIR": "",
        "DEFAULT_USER": "ubuntu",
        "HTTP_PORT": 80,
        "HTTPS_PORT": 443,
        "HTTP_FORWARDED_PORT": 80,
        "HTTPS_FORWARDED_PORT": 443,
        "BRANCH": "master",
    }
}

# Global settings
GIT_REPO = "https://github.com/humbertomn/wannamigrate.git"
DEPLOYMENT_ROOT = ""  # Root folder for deploying web projects (Leave empty for a single project)
PROJECT_ALIAS = "wannamigrate"
APP_NAME = "wannamigrate"
SOURCE_ALIAS = "src"
GUNICORN_ALIAS = "gunicorn"

# Packages to be installed for django applications
LINUX_DEV_PACKAGES = [
    "python3-dev", "git", "python-psycopg2", "libpq-dev", "postgresql", "postgresql-contrib",
    "nginx", "gettext", "libjpeg-dev", "rabbitmq-server", "supervisor", "stripe", "pendulum"
]

# Virtualenv packages
VIRTUALENV_PACKAGES = [
    "django==1.9.10",
    "django-stdimage==2.3.3",
    "pytz==2016.6.1",
    "requests==2.11.1",
    "celery==3.1.23",
    "gunicorn==19.6.0",
    "psycopg2==2.6.2",
    "pendulum==0.6.2",
    "stripe==1.38.0",
    "django-compressor==2.1",
    "csscompressor==0.9.4",
    "beautifulsoup4==4.5.1",
    "lxml==3.6.4",
    "slimit==0.8.1",
    "html5lib==0.999999999",
    "django-htmlmin==0.10.0",
    "analytics-python==1.2.5",
    "sendgrid==3.6.3"
]


#############################################
# PRE-CALCULATED CONFIGURATIONS (NOT RECOMMENDED TO MODIFY)
#############################################

# Pre-calculate the available servers regex pattern
AVAILABLE_SERVERS_PATTERN = '(' + '|'.join(sorted(SERVERS.keys())) + ')'

# Project root and virtualenv
PROJECT_ROOT = DEPLOYMENT_ROOT + '/' + PROJECT_ALIAS
SOURCE_ROOT = PROJECT_ROOT + '/' + SOURCE_ALIAS
PROJECT_VIRTUALENV = SOURCE_ROOT + '/' + PROJECT_ALIAS + "venv"
DATABASE_BACKUP_FOLDER = '/database_backup'

# Apache's default user
NGINX_DEFAULT_USER = "www-data"

# User group for the project
DEFAULT_USER_GROUP = PROJECT_ALIAS + "-dev"

# Gunicorn and Nginx configurations folder
GUNICORN_UPSTART_PATH = '/etc/init'
NGINX_SITES_ENABLED_PATH = "/etc/nginx/sites-enabled"
NGINX_SITES_AVAILABLE_PATH = "/etc/nginx/sites-available"

# Spacing for help messages.
N_DEFAULT_HELP_SPACING = 15


# Requires formatting on the fly. Params:
# http_port, https_port, www_domain, pt_domain, source_root, app_name, https_forwarded_port
GUNICORN_CONF = """description 'Gunicorn application server handling {app_name}'

start on runlevel [2345]
stop on runlevel [!2345]

respawn
setuid {default_user}
setgid {default_user_group}
chdir {source_root}

exec {project_alias}venv/bin/{gunicorn_alias} --workers 3 --bind unix:{source_root}/gunicorn.sock {app_name}.wsgi:application
"""

NGINX_CONF = """
server {{
    listen 80;
    server_name {www_domain};

    # For pre-compressed copies (.gz)
    gzip_static on;

    # Apple icons
    location ^~ /apple-touch-icon {{
        root {source_root}/static/site/img/favicon;
        access_log off;
        log_not_found off;
    }}

    # Favicon
    location = /favicon.ico {{
        root {source_root}/static/site/img/favicon;
        access_log off;
        log_not_found off;
    }}

    # Robots.txt
    location = /robots.txt {{
        root {source_root}/static/site/seo;
        access_log off;
        log_not_found off;
    }}

    # Site Map
    location = /sitemap.xml {{
        root {source_root}/static/site/seo;
        access_log off;
        log_not_found off;
    }}

    # Cache - cache.appcache, your document html and data
    location ~* \.(?:manifest|appcache|html?|xml|json)$ {{
        root {source_root};
        expires -1;
    }}

    # Cache - Media: images, icons, video, audio, HTC
    location ~* \.(?:jpg|jpeg|gif|png|pdf|ico|cur|gz|svg|svgz|mp4|ogg|ogv|webm|htc)$ {{
        root {source_root};
        expires 1M;
        access_log off;
        add_header Cache-Control "public";
    }}

    # Cache - CSS and Javascript
    location ~* \.(?:css|js)$ {{
        root {source_root};
        expires 1y;
        access_log off;
        add_header Cache-Control "public";
    }}

    # Static html/css/img
    location /static/ {{
        root {source_root};
    }}

    # User Uploads
    location /upload/ {{
        root {source_root};
    }}

    # Forward everything else to Django
    location / {{
        include proxy_params;
        proxy_pass http://unix:{\}/gunicorn.sock;
    }}
}}
"""

CELERY_WORKER_CONF = """
; ==================================
;  celery worker supervisor
; ==================================

[program:celery]
; Set full path to celery program if using virtualenv
command={project_virtualenv}/bin/celery worker -A {app_name} --loglevel=INFO

user={default_user}
directory={source_root}
numprocs=1
stdout_logfile=/var/log/celery/worker.log
stderr_logfile=/var/log/celery/worker.log
autostart=true
autorestart=true
startsecs=10

; Need to wait for currently executing tasks to finish at shutdown.
; Increase this if you have very long running tasks.
stopwaitsecs = 600

; When resorting to send SIGKILL to the program to terminate it
; send SIGKILL to its whole process group instead,
; taking care of its children as well.
killasgroup=true

; if rabbitmq is supervised, set its priority higher
; so it starts first
priority=1000
"""

CELERY_BEAT_CONF = """
; ==================================
;  celery beat supervisor
; ==================================

[program:celerybeat]
; Set full path to celery program if using virtualenv
command={project_virtualenv}/bin/celery beat -A {app_name} --schedule /celery_schedule/beat.db --loglevel=INFO

; remove the -A myapp argument if you are not using an app instance

directory={source_root}
user={default_user}
numprocs=1
stdout_logfile=/var/log/celery/beat.log
stderr_logfile=/var/log/celery/beat.log
autostart=true
autorestart=true
startsecs=10

; if rabbitmq is supervised, set its priority higher
; so it starts first
priority=999
"""


########################################################################
# PUBLIC METHODS
# If you want to add a new method, please follow the pattern existant
# in other methods (Regex to check usage at beginning, method help if
# usage wont match, etc).
########################################################################
def config(args):
    """
        Usage: python helper.py config <feature> on <server> (with database)
        Installs the desired app on the remote.
        :args: A string indicating the server to run the update.
    """

    # The usage regex.
    usage_pattern = "^(site) on {0}(with database)?$".format(AVAILABLE_SERVERS_PATTERN)
    cmd_str = " ".join(args)

    # Checks if the user typed the command correctly
    if not re.match(usage_pattern, cmd_str):
        print
        print("usage: python {0} {1} {2}".format(__file__, config.__name__, usage_pattern))
        print
        print("Params explanation:")
        print("    {0}{1}".format("(site)".ljust(N_DEFAULT_HELP_SPACING), "The application to install."))
        print("    {0}{1}".format("(local|staging|prod)".ljust(N_DEFAULT_HELP_SPACING), "The server to configure."))
        print("    {0}{1}".format("[with database]".ljust(N_DEFAULT_HELP_SPACING), "(Optional) Indicates to install a local database on the server."))
    else:

        # The commands to be executed in the server
        remote_commands = []

        # Extracts params from command line
        app = args[0] # App
        server = args[2] # Server

        # Defines a few constants with real time config paths
        project_root = set_real_time_config(PROJECT_ROOT, server)
        source_root = set_real_time_config(SOURCE_ROOT, server)
        project_virtualenv = set_real_time_config(PROJECT_VIRTUALENV, server)

        # Creates the user group and adds server's and apache's user to it.
        remote_commands.append("echo \" \"")
        remote_commands.append("echo \"##############################\"")
        remote_commands.append("echo \"# CONFIG. GROUP PERMISSIONS  #\"")
        remote_commands.append("echo \"##############################\"")
        remote_commands.append("echo \" \"")
        remote_commands.extend([
            "sudo groupadd {0}".format(DEFAULT_USER_GROUP),
            "sudo usermod -a -G {0} {1}".format(DEFAULT_USER_GROUP, SERVERS[server]["DEFAULT_USER"]),
            "sudo usermod -a -G {0} {1}".format(DEFAULT_USER_GROUP, NGINX_DEFAULT_USER),
       ])
        remote_commands.append("echo \"   ...DONE!\"")

        # Updates apt-get
        """
        remote_commands.append("echo \" \"")
        remote_commands.append("echo \"#########################\"")
        remote_commands.append("echo \"# UPDATING APT-GET      #\"")
        remote_commands.append("echo \"#########################\"")
        remote_commands.append("echo \" \"")
        remote_commands.append("sudo apt-get update")
        remote_commands.append("echo \"   ...DONE!\"")

        # Install packages
        remote_commands.append("echo \" \"")
        remote_commands.append("echo \"##################################\"")
        remote_commands.append("echo \"# INSTALLING REQUIRED PACKAGES   #\"")
        remote_commands.append("echo \"##################################\"")
        remote_commands.append("echo \" \"")

        INSTALL_PACKAGES = LINUX_DEV_PACKAGES
        for package in INSTALL_PACKAGES:
            remote_commands.append("sudo apt-get install {0} --yes".format(package))
        remote_commands.append("echo \"   ...DONE!\"")
        """

        # Checks for the WITH param to know if
        # there is more features to install, like database.
        """
        if "with" in args:

            # LOCAL DATABASE required?
            if "database" in args:
                # Asks for root password
                root_password = input("Please type the root's password for MySQL: ")
                root_password_confirm = input("Please confirm the root's password for MySQL: ")

                # If they are different, return.
                if root_password != root_password_confirm:
                    print("Error: Passwords do not match.")
                    return

                # Add commands to install the mysql-server
                remote_commands.append("echo \" \"")
                remote_commands.append("echo \"############################\"")
                remote_commands.append("echo \"# INSTALLING MYSQL-SERVER  #\"")
                remote_commands.append("echo \"############################\"")
                remote_commands.append("echo \" \"")
                remote_commands.extend([
                    "echo mysql-server mysql-server/root_password password {0} | sudo debconf-set-selections".format(root_password),
                    "echo mysql-server mysql-server/root_password_again password {0} | sudo debconf-set-selections".format(root_password),
                    "sudo apt-get -y install mysql-server",
               ])
                remote_commands.append("echo \"   ...DONE!\"")
        """

        # Creating the project's root folder
        remote_commands.append("echo \" \"")
        remote_commands.append("echo \"########################\"")
        remote_commands.append("echo \"# CREATING ROOT FOLDER #\"")
        remote_commands.append("echo \"########################\"")
        remote_commands.append("echo \" \"")
        remote_commands.extend([
            "sudo mkdir -p {0}".format(project_root),
            "sudo chown {0}:{1} {2}".format(SERVERS[server]["DEFAULT_USER"], DEFAULT_USER_GROUP, project_root),
            "sudo chgrp -R {0} {1}".format(DEFAULT_USER_GROUP, project_root),
        ])
        remote_commands.append("echo \"   ...DONE!\"")

        ################################
        # Configuring Django on remote.
        ################################
        if "site" in args:
            remote_commands.append("echo \" \"")
            remote_commands.append("echo \"#################################\"")
            remote_commands.append("echo \"# CREATING DIRECTORY STRUCTURE  #\"")
            remote_commands.append("echo \"#################################\"")
            remote_commands.append("echo \" \"")

            # Creating folder structure
            remote_commands.extend([
                "sudo mkdir -p {0}".format(project_virtualenv),
                "sudo chown {0}:{1} {2}".format(SERVERS[server]["DEFAULT_USER"], DEFAULT_USER_GROUP, project_virtualenv),
                "sudo chgrp -R {0} {1}".format(DEFAULT_USER_GROUP, project_virtualenv),
            ])
            remote_commands.append("echo \"   ...DONE!\"")

            remote_commands.append("echo \" \"")
            remote_commands.append("echo \"##################################\"")
            remote_commands.append("echo \"# INSTALLING PIP AND VIRTUALENV  #\"")
            remote_commands.append("echo \"##################################\"")
            remote_commands.append("echo \" \"")

            # Installing pip using python3 and virtualenv
            remote_commands.extend([
                "cd {0}".format(project_virtualenv),
                "wget https://bootstrap.pypa.io/get-pip.py",
                "sudo python3 get-pip.py",
                "sudo pip install virtualenv",
                "sudo rm get-pip.py",
            ])
            remote_commands.append("echo \"   ...DONE!\"")

            # Downloading git code.
            if server != "local":
                remote_commands.append("echo \" \"")
                remote_commands.append("echo \"#########################\"")
                remote_commands.append("echo \"# DOWNLOADING CODE      #\"")
                remote_commands.append("echo \"#########################\"")
                remote_commands.append("echo \" \"")
                remote_commands.extend([
                    "cd {0}".format(project_root),
                    "git clone {0} temp".format(GIT_REPO),
                    "shopt -s dotglob",
                    "mv temp/* {0}".format(project_root),
                    "git checkout {0}".format(SERVERS[server]["BRANCH"]),
                    "rm -R temp",
                    "rm -R infra",
                ])
                remote_commands.append("echo \"   ...DONE!\"")

            remote_commands.append("echo \" \"")
            remote_commands.append("echo \"###########################\"")
            remote_commands.append("echo \"# CONFIGURING VIRTUALENV  #\"")
            remote_commands.append("echo \"###########################\"")
            remote_commands.append("echo \" \"")

            # Installing and configuring virtualenv
            remote_commands.extend([
                "virtualenv {0}".format(project_virtualenv),
                "source {0}/bin/activate".format(project_virtualenv),
                "sudo chmod 777 {0}".format(project_virtualenv),
            ])
            for package in VIRTUALENV_PACKAGES:
                remote_commands.append("pip install {0}".format(package))
            remote_commands.extend([
                "deactivate",
                "sudo chmod 755 {0}".format(project_virtualenv),
            ])
            remote_commands.append("echo \"   ...DONE!\"")

            remote_commands.append("echo \" \"")
            remote_commands.append("echo \"#########################\"")
            remote_commands.append("echo \"# GENERATING CONF FILES #\"")
            remote_commands.append("echo \"#########################\"")
            remote_commands.append("echo \" \"")

            # Formats the gunicorn upstart file for the given server
            gunicorn_conf = set_real_time_config(GUNICORN_CONF, server)

            # Generates gunicorn upstart file
            """
            remote_commands.extend([
                # wsgi conf file
                "sudo rm -rf {0}/{1}.conf".format(GUNICORN_UPSTART_PATH, GUNICORN_ALIAS),
                "sudo touch {0}/{1}.conf".format(GUNICORN_UPSTART_PATH, GUNICORN_ALIAS),
                "sudo chmod 777 {0}/{1}.conf".format(GUNICORN_UPSTART_PATH, GUNICORN_ALIAS),
                "echo \"{0}\" > {1}/{2}.conf".format(gunicorn_conf, GUNICORN_UPSTART_PATH, GUNICORN_ALIAS),
                "sudo chmod 644 {0}/{1}.conf".format(GUNICORN_UPSTART_PATH, GUNICORN_ALIAS),
                "sudo service gunicorn start"
            ])

            # Formats the conf file for the given server
            nginx_conf = set_real_time_config(NGINX_CONF, server)

            # Generates nginx conf
            remote_commands.extend([
                "sudo rm -rf {0}/{1}".format(NGINX_SITES_AVAILABLE_PATH, APP_NAME),
                "sudo rm -rf {0}/{1}".format(NGINX_SITES_ENABLED_PATH, APP_NAME),
                "sudo touch {0}/{1}".format(NGINX_SITES_AVAILABLE_PATH, APP_NAME),
                "sudo chmod 777 {0}/{1}".format(NGINX_SITES_AVAILABLE_PATH, APP_NAME),
                "echo \"{0}\" > {1}/{2}".format(nginx_conf, NGINX_SITES_AVAILABLE_PATH, APP_NAME),
                "sudo chmod 644 {0}/{1}".format(NGINX_SITES_AVAILABLE_PATH, APP_NAME),
                "sudo ln -s {0}/{1} {2}".format(NGINX_SITES_AVAILABLE_PATH, APP_NAME, NGINX_SITES_ENABLED_PATH)
            ])

            # Formats the conf file for the given server
            celery_worker_conf = set_real_time_config(CELERY_WORKER_CONF, server)
            celery_beat_conf = set_real_time_config(CELERY_BEAT_CONF, server)

            # Generates celery config files
            remote_commands.extend([
                "sudo mkdir -p /celery_schedule",
                "sudo chown {0}:{1} /celery_schedule".format(SERVERS[server]["DEFAULT_USER"],
                                                             DEFAULT_USER_GROUP),
                "sudo chgrp -R {0} /celery_schedule".format(DEFAULT_USER_GROUP),
                "sudo chmod 700 -R /celery_schedule",
                "sudo mkdir /var/log/celery",
                "sudo touch /var/log/celery/worker.log",
                "sudo touch /var/log/celery/beat.log",
                "sudo touch /etc/supervisor/conf.d/celery.conf",
                "sudo touch /etc/supervisor/conf.d/celerybeat.conf",
                "sudo chmod 777 /etc/supervisor/conf.d/celery.conf",
                "sudo chmod 777 /etc/supervisor/conf.d/celerybeat.conf",
                "echo \"{0}\" > /etc/supervisor/conf.d/celery.conf".format(celery_worker_conf),
                "echo \"{0}\" > /etc/supervisor/conf.d/celerybeat.conf".format(celery_beat_conf),
                "sudo chmod 644 /etc/supervisor/conf.d/celery.conf",
                "sudo chmod 644 /etc/supervisor/conf.d/celerybeat.conf",
                "sudo service supervisor restart"
            ])
            remote_commands.append("echo \"   ...DONE!\"")
            """

        # Clears nginx's default conf.
        """
        remote_commands.append("echo \"Removing nginx's default conf file\"")
        remote_commands.append("sudo rm -r {0}/default".format(NGINX_SITES_AVAILABLE_PATH))
        """

        # Reinforces the owner and group of all project's folders
        if server != 'local':
            remote_commands.append("echo \"Reinforcing owner and group over all project's folders\"")
            remote_commands.extend([
                "sudo chown -R {0}:{1} {2}".format(SERVERS[server]["DEFAULT_USER"], DEFAULT_USER_GROUP, project_root),
                "sudo chgrp -R {0} {1}".format(DEFAULT_USER_GROUP, project_root),
            ])

        # Restarts services
        remote_commands.append("sudo service gunicorn restart")
        remote_commands.append("sudo initctl stop gunicorn")
        remote_commands.append("sudo initctl start gunicorn")
        remote_commands.append("sudo service nginx restart")
        remote_commands.append("sudo service supervisor restart all")

        # Executes script
        call_by_cloning_script(server, remote_commands)

        # Print ending hints
        print()
        print()
        print("###############################################")
        print("# Installation DONE. But you should configure #")
        print("# some DATABASE settings manually. Please     #")
        print("# refer our Wiki to get extra help.           #")
        print("###############################################")
        print()
        print("1. Connect to the server.")
        print("     python helper.py connect <server>")
        print("2. Access psql as postgre user")
        print("     sudo su - postgres")
        print("     psql")
        print("3. Create the database.")
        print("     create database <database>;")
        print("4. Create the user for this database.")
        print("     create user <username>@localhost identified by <password>;")
        print("5. Grant all privilegies to the user on the database. ")
        print("     grant all on <database>.* to <username>@localhost;")
        print("6. Exit PostgreSQL and SSH and run \"update\" to populate the database.")
        print("     python helper.py update <server>")


def connect(args):
    """
        Connects to the specified server via ssh.
        :args: A string indicating the server to connect to.
    """

    # The usage regex.
    usage_pattern = "{0}".format(AVAILABLE_SERVERS_PATTERN)
    cmd_str = " ".join(args)

    # Checks if the user typed the command correctly
    if not re.match(usage_pattern, cmd_str):
        print
        print("usage: python {0} {1} {2}".format(__file__, connect.__name__, usage_pattern))
        print
        print("Params explanation:")
        print("    {0}{1}".format("local".ljust(N_DEFAULT_HELP_SPACING), "Connects to your local vagrant instance."))
        print("    {0}{1}".format("staging".ljust(N_DEFAULT_HELP_SPACING), "Connects to your development instance."))
        print("    {0}{1}".format("prod".ljust(N_DEFAULT_HELP_SPACING), "Connects to production instance."))
    else:
        # Gets the server name
        server = args[0]

        # Connects to the server.
        if server == "local":
            return cmd("vagrant ssh")
        else:
            return cmd("ssh -i {0} {1}@{2}".format(SERVERS[server]["KEYPAIR"], SERVERS[server]["DEFAULT_USER"], SERVERS[server]["IP"]))


def restart(args):
    """
        Restarts the required services running on the server.
        :args: A string indicating the server to restart.
    """

    # The usage regex.
    usage_pattern = "{0}".format(AVAILABLE_SERVERS_PATTERN)
    cmd_str = " ".join(args)

    # Checks if the user typed the command correctly
    if not re.match(usage_pattern, cmd_str):
        print
        print("usage: python {0} {1} {2}".format(__file__, restart.__name__, usage_pattern))
        print
        print("Params explanation:")
        print("    {0}{1}".format("local".ljust(N_DEFAULT_HELP_SPACING), "Restarts the services on the local instance (vagrant)."))
        print("    {0}{1}".format("staging".ljust(N_DEFAULT_HELP_SPACING), "Restarts the services on the development instance."))
        print("    {0}{1}".format("prod".ljust(N_DEFAULT_HELP_SPACING), "Restarts the services on the production instance."))
    else:
        # Gets the server name
        server = args[0]
        services = ["postgresql", "supervisor", "nginx", "gunicorn"]

        cmd_str = ""
        for service in services:
            cmd_str += "sudo service {0} restart; ".format(service)
        cmd_str += "sudo service supervisor restart all; "

        if server == "local":
            cmd("vagrant ssh -c '{0}'".format(cmd_str))
        else:
            # Generates the ssh command for the given server
            ssh_command = "ssh -i {0} {1}@{2} -t".format(
                SERVERS[server]["KEYPAIR"],
                SERVERS[server]["DEFAULT_USER"],
                SERVERS[server]["IP"]
           )
            cmd("{0} '{1}'".format(ssh_command, cmd_str))


def update(args):
    """
        Updates the code of the instance with git HEAD modifications.
        :args: A string indicating the server to run the update.
    """
    # The usage regex.
    usage_pattern = "{0}".format(AVAILABLE_SERVERS_PATTERN)
    cmd_str = " ".join(args)

    # Checks if the user typed the command correctly
    if not re.match(usage_pattern, cmd_str):
        print
        print("usage: python {0} {1} {2}".format(__file__, update.__name__, usage_pattern))
        print
        print("Params explanation:")
        print("    {0}{1}".format("local".ljust(N_DEFAULT_HELP_SPACING), "Updates your local instance."))
        print("    {0}{1}".format("staging".ljust(N_DEFAULT_HELP_SPACING), "Updates your development instance."))
        print("    {0}{1}".format("prod".ljust(N_DEFAULT_HELP_SPACING), "Updates your production instance."))
    else:
        # Configuring the params and the commands to call.
        server = args[0]

        # Defines a few constants with real time config paths
        project_root = set_real_time_config(PROJECT_ROOT, server)
        source_root = set_real_time_config(SOURCE_ROOT, server)
        project_virtualenv = set_real_time_config(PROJECT_VIRTUALENV, server)

        remote_commands = []
        # Connects to the server.
        if server == "local":
            remote_commands = [
                "source {0}/bin/activate".format(project_virtualenv),
                "python {0}/manage.py migrate".format(source_root),
                "deactivate",
                "sudo service nginx restart",
                "sudo service gunicorn restart",
                "sudo service supervisor restart all",
           ]

        else:
            # Configuring the remote commands.
            remote_commands = [
                "cd {0}".format(project_root),
                "git checkout {0}".format(SERVERS[server]["BRANCH"]),
                "git pull origin {0}".format(SERVERS[server]["BRANCH"]),
                "rm -R infra",
                "source {0}/bin/activate".format(project_virtualenv),
                "python {0}/manage.py migrate".format(source_root),
                "deactivate",
                "sudo service nginx restart",
                "sudo service gunicorn restart",
                "sudo service supervisor restart all",
           ]

        return call_by_cloning_script(server, remote_commands)


###########################################################
# Utility function to extract the filename from a string.
###########################################################
def path_leaf(path):
    import ntpath
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)
###########################################################


def copy(args):
    """
    Copy a file or a folder from/to the remote server.
    :args: A set of arguments including the server to run the command, the file and
    recursive option.
    """
    # The usage regex.
    usage_pattern = "([\S]*)(-[rR])? (from|to) {0} (to|into) ([\S]*)".format(AVAILABLE_SERVERS_PATTERN)
    cmd_str = " ".join(args)

    # Check if the minimal number of arguments was passed.
    if not re.match(usage_pattern, cmd_str):
        print
        print("usage: python {0} {1} <file> [-r] from <server> to <local_path>".format(__file__, copy.__name__))
        print("usage: python {0} {1} <file> [-r] to <server> into <remote_path>".format(__file__, copy.__name__))
        print
        print("Params explanation:")
        print("    {0}{1}".format("file".ljust(N_DEFAULT_HELP_SPACING), "The file or folder to be copied."))
        print("    {0}{1}".format("-r".ljust(N_DEFAULT_HELP_SPACING), "(Optional) param indicating to download the <file> path recursively."))
        print("    {0}{1}".format("staging".ljust(N_DEFAULT_HELP_SPACING), "Copy files from/to the development server."))
        print("    {0}{1}".format("prod".ljust(N_DEFAULT_HELP_SPACING), "Copy files from/to the production server."))
        print("    {0}{1}".format("local_path".ljust(N_DEFAULT_HELP_SPACING), "The directory on your local machine to put the file."))
        print("    {0}{1}".format("remote_path".ljust(N_DEFAULT_HELP_SPACING), "The directory on your remote to put the file."))
    else:
        # Extracts the recursive param
        recursive = ("-r" in args or "-R" in args)
        if recursive:
            del args[1]

        # Extracts the other params (Note: The recursive arg was removed if it was passed).
        src = args[0]
        from_to = args[1]
        server = args[2]
        dest = args[4]

        ################################
        # Copying from server to local.
        ################################
        if from_to == "from":
            # The scp command with params set.
            commands = ["scp", "-r", "-i", SERVERS[server]["KEYPAIR"], "{0}@{1}:{2}".format(SERVERS[server]["DEFAULT_USER"], SERVERS[server]["IP"], src), dest]
            if not recursive:
                commands.remove("-r")

            return cmd(commands)

        ################################
        # Copying from local to server.
        ################################
        else:
            if recursive:   # Recursive? (src and dest are folders)
                commands = ["scp", "-r", "-i", SERVERS[server]["KEYPAIR"], src, "{0}@{1}:{2}".format(SERVERS[server]["DEFAULT_USER"], SERVERS[server]["IP"], dest)]
            else:
                # Extracts the filename from source
                filename = path_leaf(src)
                if not dest.endswith(os.pathsep):
                    filename = '/' + filename

                commands = ["scp", "-i", SERVERS[server]["KEYPAIR"], src,  "{0}@{1}:{2}{3}".format(SERVERS[server]["DEFAULT_USER"], SERVERS[server]["IP"], dest, filename)]
            return cmd(commands)










########################################################################
# INTERNAL METHODS
# Please do not modify the code above if you don't know what you're doing.
# This script was made to you just modify the configurations bellow.
########################################################################
def init():
    """
        Parse the command line params and calls the desired method.
        If the method is not encountered displays the help.
    """
    if len(sys.argv) > 1:
        # Tries to get the method to be called.
        method = globals().get(sys.argv[1])
        # Gets the params
        params = sys.argv[2:]

        # If method exists
        if method:
            method(params)
        # Else Displays help
        else:
            h()
    # Displays help
    else:
        h()



def h():
    """
        Displays info about the helper's methods.
    """

    # A big list of dictionaries mapping available methods names
    # and its respectives descriptions
    METHODS_HELP = [
        {
            "name": config.__name__,
            "description": "Configures the site on the remote server."
        },

        {
            "name": connect.__name__,
            "description": "Connects via ssh to the remote server."
        },
        {
            "name": update.__name__,
            "description": "Updates the remote server."
        },
        {
            "name": copy.__name__,
            "description": "Copy files from/to remote server."
        },
        {
            "name": restart.__name__,
            "description": "Restarts the services running on the server."
        },
   ]
    print
    print("USAGE: python {0} <command> <params>".format(__file__))
    print
    print("Available commands:")

    for help in METHODS_HELP:
        print("    {0}{1}".format(help["name"].ljust(N_DEFAULT_HELP_SPACING), help["description"]))


def cmd(commands):
    """
        Internal function. Used to call command line methods and pass input to it.
    """

    # Converts commands to string
    if type(commands) is list:
        commands = " ".join(commands)

    # Calls the command
    shell = subprocess.call(commands, shell = True)


def set_real_time_config(constant, server, deep = True):
    return constant.format(
        ip=SERVERS[server]["IP"],
        http_port=SERVERS[server]["HTTP_PORT"],
        https_port=SERVERS[server]["HTTPS_PORT"],
        https_forwarded_port=SERVERS[server]["HTTPS_FORWARDED_PORT"],
        default_user=SERVERS[server]["DEFAULT_USER"],
        default_user_group=DEFAULT_USER_GROUP,
        www_domain="www.{0}".format(SERVERS[server]["DOMAIN"]) if server == "prod" else SERVERS[server]["DOMAIN"],
        app_name=APP_NAME,
        project_alias=PROJECT_ALIAS,
        gunicorn_alias=GUNICORN_ALIAS,
        source_alias=SOURCE_ALIAS,
        source_root=set_real_time_config(SOURCE_ROOT, server, False) if deep else SOURCE_ROOT,
        project_virtualenv=set_real_time_config(PROJECT_VIRTUALENV, server, False) if deep else PROJECT_VIRTUALENV
   )


def call_by_cloning_script(server, commands):

    # Generates the script file.
    script_filename = "cs-{0}.sh".format(time.time())
    with open(script_filename, "wb") as script:
        script.write(bytes("\n".join(commands).replace("\r", ''), "UTF-8"))


    # Sending and executing the script
    if server == "local":
        cmd("vagrant ssh -c 'bash /vagrant/{0};'".format(script_filename))
    else:
        home_folder = "/home/" + SERVERS[server]["DEFAULT_USER"]
        copy([script_filename, "to", server, "into", home_folder])

        # Generates the ssh command for the given server
        ssh_command = "ssh -i {0} {1}@{2} -t".format(
            SERVERS[server]["KEYPAIR"],
            SERVERS[server]["DEFAULT_USER"],
            SERVERS[server]["IP"]
       )

        # The full path to the script on the remote server
        script_remote_path = home_folder + '/' + script_filename

        # Call the script and removes it
        callcmd = "{0} 'bash {1}; sudo rm {1};'".format(ssh_command, script_remote_path)
        cmd(callcmd)

    # Removes the generated file
    cmd("rm {0}".format(script_filename))

# Calls the initial method and exit.
init()
exit()
