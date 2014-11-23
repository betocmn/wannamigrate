from wannamigrate.core.models import (
    Country, CountryPoints, Question, Answer, User, UserEducation,
    UserEducationHistory, UserLanguage, UserLanguageProficiency,
    UserPersonal, UserPersonalFamily, UserResult, UserWork,
    UserWorkExperience, UserWorkOffer
)
from wannamigrate.core.util import calculate_age, get_object_or_false, get_list_or_false, date_difference
from django.conf import settings
import inspect
import math


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
        settings.ID_QUESTION_ENGLISH: { 'method': 'get_english_points', 'type': 'language' },
        settings.ID_QUESTION_FRENCH: { 'method': 'get_french_points', 'type': 'language' },
        settings.ID_QUESTION_EDUCATION_DEGREE: { 'method': 'get_education_degree_points', 'type': 'education' },
        settings.ID_QUESTION_WORK_OFFER: { 'method': 'get_work_offer_points', 'type': 'work' },
        settings.ID_QUESTION_WORK_EXPERIENCE_OUTSIDE: { 'method': 'get_work_experience_outside_points', 'type': 'work' },
        settings.ID_QUESTION_WORK_EXPERIENCE_INSIDE: { 'method': 'get_work_experience_inside_points', 'type': 'work' },
        settings.ID_QUESTION_OCCUPATION: { 'method': 'get_occupation_points', 'type': 'work' },
        settings.ID_QUESTION_SKILLED_PARTNER: { 'method': 'get_skilled_partner_points', 'type': 'work' },
        settings.ID_QUESTION_INVEST: { 'method': 'get_invest_points', 'type': 'work' },
        settings.ID_QUESTION_STARTUP_LETTER: { 'method': 'get_startup_letter_points', 'type': 'work' },
        settings.ID_QUESTION_US_CITIZEN: { 'method': 'get_us_citizen_points', 'type': 'personal' },
        settings.ID_QUESTION_STUDY_REGIONAL_AU: { 'method': 'get_study_regional_au_points', 'type': 'education' },
        settings.ID_QUESTION_PROFESSIONAL_YEAR_AU: { 'method': 'get_professional_year_au_points', 'type': 'education' },
        settings.ID_QUESTION_LIVE_REGIONAL_AU: { 'method': 'get_live_regional_au_points', 'type': 'personal' },
        settings.ID_QUESTION_COMMUNITY_LANGUAGE_AU: { 'method': 'get_community_language_au_points', 'type': 'language' },
        settings.ID_QUESTION_PARTNER_WORKED_STUDIED_CA: { 'method': 'get_partner_worked_studied_ca_points', 'type': 'work' },
        settings.ID_QUESTION_PARTNER_ENGLISH: { 'method': 'get_partner_english_points', 'type': 'language' },
        settings.ID_QUESTION_PARTNER_FRENCH: { 'method': 'get_partner_french_points', 'type': 'language' },
        settings.ID_QUESTION_PARTNER_EDUCATION_DEGREE: { 'method': 'get_partner_education_degree_points', 'type': 'education' },
    }

    def __init__( self, user, country ):
        """
        Constructor responsible to set user and country

        :param user:
        :param country:
        :return None:
        """

        # Instantiate user and country
        self.user = user
        self.country = country

        # Instantiate all user related models
        try:
            self.user_personal = self.user.userpersonal
        except UserPersonal.DoesNotExist:
            self.user_personal = False

        try:
            self.user_personal_family = self.user.userpersonalfamily_set.all()
        except UserPersonalFamily.DoesNotExist:
            self.user_personal_family = False

        try:
            self.user_language = self.user.userlanguage
        except UserLanguage.DoesNotExist:
            self.user_language = False

        try:
            self.user_language_proficiency = self.user.userlanguageproficiency_set.all()
        except UserLanguageProficiency.DoesNotExist:
            self.user_language_proficiency = False

        try:
            self.user_education = self.user.usereducation
        except UserEducation.DoesNotExist:
            self.user_education = False

        try:
            self.user_education_history = self.user.usereducationhistory_set.all()
        except UserEducationHistory.DoesNotExist:
            self.user_education_history = False

        try:
            self.user_work = self.user.userwork
        except UserWork.DoesNotExist:
            self.user_work = False

        try:
            self.user_work_experience = self.user.userworkexperience_set.all()
        except UserWorkExperience.DoesNotExist:
            self.user_work_experience = False

        try:
            self.user_work_offer = self.user.userworkoffer_set.all()
        except UserWorkOffer.DoesNotExist:
            self.user_work_offer = False

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
        how many points it's worth.

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
        #question = get_object_or_false( Question, pk = question_id )
        if question_id:

            # search for thew answer with the given parameters
            if type == 'description':
                answer = get_object_or_false( Answer, question_id = question_id, description = value )
            else:
                answer = get_object_or_false( Answer, question_id = question_id, pk = value )
            if answer:

                # search for the points for the record with this age
                country_points = get_object_or_false( CountryPoints, country = self.country, answer = answer )
                if ( country_points ):
                    return country_points.points

        # If nothing was found, return 0 points
        return 0

    def get_total_results( self ):
        """
        Calculates the total points for the given user/country.

        If type was given, it will return the total for just those questions
        They can be 'personal', 'language', 'education' or 'work'

        It will return a dictionary with the following total numbers:

        'total', 'personal', 'language', 'education' and 'work'

        :return Mixed - Int or False on failure:
        """

        # Initialize totals
        result = {
            'total': 0,
            'personal': 0,
            'language': 0,
            'education': 0,
            'work': 0,
        }

        # Run trough every question
        for question_id, value in self.question_methods.items():

                # call the appropriate method by its name to return the number of points
                points = getattr( self, value['method'] )()
                result['total'] += points
                result[value['type']] += points

        # @TODO do additional points here (specific addition rules for each country)

        return result

    def get_family_overseas_points( self, forced_value = None ):
        """
        Points if user has a close relative living abroad (in canada, australia...)

        :param forced_value:
        :return Int - Total of points:
        """
        points = 0
        if ( self.user_personal_family ):

            # Use given value or search for it
            if forced_value is not None:
                value = forced_value
            else:
                # search for a relative on the current country
                value = ""
                for item in self.user_personal_family:
                    if item.country_id == self.country.id:
                        value = "Yes"
                        break

            # search for how many points this answer is worth
            if value == "Yes":
                points = self.__get_points( value, 'description' )

        return points

    def get_age_points( self, forced_value = None ):
        """
        calculate how many points user will get by his age.

        :param forced_value:
        :return Int - Total of points:
        """
        points = 0
        if ( self.user_personal ):

            # Use given value or search for it
            if forced_value is not None:
                value = forced_value
            else:
                # get user age from birth date
                age = calculate_age( self.user_personal.birth_date )
                value = age

            # search for how many points this answer is worth
            points = self.__get_points( value, 'description' )

        return points

    def get_english_points( self, forced_value = None ):
        """
        Points for skills with the english language

        :param forced_value:
        :return Int - Total of points:
        """
        points = 0
        if ( self.user_language_proficiency ):

            # Use given value or search for it
            if forced_value is not None:
                value = forced_value
            else:
                # search for a relative on the current country
                value = ""
                for item in self.user_language_proficiency:
                    if item.language_id == settings.ID_LANGUAGE_ENGLISH:
                        value = item.language_level_answer.id
                        break

            # search for how many points this answer is worth
            if value != "":
                points = self.__get_points( value, 'id' )

        return points

    def get_french_points( self, forced_value = None ):
        """
        Points for skills with the french language

        :param forced_value:
        :return Int - Total of points:
        """
        points = 0
        if ( self.user_language_proficiency ):

            # Use given value or search for it
            if forced_value is not None:
                value = forced_value
            else:
                # search for a relative on the current country
                value = ""
                for item in self.user_language_proficiency:
                    if item.language_id == settings.ID_LANGUAGE_FRENCH:
                        value = item.language_level_answer.id
                        break

            # search for how many points this answer is worth
            if value != "":
                points = self.__get_points( value, 'id' )

        return points

    def get_education_degree_points( self, forced_value = None ):
        """
        Points for the highest level of education (degree: bacherlor, masters, etc.)

        :param forced_value:
        :return Int - Total of points:
        """
        points = 0
        if ( self.user_education_history ):

            # Use given value or search for it
            if forced_value is not None:
                value = forced_value
            else:
                # search for a relative on the current country
                highest_points = 0
                for item in self.user_education_history:

                    # search for points (we will store only the highest points (highest degree of education)
                    value = item.education_level_answer.id
                    current_points = self.__get_points( value, 'id' )
                    if ( current_points > highest_points ):
                        highest_points = current_points

                points = highest_points

        return points

    def get_work_offer_points( self, forced_value = None ):
        """
        Points for users that have a job offer on country of destination

        :param forced_value:
        :return Int - Total of points:
        """
        points = 0
        if ( self.user_work_offer ):

            # Use given value or search for it
            if forced_value is not None:
                value = forced_value
            else:
                # search for work offers in other countries
                value = ""
                for item in self.user_work_offer:
                    if item.country_id == self.country.id:
                        value = "Yes"
                        break

            # search for how many points this answer is worth
            if value == "Yes":
                points = self.__get_points( value, 'description' )

        return points

    def get_work_experience_outside_points( self, forced_value = None ):
        """
        Points for work experience gained outside country of destination

        :param forced_value:
        :return Int - Total of points:
        """
        points = 0
        if ( self.user_work_experience ):

            # Use given value or search for it
            if forced_value is not None:
                value = forced_value
            else:
                # search for work experiences outside country of destination
                years_of_experience = 0
                for item in self.user_work_experience:
                    if item.country_id != self.country.id:
                        years_of_experience += ( item.months / 12 )

                value = math.floor( years_of_experience )

            # search for how many points this answer is worth
            if value > 0:
                points = self.__get_points( value, 'description' )

        return points

    def get_work_experience_inside_points( self, forced_value = None ):
        """
        Points for work experience gained at country of destination

        :param forced_value:
        :return Int - Total of points:
        """
        points = 0
        if ( self.user_work_experience ):

            # Use given value or search for it
            if forced_value is not None:
                value = forced_value
            else:
                # search for work experiences on the current country
                years_of_experience = 0
                for item in self.user_work_experience:
                    if item.country_id == self.country.id:
                        years_of_experience += ( item.months / 12 )

                value = math.floor( years_of_experience )

            # search for how many points this answer is worth
            if value > 0:
                points = self.__get_points( value, 'description' )

        return points

    def get_occupation_points( self, forced_value = None ):
        """
        Points for professional occupation (engineer, doctor, architect, etc..)

        :param forced_value:
        :return Int - Total of points:
        """
        points = 0
        if ( self.user_work ):

            # Use given value or search for it
            if forced_value is not None:
                value = forced_value
            else:
                value = self.user_work.occupation_answer.id

            points = self.__get_points( value, 'id' )

        return points

    def get_skilled_partner_points( self, forced_value = None ):
        """
        Points for users with partners who have a occupation in a skilled area

        :param forced_value:
        :return Int - Total of points:
        """
        points = 0
        if ( self.user_work ):

            # Use given value or search for it
            if forced_value is not None:
                value = forced_value
            else:
                # search for a relative on the current country
                value = ""
                if self.user_work.partner_skills:
                    value = "Yes"

            # search for how many points this answer is worth
            if value == "Yes":
                points = self.__get_points( value, 'description' )

        return points

    def get_invest_points( self, forced_value = None ):
        """
        Points for users who want to invest or open a business at country of destination

        :param forced_value:
        :return Int - Total of points:
        """
        points = 0
        if ( self.user_work ):

            # Use given value or search for it
            if forced_value is not None:
                value = forced_value
            else:
                # search for a relative on the current country
                value = ""
                if self.user_work.willing_to_invest:
                    value = "Yes"

            # search for how many points this answer is worth
            if value == "Yes":
                points = self.__get_points( value, 'description' )

        return points

    def get_startup_letter_points( self, forced_value = None ):
        """
        Points for users who have a letter by a startup venture fund authority in canada

        :param forced_value:
        :return Int - Total of points:
        """
        points = 0
        if ( self.user_work ):

            # Use given value or search for it
            if forced_value is not None:
                value = forced_value
            else:
                # search for a relative on the current country
                value = ""
                if self.user_work.canadian_startup_letter:
                    value = "Yes"

            # search for how many points this answer is worth
            if value == "Yes":
                points = self.__get_points( value, 'description' )

        return points

    def get_us_citizen_points( self, forced_value = None ):
        """
        Points for users who have US Citizenship

        :param forced_value:
        :return Int - Total of points:
        """
        points = 0
        if ( self.user_personal ):

            # Use given value or search for it
            if forced_value is not None:
                value = forced_value
            else:
                # search for a relative on the current country
                value = ""
                if self.user_personal.country_id == settings.ID_COUNTRY_UNITED_STATES:
                    value = "Yes"

            # search for how many points this answer is worth
            if value == "Yes":
                points = self.__get_points( value, 'description' )

        return points

    def get_study_regional_au_points( self, forced_value = None ):
        """
        Points for users who have studied or worked in regional Australia

        :param forced_value:
        :return Int - Total of points:
        """
        points = 0
        if ( self.user_education ):

            # Use given value or search for it
            if forced_value is not None:
                value = forced_value
            else:
                # search for a relative on the current country
                value = ""
                if self.user_education.regional_australia_study:
                    value = "Yes"

            # search for how many points this answer is worth
            if value == "Yes":
                points = self.__get_points( value, 'description' )

        return points

    def get_professional_year_au_points( self, forced_value = None ):
        """
        Points for users who have completed a PROFESIONAL YEAR COURSE in Australia

        :param forced_value:
        :return Int - Total of points:
        """
        points = 0
        if ( self.user_work ):

            # Use given value or search for it
            if forced_value is not None:
                value = forced_value
            else:
                # search for a relative on the current country
                value = ""
                if self.user_work.australian_professional_year:
                    value = "Yes"

            # search for how many points this answer is worth
            if value == "Yes":
                points = self.__get_points( value, 'description' )

        return points

    def get_live_regional_au_points( self, forced_value = None ):
        """
        Points for users who are willing to live in regional Australia

        :param forced_value:
        :return Int - Total of points:
        """
        points = 0
        if ( self.user_personal ):

            # Use given value or search for it
            if forced_value is not None:
                value = forced_value
            else:
                # search for a relative on the current country
                value = ""
                if self.user_personal.australian_regional_immigration:
                    value = "Yes"

            # search for how many points this answer is worth
            if value == "Yes":
                points = self.__get_points( value, 'description' )

        return points

    def get_community_language_au_points( self, forced_value = None ):
        """
        Points for users who can be recognized by NAATI for interpreter/translator in one
        of Australian community languages

        :param forced_value:
        :return Int - Total of points:
        """
        points = 0
        if ( self.user_language ):

            # Use given value or search for it
            if forced_value is not None:
                value = forced_value
            else:
                # search for a relative on the current country
                value = ""
                if self.user_language.australian_community_language:
                    value = "Yes"

            # search for how many points this answer is worth
            if value == "Yes":
                points = self.__get_points( value, 'description' )

        return points


    def get_partner_worked_studied_ca_points( self, forced_value = None ):
        """
        Points for users who have a partner that worked or studied in Canada

        :param forced_value:
        :return Int - Total of points:
        """
        points = 0
        if ( self.user_work ):

            # Use given value or search for it
            if forced_value is not None:
                value = forced_value
            else:
                # search for a relative on the current country
                value = ""
                if self.user_work.canadian_partner_work_study_experience:
                    value = "Yes"

            # search for how many points this answer is worth
            if value == "Yes":
                points = self.__get_points( value, 'description' )

        return points

    def get_partner_english_points( self, forced_value = None ):
        """
        Points for users who have a partner with skill in English

        :param forced_value:
        :return Int - Total of points:
        """
        points = 0
        if self.user_language and self.user_language.partner_english_level_answer:

            # Use given value or search for it
            if forced_value is not None:
                value = forced_value
            else:
                value = self.user_language.partner_english_level_answer.id

            # search for how many points this answer is worth
            points = self.__get_points( value, 'id' )

        return points

    def get_partner_french_points( self, forced_value = None ):
        """
        Points for users who have a partner with skill in French

        :param forced_value:
        :return Int - Total of points:
        """
        points = 0
        if self.user_language and self.user_language.partner_french_level_answer:

            # Use given value or search for it
            if forced_value is not None:
                value = forced_value
            else:
                value = self.user_language.partner_french_level_answer.id

            # search for how many points this answer is worth
            points = self.__get_points( value, 'id' )

        return points

    def get_partner_education_degree_points( self, forced_value = None ):
        """
        Points for users who have a partner with an education degree

        :param forced_value:
        :return Int - Total of points:
        """
        points = 0
        if self.user_education and self.user_education.partner_education_level_answer:

            # Use given value or search for it
            if forced_value is not None:
                value = forced_value
            else:
                value = self.user_education.partner_education_level_answer.id

            # search for how many points this answer is worth
            points = self.__get_points( value, 'id' )

        return points


