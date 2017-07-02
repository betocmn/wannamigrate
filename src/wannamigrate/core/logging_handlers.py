"""
Custom Loggers/Handlers - https://docs.djangoproject.com/en/1.9/topics/logging/

"""

##########################
# Imports
##########################
import logging
import traceback


##########################
# Logging Handlers
##########################
class SlackHandler(logging.Handler):
    """
    An exception log handler that sends a summary notification to slack

    """

    def emit(self, record):
        from wannamigrate.core.tasks import create_alert

        message = record.message
        try:
            message += '\nTraceback: %s' % traceback.format_exc()
        except:
            pass
        create_alert('Attention: System ERROR', "%s" % message)
