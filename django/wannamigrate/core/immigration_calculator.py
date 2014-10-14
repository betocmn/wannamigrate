from wannamigrate.core.models import (
    Country, CountryPoints, Question, Answer, User, UserEducation,
    UserEducationHistory, UserLanguage, UserLanguageProficiency,
    UserPersonal, UserPersonalFamily, UserResult, UserWork,
    UserWorkExperience, UserWorkOffer
)
from wannamigrate.core.util import calculate_age, get_object_or_false, get_list_or_false
from django.conf import settings
import inspect


class ImmigrationCalculator( object ):
    """
    Class responsible to make all calculations of immigration points.

    It should grab all user information and compare to the question/answers
    tables so that it can given total of points per country and per area.

    Rules can be found here:

    - Australia: http://www.immi.gov.au/Visas/Pages/189.aspx
    - Canada: http://www.cic.gc.ca/english/immigrate/skilled/apply-factors.asp
    - New Zealand: https://www.immigration.govt.nz/pointsindicator/

    """

    # Class variable to map which questions each country should evaluate
    question_methods = {
        settings.ID_QUESTION_FAMILY_OVERSEAS: { 'method': 'get_family_overseas_points', 'type': 'personal' },
        settings.ID_QUESTION_AGE: { 'method': 'get_age_points', 'type': 'personal' },
    }

    def __init__( self, user_id, country_id ):
        """
        Constructor responsible to set user and country

        :param user_id:
        :param country_id:
        :return None:
        """

        # Instantiate user and country
        self.user = User.objects.get( pk = user_id )
        self.country = Country.objects.get( pk = country_id )

        # Instantiate all user related models
        self.user_personal = get_object_or_false( UserPersonal, user = self.user )
        self.user_personal_family = get_list_or_false( self.user.userpersonalfamily_set )
        self.user_language = get_object_or_false( UserLanguage, user = self.user )
        self.user_language_proficiency = get_list_or_false( self.user.userlanguageproficiency_set )
        self.user_education = get_object_or_false( UserEducation, user = self.user )
        self.user_education_history = get_list_or_false( self.user.usereducationhistory_set )
        self.user_work = get_object_or_false( UserWork, user = self.user )
        self.user_work_experience = get_list_or_false( self.user.userworkexperience_set )
        self.user_work_offer = get_list_or_false( self.user.userworkoffer_set )

        # Initialize all totals
        self.total_personal_points = 0
        self.total_language_points = 0
        self.total_education_points = 0
        self.total_work_points = 0

    def __get_question_id( self, method_name ):
        """
        Search the 'question_methods' class variable to return the
        ID (key) from the anwer, based on method_name

        :param method_name:
        :return Mixed - Int or False on failure:
        """

        # Now we search the dictionary to find the key (answer_id) that holds this method name
        for question_id, value in self.question_methods.items():
            if value['method'] == method_name:
                return question_id
        return False

    def __get_points( self, value, type ):
        """
        Search the table 'core_countrypoints' by the value to localize
        how many points it' worth.

        type needs to be either:
            'id' - the search will be per answer_id
            'description' - the search will be per answer description

        :param value:
        :param type:
        :return Int:
        """

        # Get question ID
        method_name = inspect.stack()[1][3] # This give us the name of the parent method calling this one
        question_id = self.__get_question_id( method_name )

        # search for question object
        question = get_object_or_false( Question, pk = question_id )
        if question:

            # search for thew answer with the given paramaters
            if type == 'description':
                answer = get_object_or_false( Answer, question = question, description = value )
            else:
                answer = get_object_or_false( Answer, pk = value )
            if answer:

                # search for the points for the record with this age
                country_points = get_object_or_false( CountryPoints, country = self.country, answer = answer )
                if ( country_points ):
                    return country_points.points

        # If nothing was found, return 0 points
        return 0

    def get_total_points( self, type = None ):
        """
        Calculates the total points for the given user/country.

        If type was given, it will return the total for just those questions
        They can be 'personal', 'language', 'education' or 'work'

        :param String type:
        :return Mixed - Int or False on failure:
        """

        # Get possible questions for this country
        country_questions = [2,]

        # Initialize totals
        result = {
            'total': 0,
            'personal': 0,
            'language': 0,
            'education': 0,
            'work': 0,
        }

        # Now we search the dictionary to find the key (answer_id) that holds this method name
        for question_id in country_questions:
            if type is None or self.question_methods[question_id]['type'] == type:

                # call the appropriate method by its name to return the number of points
                points = getattr( self, self.question_methods[question_id]['method'] )()
                result['total'] += points
                if type is not None:
                    result[type] += points

        return result

    def get_age_points( self ):
        """
        calculate how many points user will get by his age.

        :return Int - Total of points:
        """
        if ( self.user_personal ):

            # get user age from birth date
            age = calculate_age( self.user_personal.birth_date )

            # search for how many points this answer is worth
            points = self.__get_points( age, 'description' )

            return points