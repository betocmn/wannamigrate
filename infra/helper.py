#!/usr/bin/python
import sys, getopt, os, subprocess, re, time, datetime


##############################
# Configurations
##############################
# Servers' info
SERVERS = {
    "local" : {
        "ip" : "localhost",
        "url" : "localhost",
        "keypair" : "",
    },
    "dev" : {
        "ip" : "54.213.143.121",
        "url" : "dev.wannamigrate.com",
        "keypair" : "dev.pem",
    },
    "prod" : {
        "ip" : "54.148.167.28",
        "url" : "wannamigrate.com",
        "keypair" : "prod.pem",
    },
}

# Vagrant redirected ports
VAGRANT_HTTP = 8080
VAGRANT_HTTPS = 4443
VAGRANT_WIKI = 8181


# The default user and user group of each server.
USER_GROUPS = {
    "local" : "vagrant",
    "dev" : "ubuntu",
    "prod" : "ubuntu",
}

# Application's default folder
APP_ROOT = "/wanna"
SITE_ALIAS = "django"
WIKI_ALIAS = "wiki"
WSGI_ALIAS = "wsgi"
DEFAULT_SITE_PATH = APP_ROOT + '/' + SITE_ALIAS
DEFAULT_WIKI_PATH = APP_ROOT + '/' + WIKI_ALIAS

# Path to the virtualenv.
VIRTUALENV_PATH = "/wannavenv"

# Git repository
WANNAMIGRATE_GIT = "https://github.com/humbertomn/wannamigrate.git"



# Apache's configurations
APACHE_SITES_ENABLED_PATH = "/etc/apache2/sites-enabled"
APACHE_MODS_ENABLED_PATH = "/etc/apache2/mods-enabled"

# Spaces between names and descripts to display help.
N_DEFAULT_HELP_SPACING = 15

# The packages that should be installed.
INSTALL_PACKAGES = [ 
    "python3-dev", "git", "apache2", "libapache2-mod-wsgi-py3", 
    "libapache2-mod-php5", "php5-mysql", "libmysqlclient-dev", 
    "mysql-client", "gettext", "libjpeg-dev"
]

# The packages that should be installed on virtualenv
VIRTUALENV_PACKAGES = [ 
    "django==1.7.5",
    "https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-1.2.3.tar.gz",
    #"mysqlclient",
    "python-social-auth==0.2.2",
    "pillow==2.8.1",
    "django-stdimage==1.2.2",
    "pytz==2014.10",
]
    




########################################################################
# PUBLIC METHODS
# If you want to add a new method, please follow the pattern existant
# in other methods (Regex to check usage at beginning, method help if 
# usage wont match, etc).
########################################################################
def connect( args ):
    """
        Connects to the specified server via ssh.
        :args: A string indicating the server to connect to.
    """

    # The usage regex.
    usage_pattern = "(local|dev|prod)"
    cmd_str = " ".join( args )

    # Checks if the user typed the command correctly
    if not re.match( usage_pattern, cmd_str ):
        print( "usage: python {0} {1} (local|dev|prod)".format( __file__, connect.__name__ ) )
        print
        print( "Params explanation:")
        print( "    {0}{1}".format( "local".ljust( N_DEFAULT_HELP_SPACING ), "Connects to your local vagrant instance." ) )
        print( "    {0}{1}".format( "dev".ljust( N_DEFAULT_HELP_SPACING ), "Connects to Wanna Migrate's development instance." ) )
        print( "    {0}{1}".format( "prod".ljust( N_DEFAULT_HELP_SPACING ), "Connects to Wanna Migrate's production instance." ) )
    else:
        # Gets the server name
        server = args[0]

        # Connects to the server.
        if server == "local":
            return cmd( "vagrant ssh" )
        else:
            return cmd( "ssh -i {0} {1}@{2}".format( SERVERS[ server ][ "keypair" ], USER_GROUPS[ server ], SERVERS[ server ][ "ip" ] ) )



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
            "git pull", 
            "rm -R infra",
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
        print( "    {0}{1}".format( "--local_database".ljust( N_DEFAULT_HELP_SPACING ), "(Optional) Configures a MySQL Server on the remote." ) )
    else:
        
        # Configuring the params and the commands to call.
        server = args[0]


        # The command to generate the conf file for the specified app (site or wiki).
        conf_file_generator_cmd = ""

        # Remote commands
        remote_commands = []

        # Checking server...
        if server == "local":
            commands = [ "vagrant ssh" ]

            # Fix for vagrant port-forwarding
            http_port = ":{0}".format( VAGRANT_HTTP )
            https_port = ":{0}".format( VAGRANT_HTTPS )
            wiki_port = ":{0}".format( VAGRANT_WIKI )

        else:
            commands = [ "ssh", "-i", SERVERS[ server ][ "keypair" ], "ubuntu@{0}".format( SERVERS[ server ][ "ip" ] ) ]

            # Empty values. Dev and Prod doesn't have port-forwarding.
            http_port = ""
            https_port = ""
            wiki_port = ""
        
        
        # Configuring Wiki on remote. Fills remote_commands with wiki's configuration commands.
        if "wiki" in args:
            remote_commands.append( "sudo mkdir -p {0}".format( APP_ROOT ) )
            remote_commands.append( "sudo chown {1}:{1} {0}".format( APP_ROOT, USER_GROUPS[ server ] ) )
            remote_commands.append( "cd {0}".format( APP_ROOT ) )
            remote_commands.append( "wget http://releases.wikimedia.org/mediawiki/1.23/mediawiki-1.23.2.tar.gz" )
            remote_commands.append( "tar -zxf mediawiki-1.23.2.tar.gz" )
            remote_commands.append( "rm mediawiki-1.23.2.tar.gz" )
            remote_commands.append( "mv mediawiki-1.23.2 {0}".format( WIKI_ALIAS ) )

            # Command to create the wiki's ".conf" file.
            conf_file_generator_cmd = """echo \"Listen 81
                <VirtualHost *:81>
                    ServerName wiki.{0}
                    DocumentRoot {1}
                    <Directory {1}>
                        Require all granted
                    </Directory>
                </VirtualHost>\" > {2}/{3}.conf""".format( 
                    SERVERS[ server ][ "url" ], 
                    DEFAULT_WIKI_PATH,
                    APACHE_SITES_ENABLED_PATH,
                    WIKI_ALIAS 
                )

            # Creates the conf file containing the virtualhosts for the wiki on apache sites-enabled folder.
            remote_commands.append( "sudo touch {0}/{1}.conf".format( APACHE_SITES_ENABLED_PATH, WIKI_ALIAS ) )
            remote_commands.append( "sudo chmod 777 {0}/{1}.conf".format( APACHE_SITES_ENABLED_PATH, WIKI_ALIAS ) )
            remote_commands.append( conf_file_generator_cmd )
            remote_commands.append( "sudo chmod 644 {0}/{1}.conf".format( APACHE_SITES_ENABLED_PATH, WIKI_ALIAS ) )
        
        # Configuring Site on remote. Fills remote_commands with site's configuration commands.
        elif "site" in args:
            # Updates apt-get
            remote_commands.append( "sudo apt-get update" )
            
            # Install packages
            for package in INSTALL_PACKAGES:
                remote_commands.append( "sudo apt-get install {0} --yes".format( package ) )

            # Installing pip using python3 and virtualenv
            remote_commands.append( "cd ~/" )
            remote_commands.append( "wget https://bootstrap.pypa.io/get-pip.py" )
            remote_commands.append( "sudo python3 get-pip.py" )
            remote_commands.append( "sudo pip install virtualenv" )

            # Creating folders structure
            remote_commands.append( "sudo mkdir -p {0}".format( APP_ROOT ) )
            remote_commands.append( "sudo chown {1}:{1} {0}".format( APP_ROOT, USER_GROUPS[ server ] ) )
            remote_commands.append( "sudo mkdir -p {0}".format( VIRTUALENV_PATH ) )
            remote_commands.append( "sudo chown {1}:{1} {0}".format( VIRTUALENV_PATH, USER_GROUPS[ server ] ) )

            # Downloading Wanna Migrate's code.
            if server != "local":
                remote_commands.append( "cd {0}".format( APP_ROOT ) )
                remote_commands.append( "git clone {0} temp".format( WANNAMIGRATE_GIT ) )
                remote_commands.append( "shopt -s dotglob" )
                remote_commands.append( "mv temp/* {0}".format( APP_ROOT ) )
                remote_commands.append( "rm -R temp" )
                remote_commands.append( "rm -R infra" )

            # Installing and configuring virtualenv
            remote_commands.append( "virtualenv {0}".format( VIRTUALENV_PATH ) )
            remote_commands.append( "source {0}/bin/activate".format( VIRTUALENV_PATH ) )
            for package in VIRTUALENV_PACKAGES:
                remote_commands.append( "pip install {0}".format( package ) )
            remote_commands.append( "deactivate" )

            # Removes the apache's default configuration file
            remote_commands.append( "sudo rm {0}/000-default.conf".format( APACHE_SITES_ENABLED_PATH ) )

            # Creates the wsgi file on apache mods-enabled folder.
            remote_commands.append( "sudo touch {0}/{1}.conf".format( APACHE_MODS_ENABLED_PATH, WSGI_ALIAS ) )
            remote_commands.append( "sudo chmod 777 {0}/{1}.conf".format( APACHE_MODS_ENABLED_PATH, WSGI_ALIAS ) )
            remote_commands.append( 
                """echo \"<IfModule mod_wsgi.c>
                    WSGIPythonPath {0}:{1}/lib/python3.4:{1}/lib/python3.4/site-packages
                </IfModule>\" > {2}/{3}.conf""".format( DEFAULT_SITE_PATH, VIRTUALENV_PATH, APACHE_MODS_ENABLED_PATH, WSGI_ALIAS )
            )

            # Command to create the site's ".conf" file.
            conf_file_generator_cmd = """echo \"<VirtualHost *:80>
                    ServerName {0}
                    Redirect permanent / https://{0}{1}/                    
                </VirtualHost>

                <VirtualHost _default_:443>
                    ServerName {0}
                    DocumentRoot {2}

                    SSLEngine on
                    SSLProtocol All -SSLv2 -SSLv3
                    SSLCertificateFile /etc/apache2/ssl/wannamigrate.crt
                    SSLCertificateKeyFile /etc/apache2/ssl/wannamigrate.key
                    SSLCertificateChainFile /etc/apache2/ssl/wannamigrate.ca

                    WSGIScriptAlias / {2}/wannamigrate/wsgi.py

                    Alias /robots.txt {2}/static/robots.txt
                    Alias /favicon.ico {2}/static/favicon.ico
                    Alias /static/ {2}/static/

                    <Directory {2}/wannamigrate/>
                            <Files wsgi.py>
                                Require all granted
                            </Files>
                    </Directory>

                    <Directory {2}/static/>
                        Require all granted
                    </Directory>
                </VirtualHost>\" > {3}/{4}.conf""".format( 
                    SERVERS[ server ][ "url" ], 
                    https_port, 
                    DEFAULT_SITE_PATH,
                    APACHE_SITES_ENABLED_PATH,
                    SITE_ALIAS 
                )
            
            # Creates the conf file containing the virtualhosts for the site or wiki on apache sites-enabled folder.
            remote_commands.append( "sudo touch {0}/{1}.conf".format( APACHE_SITES_ENABLED_PATH, SITE_ALIAS ) )
            remote_commands.append( "sudo chmod 777 {0}/{1}.conf".format( APACHE_SITES_ENABLED_PATH, SITE_ALIAS ) )
            remote_commands.append( conf_file_generator_cmd )
            remote_commands.append( "sudo chmod 644 {0}/{1}.conf".format( APACHE_SITES_ENABLED_PATH, SITE_ALIAS ) )

        


        # Should install database locally?
        if "--local_database" in args:
            # Ask for root password
            root_password = input( "Please type the root's password for MySQL: " )
            root_password_confirm = input( "Please confirm the root's password for MySQL: " )
            # If they are different, return.
            if root_password != root_password_confirm:
                print( "Error: Passwords do not match." )
                return
            
            remote_commands.extend( [ 
                "echo mysql-server mysql-server/root_password password {0} | sudo debconf-set-selections".format( root_password ),
                "echo mysql-server mysql-server/root_password_again password {0} | sudo debconf-set-selections".format( root_password ),
                "sudo apt-get -y install mysql-server",
            ] )


        # Enabling mode rewrite on apache
        remote_commands.append( "sudo a2enmod rewrite" )
        # Enabling SSL on apache
        remote_commands.append( "sudo a2enmod ssl" )
        
        # Restarting apache
        remote_commands.append( "sudo service apache2 restart" )
            
        # Call
        if server == "local":
            cmd( commands, remote_commands, vagrant = True )
        else:
            cmd( commands, remote_commands )

        # Print ending hints
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



def cmd( commands, remote_commands = None, vagrant = False ):
    """
        Internal function. Used to call command line methods and pass input to it.
    """
    
    # Converts commands to string
    if type( commands ) is list:
        commands = " ".join( commands ) 

    # Appends the commands that should be executed on host machine.
    if remote_commands:
        if vagrant:
            commands += " -c '"
        else:
            commands += " -t '"
        commands += " \n ".join( remote_commands ) + "'"

    
    # Calls the command
    shell = subprocess.call( commands, shell = True )





# Calls the initial method and exit.
init()
exit()