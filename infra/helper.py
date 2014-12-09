#!/usr/bin/python
import sys, getopt, os, subprocess, re


##############################
# Configurations
##############################
# Servers' info
SERVERS = {
    "local" : {
        "ip" : "localhost",
        "keypair" : None,
    },
    "dev" : {
        "ip" : "54.213.143.121",
        "keypair" : "dev.pem",
    },
    "prod" : {
        "ip" : "54.148.167.28",
        "keypair" : "prod.pem",
    },
}

# Application's default folder
APP_ROOT = "/wanna"
SITE_ALIAS = "django"
WIKI_ALIAS = "wiki"
WSGI_ALIAS = "wsgi"
DEFAULT_SITE_PATH = APP_ROOT + '/' + SITE_ALIAS
DEFAULT_WIKI_PATH = APP_ROOT + '/' + WIKI_ALIAS

# Git repository
WANNAMIGRATE_GIT = "https://github.com/humbertomn/wannamigrate.git"

# Path to the virtualenv.
VIRTUALENV_PATH = "/wannavenv"

# Apache's configurations
APACHE_SITES_ENABLED_PATH = "/etc/apache2/sites-enabled"
APACHE_MODS_ENABLED_PATH = "/etc/apache2/mods-enabled"

# Spaces between names and descripts to display help.
N_DEFAULT_HELP_SPACING = 15

# The commands to execute on remote to configure site app.
CONFIGURE_SITE_COMMANDS = [
    # Updates server's repositories
    "echo \"--------------------------\"",
    "echo \"APT-GET UPDATE AND PYTHON3\"",
    "echo \"--------------------------\"",
    "sudo apt-get update",
    "sudo apt-get install python3-dev --yes",

    # Pip
    "echo \"--------------------------------------------\"",
    "echo \"INSTALLING PIP WITH PYTHON 3\"",
    "echo \"--------------------------------------------\"",
    "cd ~/",
    "sudo wget https://bootstrap.pypa.io/get-pip.py",
    "sudo python3 get-pip.py",
    
    # Virtualenv
    "echo \"--------------------------------------------\"",
    "echo \"INSTALLING VIRTUALENV WITH PYTHON 3\"",
    "echo \"--------------------------------------------\"",
    "sudo pip install virtualenv",

    # Git
    "echo \"--------------------------------------------\"",
    "echo \"INSTALLING GIT\"",
    "echo \"--------------------------------------------\"",
    "sudo apt-get install git --yes",
    
    # Apache2
    "echo \"--------------------------\"",
    "echo \"INSTALLING APACHE\"",
    "echo \"--------------------------\"",
    "sudo apt-get install apache2 --yes",
    "echo \"### Instaling Python3 WSGI ###\"",
    "sudo apt-get install libapache2-mod-wsgi-py3 --yes",
    "echo \"### Instaling PHP and PHP-MYSQL Modules ###\"",
    "sudo apt-get install libapache2-mod-php5 --yes",
    "sudo apt-get install php5-mysql --yes",

    # MySQL Tools
    "echo \"--------------------------\"",
    "echo \"INSTALLING MYSQL TOOLS\"",
    "echo \"--------------------------\"",
    "sudo apt-get install libmysqlclient-dev --yes",
    "sudo apt-get install mysql-client --yes",

    # Extra-tools
    "echo \"--------------------------\"",
    "echo \"INSTALLING EXTRA TOOLS\"",
    "echo \"--------------------------\"",
    "echo \"### Instaling gettext\"",
    "sudo apt-get install gettext --yes",
    "echo \"### Instaling libjpeg\"",
    "sudo apt-get install libjpeg-dev --yes",

    # Downloading Wanna Migrate code
    "echo \"--------------------------------------------\"",
    "echo \"DOWNLOADING WANNA MIGRATE CODE\"",
    "echo \"--------------------------------------------\"",
    "sudo mkdir {0}".format( APP_ROOT ),
    "sudo chown ubuntu:ubuntu {0}".format( APP_ROOT ),
    "cd {0}".format( APP_ROOT ),
    "git clone {0} temp".format( WANNAMIGRATE_GIT ),
    "shopt -s dotglob",
    "mv temp/* {0}".format( APP_ROOT ),
    "rm -R temp",
    "rm -R infra",
    "rm -R html",
    

    # Configuring the virtual enviroment
    "echo \"--------------------------\"",
    "echo \"CREATING THE VIRTUAL ENVIRONMENT\"",
    "echo \"--------------------------\"",
    "sudo mkdir {0}".format( VIRTUALENV_PATH ),
    "sudo chown ubuntu:ubuntu {0}".format( VIRTUALENV_PATH ),
    "virtualenv {0}".format( VIRTUALENV_PATH ),
    "source {0}/bin/activate".format( VIRTUALENV_PATH ),
    "pip install django",
    "pip install https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-1.2.3.tar.gz",
    "pip install django-debug-toolbar",
    "pip install python-social-auth",
    "pip install pillow",
    "pip install django-stdimage",
    "deactivate",

    # Removes the default configuration file
    "sudo rm {0}/000-default.conf".format( APACHE_SITES_ENABLED_PATH ),

    # Configuring apache's mods-enabled file (Yeah, it should be 777)
    "sudo touch {0}/{1}.conf".format( APACHE_MODS_ENABLED_PATH, WSGI_ALIAS ),
    "sudo chmod 777 {0}/{1}.conf".format( APACHE_MODS_ENABLED_PATH, WSGI_ALIAS ),    
    """echo \"<IfModule mod_wsgi.c>
       WSGIPythonPath {0}:{1}/lib/python3.4:{1}/lib/python3.4/site-packages
    </IfModule>\" > {2}/{3}.conf""".format( DEFAULT_SITE_PATH, VIRTUALENV_PATH, APACHE_MODS_ENABLED_PATH, WSGI_ALIAS ),

    # Configuring apache's sites-enabled file
    "sudo touch {0}/{1}.conf".format( APACHE_SITES_ENABLED_PATH, SITE_ALIAS ),
    "sudo chmod 777 {0}/{1}.conf".format( APACHE_SITES_ENABLED_PATH, SITE_ALIAS ),    
    """echo \"<VirtualHost *:80>
        ServerName www.wannamigrate.com
        DocumentRoot {0}

        WSGIScriptAlias / {0}/wannamigrate/wsgi.py

        Alias /robots.txt {0}/static/robots.txt
        Alias /favicon.ico {0}/static/favicon.ico
        Alias /static/ {0}/static/

        <Directory {0}/wannamigrate/>
                <Files wsgi.py>
                    Require all granted
                </Files>
        </Directory>

        <Directory {0}/static/>
            Require all granted
        </Directory>
    </VirtualHost>\" > {1}/{2}.conf""".format( DEFAULT_SITE_PATH, APACHE_SITES_ENABLED_PATH, SITE_ALIAS ),
    "sudo chmod 644 {0}/{1}.conf".format( APACHE_SITES_ENABLED_PATH, SITE_ALIAS ),
    
    # Restarts server
    "sudo service apache2 restart"
]

# The commands to execute on remote to configure wiki app.
CONFIGURE_WIKI_COMMANDS = [
    "sudo mkdir {0}".format( APP_ROOT ),
    "sudo chown ubuntu:ubuntu {0}".format( APP_ROOT ),
    "cd {0}".format( APP_ROOT ),
    "wget http://releases.wikimedia.org/mediawiki/1.23/mediawiki-1.23.2.tar.gz",
    "tar -zxf mediawiki-1.23.2.tar.gz",
    "rm mediawiki-1.23.2.tar.gz",
    "mv mediawiki-1.23.2 {0}".format( WIKI_ALIAS ),
    "sudo touch {0}/{1}.conf".format( APACHE_SITES_ENABLED_PATH, WIKI_ALIAS ),
    "sudo chmod 777 {0}/{1}.conf".format( APACHE_SITES_ENABLED_PATH, WIKI_ALIAS ),    
    """echo \"Listen 81
    <VirtualHost *:81>
        ServerName dev.wannamigrate.com
        DocumentRoot {0}
        <Directory {0}/>
            Require all granted
        </Directory>
    </VirtualHost>\" > {1}/{2}.conf""".format( DEFAULT_WIKI_PATH, APACHE_SITES_ENABLED_PATH, WIKI_ALIAS ),
    "sudo chmod 644 {0}/{1}.conf".format( APACHE_SITES_ENABLED_PATH, WIKI_ALIAS ),    
    "sudo service apache2 restart",
]





####################################
# Methods
####################################
# Please do not modify the code above if you don't know what you're doing.
# This script was made to you just have to modify the configurations bellow.
def init():
    """
        Parse the command line params and calls the desired method.
        If the method is not encountered displays the help.
    """
    if len( sys.argv ) > 1:
        # Tries to get the method to be called.
        method = globals().get( sys.argv[1] )
        # Gets the params
        params = sys.argv[2:]

        # If method exists
        if method:
            method( params )
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
            "name": "connect",
            "description": "Connects via ssh to the remote server."
        },
        {
            "name": "up",
            "description": "Send git changes to the remote server."
        },
        {
            "name": "get_file",
            "description": "Get files from the remote server."
        },
        {
            "name": "put_file",
            "description": "Put files on the remote server."
        },
        {
            "name": "install",
            "description": "Installs an available app on the remote server."
        },
    ]

    print( "usage: python {0} <command> [<params>]".format( __file__ ) )
    print
    print( "Available commands:" )

    for help in METHODS_HELP:
        print( "    {0}{1}".format( help[ "name" ].ljust( N_DEFAULT_HELP_SPACING ), help[ "description" ] ) )



def connect( args ):
    """
        Connects to the specified server via ssh.
        :args: A string indicating the server to connect to.
    """

    # Local
    if "local" in args:
        return cmd( "vagrant ssh" )
    # Development
    elif "dev" in args:
        return cmd( "ssh -i {0} ubuntu@{1}".format( SERVERS[ "dev" ][ "keypair" ], SERVERS[ "dev" ][ "ip" ] ) )
    # Production
    elif "prod" in args:
        return cmd( "ssh -i {0} ubuntu@{1}".format( SERVERS[ "prod" ][ "keypair" ], SERVERS[ "prod" ][ "ip" ] ) )
    else:
        print( "usage: python {0} {1} (local|dev|prod)".format( __file__, connect.__name__ ) )
        print
        print( "Params explanation:")
        print( "    {0}{1}".format( "local".ljust( N_DEFAULT_HELP_SPACING ), "Connects to your local vagrant instance." ) )
        print( "    {0}{1}".format( "dev".ljust( N_DEFAULT_HELP_SPACING ), "Connects to Wanna Migrate's development instance." ) )
        print( "    {0}{1}".format( "prod".ljust( N_DEFAULT_HELP_SPACING ), "Connects to Wanna Migrate's production instance." ) )



def cmd( commands, remote_commands = None ):
    """
        Internal function. Used to call command line methods and pass input to it.
    """
    
    # Converts commands to string
    if type( commands ) is list:
        commands = " ".join( commands ) 

    # Appends the commands that should be executed on host machine.
    if remote_commands:
        commands += " -t '" + " \n ".join( remote_commands ) + "'"

    
    # Calls the command
    shell = subprocess.call( commands, shell = True )



def up( args ):
    """
        Updates the code of the instance with git HEAD modifications.
        :args: A string indicating the server to run the update.
    """

    # The usage regex.
    usage_pattern = "(dev|prod)"
    cmd_str = " ".join( args )

    # Checks if the user typed the command correctly
    if not re.match( usage_pattern, cmd_str ):
        print( "usage: python {0} {1} (dev|prod)".format( __file__, up.__name__ ) )
        print
        print( "Params explanation:")
        print( "    {0}{1}".format( "dev".ljust( N_DEFAULT_HELP_SPACING ), "Send git changes to Wanna Migrate's development instance." ) )
        print( "    {0}{1}".format( "prod".ljust( N_DEFAULT_HELP_SPACING ), "Send git changes to Wanna Migrate's production instance." ) )
    else:
        # Configuring the params and the commands to call.
        server = args[0]
        commands = [ "ssh", "-i", SERVERS[ server ][ "keypair" ], "ubuntu@{0}".format( SERVERS[ server ][ "ip" ] ) ]
        # Configuring the remote commands.
        remote_commands = [ 
            "cd {0}".format( APP_ROOT ), 
            "git fetch", 
            "git checkout HEAD {0}".format( DEFAULT_SITE_PATH ),
            "source {0}/bin/activate".format( VIRTUALENV_PATH ),
            "python {0}/manage.py migrate".format( DEFAULT_SITE_PATH ),
            "deactivate"
        ]
        # Call
        return cmd( commands, remote_commands )
        



def get_file( args ):
    """
        Gets a file or a folder from the remote server.
        :args: A set of arguments including the server to run the command, the file and
        recursive option.
    """
    # The usage regex.
    usage_pattern = "(dev|prod) [^ ]+ [^ ]+( -[rR])?"
    cmd_str = " ".join( args )

    # Check if the minimal number of arguments was passed.
    if not re.match( usage_pattern, cmd_str ):
        print( "usage: python {0} {1} (dev|prod) <src> <dest> [-r]".format( __file__, get_file.__name__ ) )
        print
        print( "Params explanation:")
        print( "    {0}{1}".format( "dev".ljust( N_DEFAULT_HELP_SPACING ), "Copy files from the development server." ) )
        print( "    {0}{1}".format( "prod".ljust( N_DEFAULT_HELP_SPACING ), "Copy files from the production server." ) )
        print( "    {0}{1}".format( "src".ljust( N_DEFAULT_HELP_SPACING ), "The path to the file on the remote machine." ) )
        print( "    {0}{1}".format( "dest".ljust( N_DEFAULT_HELP_SPACING ), "The directory on your local machine to download the file." ) )
        print( "    {0}{1}".format( "-r".ljust( N_DEFAULT_HELP_SPACING ), "Optional param indicating to download the source path recursively." ) )
    else:

        # Extracts the scp params.
        server = args[0]
        src = args[1]
        dest = args[2]

        # The scp command with params set.
        commands = [ "scp", "-r", "-i", SERVERS[ server ][ "keypair" ], "ubuntu@{0}:{1}".format( SERVERS[ server ][ "ip" ], src ), dest ]

        # If recursive mode wasn't set then remove it from commands.
        if not ["-r","-R"] in args:
            commands.remove( "-r" )
        
        return cmd( commands ) 


def put_file( args ):
    """
        Puts a file or a folder from the remote server.
        :args: A set of arguments including the server to run the command, the file and
        recursive option.
    """
    # The usage regex.
    usage_pattern = "(dev|prod) [^ ]+ [^ ]+ [^ ]+"
    cmd_str = " ".join( args )

    # Check if the minimal number of arguments was passed.
    if not re.match( usage_pattern, cmd_str ):
        print( "usage: python {0} {1} (dev|prod) <src> <dest> (-r|<filename>)".format( __file__, put_file.__name__ ) )
        print
        print( "Params explanation:")
        print( "    {0}{1}".format( "dev".ljust( N_DEFAULT_HELP_SPACING ), "Copy files from the development server." ) )
        print( "    {0}{1}".format( "prod".ljust( N_DEFAULT_HELP_SPACING ), "Copy files from the production server." ) )
        print( "    {0}{1}".format( "src".ljust( N_DEFAULT_HELP_SPACING ), "The path to the file on the local machine." ) )
        print( "    {0}{1}".format( "dest".ljust( N_DEFAULT_HELP_SPACING ), "The directory on your remote machine to send the file." ) )
        print( "    {0}{1}".format( "-r".ljust( N_DEFAULT_HELP_SPACING ), "Uploads the source path recursively." ) )
        print( "    {0}{1}".format( "filename".ljust( N_DEFAULT_HELP_SPACING ), "The target filename on the remote machine." ) )
    else:
        # Extracts the scp params.
        server = args[0]
        src = args[1]
        dest = args[2]
        filename_or_recursive = args[3]

        # The scp command with params set.
        commands = [ "scp", "-r", "-i", SERVERS[ server ][ "keypair" ], src ]

        # Recursive mode?        
        if filename_or_recursive == "-r" or filename_or_recursive == "-R":
            commands.append( "ubuntu@{0}:{1}".format( SERVERS[ server ][ "ip" ], dest ) )

        # If recursive mode wasn't set then remove it from commands.
        else:            
            commands.remove( "-r" )
            # Adds the filename to the end of the destination.
            if not dest.endswith( '/' ):
                filename_or_recursive = '/' + filename_or_recursive
            commands.append( "ubuntu@{0}:{1}{2}".format( SERVERS[ server ][ "ip" ], dest, filename_or_recursive ) )
        
        return cmd( " ".join( commands ) )



def install( args ):
    """
        Installs the desired app on the remote.
        :args: A string indicating the server to run the update.
    """

    # The usage regex.
    usage_pattern = "(local|dev|prod) (site|wiki)( --local_database)?"
    cmd_str = " ".join( args )

    # Checks if the user typed the command correctly
    if not re.match( usage_pattern, cmd_str ):
        print( "usage: python {0} {1} (local|dev|prod) (site|wiki) [--local_database]".format( __file__, install.__name__ ) )
        print
        print( "Params explanation:")
        print( "    {0}{1}".format( "local".ljust( N_DEFAULT_HELP_SPACING ), "Configures the desired feature into your local vagrant instance." ) )
        print( "    {0}{1}".format( "dev".ljust( N_DEFAULT_HELP_SPACING ), "Configures the desired feature into Wanna Migrate's development instance." ) )
        print( "    {0}{1}".format( "prod".ljust( N_DEFAULT_HELP_SPACING ), "Configures the desired feature into Wanna Migrate's production instance." ) )
        print( "    {0}{1}".format( "site".ljust( N_DEFAULT_HELP_SPACING ), "Configures the site." ) )
        print( "    {0}{1}".format( "wiki".ljust( N_DEFAULT_HELP_SPACING ), "Configures the wiki." ) )
        print( "    {0}{1}".format( "--local-database".ljust( N_DEFAULT_HELP_SPACING ), "(Optional) Configures a MySQL Server on the remote." ) )
    else:
        # Configuring the params and the commands to call.
        server = args[0]

        if server == "local":
            commands = [ "vagrant ssh" ]
        else:
            commands = [ "ssh", "-i", SERVERS[ server ][ "keypair" ], "ubuntu@{0}".format( SERVERS[ server ][ "ip" ] ) ]
        
        # Configuring the remote commands.
        remote_commands = None
        
        if "wiki" in args:
            remote_commands = CONFIGURE_WIKI_COMMANDS
        elif "site" in args:
            remote_commands = CONFIGURE_SITE_COMMANDS

        if "--local_database" in args:
            # Ask for root password
            root_password = raw_input( "Please type the root's password for MySQL: " )
            root_password_confirm = raw_input( "Please confirm the root's password for MySQL: " )
            # If they are different, return.
            if root_password != root_password_confirm:
                print( "Error: Passwords do not match." )
                return
            
            remote_commands.extend( [ 
                "echo mysql-server mysql-server/root_password password {0} | sudo debconf-set-selections".format( root_password ),
                "echo mysql-server mysql-server/root_password_again password {0} | sudo debconf-set-selections".format( root_password ),
                "sudo apt-get -y install mysql-server",
            ] )
        
        # Call
        cmd( commands, remote_commands )

        print
        print( "Installation DONE. But you should configure some DATABASE settings manually." )
        print( "Please refer Wanna Migrate's Wiki to get extra help.")
        if "site" in args:
            print( "1. Create the database \"wannamigrate\".")
            print( "2. Create the user \"wannamigrate\" granting all privilegies over \"wannamigrate\" database.")
            print( "3. After that, you should run \"python helper.py up\" to populate the database on the remote server." )
        elif "wiki" in args:
            print( "1. Create the database \"wiki\".")
            print( "2. Create the user \"wiki\" granting all privilegies over \"wiki\" database.")
            print( "3. After that, you should access http://{0}:81/mw-config/index.php to configure wiki.".format( SERVERS[ server ][ "ip" ] ) )





# Calls the initial method and exit.
init()
exit()