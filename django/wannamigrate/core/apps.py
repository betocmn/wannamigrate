from django.apps import AppConfig
 
 
class CoreConfig( AppConfig ):
 
    name = 'wannamigrate.core'
    verbose_name = 'Core'
 
    def ready( self ):
 
        # import signal handlers
        import wannamigrate.core.signals