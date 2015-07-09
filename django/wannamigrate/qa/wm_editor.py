from html.parser import HTMLParser
from html.entities import name2codepoint
from django.utils.translation import ugettext_lazy as _
import re


class WMEditorParser( HTMLParser ):
    """ This class handles the content generated by the wm_editor (Rich Text Editor) and provides
        validation, cleaning, etc. """

    # List of available tags
    whitelist = [ "p", "b", "h1", "i", "br", "div", "u", "ol", "ul", "li", "a", "blockquote", "img" ]

    # Errors list
    errors = []

    # Current opened tag
    tags_stack = []

    # Opening tags, closing tags, data counters.
    total_opening_tags = 0
    total_closing_tags = 0
    total_data = 0

    # Invalid tags counters
    total_invalid_opening_tags = 0
    total_invalid_closing_tags = 0

    # Number of mismatching tags (opens and closes with a different tag)
    total_mismatching_tags = 0



    def __init__( self, *args, **kwargs ):
        super( WMEditorParser, self ).__init__( *args, **kwargs )


    def handle_starttag( self, tag, attrs ):
        # Increments the opening tags counter
        self.total_opening_tags += 1

        # Checks if the tag is whitelisted
        if tag not in self.whitelist:
            self.total_invalid_opening_tags += 1

        # Adds the current tag to the stack
        if tag != "br":
            self.tags_stack.append( tag )


    def handle_endtag( self, tag ):

        # Increments the closing tags counter
        self.total_closing_tags += 1

        # Checks if the ending tag is whitelisted
        if tag not in self.whitelist:
            self.total_invalid_closing_tags += 1

        # Stackcheck
        if tag != "br":
            match_tag = self.tags_stack.pop()
            if tag != match_tag:
                self.total_mismatching_tags += 1


    def handle_data( self, data ):
        self.total_data += 1
    

    def handle_comment(self, data):
        pass
    
    def handle_entityref(self, name):
        pass
    
    def handle_charref(self, name):
        pass
    
    def handle_decl(self, data):
        pass

    def is_valid( self ):
        """
        Verifies if the html parsed is valid
        """

        # Invalid tags check.
        total_invalid_tags = self.total_invalid_opening_tags + self.total_invalid_closing_tags
        if total_invalid_tags > 0:
            self.errors.append( _( "Your content has some invalid tags.") )

        # Empty HTML check.
        if self.is_empty():
            self.errors.append( _( "Please provide a body to your content." ) )

        # Mismatching tags check.
        if self.total_mismatching_tags > 0 :
            self.errors.append( _( "Your content has a invalid markup." ) )

        return ( len( self.errors ) == 0 )

    def is_empty( self ):
        """
        Checks if the parsed HTML is empty (no data provied).
        :return: True if no data was provided. False otherwise.
        """
        return ( self.total_data == 0 )

    def get_errors( self ):
        """
        Returns the list of errors found by the parser.
        :return: The list of errors found by the parser.
        """
        return self.errors