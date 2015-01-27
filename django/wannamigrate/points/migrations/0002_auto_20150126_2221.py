# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

#######################
# OFFICIAL IMMIGRATION POINTS DATABASE RECORDS
#######################
def points_immigration_rules( apps, schema_editor ):


    # Get model to use (historical version)
    Question = apps.get_model( "points", "Question" )
    Answer = apps.get_model( "points", "Answer" )
    CountryPoints = apps.get_model( "points", "CountryPoints" )
    OccupationCategory = apps.get_model( "points", "OccupationCategory" )
    Occupation = apps.get_model( "points", "Occupation" )

    #Questions
    question = Question()
    question.id = 1
    question.description = 'Do you have any family members who are citizens in the country of destination?'
    question.help_text = 'If you have a close family member who lives in CA or AU, as an example, you may get some points'
    question.modified_date = '2014-11-24 21:37:10+00:00'
    question.created_date = '2014-10-14 19:56:11+00:00'
    question.save()

    question = Question()
    question.id = 2
    question.description = 'How old are you?'
    question.help_text = 'test'
    question.modified_date = '2014-11-24 22:31:35+00:00'
    question.created_date = '2014-10-14 19:56:11+00:00'
    question.save()

    question = Question()
    question.id = 3
    question.description = 'What is your English Level?'
    question.help_text = ''
    question.modified_date = '2014-11-24 22:49:25+00:00'
    question.created_date = '2014-10-14 19:56:11+00:00'
    question.save()

    question = Question()
    question.id = 4
    question.description = 'What is your French Level?'
    question.help_text = ''
    question.modified_date = '2014-11-24 22:50:10+00:00'
    question.created_date = '2014-10-14 19:56:11+00:00'
    question.save()

    question = Question()
    question.id = 5
    question.description = 'What is your highest degree of education?'
    question.help_text = 'Phd, Masters, bachelors, etc..'
    question.modified_date = '2014-11-24 23:11:53+00:00'
    question.created_date = '2014-10-14 19:56:11+00:00'
    question.save()

    question = Question()
    question.id = 6
    question.description = 'Do you have a written job offer on country of destination?'
    question.help_text = ''
    question.modified_date = '2014-11-24 23:27:11+00:00'
    question.created_date = '2014-10-14 19:56:11+00:00'
    question.save()

    question = Question()
    question.id = 7
    question.description = 'How many years of experience in a skilled occupation outside country of destination?'
    question.help_text = ''
    question.modified_date = '2014-11-25 00:01:06+00:00'
    question.created_date = '2014-10-14 19:56:11+00:00'
    question.save()

    question = Question()
    question.id = 8
    question.description = 'How many years of experience in a skilled occupation at country of destination?'
    question.help_text = ''
    question.modified_date = '2014-11-25 01:49:27+00:00'
    question.created_date = '2014-10-14 19:56:11+00:00'
    question.save()

    question = Question()
    question.id = 10
    question.description = 'Do you have a high skilled partner?'
    question.help_text = 'partner skills for australia or job offer/occupation for new zealand'
    question.modified_date = '2014-11-25 02:04:11+00:00'
    question.created_date = '2014-10-14 19:56:11+00:00'
    question.save()

    question = Question()
    question.id = 11
    question.description = 'Do you plan to invest or open a business?'
    question.help_text = ''
    question.modified_date = '2014-11-25 02:04:37+00:00'
    question.created_date = '2014-10-14 19:56:11+00:00'
    question.save()

    question = Question()
    question.id = 12
    question.description = 'Do you have a letter of support for a start-up venture from a canadian designated entity?'
    question.help_text = ''
    question.modified_date = '2014-11-25 02:05:34+00:00'
    question.created_date = '2014-10-14 19:56:11+00:00'
    question.save()

    question = Question()
    question.id = 13
    question.description = 'Are You a U.S citizen?'
    question.help_text = ''
    question.modified_date = '2014-11-25 02:06:35+00:00'
    question.created_date = '2014-10-14 19:56:11+00:00'
    question.save()

    question = Question()
    question.id = 14
    question.description = 'Did you study in regional Australia or low population growth metropolitan area?'
    question.help_text = ''
    question.modified_date = '2014-11-25 02:07:16+00:00'
    question.created_date = '2014-10-14 19:56:11+00:00'
    question.save()

    question = Question()
    question.id = 15
    question.description = 'Did you complete a Professional Year (Course) in Australia?'
    question.help_text = ''
    question.modified_date = '2014-11-25 02:07:44+00:00'
    question.created_date = '2014-10-14 19:56:11+00:00'
    question.save()

    question = Question()
    question.id = 16
    question.description = 'Are you willing to live and work in regional Australia?'
    question.help_text = ''
    question.modified_date = '2014-11-25 02:08:59+00:00'
    question.created_date = '2014-10-14 19:56:11+00:00'
    question.save()

    question = Question()
    question.id = 18
    question.description = 'Has your partner worked or studied in Canada?'
    question.help_text = ''
    question.modified_date = '2014-11-25 02:10:03+00:00'
    question.created_date = '2014-10-14 19:56:11+00:00'
    question.save()

    question = Question()
    question.id = 19
    question.description = 'What is your partner English Level?'
    question.help_text = ''
    question.modified_date = '2014-11-25 02:14:20+00:00'
    question.created_date = '2014-10-14 19:56:11+00:00'
    question.save()

    question = Question()
    question.id = 20
    question.description = 'What is your partner French Level?'
    question.help_text = ''
    question.modified_date = '2014-11-25 02:14:46+00:00'
    question.created_date = '2014-10-14 19:56:11+00:00'
    question.save()

    question = Question()
    question.id = 21
    question.description = 'What is your partner level of education?'
    question.help_text = ''
    question.modified_date = '2014-11-25 02:20:05+00:00'
    question.created_date = '2014-10-14 19:56:11+00:00'
    question.save()

    question = Question()
    question.id = 22
    question.description = 'What is your Language Level (Others)?'
    question.help_text = 'Users can add any other language and this is to store the level of it'
    question.modified_date = '2014-11-25 13:17:23+00:00'
    question.created_date = '2014-11-19 18:11:51+00:00'
    question.save()

    question = Question()
    question.id = 23
    question.description = 'Did you complete any studies in country of destination?'
    question.help_text = ''
    question.modified_date = '2014-11-25 03:22:37+00:00'
    question.created_date = '2014-11-24 18:53:15+00:00'
    question.save()

    question = Question()
    question.id = 24
    question.description = 'How many years of experience in a skilled occupation anywhere (totals)?'
    question.help_text = ''
    question.modified_date = '2014-11-24 23:50:57+00:00'
    question.created_date = '2014-11-24 18:53:15+00:00'
    question.save()

#Answers
    answer = Answer()
    answer.id = 1
    answer.description = 'Yes'
    answer.question_id = 1
    answer.modified_date = '2014-11-24 21:37:10+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 2
    answer.description = 'No'
    answer.question_id = 1
    answer.modified_date = '2014-11-24 21:37:10+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 3
    answer.description = '1'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:19+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 4
    answer.description = '2'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:19+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 5
    answer.description = '3'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:19+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 6
    answer.description = '4'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:19+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 7
    answer.description = '5'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:19+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 8
    answer.description = '6'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:19+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 9
    answer.description = '7'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:19+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 10
    answer.description = '8'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:19+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 11
    answer.description = '9'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:19+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 12
    answer.description = '10'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:19+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 13
    answer.description = '11'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:19+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 14
    answer.description = '12'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:19+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 15
    answer.description = '13'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:20+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 16
    answer.description = '14'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:20+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 17
    answer.description = '15'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:20+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 18
    answer.description = '16'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:20+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 19
    answer.description = '17'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:20+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 20
    answer.description = '18'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:30:38+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 21
    answer.description = '19'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:30:38+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 22
    answer.description = '20'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:30:38+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 23
    answer.description = '21'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:30:38+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 24
    answer.description = '22'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:30:38+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 25
    answer.description = '23'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:30:38+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 26
    answer.description = '24'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:30:39+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 27
    answer.description = '25'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:30:39+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 28
    answer.description = '26'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:30:39+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 29
    answer.description = '27'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:30:39+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 30
    answer.description = '28'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:30:39+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 31
    answer.description = '29'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:30:40+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 32
    answer.description = '30'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:30:40+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 33
    answer.description = '31'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:30:40+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 34
    answer.description = '32'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:30:40+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 35
    answer.description = '33'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:30:40+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 36
    answer.description = '34'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:30:40+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 37
    answer.description = '35'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:30:41+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 38
    answer.description = '36'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:31:36+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 39
    answer.description = '37'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:31:37+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 40
    answer.description = '38'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:31:37+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 41
    answer.description = '39'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:31:37+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 42
    answer.description = '40'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:31:37+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 43
    answer.description = '41'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:31:37+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 44
    answer.description = '42'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:31:37+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 45
    answer.description = '43'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:31:38+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 46
    answer.description = '44'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:31:38+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 47
    answer.description = '45'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:31:38+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 48
    answer.description = '46'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:31:38+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 49
    answer.description = '47'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:21+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 50
    answer.description = '48'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:21+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 51
    answer.description = '49'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:21+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 52
    answer.description = '50'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:22+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 53
    answer.description = '51'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:22+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 54
    answer.description = '52'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:22+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 55
    answer.description = '53'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:22+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 56
    answer.description = '54'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:22+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 57
    answer.description = '55'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:22+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 58
    answer.description = '56'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:22+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 59
    answer.description = '57'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:22+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 60
    answer.description = '58'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:22+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 61
    answer.description = '59'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:22+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 62
    answer.description = '60'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:22+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 63
    answer.description = '61'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:22+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 64
    answer.description = '62'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:22+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 65
    answer.description = '63'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:22+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 66
    answer.description = '64'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:22+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 67
    answer.description = '65'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:22+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 68
    answer.description = '66'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:22+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 69
    answer.description = '67'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:22+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 70
    answer.description = '68'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:22+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 71
    answer.description = '69'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:23+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 72
    answer.description = '70'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:23+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 73
    answer.description = '71'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:23+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 74
    answer.description = '72'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:23+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 75
    answer.description = '73'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:23+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 76
    answer.description = '74'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:23+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 77
    answer.description = '75'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:23+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 78
    answer.description = '76'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:23+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 79
    answer.description = '77'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:23+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 80
    answer.description = '78'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:23+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 81
    answer.description = '79'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:23+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 82
    answer.description = '80'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:23+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 83
    answer.description = '81'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:23+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 84
    answer.description = '82'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:23+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 85
    answer.description = '83'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:23+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 86
    answer.description = '84'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:23+00:00'
    answer.created_date = '2014-10-14 19:56:11+00:00'
    answer.save()

    answer = Answer()
    answer.id = 87
    answer.description = '85'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:23+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 88
    answer.description = '86'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:23+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 89
    answer.description = '87'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:23+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 90
    answer.description = '88'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:24+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 91
    answer.description = '89'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:24+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 92
    answer.description = '90'
    answer.question_id = 2
    answer.modified_date = '2014-11-24 22:00:24+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 93
    answer.description = 'None'
    answer.question_id = 3
    answer.modified_date = '2014-11-24 22:49:25+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 94
    answer.description = 'Basic Proficiency'
    answer.question_id = 3
    answer.modified_date = '2014-11-24 22:49:25+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 95
    answer.description = 'Moderate Proficiency'
    answer.question_id = 3
    answer.modified_date = '2014-11-24 22:49:25+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 96
    answer.description = 'High Proficiency'
    answer.question_id = 3
    answer.modified_date = '2014-11-24 22:49:26+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 97
    answer.description = 'None'
    answer.question_id = 4
    answer.modified_date = '2014-11-24 22:50:11+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 98
    answer.description = 'Basic Proficiency'
    answer.question_id = 4
    answer.modified_date = '2014-11-24 22:50:11+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 99
    answer.description = 'Moderate Proficiency'
    answer.question_id = 4
    answer.modified_date = '2014-11-24 22:50:11+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 100
    answer.description = 'High Proficiency'
    answer.question_id = 4
    answer.modified_date = '2014-11-24 22:50:11+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 101
    answer.description = 'None'
    answer.question_id = 5
    answer.modified_date = '2014-11-24 22:59:48+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 102
    answer.description = 'Primary Education'
    answer.question_id = 5
    answer.modified_date = '2014-11-24 22:59:49+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 103
    answer.description = 'Secondary Education - Lower'
    answer.question_id = 5
    answer.modified_date = '2014-11-24 22:59:49+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 104
    answer.description = 'Secondary Education - Upper (High-School)'
    answer.question_id = 5
    answer.modified_date = '2014-11-24 23:11:54+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 105
    answer.description = 'Post Secondary Education (Trades, associate, technical)'
    answer.question_id = 5
    answer.modified_date = '2014-11-24 23:11:54+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 106
    answer.description = 'Recognised by the Assessing Authority'
    answer.question_id = 5
    answer.modified_date = '2014-11-24 22:59:49+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 107
    answer.description = 'Bachelors Level'
    answer.question_id = 5
    answer.modified_date = '2014-11-24 23:11:54+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 108
    answer.description = 'Masters Level'
    answer.question_id = 5
    answer.modified_date = '2014-11-24 23:11:54+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 109
    answer.description = 'Yes'
    answer.question_id = 6
    answer.modified_date = '2014-11-24 23:27:11+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 110
    answer.description = 'No'
    answer.question_id = 6
    answer.modified_date = '2014-11-24 23:27:11+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 111
    answer.description = '1'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:07+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 112
    answer.description = '2'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:07+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 113
    answer.description = '3'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:07+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 114
    answer.description = '4'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:07+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 115
    answer.description = '5'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:07+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 116
    answer.description = '6'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:07+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 117
    answer.description = '7'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:08+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 118
    answer.description = '8'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:08+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 119
    answer.description = '9'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:08+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 120
    answer.description = '10'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:08+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 121
    answer.description = '11'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:08+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 122
    answer.description = '12'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:09+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 123
    answer.description = '13'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:09+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 124
    answer.description = '14'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:09+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 125
    answer.description = '15'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:09+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 126
    answer.description = '16'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:09+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 127
    answer.description = '17'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:09+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 128
    answer.description = '18'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:10+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 129
    answer.description = '19'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:10+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 130
    answer.description = '20'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:10+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 131
    answer.description = '21'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:10+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 132
    answer.description = '22'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:10+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 133
    answer.description = '23'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:10+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 134
    answer.description = '24'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:11+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 135
    answer.description = '25'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:11+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 136
    answer.description = '26'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:11+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 137
    answer.description = '27'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:11+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 138
    answer.description = '28'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:11+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 139
    answer.description = '29'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:12+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 140
    answer.description = '30'
    answer.question_id = 7
    answer.modified_date = '2014-11-25 00:01:12+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 141
    answer.description = '1'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:28+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 142
    answer.description = '2'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:28+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 143
    answer.description = '3'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:28+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 144
    answer.description = '4'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:28+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 145
    answer.description = '5'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:29+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 146
    answer.description = '6'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:29+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 147
    answer.description = '7'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:29+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 148
    answer.description = '8'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:29+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 149
    answer.description = '9'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:29+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 150
    answer.description = '10'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:29+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 151
    answer.description = '11'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:30+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 152
    answer.description = '12'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:30+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 153
    answer.description = '13'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:30+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 154
    answer.description = '14'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:30+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 155
    answer.description = '15'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:30+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 156
    answer.description = '16'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:31+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 157
    answer.description = '17'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:31+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 158
    answer.description = '18'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:31+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 159
    answer.description = '19'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:31+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 160
    answer.description = '20'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:31+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 161
    answer.description = '21'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:31+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 162
    answer.description = '22'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:32+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 163
    answer.description = '23'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:32+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 164
    answer.description = '24'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:32+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 165
    answer.description = '25'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:32+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 166
    answer.description = '26'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:32+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 167
    answer.description = '27'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:32+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 168
    answer.description = '28'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:33+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 169
    answer.description = '29'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:33+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 170
    answer.description = '30'
    answer.question_id = 8
    answer.modified_date = '2014-11-25 01:49:33+00:00'
    answer.created_date = '2014-10-14 19:56:12+00:00'
    answer.save()

    answer = Answer()
    answer.id = 878
    answer.description = 'Yes'
    answer.question_id = 10
    answer.modified_date = '2014-11-25 02:04:11+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 879
    answer.description = 'No'
    answer.question_id = 10
    answer.modified_date = '2014-11-25 02:04:11+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 880
    answer.description = 'Yes'
    answer.question_id = 11
    answer.modified_date = '2014-11-25 02:04:37+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 881
    answer.description = 'No'
    answer.question_id = 11
    answer.modified_date = '2014-11-25 02:04:38+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 882
    answer.description = 'Yes'
    answer.question_id = 12
    answer.modified_date = '2014-11-25 02:05:34+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 883
    answer.description = 'No'
    answer.question_id = 12
    answer.modified_date = '2014-11-25 02:05:34+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 884
    answer.description = 'Yes'
    answer.question_id = 13
    answer.modified_date = '2014-11-25 02:06:35+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 885
    answer.description = 'No'
    answer.question_id = 13
    answer.modified_date = '2014-11-25 02:06:35+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 886
    answer.description = 'Yes'
    answer.question_id = 14
    answer.modified_date = '2014-11-25 02:07:16+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 887
    answer.description = 'No'
    answer.question_id = 14
    answer.modified_date = '2014-11-25 02:07:16+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 888
    answer.description = 'Yes'
    answer.question_id = 15
    answer.modified_date = '2014-11-25 02:07:44+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 889
    answer.description = 'No'
    answer.question_id = 15
    answer.modified_date = '2014-11-25 02:07:44+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 890
    answer.description = 'Yes'
    answer.question_id = 16
    answer.modified_date = '2014-11-25 02:08:59+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 891
    answer.description = 'No'
    answer.question_id = 16
    answer.modified_date = '2014-11-25 02:08:59+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 894
    answer.description = 'Yes'
    answer.question_id = 18
    answer.modified_date = '2014-11-25 02:10:04+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 895
    answer.description = 'No'
    answer.question_id = 18
    answer.modified_date = '2014-11-25 02:10:04+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 896
    answer.description = 'None'
    answer.question_id = 19
    answer.modified_date = '2014-11-25 02:14:20+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 897
    answer.description = 'Basic Proficiency'
    answer.question_id = 19
    answer.modified_date = '2014-11-25 02:14:20+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 898
    answer.description = 'Moderate Proficiency'
    answer.question_id = 19
    answer.modified_date = '2014-11-25 02:14:20+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 899
    answer.description = 'High Proficiency'
    answer.question_id = 19
    answer.modified_date = '2014-11-25 02:14:20+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 900
    answer.description = 'None'
    answer.question_id = 20
    answer.modified_date = '2014-11-25 02:14:46+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 901
    answer.description = 'Basic Proficiency'
    answer.question_id = 20
    answer.modified_date = '2014-11-25 02:14:46+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 902
    answer.description = 'Moderate Proficiency'
    answer.question_id = 20
    answer.modified_date = '2014-11-25 02:14:46+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 903
    answer.description = 'High Proficiency'
    answer.question_id = 20
    answer.modified_date = '2014-11-25 02:14:47+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 904
    answer.description = 'None'
    answer.question_id = 21
    answer.modified_date = '2014-11-25 02:20:05+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 905
    answer.description = 'Primary Education'
    answer.question_id = 21
    answer.modified_date = '2014-11-25 02:20:05+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 906
    answer.description = 'Secondary Education - Lower'
    answer.question_id = 21
    answer.modified_date = '2014-11-25 02:20:05+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 907
    answer.description = 'Secondary Education - Upper (High-School)'
    answer.question_id = 21
    answer.modified_date = '2014-11-25 02:20:05+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 908
    answer.description = 'Post Secondary Education (Trades, associate, technical)'
    answer.question_id = 21
    answer.modified_date = '2014-11-25 02:20:06+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 909
    answer.description = 'Bachelors Level'
    answer.question_id = 21
    answer.modified_date = '2014-11-25 02:20:06+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 910
    answer.description = 'Masters Level'
    answer.question_id = 21
    answer.modified_date = '2014-11-25 02:20:06+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 911
    answer.description = 'Doctoral Level'
    answer.question_id = 21
    answer.modified_date = '2014-11-25 02:20:06+00:00'
    answer.created_date = '2014-10-14 19:56:18+00:00'
    answer.save()

    answer = Answer()
    answer.id = 912
    answer.description = 'None'
    answer.question_id = 22
    answer.modified_date = '2014-11-25 02:22:40+00:00'
    answer.created_date = '2014-11-19 18:11:51+00:00'
    answer.save()

    answer = Answer()
    answer.id = 913
    answer.description = 'Basic Proficiency'
    answer.question_id = 22
    answer.modified_date = '2014-11-25 02:22:40+00:00'
    answer.created_date = '2014-11-19 18:11:51+00:00'
    answer.save()

    answer = Answer()
    answer.id = 914
    answer.description = 'Moderate Proficiency'
    answer.question_id = 22
    answer.modified_date = '2014-11-25 02:22:40+00:00'
    answer.created_date = '2014-11-19 18:11:51+00:00'
    answer.save()

    answer = Answer()
    answer.id = 915
    answer.description = 'High Proficiency'
    answer.question_id = 22
    answer.modified_date = '2014-11-25 13:17:23+00:00'
    answer.created_date = '2014-11-19 18:11:51+00:00'
    answer.save()

    answer = Answer()
    answer.id = 916
    answer.description = 'Yes'
    answer.question_id = 23
    answer.modified_date = '2014-11-25 03:22:37+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 917
    answer.description = 'No'
    answer.question_id = 23
    answer.modified_date = '2014-11-25 03:22:37+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 918
    answer.description = '1'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:50:57+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 919
    answer.description = '2'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:50:57+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 920
    answer.description = '3'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:50:57+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 921
    answer.description = '4'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:50:58+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 922
    answer.description = '5'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:50:58+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 923
    answer.description = '6'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:50:58+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 924
    answer.description = '7'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:50:58+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 925
    answer.description = '8'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:50:58+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 926
    answer.description = '9'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:50:58+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 927
    answer.description = '10'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:50:59+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 928
    answer.description = '11'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:50:59+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 929
    answer.description = '12'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:50:59+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 930
    answer.description = '13'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:50:59+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 931
    answer.description = '14'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:50:59+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 932
    answer.description = '15'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:50:59+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 933
    answer.description = '16'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:51:00+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 934
    answer.description = '17'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:51:00+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 935
    answer.description = '18'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:51:00+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 936
    answer.description = '19'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:51:00+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 937
    answer.description = '20'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:51:00+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 938
    answer.description = '21'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:51:01+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 939
    answer.description = '22'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:51:01+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 940
    answer.description = '23'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:51:01+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 941
    answer.description = '24'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:51:01+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 942
    answer.description = '25'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:51:01+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 943
    answer.description = '26'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:51:01+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 944
    answer.description = '27'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:51:02+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 945
    answer.description = '28'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:51:02+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 946
    answer.description = '29'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:51:02+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 947
    answer.description = '30'
    answer.question_id = 24
    answer.modified_date = '2014-11-24 23:51:02+00:00'
    answer.created_date = '2014-11-24 18:53:15+00:00'
    answer.save()

    answer = Answer()
    answer.id = 948
    answer.description = 'Doctoral Level'
    answer.question_id = 5
    answer.modified_date = '2014-11-24 23:11:54+00:00'
    answer.created_date = '2014-11-24 22:59:50+00:00'
    answer.save()

#CountryPointss
    country_points = CountryPoints()
    country_points.id = 1
    country_points.points = 5
    country_points.answer_id = 1
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 21:37:10+00:00'
    country_points.created_date = '2014-11-24 21:37:10+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 2
    country_points.points = 5
    country_points.answer_id = 1
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 21:37:10+00:00'
    country_points.created_date = '2014-11-24 21:37:10+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 3
    country_points.points = 10
    country_points.answer_id = 1
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 21:37:10+00:00'
    country_points.created_date = '2014-11-24 21:37:10+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 4
    country_points.points = 0
    country_points.answer_id = 2
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 21:37:10+00:00'
    country_points.created_date = '2014-11-24 21:37:10+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 5
    country_points.points = 0
    country_points.answer_id = 2
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 21:37:10+00:00'
    country_points.created_date = '2014-11-24 21:37:10+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 6
    country_points.points = 0
    country_points.answer_id = 2
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 21:37:10+00:00'
    country_points.created_date = '2014-11-24 21:37:10+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 7
    country_points.points = 0
    country_points.answer_id = 3
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 8
    country_points.points = 0
    country_points.answer_id = 3
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 9
    country_points.points = 0
    country_points.answer_id = 3
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 10
    country_points.points = 0
    country_points.answer_id = 4
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 11
    country_points.points = 0
    country_points.answer_id = 4
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 12
    country_points.points = 0
    country_points.answer_id = 4
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 13
    country_points.points = 0
    country_points.answer_id = 5
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 14
    country_points.points = 0
    country_points.answer_id = 5
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 15
    country_points.points = 0
    country_points.answer_id = 5
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 16
    country_points.points = 0
    country_points.answer_id = 6
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 17
    country_points.points = 0
    country_points.answer_id = 6
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 18
    country_points.points = 0
    country_points.answer_id = 6
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 19
    country_points.points = 0
    country_points.answer_id = 7
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 20
    country_points.points = 0
    country_points.answer_id = 7
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 21
    country_points.points = 0
    country_points.answer_id = 7
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 22
    country_points.points = 0
    country_points.answer_id = 8
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 23
    country_points.points = 0
    country_points.answer_id = 8
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 24
    country_points.points = 0
    country_points.answer_id = 8
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 25
    country_points.points = 0
    country_points.answer_id = 9
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 26
    country_points.points = 0
    country_points.answer_id = 9
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 27
    country_points.points = 0
    country_points.answer_id = 9
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 28
    country_points.points = 0
    country_points.answer_id = 10
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 29
    country_points.points = 0
    country_points.answer_id = 10
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 30
    country_points.points = 0
    country_points.answer_id = 10
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 31
    country_points.points = 0
    country_points.answer_id = 11
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 32
    country_points.points = 0
    country_points.answer_id = 11
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 33
    country_points.points = 0
    country_points.answer_id = 11
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 34
    country_points.points = 0
    country_points.answer_id = 12
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 35
    country_points.points = 0
    country_points.answer_id = 12
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 36
    country_points.points = 0
    country_points.answer_id = 12
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 37
    country_points.points = 0
    country_points.answer_id = 13
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 38
    country_points.points = 0
    country_points.answer_id = 13
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 39
    country_points.points = 0
    country_points.answer_id = 13
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:19+00:00'
    country_points.created_date = '2014-11-24 22:00:19+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 40
    country_points.points = 0
    country_points.answer_id = 14
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:20+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 41
    country_points.points = 0
    country_points.answer_id = 14
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:20+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 42
    country_points.points = 0
    country_points.answer_id = 14
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:20+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 43
    country_points.points = 0
    country_points.answer_id = 15
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:20+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 44
    country_points.points = 0
    country_points.answer_id = 15
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:20+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 45
    country_points.points = 0
    country_points.answer_id = 15
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:20+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 46
    country_points.points = 0
    country_points.answer_id = 16
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:20+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 47
    country_points.points = 0
    country_points.answer_id = 16
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:20+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 48
    country_points.points = 0
    country_points.answer_id = 16
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:20+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 49
    country_points.points = 0
    country_points.answer_id = 17
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:20+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 50
    country_points.points = 0
    country_points.answer_id = 17
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:20+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 51
    country_points.points = 0
    country_points.answer_id = 17
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:20+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 52
    country_points.points = 0
    country_points.answer_id = 18
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:20+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 53
    country_points.points = 0
    country_points.answer_id = 18
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:20+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 54
    country_points.points = 0
    country_points.answer_id = 18
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:20+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 55
    country_points.points = 0
    country_points.answer_id = 19
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:20+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 56
    country_points.points = 0
    country_points.answer_id = 19
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:20+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 57
    country_points.points = 0
    country_points.answer_id = 19
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:20+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 58
    country_points.points = 25
    country_points.answer_id = 20
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:30:38+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 59
    country_points.points = 12
    country_points.answer_id = 20
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:30:38+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 60
    country_points.points = 0
    country_points.answer_id = 20
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:30:38+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 61
    country_points.points = 25
    country_points.answer_id = 21
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:30:38+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 62
    country_points.points = 12
    country_points.answer_id = 21
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:30:38+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 63
    country_points.points = 0
    country_points.answer_id = 21
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:30:38+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 64
    country_points.points = 25
    country_points.answer_id = 22
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:30:38+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 65
    country_points.points = 12
    country_points.answer_id = 22
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:30:38+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 66
    country_points.points = 30
    country_points.answer_id = 22
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:30:38+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 67
    country_points.points = 25
    country_points.answer_id = 23
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:30:38+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 68
    country_points.points = 12
    country_points.answer_id = 23
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:30:38+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 69
    country_points.points = 30
    country_points.answer_id = 23
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:30:38+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 70
    country_points.points = 25
    country_points.answer_id = 24
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:30:38+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 71
    country_points.points = 12
    country_points.answer_id = 24
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:30:38+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 72
    country_points.points = 30
    country_points.answer_id = 24
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:30:38+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 73
    country_points.points = 25
    country_points.answer_id = 25
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:30:39+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 74
    country_points.points = 12
    country_points.answer_id = 25
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:30:39+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 75
    country_points.points = 30
    country_points.answer_id = 25
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:30:38+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 76
    country_points.points = 25
    country_points.answer_id = 26
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:30:39+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 77
    country_points.points = 12
    country_points.answer_id = 26
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:30:39+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 78
    country_points.points = 30
    country_points.answer_id = 26
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:30:39+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 79
    country_points.points = 30
    country_points.answer_id = 27
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:30:39+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 80
    country_points.points = 12
    country_points.answer_id = 27
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:30:39+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 81
    country_points.points = 30
    country_points.answer_id = 27
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:30:39+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 82
    country_points.points = 30
    country_points.answer_id = 28
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:30:39+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 83
    country_points.points = 12
    country_points.answer_id = 28
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:30:39+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 84
    country_points.points = 30
    country_points.answer_id = 28
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:30:39+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 85
    country_points.points = 30
    country_points.answer_id = 29
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:30:39+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 86
    country_points.points = 12
    country_points.answer_id = 29
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:30:39+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 87
    country_points.points = 30
    country_points.answer_id = 29
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:30:39+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 88
    country_points.points = 30
    country_points.answer_id = 30
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:30:39+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 89
    country_points.points = 12
    country_points.answer_id = 30
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:30:39+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 90
    country_points.points = 30
    country_points.answer_id = 30
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:30:39+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 91
    country_points.points = 30
    country_points.answer_id = 31
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:30:40+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 92
    country_points.points = 12
    country_points.answer_id = 31
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:30:40+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 93
    country_points.points = 30
    country_points.answer_id = 31
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:30:40+00:00'
    country_points.created_date = '2014-11-24 22:00:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 94
    country_points.points = 30
    country_points.answer_id = 32
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:30:40+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 95
    country_points.points = 12
    country_points.answer_id = 32
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:30:40+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 96
    country_points.points = 25
    country_points.answer_id = 32
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:30:40+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 97
    country_points.points = 30
    country_points.answer_id = 33
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:30:40+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 98
    country_points.points = 12
    country_points.answer_id = 33
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:30:40+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 99
    country_points.points = 25
    country_points.answer_id = 33
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:30:40+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 100
    country_points.points = 30
    country_points.answer_id = 34
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:30:40+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 101
    country_points.points = 12
    country_points.answer_id = 34
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:30:40+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 102
    country_points.points = 25
    country_points.answer_id = 34
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:30:40+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 103
    country_points.points = 25
    country_points.answer_id = 35
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:30:40+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 104
    country_points.points = 12
    country_points.answer_id = 35
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:30:40+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 105
    country_points.points = 25
    country_points.answer_id = 35
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:30:40+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 106
    country_points.points = 25
    country_points.answer_id = 36
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:30:40+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 107
    country_points.points = 12
    country_points.answer_id = 36
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:30:40+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 108
    country_points.points = 25
    country_points.answer_id = 36
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:30:40+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 109
    country_points.points = 25
    country_points.answer_id = 37
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:30:41+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 110
    country_points.points = 12
    country_points.answer_id = 37
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:30:41+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 111
    country_points.points = 25
    country_points.answer_id = 37
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:30:41+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 112
    country_points.points = 25
    country_points.answer_id = 38
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:31:37+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 113
    country_points.points = 11
    country_points.answer_id = 38
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:31:37+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 114
    country_points.points = 25
    country_points.answer_id = 38
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:31:36+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 115
    country_points.points = 25
    country_points.answer_id = 39
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:31:37+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 116
    country_points.points = 10
    country_points.answer_id = 39
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:31:37+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 117
    country_points.points = 25
    country_points.answer_id = 39
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:31:37+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 118
    country_points.points = 25
    country_points.answer_id = 40
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:31:37+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 119
    country_points.points = 9
    country_points.answer_id = 40
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:31:37+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 120
    country_points.points = 25
    country_points.answer_id = 40
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:31:37+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 121
    country_points.points = 25
    country_points.answer_id = 41
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:31:37+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 122
    country_points.points = 8
    country_points.answer_id = 41
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:31:37+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 123
    country_points.points = 25
    country_points.answer_id = 41
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:31:37+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 124
    country_points.points = 15
    country_points.answer_id = 42
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:31:37+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 125
    country_points.points = 7
    country_points.answer_id = 42
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:31:37+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 126
    country_points.points = 20
    country_points.answer_id = 42
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:31:37+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 127
    country_points.points = 15
    country_points.answer_id = 43
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:31:37+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 128
    country_points.points = 6
    country_points.answer_id = 43
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:31:37+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 129
    country_points.points = 20
    country_points.answer_id = 43
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:31:37+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 130
    country_points.points = 15
    country_points.answer_id = 44
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:31:38+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 131
    country_points.points = 5
    country_points.answer_id = 44
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:31:38+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 132
    country_points.points = 20
    country_points.answer_id = 44
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:31:38+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 133
    country_points.points = 15
    country_points.answer_id = 45
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:31:38+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 134
    country_points.points = 4
    country_points.answer_id = 45
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:31:38+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 135
    country_points.points = 20
    country_points.answer_id = 45
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:31:38+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 136
    country_points.points = 15
    country_points.answer_id = 46
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:31:38+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 137
    country_points.points = 3
    country_points.answer_id = 46
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:31:38+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 138
    country_points.points = 20
    country_points.answer_id = 46
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:31:38+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 139
    country_points.points = 0
    country_points.answer_id = 47
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:31:38+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 140
    country_points.points = 2
    country_points.answer_id = 47
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:31:38+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 141
    country_points.points = 10
    country_points.answer_id = 47
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:31:38+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 142
    country_points.points = 0
    country_points.answer_id = 48
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:31:38+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 143
    country_points.points = 1
    country_points.answer_id = 48
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:31:38+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 144
    country_points.points = 10
    country_points.answer_id = 48
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:31:38+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 145
    country_points.points = 0
    country_points.answer_id = 49
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:21+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 146
    country_points.points = 0
    country_points.answer_id = 49
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:21+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 147
    country_points.points = 10
    country_points.answer_id = 49
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:21+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 148
    country_points.points = 0
    country_points.answer_id = 50
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:21+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 149
    country_points.points = 0
    country_points.answer_id = 50
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:21+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 150
    country_points.points = 10
    country_points.answer_id = 50
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:21+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 151
    country_points.points = 0
    country_points.answer_id = 51
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:21+00:00'
    country_points.created_date = '2014-11-24 22:00:21+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 152
    country_points.points = 0
    country_points.answer_id = 51
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 153
    country_points.points = 10
    country_points.answer_id = 51
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 154
    country_points.points = 0
    country_points.answer_id = 52
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 155
    country_points.points = 0
    country_points.answer_id = 52
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 156
    country_points.points = 5
    country_points.answer_id = 52
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 157
    country_points.points = 0
    country_points.answer_id = 53
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 158
    country_points.points = 0
    country_points.answer_id = 53
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 159
    country_points.points = 5
    country_points.answer_id = 53
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 160
    country_points.points = 0
    country_points.answer_id = 54
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 161
    country_points.points = 0
    country_points.answer_id = 54
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 162
    country_points.points = 5
    country_points.answer_id = 54
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 163
    country_points.points = 0
    country_points.answer_id = 55
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 164
    country_points.points = 0
    country_points.answer_id = 55
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 165
    country_points.points = 5
    country_points.answer_id = 55
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 166
    country_points.points = 0
    country_points.answer_id = 56
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 167
    country_points.points = 0
    country_points.answer_id = 56
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 168
    country_points.points = 5
    country_points.answer_id = 56
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 169
    country_points.points = 0
    country_points.answer_id = 57
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 170
    country_points.points = 0
    country_points.answer_id = 57
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 171
    country_points.points = 5
    country_points.answer_id = 57
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 172
    country_points.points = 0
    country_points.answer_id = 58
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 173
    country_points.points = 0
    country_points.answer_id = 58
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 174
    country_points.points = 0
    country_points.answer_id = 58
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 175
    country_points.points = 0
    country_points.answer_id = 59
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 176
    country_points.points = 0
    country_points.answer_id = 59
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 177
    country_points.points = 0
    country_points.answer_id = 59
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 178
    country_points.points = 0
    country_points.answer_id = 60
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 179
    country_points.points = 0
    country_points.answer_id = 60
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 180
    country_points.points = 0
    country_points.answer_id = 60
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 181
    country_points.points = 0
    country_points.answer_id = 61
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 182
    country_points.points = 0
    country_points.answer_id = 61
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 183
    country_points.points = 0
    country_points.answer_id = 61
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 184
    country_points.points = 0
    country_points.answer_id = 62
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 185
    country_points.points = 0
    country_points.answer_id = 62
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 186
    country_points.points = 0
    country_points.answer_id = 62
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 187
    country_points.points = 0
    country_points.answer_id = 63
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 188
    country_points.points = 0
    country_points.answer_id = 63
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 189
    country_points.points = 0
    country_points.answer_id = 63
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 190
    country_points.points = 0
    country_points.answer_id = 64
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 191
    country_points.points = 0
    country_points.answer_id = 64
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 192
    country_points.points = 0
    country_points.answer_id = 64
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 193
    country_points.points = 0
    country_points.answer_id = 65
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 194
    country_points.points = 0
    country_points.answer_id = 65
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 195
    country_points.points = 0
    country_points.answer_id = 65
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 196
    country_points.points = 0
    country_points.answer_id = 66
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 197
    country_points.points = 0
    country_points.answer_id = 66
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 198
    country_points.points = 0
    country_points.answer_id = 66
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 199
    country_points.points = 0
    country_points.answer_id = 67
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 200
    country_points.points = 0
    country_points.answer_id = 67
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 201
    country_points.points = 0
    country_points.answer_id = 67
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 202
    country_points.points = 0
    country_points.answer_id = 68
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 203
    country_points.points = 0
    country_points.answer_id = 68
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 204
    country_points.points = 0
    country_points.answer_id = 68
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 205
    country_points.points = 0
    country_points.answer_id = 69
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 206
    country_points.points = 0
    country_points.answer_id = 69
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 207
    country_points.points = 0
    country_points.answer_id = 69
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 208
    country_points.points = 0
    country_points.answer_id = 70
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 209
    country_points.points = 0
    country_points.answer_id = 70
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 210
    country_points.points = 0
    country_points.answer_id = 70
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:22+00:00'
    country_points.created_date = '2014-11-24 22:00:22+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 211
    country_points.points = 0
    country_points.answer_id = 71
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 212
    country_points.points = 0
    country_points.answer_id = 71
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 213
    country_points.points = 0
    country_points.answer_id = 71
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 214
    country_points.points = 0
    country_points.answer_id = 72
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 215
    country_points.points = 0
    country_points.answer_id = 72
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 216
    country_points.points = 0
    country_points.answer_id = 72
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 217
    country_points.points = 0
    country_points.answer_id = 73
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 218
    country_points.points = 0
    country_points.answer_id = 73
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 219
    country_points.points = 0
    country_points.answer_id = 73
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 220
    country_points.points = 0
    country_points.answer_id = 74
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 221
    country_points.points = 0
    country_points.answer_id = 74
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 222
    country_points.points = 0
    country_points.answer_id = 74
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 223
    country_points.points = 0
    country_points.answer_id = 75
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 224
    country_points.points = 0
    country_points.answer_id = 75
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 225
    country_points.points = 0
    country_points.answer_id = 75
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 226
    country_points.points = 0
    country_points.answer_id = 76
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 227
    country_points.points = 0
    country_points.answer_id = 76
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 228
    country_points.points = 0
    country_points.answer_id = 76
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 229
    country_points.points = 0
    country_points.answer_id = 77
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 230
    country_points.points = 0
    country_points.answer_id = 77
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 231
    country_points.points = 0
    country_points.answer_id = 77
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 232
    country_points.points = 0
    country_points.answer_id = 78
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 233
    country_points.points = 0
    country_points.answer_id = 78
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 234
    country_points.points = 0
    country_points.answer_id = 78
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 235
    country_points.points = 0
    country_points.answer_id = 79
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 236
    country_points.points = 0
    country_points.answer_id = 79
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 237
    country_points.points = 0
    country_points.answer_id = 79
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 238
    country_points.points = 0
    country_points.answer_id = 80
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 239
    country_points.points = 0
    country_points.answer_id = 80
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 240
    country_points.points = 0
    country_points.answer_id = 80
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 241
    country_points.points = 0
    country_points.answer_id = 81
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 242
    country_points.points = 0
    country_points.answer_id = 81
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 243
    country_points.points = 0
    country_points.answer_id = 81
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 244
    country_points.points = 0
    country_points.answer_id = 82
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 245
    country_points.points = 0
    country_points.answer_id = 82
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 246
    country_points.points = 0
    country_points.answer_id = 82
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 247
    country_points.points = 0
    country_points.answer_id = 83
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 248
    country_points.points = 0
    country_points.answer_id = 83
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 249
    country_points.points = 0
    country_points.answer_id = 83
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 250
    country_points.points = 0
    country_points.answer_id = 84
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 251
    country_points.points = 0
    country_points.answer_id = 84
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 252
    country_points.points = 0
    country_points.answer_id = 84
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 253
    country_points.points = 0
    country_points.answer_id = 85
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 254
    country_points.points = 0
    country_points.answer_id = 85
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 255
    country_points.points = 0
    country_points.answer_id = 85
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 256
    country_points.points = 0
    country_points.answer_id = 86
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 257
    country_points.points = 0
    country_points.answer_id = 86
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 258
    country_points.points = 0
    country_points.answer_id = 86
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 259
    country_points.points = 0
    country_points.answer_id = 87
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 260
    country_points.points = 0
    country_points.answer_id = 87
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 261
    country_points.points = 0
    country_points.answer_id = 87
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 262
    country_points.points = 0
    country_points.answer_id = 88
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 263
    country_points.points = 0
    country_points.answer_id = 88
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 264
    country_points.points = 0
    country_points.answer_id = 88
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 265
    country_points.points = 0
    country_points.answer_id = 89
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 266
    country_points.points = 0
    country_points.answer_id = 89
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 267
    country_points.points = 0
    country_points.answer_id = 89
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:23+00:00'
    country_points.created_date = '2014-11-24 22:00:23+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 268
    country_points.points = 0
    country_points.answer_id = 90
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:24+00:00'
    country_points.created_date = '2014-11-24 22:00:24+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 269
    country_points.points = 0
    country_points.answer_id = 90
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:24+00:00'
    country_points.created_date = '2014-11-24 22:00:24+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 270
    country_points.points = 0
    country_points.answer_id = 90
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:24+00:00'
    country_points.created_date = '2014-11-24 22:00:24+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 271
    country_points.points = 0
    country_points.answer_id = 91
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:24+00:00'
    country_points.created_date = '2014-11-24 22:00:24+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 272
    country_points.points = 0
    country_points.answer_id = 91
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:24+00:00'
    country_points.created_date = '2014-11-24 22:00:24+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 273
    country_points.points = 0
    country_points.answer_id = 91
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:24+00:00'
    country_points.created_date = '2014-11-24 22:00:24+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 274
    country_points.points = 0
    country_points.answer_id = 92
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:00:24+00:00'
    country_points.created_date = '2014-11-24 22:00:24+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 275
    country_points.points = 0
    country_points.answer_id = 92
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:00:24+00:00'
    country_points.created_date = '2014-11-24 22:00:24+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 276
    country_points.points = 0
    country_points.answer_id = 92
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:00:24+00:00'
    country_points.created_date = '2014-11-24 22:00:24+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 277
    country_points.points = 0
    country_points.answer_id = 93
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:49:25+00:00'
    country_points.created_date = '2014-11-24 22:49:25+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 278
    country_points.points = 0
    country_points.answer_id = 93
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:49:25+00:00'
    country_points.created_date = '2014-11-24 22:49:25+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 279
    country_points.points = 0
    country_points.answer_id = 93
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:49:25+00:00'
    country_points.created_date = '2014-11-24 22:49:25+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 280
    country_points.points = 0
    country_points.answer_id = 94
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:49:25+00:00'
    country_points.created_date = '2014-11-24 22:49:25+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 281
    country_points.points = 0
    country_points.answer_id = 94
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:49:25+00:00'
    country_points.created_date = '2014-11-24 22:49:25+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 282
    country_points.points = 16
    country_points.answer_id = 94
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:49:25+00:00'
    country_points.created_date = '2014-11-24 22:49:25+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 283
    country_points.points = 0
    country_points.answer_id = 95
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:49:26+00:00'
    country_points.created_date = '2014-11-24 22:49:26+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 284
    country_points.points = 10
    country_points.answer_id = 95
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:49:26+00:00'
    country_points.created_date = '2014-11-24 22:49:26+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 285
    country_points.points = 20
    country_points.answer_id = 95
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:49:26+00:00'
    country_points.created_date = '2014-11-24 22:49:26+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 286
    country_points.points = 0
    country_points.answer_id = 96
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:49:26+00:00'
    country_points.created_date = '2014-11-24 22:49:26+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 287
    country_points.points = 20
    country_points.answer_id = 96
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:49:26+00:00'
    country_points.created_date = '2014-11-24 22:49:26+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 288
    country_points.points = 24
    country_points.answer_id = 96
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:49:26+00:00'
    country_points.created_date = '2014-11-24 22:49:26+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 289
    country_points.points = 0
    country_points.answer_id = 97
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:50:11+00:00'
    country_points.created_date = '2014-11-24 22:50:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 290
    country_points.points = 0
    country_points.answer_id = 97
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:50:11+00:00'
    country_points.created_date = '2014-11-24 22:50:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 291
    country_points.points = 0
    country_points.answer_id = 97
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:50:11+00:00'
    country_points.created_date = '2014-11-24 22:50:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 292
    country_points.points = 0
    country_points.answer_id = 98
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:50:11+00:00'
    country_points.created_date = '2014-11-24 22:50:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 293
    country_points.points = 16
    country_points.answer_id = 98
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:50:11+00:00'
    country_points.created_date = '2014-11-24 22:50:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 294
    country_points.points = 0
    country_points.answer_id = 98
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:50:11+00:00'
    country_points.created_date = '2014-11-24 22:50:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 295
    country_points.points = 0
    country_points.answer_id = 99
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:50:11+00:00'
    country_points.created_date = '2014-11-24 22:50:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 296
    country_points.points = 20
    country_points.answer_id = 99
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:50:11+00:00'
    country_points.created_date = '2014-11-24 22:50:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 297
    country_points.points = 0
    country_points.answer_id = 99
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:50:11+00:00'
    country_points.created_date = '2014-11-24 22:50:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 298
    country_points.points = 0
    country_points.answer_id = 100
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:50:11+00:00'
    country_points.created_date = '2014-11-24 22:50:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 299
    country_points.points = 24
    country_points.answer_id = 100
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:50:11+00:00'
    country_points.created_date = '2014-11-24 22:50:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 300
    country_points.points = 0
    country_points.answer_id = 100
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:50:11+00:00'
    country_points.created_date = '2014-11-24 22:50:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 301
    country_points.points = 0
    country_points.answer_id = 101
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:59:48+00:00'
    country_points.created_date = '2014-11-24 22:59:48+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 302
    country_points.points = 0
    country_points.answer_id = 101
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:59:49+00:00'
    country_points.created_date = '2014-11-24 22:59:49+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 303
    country_points.points = 0
    country_points.answer_id = 101
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:59:49+00:00'
    country_points.created_date = '2014-11-24 22:59:49+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 304
    country_points.points = 0
    country_points.answer_id = 102
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:59:49+00:00'
    country_points.created_date = '2014-11-24 22:59:49+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 305
    country_points.points = 0
    country_points.answer_id = 102
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:59:49+00:00'
    country_points.created_date = '2014-11-24 22:59:49+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 306
    country_points.points = 0
    country_points.answer_id = 102
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:59:49+00:00'
    country_points.created_date = '2014-11-24 22:59:49+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 307
    country_points.points = 0
    country_points.answer_id = 103
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:59:49+00:00'
    country_points.created_date = '2014-11-24 22:59:49+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 308
    country_points.points = 0
    country_points.answer_id = 103
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:59:49+00:00'
    country_points.created_date = '2014-11-24 22:59:49+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 309
    country_points.points = 0
    country_points.answer_id = 103
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:59:49+00:00'
    country_points.created_date = '2014-11-24 22:59:49+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 310
    country_points.points = 0
    country_points.answer_id = 104
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:11:54+00:00'
    country_points.created_date = '2014-11-24 22:59:49+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 311
    country_points.points = 0
    country_points.answer_id = 104
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:11:54+00:00'
    country_points.created_date = '2014-11-24 22:59:49+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 312
    country_points.points = 5
    country_points.answer_id = 104
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:11:54+00:00'
    country_points.created_date = '2014-11-24 22:59:49+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 313
    country_points.points = 40
    country_points.answer_id = 105
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:11:54+00:00'
    country_points.created_date = '2014-11-24 22:59:49+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 314
    country_points.points = 10
    country_points.answer_id = 105
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:11:54+00:00'
    country_points.created_date = '2014-11-24 22:59:49+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 315
    country_points.points = 17
    country_points.answer_id = 105
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:11:54+00:00'
    country_points.created_date = '2014-11-24 22:59:49+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 316
    country_points.points = 0
    country_points.answer_id = 106
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 22:59:49+00:00'
    country_points.created_date = '2014-11-24 22:59:49+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 317
    country_points.points = 10
    country_points.answer_id = 106
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 22:59:49+00:00'
    country_points.created_date = '2014-11-24 22:59:49+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 318
    country_points.points = 0
    country_points.answer_id = 106
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 22:59:49+00:00'
    country_points.created_date = '2014-11-24 22:59:49+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 319
    country_points.points = 50
    country_points.answer_id = 107
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:11:54+00:00'
    country_points.created_date = '2014-11-24 22:59:50+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 320
    country_points.points = 15
    country_points.answer_id = 107
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:11:54+00:00'
    country_points.created_date = '2014-11-24 22:59:50+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 321
    country_points.points = 21
    country_points.answer_id = 107
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:11:54+00:00'
    country_points.created_date = '2014-11-24 22:59:50+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 322
    country_points.points = 60
    country_points.answer_id = 108
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:11:54+00:00'
    country_points.created_date = '2014-11-24 22:59:50+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 323
    country_points.points = 15
    country_points.answer_id = 108
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:11:54+00:00'
    country_points.created_date = '2014-11-24 22:59:50+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 324
    country_points.points = 23
    country_points.answer_id = 108
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:11:54+00:00'
    country_points.created_date = '2014-11-24 22:59:50+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 325
    country_points.points = 60
    country_points.answer_id = 948
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:11:55+00:00'
    country_points.created_date = '2014-11-24 22:59:50+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 326
    country_points.points = 20
    country_points.answer_id = 948
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:11:54+00:00'
    country_points.created_date = '2014-11-24 22:59:50+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 327
    country_points.points = 25
    country_points.answer_id = 948
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:11:55+00:00'
    country_points.created_date = '2014-11-24 22:59:50+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 328
    country_points.points = 0
    country_points.answer_id = 109
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:27:11+00:00'
    country_points.created_date = '2014-11-24 23:27:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 329
    country_points.points = 10
    country_points.answer_id = 109
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:27:11+00:00'
    country_points.created_date = '2014-11-24 23:27:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 330
    country_points.points = 50
    country_points.answer_id = 109
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:27:11+00:00'
    country_points.created_date = '2014-11-24 23:27:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 331
    country_points.points = 0
    country_points.answer_id = 110
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:27:11+00:00'
    country_points.created_date = '2014-11-24 23:27:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 332
    country_points.points = 0
    country_points.answer_id = 110
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:27:11+00:00'
    country_points.created_date = '2014-11-24 23:27:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 333
    country_points.points = 0
    country_points.answer_id = 110
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:27:11+00:00'
    country_points.created_date = '2014-11-24 23:27:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 334
    country_points.points = 0
    country_points.answer_id = 111
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:07+00:00'
    country_points.created_date = '2014-11-24 23:35:08+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 335
    country_points.points = 0
    country_points.answer_id = 111
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:07+00:00'
    country_points.created_date = '2014-11-24 23:35:08+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 336
    country_points.points = 0
    country_points.answer_id = 111
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:07+00:00'
    country_points.created_date = '2014-11-24 23:35:08+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 337
    country_points.points = 0
    country_points.answer_id = 112
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:07+00:00'
    country_points.created_date = '2014-11-24 23:35:08+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 338
    country_points.points = 0
    country_points.answer_id = 112
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:07+00:00'
    country_points.created_date = '2014-11-24 23:35:08+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 339
    country_points.points = 0
    country_points.answer_id = 112
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:07+00:00'
    country_points.created_date = '2014-11-24 23:35:08+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 340
    country_points.points = 0
    country_points.answer_id = 113
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:07+00:00'
    country_points.created_date = '2014-11-24 23:35:08+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 341
    country_points.points = 5
    country_points.answer_id = 113
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:07+00:00'
    country_points.created_date = '2014-11-24 23:35:08+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 342
    country_points.points = 0
    country_points.answer_id = 113
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:07+00:00'
    country_points.created_date = '2014-11-24 23:35:08+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 343
    country_points.points = 0
    country_points.answer_id = 114
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:07+00:00'
    country_points.created_date = '2014-11-24 23:35:09+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 344
    country_points.points = 5
    country_points.answer_id = 114
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:07+00:00'
    country_points.created_date = '2014-11-24 23:35:09+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 345
    country_points.points = 0
    country_points.answer_id = 114
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:07+00:00'
    country_points.created_date = '2014-11-24 23:35:09+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 346
    country_points.points = 0
    country_points.answer_id = 115
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:07+00:00'
    country_points.created_date = '2014-11-24 23:35:09+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 347
    country_points.points = 10
    country_points.answer_id = 115
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:07+00:00'
    country_points.created_date = '2014-11-24 23:35:09+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 348
    country_points.points = 0
    country_points.answer_id = 115
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:07+00:00'
    country_points.created_date = '2014-11-24 23:35:09+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 349
    country_points.points = 0
    country_points.answer_id = 116
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:08+00:00'
    country_points.created_date = '2014-11-24 23:35:09+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 350
    country_points.points = 10
    country_points.answer_id = 116
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:08+00:00'
    country_points.created_date = '2014-11-24 23:35:09+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 351
    country_points.points = 0
    country_points.answer_id = 116
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:08+00:00'
    country_points.created_date = '2014-11-24 23:35:09+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 352
    country_points.points = 0
    country_points.answer_id = 117
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:08+00:00'
    country_points.created_date = '2014-11-24 23:35:09+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 353
    country_points.points = 10
    country_points.answer_id = 117
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:08+00:00'
    country_points.created_date = '2014-11-24 23:35:09+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 354
    country_points.points = 0
    country_points.answer_id = 117
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:08+00:00'
    country_points.created_date = '2014-11-24 23:35:09+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 355
    country_points.points = 0
    country_points.answer_id = 118
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:08+00:00'
    country_points.created_date = '2014-11-24 23:35:09+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 356
    country_points.points = 15
    country_points.answer_id = 118
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:08+00:00'
    country_points.created_date = '2014-11-24 23:35:09+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 357
    country_points.points = 0
    country_points.answer_id = 118
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:08+00:00'
    country_points.created_date = '2014-11-24 23:35:09+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 358
    country_points.points = 0
    country_points.answer_id = 119
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:08+00:00'
    country_points.created_date = '2014-11-24 23:35:09+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 359
    country_points.points = 15
    country_points.answer_id = 119
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:08+00:00'
    country_points.created_date = '2014-11-24 23:35:09+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 360
    country_points.points = 0
    country_points.answer_id = 119
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:08+00:00'
    country_points.created_date = '2014-11-24 23:35:10+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 361
    country_points.points = 0
    country_points.answer_id = 120
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:08+00:00'
    country_points.created_date = '2014-11-24 23:35:10+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 362
    country_points.points = 15
    country_points.answer_id = 120
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:08+00:00'
    country_points.created_date = '2014-11-24 23:35:10+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 363
    country_points.points = 0
    country_points.answer_id = 120
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:08+00:00'
    country_points.created_date = '2014-11-24 23:35:10+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 364
    country_points.points = 0
    country_points.answer_id = 121
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:08+00:00'
    country_points.created_date = '2014-11-24 23:35:10+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 365
    country_points.points = 15
    country_points.answer_id = 121
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:09+00:00'
    country_points.created_date = '2014-11-24 23:35:10+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 366
    country_points.points = 0
    country_points.answer_id = 121
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:08+00:00'
    country_points.created_date = '2014-11-24 23:35:10+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 367
    country_points.points = 0
    country_points.answer_id = 122
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:09+00:00'
    country_points.created_date = '2014-11-24 23:35:10+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 368
    country_points.points = 15
    country_points.answer_id = 122
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:09+00:00'
    country_points.created_date = '2014-11-24 23:35:10+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 369
    country_points.points = 0
    country_points.answer_id = 122
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:09+00:00'
    country_points.created_date = '2014-11-24 23:35:10+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 370
    country_points.points = 0
    country_points.answer_id = 123
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:09+00:00'
    country_points.created_date = '2014-11-24 23:35:10+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 371
    country_points.points = 15
    country_points.answer_id = 123
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:09+00:00'
    country_points.created_date = '2014-11-24 23:35:10+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 372
    country_points.points = 0
    country_points.answer_id = 123
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:09+00:00'
    country_points.created_date = '2014-11-24 23:35:10+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 373
    country_points.points = 0
    country_points.answer_id = 124
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:09+00:00'
    country_points.created_date = '2014-11-24 23:35:10+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 374
    country_points.points = 15
    country_points.answer_id = 124
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:09+00:00'
    country_points.created_date = '2014-11-24 23:35:10+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 375
    country_points.points = 0
    country_points.answer_id = 124
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:09+00:00'
    country_points.created_date = '2014-11-24 23:35:10+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 376
    country_points.points = 0
    country_points.answer_id = 125
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:09+00:00'
    country_points.created_date = '2014-11-24 23:35:10+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 377
    country_points.points = 15
    country_points.answer_id = 125
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:09+00:00'
    country_points.created_date = '2014-11-24 23:35:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 378
    country_points.points = 0
    country_points.answer_id = 125
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:09+00:00'
    country_points.created_date = '2014-11-24 23:35:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 379
    country_points.points = 0
    country_points.answer_id = 126
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:09+00:00'
    country_points.created_date = '2014-11-24 23:35:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 380
    country_points.points = 15
    country_points.answer_id = 126
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:09+00:00'
    country_points.created_date = '2014-11-24 23:35:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 381
    country_points.points = 0
    country_points.answer_id = 126
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:09+00:00'
    country_points.created_date = '2014-11-24 23:35:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 382
    country_points.points = 0
    country_points.answer_id = 127
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:09+00:00'
    country_points.created_date = '2014-11-24 23:35:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 383
    country_points.points = 15
    country_points.answer_id = 127
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:10+00:00'
    country_points.created_date = '2014-11-24 23:35:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 384
    country_points.points = 0
    country_points.answer_id = 127
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:10+00:00'
    country_points.created_date = '2014-11-24 23:35:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 385
    country_points.points = 0
    country_points.answer_id = 128
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:10+00:00'
    country_points.created_date = '2014-11-24 23:35:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 386
    country_points.points = 15
    country_points.answer_id = 128
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:10+00:00'
    country_points.created_date = '2014-11-24 23:35:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 387
    country_points.points = 0
    country_points.answer_id = 128
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:10+00:00'
    country_points.created_date = '2014-11-24 23:35:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 388
    country_points.points = 0
    country_points.answer_id = 129
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:10+00:00'
    country_points.created_date = '2014-11-24 23:35:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 389
    country_points.points = 15
    country_points.answer_id = 129
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:10+00:00'
    country_points.created_date = '2014-11-24 23:35:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 390
    country_points.points = 0
    country_points.answer_id = 129
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:10+00:00'
    country_points.created_date = '2014-11-24 23:35:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 391
    country_points.points = 0
    country_points.answer_id = 130
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:10+00:00'
    country_points.created_date = '2014-11-24 23:35:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 392
    country_points.points = 15
    country_points.answer_id = 130
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:10+00:00'
    country_points.created_date = '2014-11-24 23:35:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 393
    country_points.points = 0
    country_points.answer_id = 130
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:10+00:00'
    country_points.created_date = '2014-11-24 23:35:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 394
    country_points.points = 0
    country_points.answer_id = 131
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:10+00:00'
    country_points.created_date = '2014-11-24 23:35:12+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 395
    country_points.points = 15
    country_points.answer_id = 131
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:10+00:00'
    country_points.created_date = '2014-11-24 23:35:12+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 396
    country_points.points = 0
    country_points.answer_id = 131
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:10+00:00'
    country_points.created_date = '2014-11-24 23:35:12+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 397
    country_points.points = 0
    country_points.answer_id = 132
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:10+00:00'
    country_points.created_date = '2014-11-24 23:35:12+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 398
    country_points.points = 15
    country_points.answer_id = 132
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:10+00:00'
    country_points.created_date = '2014-11-24 23:35:12+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 399
    country_points.points = 0
    country_points.answer_id = 132
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:10+00:00'
    country_points.created_date = '2014-11-24 23:35:12+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 400
    country_points.points = 0
    country_points.answer_id = 133
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:11+00:00'
    country_points.created_date = '2014-11-24 23:35:12+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 401
    country_points.points = 15
    country_points.answer_id = 133
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:11+00:00'
    country_points.created_date = '2014-11-24 23:35:12+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 402
    country_points.points = 0
    country_points.answer_id = 133
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:11+00:00'
    country_points.created_date = '2014-11-24 23:35:12+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 403
    country_points.points = 0
    country_points.answer_id = 134
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:11+00:00'
    country_points.created_date = '2014-11-24 23:35:12+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 404
    country_points.points = 15
    country_points.answer_id = 134
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:11+00:00'
    country_points.created_date = '2014-11-24 23:35:12+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 405
    country_points.points = 0
    country_points.answer_id = 134
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:11+00:00'
    country_points.created_date = '2014-11-24 23:35:12+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 406
    country_points.points = 0
    country_points.answer_id = 135
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:11+00:00'
    country_points.created_date = '2014-11-24 23:35:12+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 407
    country_points.points = 15
    country_points.answer_id = 135
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:11+00:00'
    country_points.created_date = '2014-11-24 23:35:12+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 408
    country_points.points = 0
    country_points.answer_id = 135
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:11+00:00'
    country_points.created_date = '2014-11-24 23:35:12+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 409
    country_points.points = 0
    country_points.answer_id = 136
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:11+00:00'
    country_points.created_date = '2014-11-24 23:35:12+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 410
    country_points.points = 15
    country_points.answer_id = 136
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:11+00:00'
    country_points.created_date = '2014-11-24 23:35:12+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 411
    country_points.points = 0
    country_points.answer_id = 136
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:11+00:00'
    country_points.created_date = '2014-11-24 23:35:13+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 412
    country_points.points = 0
    country_points.answer_id = 137
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:11+00:00'
    country_points.created_date = '2014-11-24 23:35:13+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 413
    country_points.points = 15
    country_points.answer_id = 137
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:11+00:00'
    country_points.created_date = '2014-11-24 23:35:13+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 414
    country_points.points = 0
    country_points.answer_id = 137
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:11+00:00'
    country_points.created_date = '2014-11-24 23:35:13+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 415
    country_points.points = 0
    country_points.answer_id = 138
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:11+00:00'
    country_points.created_date = '2014-11-24 23:35:13+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 416
    country_points.points = 15
    country_points.answer_id = 138
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:12+00:00'
    country_points.created_date = '2014-11-24 23:35:13+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 417
    country_points.points = 0
    country_points.answer_id = 138
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:11+00:00'
    country_points.created_date = '2014-11-24 23:35:13+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 418
    country_points.points = 0
    country_points.answer_id = 139
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:12+00:00'
    country_points.created_date = '2014-11-24 23:35:13+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 419
    country_points.points = 15
    country_points.answer_id = 139
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:12+00:00'
    country_points.created_date = '2014-11-24 23:35:13+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 420
    country_points.points = 0
    country_points.answer_id = 139
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:12+00:00'
    country_points.created_date = '2014-11-24 23:35:13+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 421
    country_points.points = 0
    country_points.answer_id = 140
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 00:01:12+00:00'
    country_points.created_date = '2014-11-24 23:35:13+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 422
    country_points.points = 15
    country_points.answer_id = 140
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 00:01:12+00:00'
    country_points.created_date = '2014-11-24 23:35:13+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 423
    country_points.points = 0
    country_points.answer_id = 140
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 00:01:12+00:00'
    country_points.created_date = '2014-11-24 23:35:13+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 424
    country_points.points = 0
    country_points.answer_id = 918
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:50:57+00:00'
    country_points.created_date = '2014-11-24 23:50:57+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 425
    country_points.points = 9
    country_points.answer_id = 918
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:50:57+00:00'
    country_points.created_date = '2014-11-24 23:50:57+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 426
    country_points.points = 0
    country_points.answer_id = 918
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:50:57+00:00'
    country_points.created_date = '2014-11-24 23:50:57+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 427
    country_points.points = 10
    country_points.answer_id = 919
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:50:57+00:00'
    country_points.created_date = '2014-11-24 23:50:57+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 428
    country_points.points = 11
    country_points.answer_id = 919
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:50:57+00:00'
    country_points.created_date = '2014-11-24 23:50:57+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 429
    country_points.points = 0
    country_points.answer_id = 919
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:50:57+00:00'
    country_points.created_date = '2014-11-24 23:50:57+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 430
    country_points.points = 10
    country_points.answer_id = 920
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:50:57+00:00'
    country_points.created_date = '2014-11-24 23:50:57+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 431
    country_points.points = 11
    country_points.answer_id = 920
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:50:58+00:00'
    country_points.created_date = '2014-11-24 23:50:58+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 432
    country_points.points = 0
    country_points.answer_id = 920
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:50:58+00:00'
    country_points.created_date = '2014-11-24 23:50:58+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 433
    country_points.points = 15
    country_points.answer_id = 921
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:50:58+00:00'
    country_points.created_date = '2014-11-24 23:50:58+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 434
    country_points.points = 13
    country_points.answer_id = 921
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:50:58+00:00'
    country_points.created_date = '2014-11-24 23:50:58+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 435
    country_points.points = 0
    country_points.answer_id = 921
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:50:58+00:00'
    country_points.created_date = '2014-11-24 23:50:58+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 436
    country_points.points = 15
    country_points.answer_id = 922
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:50:58+00:00'
    country_points.created_date = '2014-11-24 23:50:58+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 437
    country_points.points = 13
    country_points.answer_id = 922
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:50:58+00:00'
    country_points.created_date = '2014-11-24 23:50:58+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 438
    country_points.points = 0
    country_points.answer_id = 922
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:50:58+00:00'
    country_points.created_date = '2014-11-24 23:50:58+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 439
    country_points.points = 20
    country_points.answer_id = 923
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:50:58+00:00'
    country_points.created_date = '2014-11-24 23:50:58+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 440
    country_points.points = 15
    country_points.answer_id = 923
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:50:58+00:00'
    country_points.created_date = '2014-11-24 23:50:58+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 441
    country_points.points = 0
    country_points.answer_id = 923
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:50:58+00:00'
    country_points.created_date = '2014-11-24 23:50:58+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 442
    country_points.points = 20
    country_points.answer_id = 924
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:50:58+00:00'
    country_points.created_date = '2014-11-24 23:50:58+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 443
    country_points.points = 15
    country_points.answer_id = 924
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:50:58+00:00'
    country_points.created_date = '2014-11-24 23:50:58+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 444
    country_points.points = 0
    country_points.answer_id = 924
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:50:58+00:00'
    country_points.created_date = '2014-11-24 23:50:58+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 445
    country_points.points = 25
    country_points.answer_id = 925
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:50:58+00:00'
    country_points.created_date = '2014-11-24 23:50:58+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 446
    country_points.points = 15
    country_points.answer_id = 925
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:50:58+00:00'
    country_points.created_date = '2014-11-24 23:50:58+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 447
    country_points.points = 0
    country_points.answer_id = 925
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:50:58+00:00'
    country_points.created_date = '2014-11-24 23:50:58+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 448
    country_points.points = 25
    country_points.answer_id = 926
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:50:59+00:00'
    country_points.created_date = '2014-11-24 23:50:59+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 449
    country_points.points = 15
    country_points.answer_id = 926
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:50:59+00:00'
    country_points.created_date = '2014-11-24 23:50:59+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 450
    country_points.points = 0
    country_points.answer_id = 926
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:50:59+00:00'
    country_points.created_date = '2014-11-24 23:50:59+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 451
    country_points.points = 30
    country_points.answer_id = 927
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:50:59+00:00'
    country_points.created_date = '2014-11-24 23:50:59+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 452
    country_points.points = 15
    country_points.answer_id = 927
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:50:59+00:00'
    country_points.created_date = '2014-11-24 23:50:59+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 453
    country_points.points = 0
    country_points.answer_id = 927
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:50:59+00:00'
    country_points.created_date = '2014-11-24 23:50:59+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 454
    country_points.points = 30
    country_points.answer_id = 928
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:50:59+00:00'
    country_points.created_date = '2014-11-24 23:50:59+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 455
    country_points.points = 15
    country_points.answer_id = 928
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:50:59+00:00'
    country_points.created_date = '2014-11-24 23:50:59+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 456
    country_points.points = 0
    country_points.answer_id = 928
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:50:59+00:00'
    country_points.created_date = '2014-11-24 23:50:59+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 457
    country_points.points = 30
    country_points.answer_id = 929
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:50:59+00:00'
    country_points.created_date = '2014-11-24 23:50:59+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 458
    country_points.points = 15
    country_points.answer_id = 929
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:50:59+00:00'
    country_points.created_date = '2014-11-24 23:50:59+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 459
    country_points.points = 0
    country_points.answer_id = 929
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:50:59+00:00'
    country_points.created_date = '2014-11-24 23:50:59+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 460
    country_points.points = 30
    country_points.answer_id = 930
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:50:59+00:00'
    country_points.created_date = '2014-11-24 23:50:59+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 461
    country_points.points = 15
    country_points.answer_id = 930
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:50:59+00:00'
    country_points.created_date = '2014-11-24 23:50:59+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 462
    country_points.points = 0
    country_points.answer_id = 930
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:50:59+00:00'
    country_points.created_date = '2014-11-24 23:50:59+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 463
    country_points.points = 30
    country_points.answer_id = 931
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:50:59+00:00'
    country_points.created_date = '2014-11-24 23:50:59+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 464
    country_points.points = 15
    country_points.answer_id = 931
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:50:59+00:00'
    country_points.created_date = '2014-11-24 23:50:59+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 465
    country_points.points = 0
    country_points.answer_id = 931
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:50:59+00:00'
    country_points.created_date = '2014-11-24 23:50:59+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 466
    country_points.points = 30
    country_points.answer_id = 932
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:51:00+00:00'
    country_points.created_date = '2014-11-24 23:51:00+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 467
    country_points.points = 15
    country_points.answer_id = 932
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:51:00+00:00'
    country_points.created_date = '2014-11-24 23:51:00+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 468
    country_points.points = 0
    country_points.answer_id = 932
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:51:00+00:00'
    country_points.created_date = '2014-11-24 23:51:00+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 469
    country_points.points = 30
    country_points.answer_id = 933
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:51:00+00:00'
    country_points.created_date = '2014-11-24 23:51:00+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 470
    country_points.points = 15
    country_points.answer_id = 933
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:51:00+00:00'
    country_points.created_date = '2014-11-24 23:51:00+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 471
    country_points.points = 0
    country_points.answer_id = 933
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:51:00+00:00'
    country_points.created_date = '2014-11-24 23:51:00+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 472
    country_points.points = 30
    country_points.answer_id = 934
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:51:00+00:00'
    country_points.created_date = '2014-11-24 23:51:00+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 473
    country_points.points = 15
    country_points.answer_id = 934
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:51:00+00:00'
    country_points.created_date = '2014-11-24 23:51:00+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 474
    country_points.points = 0
    country_points.answer_id = 934
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:51:00+00:00'
    country_points.created_date = '2014-11-24 23:51:00+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 475
    country_points.points = 30
    country_points.answer_id = 935
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:51:00+00:00'
    country_points.created_date = '2014-11-24 23:51:00+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 476
    country_points.points = 15
    country_points.answer_id = 935
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:51:00+00:00'
    country_points.created_date = '2014-11-24 23:51:00+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 477
    country_points.points = 0
    country_points.answer_id = 935
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:51:00+00:00'
    country_points.created_date = '2014-11-24 23:51:00+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 478
    country_points.points = 30
    country_points.answer_id = 936
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:51:00+00:00'
    country_points.created_date = '2014-11-24 23:51:00+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 479
    country_points.points = 15
    country_points.answer_id = 936
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:51:00+00:00'
    country_points.created_date = '2014-11-24 23:51:00+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 480
    country_points.points = 0
    country_points.answer_id = 936
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:51:00+00:00'
    country_points.created_date = '2014-11-24 23:51:00+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 481
    country_points.points = 30
    country_points.answer_id = 937
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:51:00+00:00'
    country_points.created_date = '2014-11-24 23:51:00+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 482
    country_points.points = 15
    country_points.answer_id = 937
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:51:00+00:00'
    country_points.created_date = '2014-11-24 23:51:00+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 483
    country_points.points = 0
    country_points.answer_id = 937
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:51:00+00:00'
    country_points.created_date = '2014-11-24 23:51:00+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 484
    country_points.points = 30
    country_points.answer_id = 938
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:51:01+00:00'
    country_points.created_date = '2014-11-24 23:51:01+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 485
    country_points.points = 15
    country_points.answer_id = 938
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:51:01+00:00'
    country_points.created_date = '2014-11-24 23:51:01+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 486
    country_points.points = 0
    country_points.answer_id = 938
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:51:01+00:00'
    country_points.created_date = '2014-11-24 23:51:01+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 487
    country_points.points = 30
    country_points.answer_id = 939
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:51:01+00:00'
    country_points.created_date = '2014-11-24 23:51:01+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 488
    country_points.points = 15
    country_points.answer_id = 939
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:51:01+00:00'
    country_points.created_date = '2014-11-24 23:51:01+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 489
    country_points.points = 0
    country_points.answer_id = 939
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:51:01+00:00'
    country_points.created_date = '2014-11-24 23:51:01+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 490
    country_points.points = 30
    country_points.answer_id = 940
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:51:01+00:00'
    country_points.created_date = '2014-11-24 23:51:01+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 491
    country_points.points = 15
    country_points.answer_id = 940
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:51:01+00:00'
    country_points.created_date = '2014-11-24 23:51:01+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 492
    country_points.points = 0
    country_points.answer_id = 940
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:51:01+00:00'
    country_points.created_date = '2014-11-24 23:51:01+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 493
    country_points.points = 30
    country_points.answer_id = 941
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:51:01+00:00'
    country_points.created_date = '2014-11-24 23:51:01+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 494
    country_points.points = 15
    country_points.answer_id = 941
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:51:01+00:00'
    country_points.created_date = '2014-11-24 23:51:01+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 495
    country_points.points = 0
    country_points.answer_id = 941
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:51:01+00:00'
    country_points.created_date = '2014-11-24 23:51:01+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 496
    country_points.points = 30
    country_points.answer_id = 942
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:51:01+00:00'
    country_points.created_date = '2014-11-24 23:51:01+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 497
    country_points.points = 15
    country_points.answer_id = 942
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:51:01+00:00'
    country_points.created_date = '2014-11-24 23:51:01+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 498
    country_points.points = 0
    country_points.answer_id = 942
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:51:01+00:00'
    country_points.created_date = '2014-11-24 23:51:01+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 499
    country_points.points = 30
    country_points.answer_id = 943
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:51:01+00:00'
    country_points.created_date = '2014-11-24 23:51:01+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 500
    country_points.points = 15
    country_points.answer_id = 943
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:51:01+00:00'
    country_points.created_date = '2014-11-24 23:51:01+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 501
    country_points.points = 0
    country_points.answer_id = 943
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:51:01+00:00'
    country_points.created_date = '2014-11-24 23:51:01+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 502
    country_points.points = 30
    country_points.answer_id = 944
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:51:02+00:00'
    country_points.created_date = '2014-11-24 23:51:02+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 503
    country_points.points = 15
    country_points.answer_id = 944
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:51:02+00:00'
    country_points.created_date = '2014-11-24 23:51:02+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 504
    country_points.points = 0
    country_points.answer_id = 944
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:51:02+00:00'
    country_points.created_date = '2014-11-24 23:51:02+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 505
    country_points.points = 30
    country_points.answer_id = 945
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:51:02+00:00'
    country_points.created_date = '2014-11-24 23:51:02+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 506
    country_points.points = 15
    country_points.answer_id = 945
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:51:02+00:00'
    country_points.created_date = '2014-11-24 23:51:02+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 507
    country_points.points = 0
    country_points.answer_id = 945
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:51:02+00:00'
    country_points.created_date = '2014-11-24 23:51:02+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 508
    country_points.points = 30
    country_points.answer_id = 946
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:51:02+00:00'
    country_points.created_date = '2014-11-24 23:51:02+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 509
    country_points.points = 15
    country_points.answer_id = 946
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:51:02+00:00'
    country_points.created_date = '2014-11-24 23:51:02+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 510
    country_points.points = 0
    country_points.answer_id = 946
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:51:02+00:00'
    country_points.created_date = '2014-11-24 23:51:02+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 511
    country_points.points = 30
    country_points.answer_id = 947
    country_points.country_id = 131
    country_points.modified_date = '2014-11-24 23:51:02+00:00'
    country_points.created_date = '2014-11-24 23:51:02+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 512
    country_points.points = 15
    country_points.answer_id = 947
    country_points.country_id = 204
    country_points.modified_date = '2014-11-24 23:51:02+00:00'
    country_points.created_date = '2014-11-24 23:51:02+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 513
    country_points.points = 0
    country_points.answer_id = 947
    country_points.country_id = 117
    country_points.modified_date = '2014-11-24 23:51:02+00:00'
    country_points.created_date = '2014-11-24 23:51:02+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 514
    country_points.points = 5
    country_points.answer_id = 141
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:28+00:00'
    country_points.created_date = '2014-11-25 01:49:28+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 515
    country_points.points = 5
    country_points.answer_id = 141
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:28+00:00'
    country_points.created_date = '2014-11-25 01:49:28+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 516
    country_points.points = 10
    country_points.answer_id = 141
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:28+00:00'
    country_points.created_date = '2014-11-25 01:49:28+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 517
    country_points.points = 10
    country_points.answer_id = 142
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:28+00:00'
    country_points.created_date = '2014-11-25 01:49:28+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 518
    country_points.points = 5
    country_points.answer_id = 142
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:28+00:00'
    country_points.created_date = '2014-11-25 01:49:28+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 519
    country_points.points = 10
    country_points.answer_id = 142
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:28+00:00'
    country_points.created_date = '2014-11-25 01:49:28+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 520
    country_points.points = 15
    country_points.answer_id = 143
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:28+00:00'
    country_points.created_date = '2014-11-25 01:49:28+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 521
    country_points.points = 10
    country_points.answer_id = 143
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:28+00:00'
    country_points.created_date = '2014-11-25 01:49:28+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 522
    country_points.points = 10
    country_points.answer_id = 143
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:28+00:00'
    country_points.created_date = '2014-11-25 01:49:28+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 523
    country_points.points = 15
    country_points.answer_id = 144
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:28+00:00'
    country_points.created_date = '2014-11-25 01:49:28+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 524
    country_points.points = 10
    country_points.answer_id = 144
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:28+00:00'
    country_points.created_date = '2014-11-25 01:49:28+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 525
    country_points.points = 10
    country_points.answer_id = 144
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:29+00:00'
    country_points.created_date = '2014-11-25 01:49:29+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 526
    country_points.points = 15
    country_points.answer_id = 145
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:29+00:00'
    country_points.created_date = '2014-11-25 01:49:29+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 527
    country_points.points = 15
    country_points.answer_id = 145
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:29+00:00'
    country_points.created_date = '2014-11-25 01:49:29+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 528
    country_points.points = 10
    country_points.answer_id = 145
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:29+00:00'
    country_points.created_date = '2014-11-25 01:49:29+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 529
    country_points.points = 15
    country_points.answer_id = 146
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:29+00:00'
    country_points.created_date = '2014-11-25 01:49:29+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 530
    country_points.points = 15
    country_points.answer_id = 146
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:29+00:00'
    country_points.created_date = '2014-11-25 01:49:29+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 531
    country_points.points = 10
    country_points.answer_id = 146
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:29+00:00'
    country_points.created_date = '2014-11-25 01:49:29+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 532
    country_points.points = 15
    country_points.answer_id = 147
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:29+00:00'
    country_points.created_date = '2014-11-25 01:49:29+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 533
    country_points.points = 15
    country_points.answer_id = 147
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:29+00:00'
    country_points.created_date = '2014-11-25 01:49:29+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 534
    country_points.points = 10
    country_points.answer_id = 147
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:29+00:00'
    country_points.created_date = '2014-11-25 01:49:29+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 535
    country_points.points = 15
    country_points.answer_id = 148
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:29+00:00'
    country_points.created_date = '2014-11-25 01:49:29+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 536
    country_points.points = 20
    country_points.answer_id = 148
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:29+00:00'
    country_points.created_date = '2014-11-25 01:49:29+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 537
    country_points.points = 10
    country_points.answer_id = 148
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:29+00:00'
    country_points.created_date = '2014-11-25 01:49:29+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 538
    country_points.points = 15
    country_points.answer_id = 149
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:29+00:00'
    country_points.created_date = '2014-11-25 01:49:29+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 539
    country_points.points = 20
    country_points.answer_id = 149
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:29+00:00'
    country_points.created_date = '2014-11-25 01:49:29+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 540
    country_points.points = 10
    country_points.answer_id = 149
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:29+00:00'
    country_points.created_date = '2014-11-25 01:49:29+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 541
    country_points.points = 15
    country_points.answer_id = 150
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:29+00:00'
    country_points.created_date = '2014-11-25 01:49:29+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 542
    country_points.points = 20
    country_points.answer_id = 150
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:30+00:00'
    country_points.created_date = '2014-11-25 01:49:30+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 543
    country_points.points = 10
    country_points.answer_id = 150
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:30+00:00'
    country_points.created_date = '2014-11-25 01:49:30+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 544
    country_points.points = 15
    country_points.answer_id = 151
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:30+00:00'
    country_points.created_date = '2014-11-25 01:49:30+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 545
    country_points.points = 20
    country_points.answer_id = 151
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:30+00:00'
    country_points.created_date = '2014-11-25 01:49:30+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 546
    country_points.points = 10
    country_points.answer_id = 151
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:30+00:00'
    country_points.created_date = '2014-11-25 01:49:30+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 547
    country_points.points = 15
    country_points.answer_id = 152
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:30+00:00'
    country_points.created_date = '2014-11-25 01:49:30+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 548
    country_points.points = 20
    country_points.answer_id = 152
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:30+00:00'
    country_points.created_date = '2014-11-25 01:49:30+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 549
    country_points.points = 10
    country_points.answer_id = 152
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:30+00:00'
    country_points.created_date = '2014-11-25 01:49:30+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 550
    country_points.points = 15
    country_points.answer_id = 153
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:30+00:00'
    country_points.created_date = '2014-11-25 01:49:30+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 551
    country_points.points = 20
    country_points.answer_id = 153
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:30+00:00'
    country_points.created_date = '2014-11-25 01:49:30+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 552
    country_points.points = 10
    country_points.answer_id = 153
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:30+00:00'
    country_points.created_date = '2014-11-25 01:49:30+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 553
    country_points.points = 15
    country_points.answer_id = 154
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:30+00:00'
    country_points.created_date = '2014-11-25 01:49:30+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 554
    country_points.points = 20
    country_points.answer_id = 154
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:30+00:00'
    country_points.created_date = '2014-11-25 01:49:30+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 555
    country_points.points = 10
    country_points.answer_id = 154
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:30+00:00'
    country_points.created_date = '2014-11-25 01:49:30+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 556
    country_points.points = 15
    country_points.answer_id = 155
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:30+00:00'
    country_points.created_date = '2014-11-25 01:49:30+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 557
    country_points.points = 20
    country_points.answer_id = 155
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:30+00:00'
    country_points.created_date = '2014-11-25 01:49:30+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 558
    country_points.points = 10
    country_points.answer_id = 155
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:30+00:00'
    country_points.created_date = '2014-11-25 01:49:30+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 559
    country_points.points = 15
    country_points.answer_id = 156
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:31+00:00'
    country_points.created_date = '2014-11-25 01:49:31+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 560
    country_points.points = 20
    country_points.answer_id = 156
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:31+00:00'
    country_points.created_date = '2014-11-25 01:49:31+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 561
    country_points.points = 10
    country_points.answer_id = 156
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:31+00:00'
    country_points.created_date = '2014-11-25 01:49:31+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 562
    country_points.points = 15
    country_points.answer_id = 157
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:31+00:00'
    country_points.created_date = '2014-11-25 01:49:31+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 563
    country_points.points = 20
    country_points.answer_id = 157
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:31+00:00'
    country_points.created_date = '2014-11-25 01:49:31+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 564
    country_points.points = 10
    country_points.answer_id = 157
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:31+00:00'
    country_points.created_date = '2014-11-25 01:49:31+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 565
    country_points.points = 15
    country_points.answer_id = 158
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:31+00:00'
    country_points.created_date = '2014-11-25 01:49:31+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 566
    country_points.points = 20
    country_points.answer_id = 158
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:31+00:00'
    country_points.created_date = '2014-11-25 01:49:31+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 567
    country_points.points = 10
    country_points.answer_id = 158
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:31+00:00'
    country_points.created_date = '2014-11-25 01:49:31+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 568
    country_points.points = 15
    country_points.answer_id = 159
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:31+00:00'
    country_points.created_date = '2014-11-25 01:49:31+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 569
    country_points.points = 20
    country_points.answer_id = 159
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:31+00:00'
    country_points.created_date = '2014-11-25 01:49:31+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 570
    country_points.points = 10
    country_points.answer_id = 159
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:31+00:00'
    country_points.created_date = '2014-11-25 01:49:31+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 571
    country_points.points = 15
    country_points.answer_id = 160
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:31+00:00'
    country_points.created_date = '2014-11-25 01:49:31+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 572
    country_points.points = 20
    country_points.answer_id = 160
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:31+00:00'
    country_points.created_date = '2014-11-25 01:49:31+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 573
    country_points.points = 10
    country_points.answer_id = 160
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:31+00:00'
    country_points.created_date = '2014-11-25 01:49:31+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 574
    country_points.points = 15
    country_points.answer_id = 161
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:31+00:00'
    country_points.created_date = '2014-11-25 01:49:31+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 575
    country_points.points = 20
    country_points.answer_id = 161
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:31+00:00'
    country_points.created_date = '2014-11-25 01:49:31+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 576
    country_points.points = 10
    country_points.answer_id = 161
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:31+00:00'
    country_points.created_date = '2014-11-25 01:49:31+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 577
    country_points.points = 15
    country_points.answer_id = 162
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:32+00:00'
    country_points.created_date = '2014-11-25 01:49:32+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 578
    country_points.points = 20
    country_points.answer_id = 162
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:32+00:00'
    country_points.created_date = '2014-11-25 01:49:32+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 579
    country_points.points = 10
    country_points.answer_id = 162
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:32+00:00'
    country_points.created_date = '2014-11-25 01:49:32+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 580
    country_points.points = 15
    country_points.answer_id = 163
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:32+00:00'
    country_points.created_date = '2014-11-25 01:49:32+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 581
    country_points.points = 20
    country_points.answer_id = 163
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:32+00:00'
    country_points.created_date = '2014-11-25 01:49:32+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 582
    country_points.points = 10
    country_points.answer_id = 163
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:32+00:00'
    country_points.created_date = '2014-11-25 01:49:32+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 583
    country_points.points = 15
    country_points.answer_id = 164
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:32+00:00'
    country_points.created_date = '2014-11-25 01:49:32+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 584
    country_points.points = 20
    country_points.answer_id = 164
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:32+00:00'
    country_points.created_date = '2014-11-25 01:49:32+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 585
    country_points.points = 10
    country_points.answer_id = 164
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:32+00:00'
    country_points.created_date = '2014-11-25 01:49:32+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 586
    country_points.points = 15
    country_points.answer_id = 165
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:32+00:00'
    country_points.created_date = '2014-11-25 01:49:32+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 587
    country_points.points = 20
    country_points.answer_id = 165
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:32+00:00'
    country_points.created_date = '2014-11-25 01:49:32+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 588
    country_points.points = 10
    country_points.answer_id = 165
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:32+00:00'
    country_points.created_date = '2014-11-25 01:49:32+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 589
    country_points.points = 15
    country_points.answer_id = 166
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:32+00:00'
    country_points.created_date = '2014-11-25 01:49:32+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 590
    country_points.points = 20
    country_points.answer_id = 166
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:32+00:00'
    country_points.created_date = '2014-11-25 01:49:32+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 591
    country_points.points = 10
    country_points.answer_id = 166
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:32+00:00'
    country_points.created_date = '2014-11-25 01:49:32+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 592
    country_points.points = 15
    country_points.answer_id = 167
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:32+00:00'
    country_points.created_date = '2014-11-25 01:49:32+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 593
    country_points.points = 20
    country_points.answer_id = 167
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:32+00:00'
    country_points.created_date = '2014-11-25 01:49:32+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 594
    country_points.points = 10
    country_points.answer_id = 167
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:33+00:00'
    country_points.created_date = '2014-11-25 01:49:33+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 595
    country_points.points = 15
    country_points.answer_id = 168
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:33+00:00'
    country_points.created_date = '2014-11-25 01:49:33+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 596
    country_points.points = 20
    country_points.answer_id = 168
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:33+00:00'
    country_points.created_date = '2014-11-25 01:49:33+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 597
    country_points.points = 10
    country_points.answer_id = 168
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:33+00:00'
    country_points.created_date = '2014-11-25 01:49:33+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 598
    country_points.points = 15
    country_points.answer_id = 169
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:33+00:00'
    country_points.created_date = '2014-11-25 01:49:33+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 599
    country_points.points = 20
    country_points.answer_id = 169
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:33+00:00'
    country_points.created_date = '2014-11-25 01:49:33+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 600
    country_points.points = 10
    country_points.answer_id = 169
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:33+00:00'
    country_points.created_date = '2014-11-25 01:49:33+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 601
    country_points.points = 15
    country_points.answer_id = 170
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 01:49:33+00:00'
    country_points.created_date = '2014-11-25 01:49:33+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 602
    country_points.points = 20
    country_points.answer_id = 170
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 01:49:33+00:00'
    country_points.created_date = '2014-11-25 01:49:33+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 603
    country_points.points = 10
    country_points.answer_id = 170
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 01:49:33+00:00'
    country_points.created_date = '2014-11-25 01:49:33+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 604
    country_points.points = 20
    country_points.answer_id = 878
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:04:11+00:00'
    country_points.created_date = '2014-11-25 02:04:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 605
    country_points.points = 0
    country_points.answer_id = 878
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:04:11+00:00'
    country_points.created_date = '2014-11-25 02:04:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 606
    country_points.points = 5
    country_points.answer_id = 878
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:04:11+00:00'
    country_points.created_date = '2014-11-25 02:04:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 607
    country_points.points = 0
    country_points.answer_id = 879
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:04:11+00:00'
    country_points.created_date = '2014-11-25 02:04:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 608
    country_points.points = 0
    country_points.answer_id = 879
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:04:11+00:00'
    country_points.created_date = '2014-11-25 02:04:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 609
    country_points.points = 0
    country_points.answer_id = 879
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:04:11+00:00'
    country_points.created_date = '2014-11-25 02:04:11+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 610
    country_points.points = 0
    country_points.answer_id = 880
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:04:37+00:00'
    country_points.created_date = '2014-11-25 02:04:37+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 611
    country_points.points = 0
    country_points.answer_id = 880
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:04:37+00:00'
    country_points.created_date = '2014-11-25 02:04:37+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 612
    country_points.points = 0
    country_points.answer_id = 880
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:04:38+00:00'
    country_points.created_date = '2014-11-25 02:04:38+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 613
    country_points.points = 0
    country_points.answer_id = 881
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:04:38+00:00'
    country_points.created_date = '2014-11-25 02:04:38+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 614
    country_points.points = 0
    country_points.answer_id = 881
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:04:38+00:00'
    country_points.created_date = '2014-11-25 02:04:38+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 615
    country_points.points = 0
    country_points.answer_id = 881
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:04:38+00:00'
    country_points.created_date = '2014-11-25 02:04:38+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 616
    country_points.points = 0
    country_points.answer_id = 882
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:05:34+00:00'
    country_points.created_date = '2014-11-25 02:05:34+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 617
    country_points.points = 0
    country_points.answer_id = 882
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:05:34+00:00'
    country_points.created_date = '2014-11-25 02:05:34+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 618
    country_points.points = 0
    country_points.answer_id = 882
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:05:34+00:00'
    country_points.created_date = '2014-11-25 02:05:34+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 619
    country_points.points = 0
    country_points.answer_id = 883
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:05:34+00:00'
    country_points.created_date = '2014-11-25 02:05:34+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 620
    country_points.points = 0
    country_points.answer_id = 883
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:05:34+00:00'
    country_points.created_date = '2014-11-25 02:05:34+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 621
    country_points.points = 0
    country_points.answer_id = 883
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:05:34+00:00'
    country_points.created_date = '2014-11-25 02:05:34+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 622
    country_points.points = 0
    country_points.answer_id = 884
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:06:35+00:00'
    country_points.created_date = '2014-11-25 02:06:35+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 623
    country_points.points = 0
    country_points.answer_id = 884
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:06:35+00:00'
    country_points.created_date = '2014-11-25 02:06:35+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 624
    country_points.points = 0
    country_points.answer_id = 884
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:06:35+00:00'
    country_points.created_date = '2014-11-25 02:06:35+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 625
    country_points.points = 0
    country_points.answer_id = 885
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:06:35+00:00'
    country_points.created_date = '2014-11-25 02:06:35+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 626
    country_points.points = 0
    country_points.answer_id = 885
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:06:35+00:00'
    country_points.created_date = '2014-11-25 02:06:35+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 627
    country_points.points = 0
    country_points.answer_id = 885
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:06:35+00:00'
    country_points.created_date = '2014-11-25 02:06:35+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 628
    country_points.points = 0
    country_points.answer_id = 886
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:07:16+00:00'
    country_points.created_date = '2014-11-25 02:07:16+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 629
    country_points.points = 5
    country_points.answer_id = 886
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:07:16+00:00'
    country_points.created_date = '2014-11-25 02:07:16+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 630
    country_points.points = 0
    country_points.answer_id = 886
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:07:16+00:00'
    country_points.created_date = '2014-11-25 02:07:16+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 631
    country_points.points = 0
    country_points.answer_id = 887
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:07:16+00:00'
    country_points.created_date = '2014-11-25 02:07:16+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 632
    country_points.points = 0
    country_points.answer_id = 887
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:07:17+00:00'
    country_points.created_date = '2014-11-25 02:07:17+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 633
    country_points.points = 0
    country_points.answer_id = 887
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:07:17+00:00'
    country_points.created_date = '2014-11-25 02:07:17+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 634
    country_points.points = 0
    country_points.answer_id = 888
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:07:44+00:00'
    country_points.created_date = '2014-11-25 02:07:44+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 635
    country_points.points = 5
    country_points.answer_id = 888
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:07:44+00:00'
    country_points.created_date = '2014-11-25 02:07:44+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 636
    country_points.points = 0
    country_points.answer_id = 888
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:07:44+00:00'
    country_points.created_date = '2014-11-25 02:07:44+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 637
    country_points.points = 0
    country_points.answer_id = 889
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:07:44+00:00'
    country_points.created_date = '2014-11-25 02:07:44+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 638
    country_points.points = 0
    country_points.answer_id = 889
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:07:44+00:00'
    country_points.created_date = '2014-11-25 02:07:44+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 639
    country_points.points = 0
    country_points.answer_id = 889
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:07:44+00:00'
    country_points.created_date = '2014-11-25 02:07:44+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 640
    country_points.points = 0
    country_points.answer_id = 890
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:08:59+00:00'
    country_points.created_date = '2014-11-25 02:08:59+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 641
    country_points.points = 0
    country_points.answer_id = 890
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:08:59+00:00'
    country_points.created_date = '2014-11-25 02:08:59+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 642
    country_points.points = 0
    country_points.answer_id = 890
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:08:59+00:00'
    country_points.created_date = '2014-11-25 02:08:59+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 643
    country_points.points = 0
    country_points.answer_id = 891
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:08:59+00:00'
    country_points.created_date = '2014-11-25 02:08:59+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 644
    country_points.points = 0
    country_points.answer_id = 891
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:08:59+00:00'
    country_points.created_date = '2014-11-25 02:08:59+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 645
    country_points.points = 0
    country_points.answer_id = 891
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:08:59+00:00'
    country_points.created_date = '2014-11-25 02:08:59+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 652
    country_points.points = 0
    country_points.answer_id = 894
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:10:04+00:00'
    country_points.created_date = '2014-11-25 02:10:04+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 653
    country_points.points = 0
    country_points.answer_id = 894
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:10:04+00:00'
    country_points.created_date = '2014-11-25 02:10:04+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 654
    country_points.points = 5
    country_points.answer_id = 894
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:10:04+00:00'
    country_points.created_date = '2014-11-25 02:10:04+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 655
    country_points.points = 0
    country_points.answer_id = 895
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:10:04+00:00'
    country_points.created_date = '2014-11-25 02:10:04+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 656
    country_points.points = 0
    country_points.answer_id = 895
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:10:04+00:00'
    country_points.created_date = '2014-11-25 02:10:04+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 657
    country_points.points = 0
    country_points.answer_id = 895
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:10:04+00:00'
    country_points.created_date = '2014-11-25 02:10:04+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 658
    country_points.points = 0
    country_points.answer_id = 896
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:14:20+00:00'
    country_points.created_date = '2014-11-25 02:14:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 659
    country_points.points = 0
    country_points.answer_id = 896
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:14:20+00:00'
    country_points.created_date = '2014-11-25 02:14:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 660
    country_points.points = 0
    country_points.answer_id = 896
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:14:20+00:00'
    country_points.created_date = '2014-11-25 02:14:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 661
    country_points.points = 0
    country_points.answer_id = 897
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:14:20+00:00'
    country_points.created_date = '2014-11-25 02:14:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 662
    country_points.points = 5
    country_points.answer_id = 897
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:14:20+00:00'
    country_points.created_date = '2014-11-25 02:14:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 663
    country_points.points = 0
    country_points.answer_id = 897
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:14:20+00:00'
    country_points.created_date = '2014-11-25 02:14:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 664
    country_points.points = 0
    country_points.answer_id = 898
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:14:20+00:00'
    country_points.created_date = '2014-11-25 02:14:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 665
    country_points.points = 5
    country_points.answer_id = 898
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:14:20+00:00'
    country_points.created_date = '2014-11-25 02:14:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 666
    country_points.points = 0
    country_points.answer_id = 898
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:14:20+00:00'
    country_points.created_date = '2014-11-25 02:14:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 667
    country_points.points = 0
    country_points.answer_id = 899
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:14:20+00:00'
    country_points.created_date = '2014-11-25 02:14:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 668
    country_points.points = 5
    country_points.answer_id = 899
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:14:20+00:00'
    country_points.created_date = '2014-11-25 02:14:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 669
    country_points.points = 0
    country_points.answer_id = 899
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:14:20+00:00'
    country_points.created_date = '2014-11-25 02:14:20+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 670
    country_points.points = 0
    country_points.answer_id = 900
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:14:46+00:00'
    country_points.created_date = '2014-11-25 02:14:46+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 671
    country_points.points = 0
    country_points.answer_id = 900
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:14:46+00:00'
    country_points.created_date = '2014-11-25 02:14:46+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 672
    country_points.points = 0
    country_points.answer_id = 900
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:14:46+00:00'
    country_points.created_date = '2014-11-25 02:14:46+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 673
    country_points.points = 0
    country_points.answer_id = 901
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:14:46+00:00'
    country_points.created_date = '2014-11-25 02:14:46+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 674
    country_points.points = 0
    country_points.answer_id = 901
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:14:46+00:00'
    country_points.created_date = '2014-11-25 02:14:46+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 675
    country_points.points = 5
    country_points.answer_id = 901
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:14:46+00:00'
    country_points.created_date = '2014-11-25 02:14:46+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 676
    country_points.points = 0
    country_points.answer_id = 902
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:14:46+00:00'
    country_points.created_date = '2014-11-25 02:14:46+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 677
    country_points.points = 0
    country_points.answer_id = 902
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:14:46+00:00'
    country_points.created_date = '2014-11-25 02:14:46+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 678
    country_points.points = 5
    country_points.answer_id = 902
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:14:47+00:00'
    country_points.created_date = '2014-11-25 02:14:47+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 679
    country_points.points = 0
    country_points.answer_id = 903
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:14:47+00:00'
    country_points.created_date = '2014-11-25 02:14:47+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 680
    country_points.points = 0
    country_points.answer_id = 903
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:14:47+00:00'
    country_points.created_date = '2014-11-25 02:14:47+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 681
    country_points.points = 5
    country_points.answer_id = 903
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:14:47+00:00'
    country_points.created_date = '2014-11-25 02:14:47+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 682
    country_points.points = 0
    country_points.answer_id = 904
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:20:05+00:00'
    country_points.created_date = '2014-11-25 02:20:05+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 683
    country_points.points = 0
    country_points.answer_id = 904
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:20:05+00:00'
    country_points.created_date = '2014-11-25 02:20:05+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 684
    country_points.points = 0
    country_points.answer_id = 904
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:20:05+00:00'
    country_points.created_date = '2014-11-25 02:20:05+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 685
    country_points.points = 0
    country_points.answer_id = 905
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:20:05+00:00'
    country_points.created_date = '2014-11-25 02:20:05+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 686
    country_points.points = 0
    country_points.answer_id = 905
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:20:05+00:00'
    country_points.created_date = '2014-11-25 02:20:05+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 687
    country_points.points = 0
    country_points.answer_id = 905
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:20:05+00:00'
    country_points.created_date = '2014-11-25 02:20:05+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 688
    country_points.points = 0
    country_points.answer_id = 906
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:20:05+00:00'
    country_points.created_date = '2014-11-25 02:20:05+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 689
    country_points.points = 0
    country_points.answer_id = 906
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:20:05+00:00'
    country_points.created_date = '2014-11-25 02:20:05+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 690
    country_points.points = 0
    country_points.answer_id = 906
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:20:05+00:00'
    country_points.created_date = '2014-11-25 02:20:05+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 691
    country_points.points = 0
    country_points.answer_id = 907
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:20:05+00:00'
    country_points.created_date = '2014-11-25 02:20:05+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 692
    country_points.points = 0
    country_points.answer_id = 907
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:20:06+00:00'
    country_points.created_date = '2014-11-25 02:20:06+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 693
    country_points.points = 0
    country_points.answer_id = 907
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:20:06+00:00'
    country_points.created_date = '2014-11-25 02:20:06+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 694
    country_points.points = 0
    country_points.answer_id = 908
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:20:06+00:00'
    country_points.created_date = '2014-11-25 02:20:06+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 695
    country_points.points = 10
    country_points.answer_id = 908
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:20:06+00:00'
    country_points.created_date = '2014-11-25 02:20:06+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 696
    country_points.points = 0
    country_points.answer_id = 908
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:20:06+00:00'
    country_points.created_date = '2014-11-25 02:20:06+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 697
    country_points.points = 0
    country_points.answer_id = 909
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:20:06+00:00'
    country_points.created_date = '2014-11-25 02:20:06+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 698
    country_points.points = 20
    country_points.answer_id = 909
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:20:06+00:00'
    country_points.created_date = '2014-11-25 02:20:06+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 699
    country_points.points = 0
    country_points.answer_id = 909
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:20:06+00:00'
    country_points.created_date = '2014-11-25 02:20:06+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 700
    country_points.points = 0
    country_points.answer_id = 910
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:20:06+00:00'
    country_points.created_date = '2014-11-25 02:20:06+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 701
    country_points.points = 20
    country_points.answer_id = 910
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:20:06+00:00'
    country_points.created_date = '2014-11-25 02:20:06+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 702
    country_points.points = 0
    country_points.answer_id = 910
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:20:06+00:00'
    country_points.created_date = '2014-11-25 02:20:06+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 703
    country_points.points = 0
    country_points.answer_id = 911
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:20:06+00:00'
    country_points.created_date = '2014-11-25 02:20:06+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 704
    country_points.points = 20
    country_points.answer_id = 911
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:20:06+00:00'
    country_points.created_date = '2014-11-25 02:20:06+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 705
    country_points.points = 0
    country_points.answer_id = 911
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:20:06+00:00'
    country_points.created_date = '2014-11-25 02:20:06+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 706
    country_points.points = 0
    country_points.answer_id = 912
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:22:40+00:00'
    country_points.created_date = '2014-11-25 02:22:40+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 707
    country_points.points = 0
    country_points.answer_id = 912
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:22:40+00:00'
    country_points.created_date = '2014-11-25 02:22:40+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 708
    country_points.points = 0
    country_points.answer_id = 912
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:22:40+00:00'
    country_points.created_date = '2014-11-25 02:22:40+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 709
    country_points.points = 0
    country_points.answer_id = 913
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:22:40+00:00'
    country_points.created_date = '2014-11-25 02:22:40+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 710
    country_points.points = 0
    country_points.answer_id = 913
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:22:40+00:00'
    country_points.created_date = '2014-11-25 02:22:40+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 711
    country_points.points = 0
    country_points.answer_id = 913
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:22:40+00:00'
    country_points.created_date = '2014-11-25 02:22:40+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 712
    country_points.points = 0
    country_points.answer_id = 914
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 02:22:40+00:00'
    country_points.created_date = '2014-11-25 02:22:40+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 713
    country_points.points = 0
    country_points.answer_id = 914
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 02:22:40+00:00'
    country_points.created_date = '2014-11-25 02:22:40+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 714
    country_points.points = 0
    country_points.answer_id = 914
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 02:22:40+00:00'
    country_points.created_date = '2014-11-25 02:22:40+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 715
    country_points.points = 5
    country_points.answer_id = 915
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 13:17:23+00:00'
    country_points.created_date = '2014-11-25 02:22:40+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 716
    country_points.points = 0
    country_points.answer_id = 915
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 13:17:23+00:00'
    country_points.created_date = '2014-11-25 02:22:40+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 717
    country_points.points = 0
    country_points.answer_id = 915
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 13:17:23+00:00'
    country_points.created_date = '2014-11-25 02:22:40+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 718
    country_points.points = 5
    country_points.answer_id = 916
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 03:22:37+00:00'
    country_points.created_date = '2014-11-25 03:22:37+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 719
    country_points.points = 10
    country_points.answer_id = 916
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 03:22:37+00:00'
    country_points.created_date = '2014-11-25 03:22:37+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 720
    country_points.points = 5
    country_points.answer_id = 916
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 03:22:37+00:00'
    country_points.created_date = '2014-11-25 03:22:37+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 721
    country_points.points = 0
    country_points.answer_id = 917
    country_points.country_id = 117
    country_points.modified_date = '2014-11-25 03:22:37+00:00'
    country_points.created_date = '2014-11-25 03:22:37+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 722
    country_points.points = 0
    country_points.answer_id = 917
    country_points.country_id = 131
    country_points.modified_date = '2014-11-25 03:22:37+00:00'
    country_points.created_date = '2014-11-25 03:22:37+00:00'
    country_points.save()

    country_points = CountryPoints()
    country_points.id = 723
    country_points.points = 0
    country_points.answer_id = 917
    country_points.country_id = 204
    country_points.modified_date = '2014-11-25 03:22:37+00:00'
    country_points.created_date = '2014-11-25 03:22:37+00:00'
    country_points.save()

#OccupationCategory
    occupation_category = OccupationCategory()
    occupation_category.id = 1
    occupation_category.name = 'Business / Finance / Administration / Advertising'
    occupation_category.modified_date = '2014-11-25 18:20:33+00:00'
    occupation_category.created_date = '2014-11-25 18:20:33+00:00'
    occupation_category.save()

    occupation_category = OccupationCategory()
    occupation_category.id = 2
    occupation_category.name = 'Art / Culture / Recreation / Sport'
    occupation_category.modified_date = '2014-11-25 18:20:33+00:00'
    occupation_category.created_date = '2014-11-25 18:20:33+00:00'
    occupation_category.save()

    occupation_category = OccupationCategory()
    occupation_category.id = 3
    occupation_category.name = 'Health'
    occupation_category.modified_date = '2014-11-25 18:20:33+00:00'
    occupation_category.created_date = '2014-11-25 18:20:33+00:00'
    occupation_category.save()

    occupation_category = OccupationCategory()
    occupation_category.id = 4
    occupation_category.name = 'Engineering / Technology / Natural and Applied Sciences / Architecture'
    occupation_category.modified_date = '2014-11-25 18:20:33+00:00'
    occupation_category.created_date = '2014-11-25 18:20:33+00:00'
    occupation_category.save()

    occupation_category = OccupationCategory()
    occupation_category.id = 5
    occupation_category.name = 'Education / Law / Social, community and gov. services'
    occupation_category.modified_date = '2014-11-25 18:20:33+00:00'
    occupation_category.created_date = '2014-11-25 18:20:33+00:00'
    occupation_category.save()

    occupation_category = OccupationCategory()
    occupation_category.id = 6
    occupation_category.name = 'Natural Resources / Agriculture / Related Production'
    occupation_category.modified_date = '2014-11-25 18:20:33+00:00'
    occupation_category.created_date = '2014-11-25 18:20:33+00:00'
    occupation_category.save()

    occupation_category = OccupationCategory()
    occupation_category.id = 7
    occupation_category.name = 'Sales / Services'
    occupation_category.modified_date = '2014-11-25 18:20:33+00:00'
    occupation_category.created_date = '2014-11-25 18:20:33+00:00'
    occupation_category.save()

    occupation_category = OccupationCategory()
    occupation_category.id = 8
    occupation_category.name = 'Trades / Transports / Equipments / Manufacturing / Utilities'
    occupation_category.modified_date = '2014-11-25 18:20:33+00:00'
    occupation_category.created_date = '2014-11-25 18:20:33+00:00'
    occupation_category.save()

#Occupation
    occupation = Occupation()
    occupation.id = 171
    occupation.name = 'Accountant (General)'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:17:16+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 172
    occupation.name = 'Financial Auditor'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:17:55+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 173
    occupation.name = 'Management Accountant'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:18:08+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 174
    occupation.name = 'Taxation Accountant'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:18:27+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 175
    occupation.name = 'External Auditor'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:20:00+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 176
    occupation.name = 'Internal Auditor'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:19:50+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 177
    occupation.name = 'Actuary'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:20:38+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 178
    occupation.name = 'Financial and investment analysts'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:21:25+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 179
    occupation.name = 'Financial Managers'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:22:05+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 180
    occupation.name = 'Insurance, real estate and financial brokerage managers'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:22:45+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 181
    occupation.name = 'Financial Market Dealer'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:23:02+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 182
    occupation.name = 'Other Financial Officers/Dealers'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:23:36+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 183
    occupation.name = 'Supervisors, finance and insurance office workers'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:25:46+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 184
    occupation.name = 'Financial Investment Adviser'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:26:01+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 185
    occupation.name = 'Financial Investment Manager'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:26:16+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 186
    occupation.name = 'Securities agents, investment dealers and brokers'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:26:54+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 187
    occupation.name = 'Financial Institution Branch Manager'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:27:08+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 188
    occupation.name = 'Land Economist'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:27:29+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 189
    occupation.name = 'Economist'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:27:47+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 190
    occupation.name = 'Valuer'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:28:07+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 191
    occupation.name = 'Stockbroking Dealer'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:28:23+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 192
    occupation.name = 'Antique Dealer'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:28:33+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 193
    occupation.name = 'Insurance Broker'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:28:45+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 194
    occupation.name = 'Business Broker'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:28:57+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 195
    occupation.name = 'Insurance Agent'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:29:10+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 196
    occupation.name = 'Insurance Investigator'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:29:29+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 197
    occupation.name = 'Insurance Loss Adjuster'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:29:45+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 198
    occupation.name = 'Insurance Risk Surveyor'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:30:00+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 199
    occupation.name = 'Property Administrators'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:30:25+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 200
    occupation.name = 'Contract Administrator'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:30:40+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 201
    occupation.name = 'Program or Project Administrator'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:30:57+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 202
    occupation.name = 'Actor'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 04:50:25+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 203
    occupation.name = 'Dancers and Other Entertainers'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 04:51:22+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 204
    occupation.name = 'Librarian'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 04:51:47+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 205
    occupation.name = 'Library Technician'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 04:52:19+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 206
    occupation.name = 'Gallery or Museum Curator'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 04:52:59+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 207
    occupation.name = 'Gallery or Museum Technician'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 04:53:24+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 208
    occupation.name = 'Conservation Officer'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 04:53:45+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 209
    occupation.name = 'Conservator'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 04:54:04+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 210
    occupation.name = 'Archivist'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 04:54:36+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 211
    occupation.name = 'Author'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 04:55:09+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 212
    occupation.name = 'Copywriter'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 04:55:30+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 213
    occupation.name = 'Journalists and Other Writers'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 04:56:49+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 214
    occupation.name = 'Technical Writer'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 04:57:20+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 215
    occupation.name = 'Signwriter'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 04:57:31+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 216
    occupation.name = 'Film and Video Editor'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 04:57:58+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 217
    occupation.name = 'Newspaper or Periodical Editor'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 04:58:13+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 218
    occupation.name = 'Book or Script Editor'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 04:58:37+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 219
    occupation.name = 'Print Journalist'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 04:58:55+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 220
    occupation.name = 'Radio Journalist'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 04:59:39+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 221
    occupation.name = 'Television Journalist'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:00:34+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 222
    occupation.name = 'Translators, terminologists and interpreters'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:01:03+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 223
    occupation.name = 'Video Producer'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:01:47+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 224
    occupation.name = 'Media Producer (excluding Video)'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:01:59+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 225
    occupation.name = 'Director (Film, Television, Radio or Stage)'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:15:25+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 226
    occupation.name = 'Director of Photography'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:16:11+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 227
    occupation.name = 'Dancer or Choreographer'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:03:58+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 228
    occupation.name = 'Composer'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:04:16+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 229
    occupation.name = 'Musician (Instrumental)'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:05:27+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 230
    occupation.name = 'Musical Instrument Maker or Repairer'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:06:43+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 231
    occupation.name = 'Music Director'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:07:02+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 232
    occupation.name = 'Music Professionals (Others)'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:07:26+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 233
    occupation.name = 'Music Teacher (Private Tuition)'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:07:34+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 234
    occupation.name = 'Singer'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:07:57+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 235
    occupation.name = 'Painter (Visual Arts)'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:08:13+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 236
    occupation.name = 'Sculptor'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:08:26+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 237
    occupation.name = 'Visual Arts and Crafts Professionals (Others)'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:08:56+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 238
    occupation.name = 'Art Director (Film, Television or Stage)'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:09:31+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 239
    occupation.name = 'Art Teacher (Private Tuition)'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:10:19+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 240
    occupation.name = 'Artistic Director'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:10:29+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 241
    occupation.name = 'Arts Administrator or Manager'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:10:39+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 242
    occupation.name = 'Community Arts Worker'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:14:51+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 243
    occupation.name = 'Entertainer or Variety Artist'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:16:59+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 244
    occupation.name = 'Potter or Ceramic Artist'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:17:19+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 245
    occupation.name = 'Performing Arts Technicians (Others)'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:17:27+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 246
    occupation.name = 'Make Up Artist'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:18:04+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 247
    occupation.name = 'Dance Teacher (Private Tuition)'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:18:16+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 248
    occupation.name = 'Drama Teacher (Private Tuition)'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:18:33+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 249
    occupation.name = 'Recreation Coordinator'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:18:57+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 250
    occupation.name = 'Photographers Assistant'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:19:16+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 251
    occupation.name = 'Photographer'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:19:28+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 252
    occupation.name = 'Camera Operator (Film, Television or Video)'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:19:45+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 253
    occupation.name = 'Graphic Pre-press Trades Worker'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:20:06+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 254
    occupation.name = 'Broadcast Transmitter Operator'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:20:56+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 255
    occupation.name = 'Records Manager'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:21:14+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 256
    occupation.name = 'Radio Communications Technician'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:22:35+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 257
    occupation.name = 'Program Director (Television or Radio)'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:23:22+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 258
    occupation.name = 'Radio Presenter'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:23:58+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 260
    occupation.name = 'Graphic Designer'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:27:56+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 261
    occupation.name = 'Fashion Designer'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:28:09+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 262
    occupation.name = 'Interior Designer'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:28:24+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 263
    occupation.name = 'Jewellery Designer'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:28:32+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 264
    occupation.name = 'Marine Designer'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:28:48+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 265
    occupation.name = 'Multimedia Designer'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:29:12+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 266
    occupation.name = 'Web Designer'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:29:31+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 267
    occupation.name = 'Industrial Designer'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:30:10+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 268
    occupation.name = 'Illustrator'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:30:27+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 269
    occupation.name = 'Interior Decorator'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:30:48+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 270
    occupation.name = 'Operating Theatre Technician'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:31:17+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 271
    occupation.name = 'Cinema or Theatre Manager'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:31:45+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 272
    occupation.name = 'Clothing Patternmaker'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:32:18+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 273
    occupation.name = 'Gymnastics Coach or Instructor'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:32:37+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 274
    occupation.name = 'Horse Riding Coach or Instructor'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:33:15+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 275
    occupation.name = 'Other Sports Coach or Instructor'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:33:46+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 276
    occupation.name = 'Swimming Coach or Instructor'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:34:16+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 277
    occupation.name = 'Tennis Coach'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:34:22+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 278
    occupation.name = 'Sports Administrator'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:34:32+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 279
    occupation.name = 'Sports Centre Manager'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:34:52+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 280
    occupation.name = 'Sports Centre Manager'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:35:05+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 281
    occupation.name = 'Sports Development Officer'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:35:16+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 282
    occupation.name = 'Other Sports Official'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:36:11+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 283
    occupation.name = 'Snowsport Instructor'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:36:18+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 284
    occupation.name = 'Sports Umpire'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:36:25+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 285
    occupation.name = 'Sportspersons (Others)'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:36:41+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 286
    occupation.name = 'Fitness Centre Manager'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:36:54+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 287
    occupation.name = 'Horse Trainer'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:37:07+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 288
    occupation.name = 'Jockey'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:37:20+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 289
    occupation.name = 'Diving Instructor (Open Water)'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 05:37:42+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 290
    occupation.name = 'Audiologists'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 05:38:19+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 291
    occupation.name = 'Licensed practical nurses'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 05:40:08+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 292
    occupation.name = 'Nursing co-ordinators and supervisors'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 05:40:43+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 293
    occupation.name = 'Registered nurses and registered psychiatric nurses'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 05:41:01+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 294
    occupation.name = 'Nurse Practitioner'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 05:41:42+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 295
    occupation.name = 'Nursing Clinical Director'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 05:42:01+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 296
    occupation.name = 'Registered Nurse (Aged Care)'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 05:42:24+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 297
    occupation.name = 'Registered Nurse (Child and Family Health)'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 05:43:12+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 298
    occupation.name = 'Registered Nurse (Community Health)'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 05:43:36+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 299
    occupation.name = 'Registered Nurse (Critical Care and Emergency)'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 05:44:04+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 300
    occupation.name = 'Registered Nurse (Developmental Disability)'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 05:44:32+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 301
    occupation.name = 'Registered Nurse (Disability and Rehabilitation)'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 05:44:57+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 302
    occupation.name = 'Registered Nurse (Medical Practice)'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 05:45:20+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 303
    occupation.name = 'Registered Nurse (Medical)'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 05:46:22+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 304
    occupation.name = 'Registered Nurse (Mental Health)'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 05:46:53+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 305
    occupation.name = 'Registered Nurse (Paediatrics)'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 05:47:15+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation = Occupation()
    occupation.id = 306
    occupation.name = 'Registered Nurse (Perioperative)'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 05:47:33+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 307
    occupation.name = 'Registered Nurse (Surgical)'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 05:47:58+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 308
    occupation.name = 'Registered Nurses (Others)'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 05:49:13+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 309
    occupation.name = 'Nurse Educator'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 05:49:33+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 310
    occupation.name = 'Nurse Manager'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 05:50:20+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 311
    occupation.name = 'Nurse Researcher'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 05:50:55+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 312
    occupation.name = 'Enrolled Nurse'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 05:51:27+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 313
    occupation.name = 'Mothercraft Nurse'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 05:51:42+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 314
    occupation.name = 'General practitioners and family physicians'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:04:36+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 315
    occupation.name = 'Specialist physicians (General Medicine)'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:05:13+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 316
    occupation.name = 'Specialist Physicians (Others)'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:05:22+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 317
    occupation.name = 'Medical Practitioners (Others)'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:05:36+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 318
    occupation.name = 'Traditional Chinese Medicine Practitioner'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 19:06:52+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 319
    occupation.name = 'Traditional Maori Health Practitioner'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:06:01+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 320
    occupation.name = 'Dentist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:06:25+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 321
    occupation.name = 'Dental Hygienist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:06:48+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 322
    occupation.name = 'Dental Prosthetist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:07:11+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 323
    occupation.name = 'Dental Specialist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:08:16+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 324
    occupation.name = 'Dental Technician'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:08:45+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 325
    occupation.name = 'Dental Therapist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:09:03+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 326
    occupation.name = 'Veterinarian'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:09:27+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 327
    occupation.name = 'Veterinary Nurse'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:09:42+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 328
    occupation.name = 'Optometrist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:10:28+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 329
    occupation.name = 'Chiropractor'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:10:42+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 330
    occupation.name = 'Inspectors in public and environmental health and occupational health and safety'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:11:18+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 331
    occupation.name = 'Hospital Pharmacist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:11:34+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 332
    occupation.name = 'Industrial Pharmacist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:11:45+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 333
    occupation.name = 'Retail Pharmacist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:11:56+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 334
    occupation.name = 'Pharmacy Technician'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:12:07+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 335
    occupation.name = 'Dietitians'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:12:33+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 336
    occupation.name = 'Nutritionists'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:12:51+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 337
    occupation.name = 'Speech Pathologist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:14:04+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 338
    occupation.name = 'Speech Language Therapist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:14:20+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 339
    occupation.name = 'Physiotherapists'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:14:49+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 340
    occupation.name = 'Occupational Therapists'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:15:13+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 341
    occupation.name = 'Respiratory therapists, clinical perfusionists and cardiopulmonary technologists'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:15:41+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 342
    occupation.name = 'Complementary Health Therapists (Others)'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:16:42+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 343
    occupation.name = 'Psychotherapist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:17:07+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 344
    occupation.name = 'Massage Therapist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:17:21+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 345
    occupation.name = 'Diversional Therapist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:17:40+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 346
    occupation.name = 'Medical Radiation Technologist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:18:16+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 347
    occupation.name = 'Medical Sonographer'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:18:32+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 348
    occupation.name = 'Paramedical occupations'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:18:50+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 349
    occupation.name = 'Medical Administrator'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:19:18+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 350
    occupation.name = 'Medical Diagnostic Radiographer'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:35:37+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 351
    occupation.name = 'Medical Laboratory Scientist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:35:50+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 352
    occupation.name = 'Medical Oncologist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:36:01+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 353
    occupation.name = 'Medical Radiation Therapist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:21:30+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 354
    occupation.name = 'Physicist (Medical Physicist only)'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:21:55+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 355
    occupation.name = 'Medical Superintendent'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:22:09+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 356
    occupation.name = 'Resident Medical Officer'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:22:52+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 357
    occupation.name = 'Medical Laboratory Technician'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:23:08+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 358
    occupation.name = 'Medical Technicians (Others)'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:23:28+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 359
    occupation.name = 'Pathologist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:36:24+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 360
    occupation.name = 'Clinical Haematologist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:25:00+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 361
    occupation.name = 'Clinical Psychologist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:25:21+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 363
    occupation.name = 'Clinical Coder'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:25:56+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 364
    occupation.name = 'Cardiologist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:37:15+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 365
    occupation.name = 'Cardiothoracic Surgeon'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:37:32+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 366
    occupation.name = 'Radiation Oncologist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:37:43+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 367
    occupation.name = 'Diagnostic and Interventional Radiologist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:37:52+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 368
    occupation.name = 'Health Diagnostic and Promotion Professionals (Others)'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:30:00+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 369
    occupation.name = 'Dermatologist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:38:07+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 370
    occupation.name = 'Neurosurgeon'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:38:15+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 371
    occupation.name = 'Orthopaedic Surgeon'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:38:20+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 372
    occupation.name = 'Paediatric Surgeon'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:38:26+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 373
    occupation.name = 'Plastic and Reconstructive Surgeon'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:38:32+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 374
    occupation.name = 'Surgeon (General)'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:38:39+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 375
    occupation.name = 'Vascular Surgeon'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:38:45+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 376
    occupation.name = 'Paediatrician'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:38:52+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 377
    occupation.name = 'Psychologists'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:33:30+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 378
    occupation.name = 'Educational Psychologist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:33:56+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 379
    occupation.name = 'Organisational Psychologist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:34:04+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 380
    occupation.name = 'Psychiatrist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:34:23+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 381
    occupation.name = 'Emergency Medicine Specialist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:35:09+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 382
    occupation.name = 'Nuclear Medicine Technologist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:35:21+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 383
    occupation.name = 'Renal Medicine Specialist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:39:13+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 384
    occupation.name = 'Thoracic Medicine Specialist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:39:24+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 385
    occupation.name = 'Endocrinologist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:39:29+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 386
    occupation.name = 'Gastroenterologist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:39:36+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 387
    occupation.name = 'Rheumatologist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:39:42+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 388
    occupation.name = 'Neurologist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:39:48+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 389
    occupation.name = 'Obstetrician and Gynaecologist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:41:40+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 390
    occupation.name = 'Ophthalmologist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:41:57+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 391
    occupation.name = 'Orthoptist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:38:38+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 392
    occupation.name = 'Orthotist or Prosthetist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:39:00+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 393
    occupation.name = 'Otorhinolaryngologist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:43:32+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 394
    occupation.name = 'Rehabilitation Counsellor'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:39:32+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 395
    occupation.name = 'Urologist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:43:55+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 396
    occupation.name = 'Cardiac Technician'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:39:59+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 397
    occupation.name = 'Exercise Physiologist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:40:31+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 398
    occupation.name = 'Health Information Manager'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:40:54+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 399
    occupation.name = 'Health Promotion Officer'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:41:09+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 400
    occupation.name = 'Midwife'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:41:23+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 401
    occupation.name = 'Ambulance Officer'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:41:37+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 402
    occupation.name = 'Ambulance Paramedic'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:41:48+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 403
    occupation.name = 'Health Practice Manager'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:42:02+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 404
    occupation.name = 'Lifeguard'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:42:14+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 405
    occupation.name = 'Primary Health Organisation Manager'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:42:33+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 406
    occupation.name = 'Health and Welfare Services Managers (Others)'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:43:19+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 407
    occupation.name = 'Aboriginal and Torres Strait Islander Health Worker'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:43:33+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 408
    occupation.name = 'Kaiawhina (Hauora) (Maori Health Assistant)'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:43:41+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 409
    occupation.name = 'Managers in health care'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 13:44:01+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 410
    occupation.name = 'Civil Engineer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:44:27+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 411
    occupation.name = 'Aeronautical Engineer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:46:19+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 412
    occupation.name = 'Agricultural Engineer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:46:32+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 413
    occupation.name = 'Electrical and Electronics Engineering Technologists and Technicians'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:47:24+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 414
    occupation.name = 'Electrical Engineer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:47:33+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 415
    occupation.name = 'Biomedical Engineer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:47:48+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 416
    occupation.name = 'Chemical Engineer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:48:12+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 417
    occupation.name = 'Civil Engineering Draftsperson'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:48:24+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 418
    occupation.name = 'Civil Engineering Technician'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:48:38+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 419
    occupation.name = 'Mechanical Engineering Technologists and Technicians'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:49:14+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 420
    occupation.name = 'Mechanical engineers'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:49:30+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 421
    occupation.name = 'Petroleum Engineer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:49:46+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 422
    occupation.name = 'Electrical Engineering Draftsperson'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:49:59+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 423
    occupation.name = 'Electrical Engineering Technician'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:50:06+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 424
    occupation.name = 'Electronics Engineer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:50:25+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 425
    occupation.name = 'Engineering Manager'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:50:37+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 426
    occupation.name = 'Engineering Technologist'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:50:53+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 427
    occupation.name = 'Environmental Engineer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:52:59+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 428
    occupation.name = 'Geotechnical Engineer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:53:16+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 429
    occupation.name = 'Industrial Engineer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:53:29+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 430
    occupation.name = 'Materials Engineer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:53:50+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 431
    occupation.name = 'Engineering Professionals (Others)'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:54:02+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 432
    occupation.name = 'Mining Engineer (Excluding Petroleum)'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:54:20+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 433
    occupation.name = 'Production or Plant Engineer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:54:42+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 434
    occupation.name = 'Ships Engineer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:55:21+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 435
    occupation.name = 'Structural Engineer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:55:36+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 436
    occupation.name = 'Telecommunications Engineer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:55:52+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 437
    occupation.name = 'Telecommunications Field Engineer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:56:07+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 438
    occupation.name = 'Telecommunications Network Engineer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:56:24+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 439
    occupation.name = 'Transport Engineer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:58:03+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 440
    occupation.name = 'Building and Engineering Technicians (Others)'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:59:20+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 441
    occupation.name = 'Electronic Engineering Draftsperson'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:00:04+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 442
    occupation.name = 'Electronic Engineering Technician'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 13:59:53+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 443
    occupation.name = 'Mechanical Engineering Draftsperson'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:00:55+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 444
    occupation.name = 'Mechanical Engineering Technician'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:01:17+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 445
    occupation.name = 'Computing professionals - Computer Network Technician'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:02:27+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 446
    occupation.name = 'Computing professionals - Web Developer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:03:05+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 447
    occupation.name = 'Computing professionals - Computer Network and Systems Engineer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:04:34+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 448
    occupation.name = 'Computing professionals - Analyst Programmer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:04:59+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 449
    occupation.name = 'Computing professionals - Developer Programmer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:05:08+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 450
    occupation.name = 'Computing professionals - Software and Applications Programmers (Others)'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:05:17+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 451
    occupation.name = 'Computing professionals - Web Administrator'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:05:31+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 452
    occupation.name = 'Computing professionals - Software Engineer or Designer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:05:39+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 453
    occupation.name = 'Computing professionals - Software Tester'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:05:51+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 454
    occupation.name = 'Computing professionals - Information Systems Analysts and Consultants'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:06:41+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 455
    occupation.name = 'Computing professionals - ICT business Analyst'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:06:59+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 456
    occupation.name = 'Computing professionals - ICT Account Manager'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:07:16+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 457
    occupation.name = 'Computing professionals - ICT Business Development Manager'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:07:35+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 458
    occupation.name = 'Computing professionals - ICT Managers (Others)'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:07:44+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 459
    occupation.name = 'Computing professionals - ICT Project Manager'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:08:12+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 460
    occupation.name = 'Computing professionals - ICT Quality Assurance Engineer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:08:42+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 461
    occupation.name = 'Computing professionals - ICT Sales Representative'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:08:59+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 462
    occupation.name = 'Computing professionals - ICT Security Specialist'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:09:13+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 463
    occupation.name = 'Computing professionals - ICT Support and Test Engineers (Others)'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:09:20+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 464
    occupation.name = 'Computing professionals - ICT Support Engineer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:09:29+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 465
    occupation.name = 'Computing professionals - ICT Systems Test Engineer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:10:14+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 466
    occupation.name = 'Computing professionals - ICT Trainer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:10:24+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 467
    occupation.name = 'Computing professionals - ICT Customer Support Officer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:10:32+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 468
    occupation.name = 'Computing professionals - ICT Support Technicians (Others)'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:10:40+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 469
    occupation.name = 'Computing professionals - Chief Information Officer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:11:42+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 470
    occupation.name = 'Computing professionals - Multimedia Specialist'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:11:58+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 471
    occupation.name = 'Computing professionals - Database Analysts and Administrators'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:12:26+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 472
    occupation.name = 'Computing professionals - Systems Analyst'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:12:33+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 473
    occupation.name = 'Computing professionals - Systems Administrator'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:16:14+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 474
    occupation.name = 'Computing professionals - Network Administrator'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:15:59+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 475
    occupation.name = 'Computing professionals - Network Analyst'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:16:36+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 476
    occupation.name = 'Physicist'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:18:09+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 477
    occupation.name = 'Biochemist'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:18:30+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 478
    occupation.name = 'Chemist'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:18:47+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 479
    occupation.name = 'Chemistry Technician'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:18:53+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 480
    occupation.name = 'Agricultural Scientist'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:19:09+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 481
    occupation.name = 'Geoscientists and Oceanographers'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:19:33+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 482
    occupation.name = 'Other Spatial Scientist'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:20:59+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 483
    occupation.name = 'Forest Scientist'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:21:12+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 484
    occupation.name = 'Life Scientist (General)'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:21:26+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 485
    occupation.name = 'Life Scientists (Others)'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:21:40+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 486
    occupation.name = 'Geophysicist'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:21:50+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 487
    occupation.name = 'Natural and Physical Science Professionals (Others)'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:22:41+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 488
    occupation.name = 'Biotechnologist'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:22:51+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 489
    occupation.name = 'Marine Biologist'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:23:10+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 490
    occupation.name = 'Microbiologist'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:23:17+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 491
    occupation.name = 'Agricultural Consultant'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:23:30+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 492
    occupation.name = 'Agricultural Technician'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:23:40+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 493
    occupation.name = 'Geologist'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:23:53+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 494
    occupation.name = 'Hydrogeologist'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:24:01+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 495
    occupation.name = 'Architect'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:24:37+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 496
    occupation.name = 'Landscape Architect'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:24:48+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 497
    occupation.name = 'Naval Architect'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:25:21+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation = Occupation()
    occupation.id = 498
    occupation.name = 'Architectural, Building and Surveying Technicians (Others)'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:25:42+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 499
    occupation.name = 'Architectural Draftsperson'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:25:57+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 500
    occupation.name = 'Urban and Regional Planner'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:26:26+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 501
    occupation.name = 'Mathematician'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:26:43+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 502
    occupation.name = 'Statistician'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:26:53+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 503
    occupation.name = 'Earth Science Technician'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:27:08+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 504
    occupation.name = 'Quantity Surveyor'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:27:32+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 505
    occupation.name = 'Surveyor'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:27:40+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 506
    occupation.name = 'Marine Surveyor'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:27:53+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 507
    occupation.name = 'Construction estimators'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:28:13+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 508
    occupation.name = 'Construction Managers or Construction Project Managers'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:28:49+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 509
    occupation.name = 'Aeroplane Pilot'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:29:03+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 510
    occupation.name = 'Helicopter Pilot'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:29:25+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 511
    occupation.name = 'Flying Instructor'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:29:35+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 512
    occupation.name = 'Air Traffic Controller'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:29:49+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 513
    occupation.name = 'Building Inspector'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:29:59+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 514
    occupation.name = 'Building Associate'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:30:09+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 515
    occupation.name = 'Environmental Consultant'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:30:19+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 516
    occupation.name = 'Environmental Manager'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:30:30+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 517
    occupation.name = 'Environmental Research Scientist'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:30:46+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 518
    occupation.name = 'Environmental Scientists (Others)'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:30:52+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 519
    occupation.name = 'Life Science Technicians'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:31:09+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 520
    occupation.name = 'Science Technicians (Others)'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:31:27+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 521
    occupation.name = 'Surveying or Spatial Science Technician'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:31:50+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 522
    occupation.name = 'University Professor or lecturer'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:43:29+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 523
    occupation.name = 'Early Childhood (Pre-primary School) Teacher'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:44:31+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 524
    occupation.name = 'Secondary School Teacher'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:45:00+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 525
    occupation.name = 'Special Education Teachers (Others)'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:45:15+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 526
    occupation.name = 'Special Needs Teacher'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:45:32+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 527
    occupation.name = 'Intermediate School Teacher'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:46:49+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 528
    occupation.name = 'Kaiako Kohanga Reo (Maori Language Nest Teacher)'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:46:56+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 529
    occupation.name = 'Kaiako Kura Kaupapa Maori (Maori-medium Primary School Teacher)'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:47:02+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 530
    occupation.name = 'Teacher of the Hearing Impaired'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:47:20+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 531
    occupation.name = 'Teacher of the Sight Impaired'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:47:35+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 532
    occupation.name = 'Polytechnic Teacher'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:47:49+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 533
    occupation.name = 'Pouako Kura Kaupapa Maori (Maori-medium Primary School Senior Teacher)'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:47:54+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 534
    occupation.name = 'Primary School Teacher'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:48:15+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 535
    occupation.name = 'Private Tutors and Teachers (Others)'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:48:33+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 536
    occupation.name = 'Secondary School Teacher'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:49:36+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 537
    occupation.name = 'Teacher of English to Speakers of Other Languages'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:49:54+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 538
    occupation.name = 'School Principal'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:50:10+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 539
    occupation.name = 'School Laboratory Technician'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:50:20+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 540
    occupation.name = 'University Tutor'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:50:32+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 541
    occupation.name = 'Early Childhood (Pre-primary school) Assistants'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:51:26+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 542
    occupation.name = 'Education Adviser'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:51:55+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 543
    occupation.name = 'Education Managers (Others)'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:52:16+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 544
    occupation.name = 'Education Reviewer'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:52:27+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 545
    occupation.name = 'Regional Education Manager'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:52:38+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 546
    occupation.name = 'Judge'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:52:50+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 547
    occupation.name = 'Intellectual Property Lawyer'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:53:02+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 548
    occupation.name = 'Law Clerk'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:53:52+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 549
    occupation.name = 'Judicial and Other Legal Professionals (Others)'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:54:19+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 550
    occupation.name = 'Legal Executive'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:54:30+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 551
    occupation.name = 'Legal Secretary'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:56:56+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 552
    occupation.name = 'Legislators (Others)'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:57:08+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 553
    occupation.name = 'Local Government Legislator'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:57:15+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 554
    occupation.name = 'Magistrate'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:57:38+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 555
    occupation.name = 'Social Worker'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:57:50+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 556
    occupation.name = 'Social Professionals (Others)'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:58:10+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 557
    occupation.name = 'Family Support Worker'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:58:20+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 558
    occupation.name = 'Family and Marriage Counsellor'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:58:36+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 559
    occupation.name = 'Student Counsellor'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:59:13+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 560
    occupation.name = 'Careers Counsellor'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:59:25+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 561
    occupation.name = 'Counsellors (Others)'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:59:49+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 562
    occupation.name = 'Drug and Alcohol Counsellor'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 17:59:59+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 563
    occupation.name = 'Minister of Religion'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:00:12+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 564
    occupation.name = 'Parole or Probation Officer'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:02:02+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 565
    occupation.name = 'Community Worker'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:02:13+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 566
    occupation.name = 'Policy Analyst'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:02:24+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 567
    occupation.name = 'Policy and Planning Manager'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:02:34+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 568
    occupation.name = 'Police Officer'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:02:50+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 569
    occupation.name = 'Commissioned Police Officer'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:02:56+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 570
    occupation.name = 'Commissioned Defence Force Officer'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:04:39+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 571
    occupation.name = 'Commissioned Fire Officer'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:04:47+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 572
    occupation.name = 'Disabilities Services Officer'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:05:27+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 573
    occupation.name = 'Detective'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:05:36+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 574
    occupation.name = 'Defence Force Senior Officer'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:05:46+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 575
    occupation.name = 'Electorate Officer'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:05:54+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 576
    occupation.name = 'Intelligence Officer'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:06:04+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 577
    occupation.name = 'Liaison Officer'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:06:13+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 578
    occupation.name = 'Residential Care Officer'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:06:22+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 579
    occupation.name = 'Court Collections Officer'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:06:37+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 580
    occupation.name = 'Court Registry Officer'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:06:53+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 581
    occupation.name = 'Clerk of Court'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:07:03+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 582
    occupation.name = 'Fire Fighter'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:07:12+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 583
    occupation.name = 'Child Care Centre Manager'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:07:26+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 584
    occupation.name = 'Welfare Worker'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:07:44+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 585
    occupation.name = 'Welfare Centre Manager'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:10:32+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 586
    occupation.name = 'Conveyancer'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:10:42+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 587
    occupation.name = 'Barrister'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:10:53+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 588
    occupation.name = 'Solicitor'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:11:05+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 589
    occupation.name = 'Forester'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 15:51:29+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation = Occupation()
    occupation.id = 590
    occupation.name = 'Market Gardener'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 15:53:59+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 591
    occupation.name = 'Production Manager (Mining)'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 15:54:18+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 592
    occupation.name = 'Production Manager (Forestry)'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 15:54:31+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 593
    occupation.name = 'Crop Farmers (Others)'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 15:54:45+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 594
    occupation.name = 'Field Crop Grower'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 15:54:55+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 595
    occupation.name = 'Mixed Crop and Livestock Farmer'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 15:55:06+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 596
    occupation.name = 'Mixed Crop Farmer'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 15:55:15+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 597
    occupation.name = 'Dairy Cattle Farmer'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 15:55:25+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 598
    occupation.name = 'Deer Farmer'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 15:55:37+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 599
    occupation.name = 'Goat Farmer'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 15:55:47+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 600
    occupation.name = 'Livestock Farmers (Others)'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 15:56:02+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 601
    occupation.name = 'Mixed Livestock Farmer'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 15:56:19+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 602
    occupation.name = 'Pig Farmer'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 15:56:27+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 603
    occupation.name = 'Poultry Farmer'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 15:56:37+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 604
    occupation.name = 'Sheep Farmer'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 15:56:47+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 605
    occupation.name = 'Aquaculture Farmer'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 17:22:55+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 606
    occupation.name = 'Beef Cattle Farmer'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 17:23:07+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 607
    occupation.name = 'Managers in natural resources production and fishing'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 17:23:43+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 608
    occupation.name = 'Master Fisher'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 17:24:13+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 609
    occupation.name = 'Fisheries Officer'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 17:24:22+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 610
    occupation.name = 'Botanist'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 17:24:38+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 611
    occupation.name = 'Drainer'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 17:24:47+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation = Occupation()
    occupation.id = 612
    occupation.name = 'Cotton Grower'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 17:24:59+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 613
    occupation.name = 'Fruit or Nut Grower'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 17:28:21+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 614
    occupation.name = 'Grape Grower'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 17:28:52+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 615
    occupation.name = 'Sugar Cane Grower'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 17:29:04+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 616
    occupation.name = 'Turf Grower'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 17:32:25+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 617
    occupation.name = 'Wine Maker'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 17:32:51+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 618
    occupation.name = 'Sales and Marketing Manager'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:52:05+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 619
    occupation.name = 'Sales Representative (Industrial Products)'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:52:19+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 620
    occupation.name = 'Sales Representative (Medical and Pharmaceutical Products)'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:52:29+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 621
    occupation.name = 'Technical Sales Representatives (Others)'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:52:47+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 622
    occupation.name = 'Real Estate Agency Licensee'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:53:16+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 623
    occupation.name = 'Real Estate Agent'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:53:26+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 624
    occupation.name = 'Real Estate Representative'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:55:19+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 625
    occupation.name = 'Accommodation and Hospitality Managers (Others)'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:55:38+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 626
    occupation.name = 'Hospitality, Retail and Service Managers (Others)'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:55:59+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 627
    occupation.name = 'Travel Agency Manager'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:56:09+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 628
    occupation.name = 'Travel Attendants (Others)'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:56:21+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 629
    occupation.name = 'Customer Service Manager'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:56:32+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 630
    occupation.name = 'Chef'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:56:44+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 631
    occupation.name = 'Cook'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:56:59+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 632
    occupation.name = 'Pastrycook'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:57:17+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 633
    occupation.name = 'Butcher or Smallgoods Maker'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:57:26+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 634
    occupation.name = 'Meat Inspector'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:57:42+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 635
    occupation.name = 'Baker'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:57:52+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 636
    occupation.name = 'Hairdresser'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:58:07+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 637
    occupation.name = 'Hair or Beauty Salon Manager'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:58:22+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 638
    occupation.name = 'Dressmaker or Tailor'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:58:36+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 639
    occupation.name = 'Shoemaker'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:58:46+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 640
    occupation.name = 'Jeweller'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:58:58+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 641
    occupation.name = 'Watch and Clock Maker and Repairer'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:59:12+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 642
    occupation.name = 'Funeral Director'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:59:23+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 643
    occupation.name = 'Funeral Workers (Others)'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:59:36+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 644
    occupation.name = 'Security Consultant'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:59:46+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 645
    occupation.name = 'Pet Groomer'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 18:59:56+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 646
    occupation.name = 'Animal Attendants and Trainers (Others)'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 19:00:08+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 647
    occupation.name = 'Podiatrist'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 19:00:32+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 648
    occupation.name = 'Supply and Distribution Manager'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 19:00:48+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 649
    occupation.name = 'Wholesaler'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 19:00:56+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 650
    occupation.name = 'Amusement Centre Manager'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 19:01:08+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 651
    occupation.name = 'Cafe or Restaurant Manager'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 19:01:55+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 652
    occupation.name = 'Bed and Breakfast Operator'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 19:02:05+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 653
    occupation.name = 'Betting Agency Manager'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 19:02:16+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 654
    occupation.name = 'Boarding Kennel or Cattery Operator'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 19:02:31+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 655
    occupation.name = 'Caravan Park and Camping Ground Manager'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 19:02:41+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 656
    occupation.name = 'Hotel or Motel Manager'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 19:02:50+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 657
    occupation.name = 'Licensed Club Manager'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 19:02:59+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 658
    occupation.name = 'Retail Manager (General)'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 19:03:14+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 659
    occupation.name = 'Metal Fabricator'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 14:57:38+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 660
    occupation.name = 'Metal Machinist (First Class)'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 14:58:01+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 661
    occupation.name = 'Metallurgist'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 14:58:11+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 662
    occupation.name = 'Sheetmetal Trades Worker'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 14:58:32+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 663
    occupation.name = 'Metallurgical or Materials Technician'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 14:58:48+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 664
    occupation.name = 'Metal Casting Trades Worker'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 14:59:01+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 665
    occupation.name = 'Metal Fitters and Machinists (Others)'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 14:59:23+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 666
    occupation.name = 'Metal Polisher'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 14:59:35+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 667
    occupation.name = 'Sheetmetal Trades Worker'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 14:59:49+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 668
    occupation.name = 'Electrical Line Mechanic'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:00:02+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 669
    occupation.name = 'Electrical Linesworker'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:00:16+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 670
    occupation.name = 'Technical Cable Jointer'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:00:29+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 671
    occupation.name = 'Printing Machinist'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:00:50+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 672
    occupation.name = 'Wood Machinist'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:01:00+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 673
    occupation.name = 'Wood Machinists and Other Wood Trades Workers (Others)'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:01:05+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 674
    occupation.name = 'Toolmaker'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:01:22+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 675
    occupation.name = 'Fitter-Welder'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:01:34+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 676
    occupation.name = 'Pressure Welder'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:01:57+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 677
    occupation.name = 'Welder (First Class)'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:02:05+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 678
    occupation.name = 'Cabler (Data and Telecommunications)'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:02:18+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 679
    occupation.name = 'Telecommunications Cable Jointer'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:02:32+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 680
    occupation.name = 'Airconditioning and Mechanical Services Plumber'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 19:07:18+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 681
    occupation.name = 'Plumber (General)'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 19:07:33+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 682
    occupation.name = 'Roof plumber'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 19:07:43+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 683
    occupation.name = 'Carpenter'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 19:07:54+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 684
    occupation.name = 'Carpenter and Joiner'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 19:08:00+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 685
    occupation.name = 'Bricklayer'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 19:08:10+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 686
    occupation.name = 'Fibrous Plasterer'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 19:08:28+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 687
    occupation.name = 'Solid Plasterer'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 19:08:48+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 688
    occupation.name = 'Print Finisher'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 19:08:57+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 689
    occupation.name = 'Floor Finisher'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:02:44+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 690
    occupation.name = 'Furniture Finisher'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:02:55+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 691
    occupation.name = 'Glazier'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:03:16+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 692
    occupation.name = 'Vehicle Painter'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:03:27+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 693
    occupation.name = 'Wall and Floor Tiler'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:03:46+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 694
    occupation.name = 'Airconditioning and Refrigeration Mechanic'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:04:01+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 695
    occupation.name = 'Diesel Motor Mechanic'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:04:13+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 696
    occupation.name = 'Lift Mechanic'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:04:30+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 697
    occupation.name = 'Motor Mechanic (General)'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:04:50+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 698
    occupation.name = 'Motorcycle Mechanic'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:05:06+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 699
    occupation.name = 'Small Engine Mechanic'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:05:18+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 700
    occupation.name = 'Aircraft Maintenance Engineer (Mechanical)'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:05:37+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 701
    occupation.name = 'Aircraft Maintenance Engineer (Avionics)'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:05:42+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 702
    occupation.name = 'Business Machine Mechanic'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:05:48+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 703
    occupation.name = 'Optical Mechanic'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:06:01+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 704
    occupation.name = 'Telecommunications Line Mechanic'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:06:14+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 705
    occupation.name = 'Automotive Electrician'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:06:32+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 706
    occupation.name = 'Air Transport Professionals (Others)'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:06:50+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 707
    occupation.name = 'Boat Builder and Repairer'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:07:08+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 708
    occupation.name = 'Electrician (General)'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:07:57+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 709
    occupation.name = 'Electrician (Special Class)'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:08:10+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 710
    occupation.name = 'Electronic Equipment Trades Worker'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:08:23+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 711
    occupation.name = 'Electronic Instrument Trades Worker (General)'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:08:33+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 712
    occupation.name = 'Electronic Instrument Trades Worker (Special Class)'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:08:41+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 713
    occupation.name = 'Fitter (General)'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:09:01+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 714
    occupation.name = 'Fitter and Turner'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:09:15+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 715
    occupation.name = 'Gasfitter'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:09:30+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 716
    occupation.name = 'Joiner'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:09:51+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 717
    occupation.name = 'Locksmith'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:10:18+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 718
    occupation.name = 'Painting trades workers'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:10:31+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation = Occupation()
    occupation.id = 719
    occupation.name = 'Ships Master'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:10:55+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 720
    occupation.name = 'Ships Officer'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:11:11+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 721
    occupation.name = 'Shipwright'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:11:23+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 722
    occupation.name = 'Stonemason'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:11:46+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 723
    occupation.name = 'Manufacturer'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:11:58+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 724
    occupation.name = 'Marine Transport Professionals (Others)'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:12:13+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 725
    occupation.name = 'Production Manager (Manufacturing)'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:12:45+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 726
    occupation.name = 'Equipment Hire Manager'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:13:58+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 727
    occupation.name = 'Fleet Manager'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:14:26+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 728
    occupation.name = 'Transport Company Manager'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:15:05+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 729
    occupation.name = 'Apparel Cutter'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:15:35+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 730
    occupation.name = 'Automotive Electrician'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:15:54+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 731
    occupation.name = 'Blacksmith'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:16:14+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 732
    occupation.name = 'Boat Builder and Repairer'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:16:35+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 733
    occupation.name = 'Cabinetmaker'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:17:24+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 734
    occupation.name = 'Canvas Goods Fabricator'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:17:36+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 735
    occupation.name = 'Chemical Plant Operator'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:17:45+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 736
    occupation.name = 'Communications Operator'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:17:56+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 737
    occupation.name = 'Drainlayer'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:18:14+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 738
    occupation.name = 'Electroplater'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:18:25+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 739
    occupation.name = 'Farrier'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:18:34+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 740
    occupation.name = 'Fire Protection Equipment Technician'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:18:45+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 741
    occupation.name = 'Gas or Petroleum Operator'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:18:55+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 742
    occupation.name = 'Leather Goods Maker'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:19:02+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 743
    occupation.name = 'Light Technician'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:19:14+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 744
    occupation.name = 'Panelbeater'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:19:27+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 745
    occupation.name = 'Picture Framer'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:19:38+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 746
    occupation.name = 'Plastics Technician'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:20:28+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 747
    occupation.name = 'Power Generation Plant Operator'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:20:42+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 748
    occupation.name = 'Precision Instrument Maker and Repairer'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:20:56+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 749
    occupation.name = 'Roof Tiler'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:21:13+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 750
    occupation.name = 'Sail Maker'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:21:34+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 751
    occupation.name = 'Saw Maker and Repairer'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:21:45+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 752
    occupation.name = 'Screen Printer'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:21:58+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 753
    occupation.name = 'Small Offset Printer'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:22:12+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 754
    occupation.name = 'Sound Technician'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:22:28+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 755
    occupation.name = 'Technicians and Trades Workers (Others)'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:22:41+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 756
    occupation.name = 'Telecommunications Technician'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:22:52+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 757
    occupation.name = 'Television Equipment Operator'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:23:04+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 758
    occupation.name = 'Textile, Clothing and Footwear Mechanic'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:23:15+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 759
    occupation.name = 'Upholsterer'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:23:36+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 760
    occupation.name = 'Vehicle Body Builder'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:23:53+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 761
    occupation.name = 'Vehicle Trimmer'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:24:16+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 762
    occupation.name = 'Wood Turner'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:24:26+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 763
    occupation.name = 'Arborist'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:24:36+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 764
    occupation.name = 'Clothing Trades Workers (Others)'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:24:49+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 765
    occupation.name = 'Florist'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:25:01+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 766
    occupation.name = 'Gardener (General)'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:25:23+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 767
    occupation.name = 'Greenkeeper'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:25:34+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 768
    occupation.name = 'Kennel Hand'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:25:48+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 769
    occupation.name = 'Landscape Gardener'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:26:01+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 770
    occupation.name = 'Nurseryperson'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:26:19+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 771
    occupation.name = 'Wool Classer'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:26:31+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 772
    occupation.name = 'Advertising Manager'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:31:35+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 773
    occupation.name = 'Advertising Specialist'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:31:52+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 774
    occupation.name = 'Home building and renovation managers'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:32:16+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 775
    occupation.name = 'Human resources managers'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:32:39+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 776
    occupation.name = 'Professional occupations in advertising, marketing and public relations (Others)'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:33:00+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 777
    occupation.name = 'Purchasing managers'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:33:16+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 778
    occupation.name = 'Chief Executive or Managing Director'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:33:56+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 779
    occupation.name = 'Senior managers – financial, communications and other business services'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:34:21+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 780
    occupation.name = 'Senior managers – trade, broadcasting and other services (Others)'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:35:01+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 781
    occupation.name = 'Company Secretary'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:35:17+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 782
    occupation.name = 'Corporate General Manager'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:37:28+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 783
    occupation.name = 'Corporate Services Manager'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:37:51+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 784
    occupation.name = 'Corporate Treasurer'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:39:22+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 785
    occupation.name = 'Futures Trader'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:39:55+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 786
    occupation.name = 'Project Builder'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:40:24+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 787
    occupation.name = 'Human Resource Adviser'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:40:48+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 788
    occupation.name = 'Human Resource Manager'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:40:57+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 789
    occupation.name = 'Importer or Exporter'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:41:07+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 790
    occupation.name = 'Information and Organisation Professionals (Others)'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:41:33+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 791
    occupation.name = 'Management Consultant'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:41:42+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 792
    occupation.name = 'Market Research Analyst'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:41:56+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 793
    occupation.name = 'Marketing Specialist'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:42:06+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 794
    occupation.name = 'Organisation and Methods Analyst'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:42:15+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 795
    occupation.name = 'Procurement Manager'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:42:26+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 796
    occupation.name = 'Public Relations Manager'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:42:36+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 797
    occupation.name = 'Public Relations Professional'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:42:46+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 798
    occupation.name = 'Quality Assurance Manager'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:43:11+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 799
    occupation.name = 'Recruitment Consultant'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:43:21+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 800
    occupation.name = 'Research and Development Manager'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:43:59+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 801
    occupation.name = 'Specialist Managers (Others)'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:44:14+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 802
    occupation.name = 'Technical Director'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:44:30+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 803
    occupation.name = 'Training and Development Professional'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:44:40+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 804
    occupation.name = 'Call or Contact Centre Manager'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:44:52+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 805
    occupation.name = 'Commodities Trader'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:45:04+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 806
    occupation.name = 'Conference and Event Organiser'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:45:14+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 807
    occupation.name = 'Facilities Manager'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:45:24+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 808
    occupation.name = 'Maintenance Planner'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:45:39+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 809
    occupation.name = 'Office Manager'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:45:58+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 810
    occupation.name = 'Post Office Manager'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:46:15+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 811
    occupation.name = 'Practice Managers (Others)'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:46:25+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 812
    occupation.name = 'Railway Station Manager'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:46:35+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 813
    occupation.name = 'Retirement Village Manager'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:46:58+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 814
    occupation.name = 'Call or Contact Centre Team Leader'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:47:13+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 815
    occupation.name = 'Personal Assistant'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:47:36+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 816
    occupation.name = 'Retail Buyer'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:47:51+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 817
    occupation.name = 'Secretary (General)'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:48:22+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 818
    occupation.name = 'Trust Officer'
    occupation.occupation_category_id = 1
    occupation.modified_date = '2014-11-26 18:48:45+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 819
    occupation.name = 'Stage Manager'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 14:52:41+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 820
    occupation.name = 'Television Presenter'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 14:52:51+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 821
    occupation.name = 'Dog or Horse Racing Official'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 14:53:03+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 822
    occupation.name = 'Footballer'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 14:53:13+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 823
    occupation.name = 'Golfer'
    occupation.occupation_category_id = 2
    occupation.modified_date = '2014-11-26 14:53:19+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 824
    occupation.name = 'Acupuncturist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:45:19+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 825
    occupation.name = 'Anaesthetist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:44:48+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 826
    occupation.name = 'Environmental Health Officer'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:45:42+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 827
    occupation.name = 'Intensive Care Specialist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:46:03+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 828
    occupation.name = 'Osteopath'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:46:15+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 829
    occupation.name = 'Podiatrist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:46:41+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 830
    occupation.name = 'Naturopath'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:46:55+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 831
    occupation.name = 'Anaesthetic Technician'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:47:06+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 832
    occupation.name = 'Quarantine Officer'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:47:17+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 833
    occupation.name = 'First Aid Trainer'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:47:29+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 834
    occupation.name = 'Phlebotomist'
    occupation.occupation_category_id = 3
    occupation.modified_date = '2014-11-26 14:48:21+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 835
    occupation.name = 'Industrial instrument technicians and mechanics'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:48:50+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 836
    occupation.name = 'Cartographer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:49:23+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 837
    occupation.name = 'Food Technologist'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:49:39+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 838
    occupation.name = 'Laboratory Manager'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:49:54+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 839
    occupation.name = 'Telecommunications Network Planner'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:50:08+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 840
    occupation.name = 'Telecommunications Technical Officer or Technologist'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:50:26+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 117 )

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 841
    occupation.name = 'Meteorologist'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:50:40+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 842
    occupation.name = 'Patents Examiner'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:50:54+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 843
    occupation.name = 'Zoologist'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:51:08+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 844
    occupation.name = 'Hydrographer'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:51:24+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 845
    occupation.name = 'Mine Deputy'
    occupation.occupation_category_id = 4
    occupation.modified_date = '2014-11-26 14:51:37+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 846
    occupation.name = 'Archaeologist'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:11:47+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 847
    occupation.name = 'Faculty Head'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:11:59+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 848
    occupation.name = 'Historian'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:12:09+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 849
    occupation.name = 'Migration Agent'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:12:26+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 850
    occupation.name = 'Member of Parliament'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:12:36+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 851
    occupation.name = 'Park Ranger'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:12:44+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 852
    occupation.name = 'Senior Non-commissioned Defence Force'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:12:53+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 853
    occupation.name = 'Tribunal Member'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:13:01+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 854
    occupation.name = 'Workplace Relations Adviser'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:13:12+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 855
    occupation.name = 'Youth Worker'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:13:24+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 856
    occupation.name = 'Defence Force Member - Other Ranks'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:13:32+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 857
    occupation.name = 'Emergency Service Worker'
    occupation.occupation_category_id = 5
    occupation.modified_date = '2014-11-26 18:13:41+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 858
    occupation.name = 'Apiarist'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 18:13:53+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 859
    occupation.name = 'Horse Breeder'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 17:33:36+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 860
    occupation.name = 'Primary Products Inspectors (Others)'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 17:34:33+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 861
    occupation.name = 'Shearer'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 17:36:42+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 862
    occupation.name = 'Stock and Station Agent'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 17:37:26+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 863
    occupation.name = 'Wool Buyer'
    occupation.occupation_category_id = 6
    occupation.modified_date = '2014-11-26 17:39:59+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 864
    occupation.name = 'Diver'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 17:40:39+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 865
    occupation.name = 'Auctioneer'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 19:09:21+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 866
    occupation.name = 'Dispensing Optician'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 19:09:30+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 867
    occupation.name = 'Dog Handler or Trainer'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 19:09:39+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 868
    occupation.name = 'Driving Instructor'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 19:09:52+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 869
    occupation.name = 'Hotel Service Manager'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 19:10:02+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 870
    occupation.name = 'Property Manager'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 19:10:30+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation.countries.add( 204 )

    occupation = Occupation()
    occupation.id = 871
    occupation.name = 'Zookeeper'
    occupation.occupation_category_id = 7
    occupation.modified_date = '2014-11-26 19:10:39+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 872
    occupation.name = 'Flower Grower'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:27:02+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 873
    occupation.name = 'Hardware Technician'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:27:13+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 874
    occupation.name = 'Plumbing Inspector'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:27:22+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 875
    occupation.name = 'Engineering Patternmaker'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:27:32+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 876
    occupation.name = 'Engraver'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:27:43+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

    occupation = Occupation()
    occupation.id = 877
    occupation.name = 'Flight Attendant'
    occupation.occupation_category_id = 8
    occupation.modified_date = '2014-11-26 15:27:52+00:00'
    occupation.created_date = '2014-11-25 18:20:21+00:00'
    occupation.save()

    occupation.countries.add( 131 )

class Migration(migrations.Migration):

    dependencies = [
        ('points', '0001_initial'),
    ]

    operations = [
        migrations.RunPython( points_immigration_rules ),
    ]
