#!/usr/bin/python
import sys, getopt, os, subprocess, re


##############################
# Configurations
##############################
# Servers' info
SERVERS = {
    "dev" : {
        "ip" : "54.213.143.121",
        "keypair" : "dev.pem"
    },
    "prod" : {
        "ip" : "54.148.167.28",
        "keypair" : "prod.pem"
    },
}

# Application's default folder
DEFAULT_APP_PATH = "/var/www/wannamigrate"
DEFAULT_WIKI_PATH = "/var/www/wiki"


# Spaces between names and descripts to display help.
N_DEFAULT_HELP_SPACING = 15




####################################
# Methods
####################################
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

def test_cmd( args ):
    return cmd( [ "ls", "-la" ], "whois" )


def cmd( commands, remote_commands = None ):
    """
        Internal function. Used to call command line methods and pass input to it.
    """
    
    # Converts commands to string
    if type( commands ) is list:
        commands = " ".join( commands ) 

    # Appends the commands that should be executed on host machine.
    if remote_commands:
        commands += " -t '" + " \n".join( remote_commands ) + "'"
               
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
        remote_commands = [ "cd /wanna", "git pull" ]
        # Call
        return cmd( cmdlist_prod, input_data )
        



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



# Calls the initial method and exit.
init()
exit()