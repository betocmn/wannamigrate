from django.db import models

class LandingPageEmail( models.Model ):
    """
        Model that contains the email from the users who are interested in platform.
    """
    email = models.EmailField( max_length = 200 )
    
    def __str__( self ):
	    return self.email