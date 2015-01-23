"""
Class responsible to calculate how many points an user scores for each country
that uses tha Points-Based Immigration System.

It will use the database and config settings to determine if the user is allowed
to get the visa or not.
"""

##########################
# Imports
##########################
from wannamigrate.core.models import (
    Country, User, UserEducation,
    UserEducationHistory, UserLanguage, UserLanguageProficiency,
    UserPersonal, UserPersonalFamily, UserWork,
    UserWorkExperience, UserWorkOffer
)
from wannamigrate.points.models import (
    Country, CountryPoints, Question, Answer, UserResult, Occupation, QuestionGroup,
    CountryConfig
)
from wannamigrate.core.util import calculate_age, get_object_or_false, get_list_or_false, date_difference
from django.conf import settings
import inspect
import math




##########################
# Class definitions
##########################
class ImmigrationCalculator( object ):
    """
    Class responsible to make all calculations of immigration points.

    It should grab all user information and compare to the question/answers
    tables so that it can given total of points per country and per area.

    Rules can be found here:

    - Australia: http://www.immi.gov.au/Visas/Pages/189.aspx
    - Canada: http://www.cic.gc.ca/english/express-entry/criteria-crs.asp
    - New Zealand: http://www.immigration.govt.nz/migrant/stream/work/skilledmigrant/caniapply/points/default.htm and https://www.immigration.govt.nz/pointsindicator/

    """

    def __init__( self, user ):
        """
        Constructor responsible to set user and country

        :param: user
        :return: None
        """

        # Instantiate user and country
        self.user = user
        self.country = None

        # Instantiate attribute to store if user's occupation is in demmand or not
        self.occupation_in_demand = False

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

        # Instantiate all questions
        self.question = Question.objects.all()

        # Instantiate all questions_groups
        question_groups = QuestionGroup.objects.all()
        self.question_groups = {}
        for question_group in question_groups:
            if question_group.country_id not in self.question_groups:
                self.question_groups[question_group.country_id] = {}
            if question_group.id not in self.question_groups[question_group.country_id]:
                self.question_groups[question_group.country_id][question_group.id] = {}

            self.question_groups[question_group.country_id][question_group.id]['name'] = question_group.name
            self.question_groups[question_group.country_id][question_group.id]['max_points'] = question_group.max_points
            self.question_groups[question_group.country_id][question_group.id]['questions'] = question_group.questions
            
        # Instantiate all country_config
        country_config = CountryConfig.objects.all()
        self.country_config = {}
        for item in country_config:
            if item.country_id not in self.country_config:
                self.country_config[item.country_id] = {}
            self.country_config[item.country_id]['pass_mark_points'] = item.pass_mark_points


    def __get_points( self, value, type, question_id ):
        """
        Search the table 'core_countrypoints' by the value to localize
        how many points it's worth.

        type needs to be either:
            'id' - the search will be per answer_id
            'description' - the search will be per answer description

        :param: value
        :param: type
        :param: question_id
        :return: Int
        """

        # Get question ID
        method_name = inspect.stack()[1][3] # This give us the name of the parent method calling this one

        # search for question object
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


    def get_total_results( self, country ):
        """
        Calculates the total points for the given user/country.

        If type was given, it will return the total for just those questions
        They can be 'personal', 'language', 'education' or 'work'

        It will return a dictionary with the following total numbers:

        'total', 'personal', 'language', 'education' and 'work'

        :param: country
        :return: Mixed - Int or False on failure
        """

        # Instantiate country
        self.country = country

        # Check if occupation is in demand
        if self.user_work and self.user_work.occupation:
            in_demand = self.user_work.occupation.countries.filter( id = self.country.id ).count()
            if in_demand > 0:
                self.occupation_in_demand = True

        # Initialize totals
        result = {
            'total': 0,
            'personal': 0,
            'language': 0,
            'education': 0,
            'work': 0,
            'user_result_status_id': ''
        }

        # Get points for every question
        question_points = {}
        for question in self.question:

            # call the appropriate method by its name to return the number of points
            points = getattr( self, question.method_name )( question.id )

            # store points per question
            question_points[question.id] = points

        # check maximum points per group (defined differently in each country)
        if self.country.id in self.question_groups:
            for key, question_group in self.question_groups[self.country.id].items():

                # calculate total points obtained from questions of this group
                group_points = 0
                for question in question_group['questions'].all():

                    # sums up total of points for questions in this group
                    group_points += question_points[question.id]

                    # If the maximum points are reached and passed we should subtract from this question points
                    if group_points > question_group['max_points']:
                        question_points[question.id] = question_points[question.id] - ( group_points - question_group['max_points'] )

        # build results by getting points per question
        for question in self.question:
            result['total'] += question_points[question.id]
            result[question.type] += question_points[question.id]

        # get status
        result['user_result_status_id'] = self.get_user_result_status_id( result )

        # return dictionary of results
        return result


    def get_user_result_status_id( self, result ):
        """
        Get status for user_result table

        :param: result
        :return: Int
        """

        # starts with not enough points
        user_result_status_id = settings.ID_RESULT_STATUS_DENIED_POINTS

        # Check if user has enough points for each country
        if result['total'] >= self.country_config[self.country.id]['pass_mark_points']:
            user_result_status_id = settings.ID_RESULT_STATUS_ALLOWED

        # If OCCUPATION is not in demand, we set status for this
        if not self.occupation_in_demand:
            user_result_status_id = settings.ID_RESULT_STATUS_DENIED_OCCUPATION

        # get age to use in minimum requirements check
        age = 0
        if self.user_personal:
            age = calculate_age( self.user_personal.birth_date )

        # get language level to use in minimum requirements check
        english_level_answer_id = 0
        french_level_answer_id = 0
        if self.user_language_proficiency:
            for item in self.user_language_proficiency:
                if item.language_id == settings.ID_LANGUAGE_ENGLISH:
                    english_level_answer_id = item.language_level_answer.id
                if item.language_id == settings.ID_LANGUAGE_FRENCH:
                    french_level_answer_id = item.language_level_answer.id

        # get total years of work experience
        years_of_experience = 0
        if self.user_work_experience and self.user_work and self.user_work.occupation is not None:
            years = 0
            for item in self.user_work_experience:
                years += ( item.months / 12 )
            years_of_experience = math.floor( years )

        # Minimum requirements per country
        if self.country.id == settings.ID_COUNTRY_AUSTRALIA:

            # less than 50 years of age
            if age >= 50:
                user_result_status_id = settings.ID_RESULT_STATUS_DENIED_AGE

            # at least 'competent' english
            if english_level_answer_id < settings.ID_MINIMUM_ENGLISH_LEVEL:
                user_result_status_id = settings.ID_RESULT_STATUS_DENIED_LANGUAGE

        elif self.country.id == settings.ID_COUNTRY_NEW_ZEALAND:

            # at least 'competent' english
            if english_level_answer_id < settings.ID_MINIMUM_ENGLISH_LEVEL:
                user_result_status_id = settings.ID_RESULT_STATUS_DENIED_LANGUAGE

        elif self.country.id == settings.ID_COUNTRY_CANADA:

            # at least 'competent' english or FRENCH
            if english_level_answer_id < settings.ID_MINIMUM_ENGLISH_LEVEL and french_level_answer_id < settings.ID_MINIMUM_FRENCH_LEVEL:
                user_result_status_id = settings.ID_RESULT_STATUS_DENIED_LANGUAGE

            # at least one year of work experience
            if years_of_experience < 1:
                user_result_status_id = settings.ID_RESULT_STATUS_DENIED_WORK_EXPERIENCE

        return user_result_status_id


    def get_family_overseas_points( self, question_id, forced_value = None ):
        """
        Points if user has a close relative living abroad (in canada, australia...)

        :param: question_id
        :param: forced_value
        :return: Int - Total of points
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
                points = self.__get_points( value, 'description', question_id )

        return points


    def get_age_points( self, question_id, forced_value = None ):
        """
        calculate how many points user will get by his age.

        :param: question_id
        :param: forced_value
        :return: Int - Total of points
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
            points = self.__get_points( value, 'description', question_id )

        return points
    

    def get_english_points( self, question_id, forced_value = None ):
        """
        Points for skills with the english language

        :param: question_id
        :param: forced_value
        :return: Int - Total of points
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
                points = self.__get_points( value, 'id', question_id )

        return points
    

    def get_french_points( self, question_id, forced_value = None ):
        """
        Points for skills with the french language

        :param: question_id
        :param: forced_value
        :return: Int - Total of points
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
                points = self.__get_points( value, 'id', question_id )

        return points
    

    def get_language_level_others_points( self, question_id, forced_value = None ):
        """
        Points for skills with Australia community languages

        :param: question_id
        :param: forced_value
        :return: Int - Total of points
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
                    if item.language_id in settings.ID_AUSTRALIAN_COMMUNITY_LANGUAGES:
                        value = item.language_level_answer.id
                        points = self.__get_points( value, 'id', question_id )
                        if points > 0:
                            break

        return points
    

    def get_education_degree_points( self, question_id, forced_value = None ):
        """
        Points for the highest level of education (degree: bacherlor, masters, etc.)

        :param: question_id
        :param: forced_value
        :return: Int - Total of points
        """
        points = 0
        if ( self.user_education_history ):

            # Use given value or search for it
            if forced_value is not None:
                value = forced_value
            else:
                # search for education history
                highest_points = 0
                for item in self.user_education_history:

                    # search for points (we will store only the highest points (highest degree of education)
                    value = item.education_level_answer.id
                    current_points = self.__get_points( value, 'id', question_id )
                    if ( current_points > highest_points ):
                        highest_points = current_points

                points = highest_points

        return points
    

    def get_past_study_country_destination_points( self, question_id, forced_value = None ):
        """
        Points for past studies in country of destination

        :param: question_id
        :param: forced_value
        :return: Int - Total of points
        """
        points = 0
        if ( self.user_education_history ):

            # Use given value or search for it
            if forced_value is not None:
                value = forced_value
            else:
                # search for education history on current country
                value = ""
                for item in self.user_education_history:
                    if item.country_id == self.country.id:
                        value = "Yes"
                        break

            # search for how many points this answer is worth
            if value == "Yes":
                points = self.__get_points( value, 'description', question_id )

        return points
    

    def get_work_offer_points( self, question_id, forced_value = None ):
        """
        Points for users that have a job offer on country of destination

        :param: question_id
        :param: forced_value
        :return: Int - Total of points
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
                points = self.__get_points( value, 'description', question_id )

        return points


    def get_work_experience_outside_points( self, question_id, forced_value = None ):
        """
        Points for work experience gained outside country of destination/

        The occupation must be set and must be on the list of demand for the currenty country

        :param: question_id
        :param: forced_value
        :return: Int - Total of points
        """
        points = 0
        if ( self.user_work_experience and self.user_work and self.user_work.occupation is not None ):

            # Check if occupation is in list of demand
            if self.occupation_in_demand:
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
                    points = self.__get_points( value, 'description', question_id )

        return points


    def get_work_experience_inside_points( self, question_id, forced_value = None ):
        """
        Points for work experience gained at country of destination

        The occupation must be set and must be on the list of demand for the currenty country

        :param: question_id
        :param: forced_value
        :return: Int - Total of points
        """
        points = 0
        if ( self.user_work_experience and self.user_work and self.user_work.occupation is not None ):

            # Check if occupation is in list of demand
            if self.occupation_in_demand:
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
                    points = self.__get_points( value, 'description', question_id )

        return points


    def get_work_experience_total_points( self, question_id, forced_value = None ):
        """
        Points for work experience gained anywhere (total)

        The occupation must be set and must be on the list of demand for the currenty country

        :param: question_id
        :param: forced_value
        :return: Int - Total of points
        """
        points = 0
        if ( self.user_work_experience and self.user_work and self.user_work.occupation is not None ):

            # Check if occupation is in list of demand
            if self.occupation_in_demand:

                # Use given value or search for it
                if forced_value is not None:
                    value = forced_value
                else:
                    # search for all work experiences
                    years_of_experience = 0
                    for item in self.user_work_experience:
                            years_of_experience += ( item.months / 12 )

                    value = math.floor( years_of_experience )

                # search for how many points this answer is worth
                if value > 0:
                    points = self.__get_points( value, 'description', question_id )

        return points


    def get_skilled_partner_points( self, question_id, forced_value = None ):
        """
        Points for users with partners who have a occupation in a skilled area

        :param: question_id
        :param: forced_value
        :return: Int - Total of points
        """
        points = 0
        if ( self.occupation_in_demand and self.user_work ):

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
                points = self.__get_points( value, 'description', question_id )

        return points


    def get_invest_points( self, question_id, forced_value = None ):
        """
        Points for users who want to invest or open a business at country of destination

        :param: question_id
        :param: forced_value
        :return: Int - Total of points
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
                points = self.__get_points( value, 'description', question_id )

        return points


    def get_startup_letter_points( self, question_id, forced_value = None ):
        """
        Points for users who have a letter by a startup venture fund authority in canada

        :param: question_id
        :param: forced_value
        :return: Int - Total of points
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
                points = self.__get_points( value, 'description', question_id )

        return points


    def get_us_citizen_points( self, question_id, forced_value = None ):
        """
        Points for users who have US Citizenship

        :param: question_id
        :param: forced_value
        :return: Int - Total of points
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
                points = self.__get_points( value, 'description', question_id )

        return points


    def get_study_regional_au_points( self, question_id, forced_value = None ):
        """
        Points for users who have studied or worked in regional Australia

        :param: question_id
        :param: forced_value
        :return: Int - Total of points
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
                points = self.__get_points( value, 'description', question_id )

        return points


    def get_professional_year_au_points( self, question_id, forced_value = None ):
        """
        Points for users who have completed a PROFESIONAL YEAR COURSE in Australia

        :param: question_id
        :param: forced_value
        :return: Int - Total of points
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
                points = self.__get_points( value, 'description', question_id )

        return points


    def get_live_regional_au_points( self, question_id, forced_value = None ):
        """
        Points for users who are willing to live in regional Australia

        :param: question_id
        :param: forced_value
        :return: Int - Total of points
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
                points = self.__get_points( value, 'description', question_id )

        return points


    def get_community_language_au_points( self, question_id, forced_value = None ):
        """
        Points for users who can be recognized by NAATI for interpreter/translator in one
        of Australian community languages

        :param: question_id
        :param: forced_value
        :return: Int - Total of points
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
                points = self.__get_points( value, 'description', question_id )

        return points


    def get_partner_worked_studied_ca_points( self, question_id, forced_value = None ):
        """
        Points for users who have a partner that worked or studied in Canada

        :param: question_id
        :param: forced_value
        :return: Int - Total of points
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
                points = self.__get_points( value, 'description', question_id )

        return points


    def get_partner_english_points( self, question_id, forced_value = None ):
        """
        Points for users who have a partner with skill in English

        :param: question_id
        :param: forced_value
        :return: Int - Total of points
        """
        points = 0
        if self.user_language and self.user_language.partner_english_level_answer:

            # Use given value or search for it
            if forced_value is not None:
                value = forced_value
            else:
                value = self.user_language.partner_english_level_answer.id

            # search for how many points this answer is worth
            points = self.__get_points( value, 'id', question_id )

        return points


    def get_partner_french_points( self, question_id, forced_value = None ):
        """
        Points for users who have a partner with skill in French

        :param: question_id
        :param: forced_value
        :return: Int - Total of points
        """
        points = 0
        if self.user_language and self.user_language.partner_french_level_answer:

            # Use given value or search for it
            if forced_value is not None:
                value = forced_value
            else:
                value = self.user_language.partner_french_level_answer.id

            # search for how many points this answer is worth
            points = self.__get_points( value, 'id', question_id )

        return points


    def get_partner_education_degree_points( self, question_id, forced_value = None ):
        """
        Points for users who have a partner with an education degree

        :param: question_id
        :param: forced_value
        :return: Int - Total of points
        """
        points = 0
        if self.user_education and self.user_education.partner_education_level_answer:

            # Use given value or search for it
            if forced_value is not None:
                value = forced_value
            else:
                value = self.user_education.partner_education_level_answer.id

            # search for how many points this answer is worth
            points = self.__get_points( value, 'id', question_id )

        return points