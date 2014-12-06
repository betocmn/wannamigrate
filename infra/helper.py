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
            "description": "Gets a file on the remote server."
        },
        {
            "name": "put_file",
            "description": "Puts a file on the remote server."
        },
    ]

    print( "usage: python {0} <command> [<params>]".format( __file__ ) )
    print()
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
        os.system( "vagrant ssh" )
    # Development
    elif "dev" in args:
        os.system( "ssh -i {0} ubuntu@{1}".format( SERVERS[ "dev" ][ "keypair" ], SERVERS[ "dev" ][ "ip" ] ) )
    # Production
    elif "prod" in args:
        os.system( "ssh -i {0} ubuntu@{1}".format( SERVERS[ "prod" ][ "keypair" ], SERVERS[ "prod" ][ "ip" ] ) )
    else:
        print( "usage: python {0} {1} (local|dev|prod)".format( __file__, connect.__name__ ) )
        print()
        print( "Params explanation:")
        print( "    {0}{1}".format( "local".ljust( N_DEFAULT_HELP_SPACING ), "Connects to your local vagrant instance." ) )
        print( "    {0}{1}".format( "dev".ljust( N_DEFAULT_HELP_SPACING ), "Connects to Wanna Migrate's development instance." ) )
        print( "    {0}{1}".format( "prod".ljust( N_DEFAULT_HELP_SPACING ), "Connects to Wanna Migrate's production instance." ) )


def run_cmd( cmdlist, input_data = None ):
    """
        Internal function. Used to call command line methods and pass input to it.
    """

    commands = " ".join( cmdlist )
    if input_data:
        commands += " " + " && ".join( input_data )
    # Put stderr and stdout into pipes
    proc = subprocess.Popen( commands, \
            shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    return_code = proc.wait()
    # Read from pipes
    for line in proc.stdout:
        print("stdout: " + str( line.rstrip() ) )
    for line in proc.stderr:
        print("stderr: " + str( line.rstrip() ) ) 



def up( args ):
    """
        Updates the code of the instance with git HEAD modifications.
        :args: A string indicating the server to run the update.
    """
    # Setup commands
    cmdlist_dev = [ "ssh", "-i", SERVERS[ "dev" ][ "keypair" ], "ubuntu@{0}".format( SERVERS[ "dev" ][ "ip" ] ) ]
    cmdlist_prod = [ "ssh", "-i", SERVERS[ "prod" ][ "keypair" ], "ubuntu@{0}".format( SERVERS[ "prod" ][ "ip" ] ) ]
    input_data = [ "cd /wanna", "git pull" ]
    

    # Development
    if "dev" in args:
        run_cmd( cmdlist_dev, input_data )
    # Production
    elif "prod" in args:
        run_cmd( cmdlist_prod, input_data )
    else:
        print( "usage: python {0} {1} (dev|prod)".format( __file__, up.__name__ ) )
        print()
        print( "Params explanation:")
        print( "    {0}{1}".format( "dev".ljust( N_DEFAULT_HELP_SPACING ), "Send git changes to Wanna Migrate's development instance." ) )
        print( "    {0}{1}".format( "prod".ljust( N_DEFAULT_HELP_SPACING ), "Send git changes to Wanna Migrate's production instance." ) )



def get_file( args ):
    """
        Gets a file or a folder from the remote server.
        :args: A set of arguments including the server to run the command, the file and
        recursive option.
    """
    # The usage regex.
    usage_pattern = "(-[rR] )?(dev|prod) .+ .+"
    cmd_str = " ".join( args )

    # Check if the minimal number of arguments was passed.
    if not re.match( usage_pattern, cmd_str ):
        print( "usage: python {0} {1} [-r] (dev|prod) src dest ".format( __file__, get_file.__name__ ) )
        print()
        print( "Params explanation:")
        print( "    {0}{1}".format( "-r".ljust( N_DEFAULT_HELP_SPACING ), "Optional param indicating to get the file recursively." ) )
        print( "    {0}{1}".format( "dev".ljust( N_DEFAULT_HELP_SPACING ), "Send git changes to Wanna Migrate's development instance." ) )
        print( "    {0}{1}".format( "prod".ljust( N_DEFAULT_HELP_SPACING ), "Send git changes to Wanna Migrate's production instance." ) )
        print( "    {0}{1}".format( "src".ljust( N_DEFAULT_HELP_SPACING ), "The path to the file on the remote machine." ) )
        print( "    {0}{1}".format( "dest".ljust( N_DEFAULT_HELP_SPACING ), "The directory on your local machine to download the file." ) )
    else:

        # Server checking
        if "prod" in args: 
            server = "prod"
        else:
            server = "dev"

        # The index of the source in the args
        src_index = 1

        # Starts command list with scp
        cmdlist = [ "scp" ]
        
        # Recursively?
        if "-r" in args:
            cmdlist.append( "-r" )
            src_index += 1

        # Append -i to the commands
        cmdlist.append( "-i" )

        # Gets the src and dest from arguments
        src = args[ src_index ]
        dest = args[ src_index + 1 ]

        # Adds command parameters
        cmdlist.append( SERVERS[ server ][ "keypair" ] )
        cmdlist.append( "ubuntu@{0}:{1} {2}".format( SERVERS[ server ][ "ip" ], src, dest ) )
        
        return run_cmd( cmdlist )


def put_file( args ):
    """
        Puts a file or a folder from the remote server.
        :args: A set of arguments including the server to run the command, the file and
        recursive option.
    """
    # The usage regex.
    usage_pattern = "(-[rR] )?(dev|prod) .+ .+ [.+]?"
    cmd_str = " ".join( args )

    # Check if the minimal number of arguments was passed.
    if not re.match( usage_pattern, cmd_str ):
        print( "usage: python {0} {1} [-r] (dev|prod) src dest filename".format( __file__, put_file.__name__ ) )
        print()
        print( "Params explanation:")
        print( "    {0}{1}".format( "-r".ljust( N_DEFAULT_HELP_SPACING ), "Optional param indicating to get the file recursively." ) )
        print( "    {0}{1}".format( "dev".ljust( N_DEFAULT_HELP_SPACING ), "Send git changes to Wanna Migrate's development instance." ) )
        print( "    {0}{1}".format( "prod".ljust( N_DEFAULT_HELP_SPACING ), "Send git changes to Wanna Migrate's production instance." ) )
        print( "    {0}{1}".format( "src".ljust( N_DEFAULT_HELP_SPACING ), "The path to the file on your local machine." ) )
        print( "    {0}{1}".format( "dest".ljust( N_DEFAULT_HELP_SPACING ), "The directory on your host machine to upload the file." ) )
        print( "    {0}{1}".format( "filename".ljust( N_DEFAULT_HELP_SPACING ), "The name of the new file on the server. Should not be passed if uploading a directory (using -r)." ) )
    else:

        # Server checking
        if "prod" in args: 
            server = "prod"
        else:
            server = "dev"

        # The index of the source in the args
        src_index = 1

        # Starts command list with scp
        cmdlist = [ "scp" ]
        
        # Recursively?
        if "-r" in args:
            cmdlist.append( "-r" )
            src_index += 1
            filename = ''
        else:
            filename = args[ src_index + 2 ]

        # Append -i to the commands
        cmdlist.append( "-i" )

        # Gets the src and dest from arguments
        src = args[ src_index ]
        dest = args[ src_index + 1 ]
        


        # Should I add a bar at the end of the dest to append the filename?
        bar = '' if dest.endswith( '/' ) else '/'

        # Adds command parameters
        cmdlist.append( SERVERS[ server ][ "keypair" ] )
        cmdlist.append( "{0} ubuntu@{1}:{2}{3}{4}".format( src, SERVERS[ server ][ "ip" ], dest, bar, filename ) )
        
        return run_cmd( cmdlist )



# Calls the initial method and exit.
init()
exit()