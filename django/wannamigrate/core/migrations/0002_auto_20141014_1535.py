# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


#######################
# AUTH GROUPS
#######################
def auth_group_initial_values( apps, schema_editor ):

    # Get model to use (historical version)
    Group = apps.get_model( "auth", "Group" )

    # Insert data
    group = Group()
    group.id = 1
    group.name = 'Admin / Staff'
    group.save()

    group = Group()
    group.id = 2
    group.name = 'Users'
    group.save()


#######################
# CONTINENTS
#######################
def core_continent_initial_values( apps, schema_editor ):

    # Get model to use (historical version)
    Continent = apps.get_model( "core", "Continent" )

    # Insert data
    continent = Continent()
    continent.id = 1
    continent.name = 'Africa'
    continent.save()

    continent = Continent()
    continent.id = 2
    continent.name = 'Antarctica'
    continent.save()

    continent = Continent()
    continent.id = 3
    continent.name = 'Asia'
    continent.save()

    continent = Continent()
    continent.id = 4
    continent.name = 'Europe'
    continent.save()

    continent = Continent()
    continent.id = 5
    continent.name = 'North America'
    continent.save()

    continent = Continent()
    continent.id = 6
    continent.name = 'Oceania'
    continent.save()

    continent = Continent()
    continent.id = 7
    continent.name = 'South America'
    continent.save()


#######################
# COUNTRIES
#######################
def core_country_initial_values( apps, schema_editor ):

    # Get model to use (historical version)
    Country = apps.get_model( "core", "Country" )
    Continent = apps.get_model( "core", "Continent" )

    # Insert data
    country = Country()
    country.id = 1
    country.name = 'Algeria'
    country.code = 'DZ'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 2
    country.name = 'Angola'
    country.code = 'AO'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 3
    country.name = 'Ascension'
    country.code = 'SH'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 4
    country.name = 'Benin'
    country.code = 'BJ'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 5
    country.name = 'Botswana'
    country.code = 'BW'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 6
    country.name = 'Burkina Faso'
    country.code = 'BF'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 7
    country.name = 'Burundi'
    country.code = 'BI'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 8
    country.name = 'Cameroon'
    country.code = 'CM'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 9
    country.name = 'Cape Verde Islands'
    country.code = 'CV'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 10
    country.name = 'Central African Republic'
    country.code = 'CF'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 11
    country.name = 'Chad Republic'
    country.code = 'TD'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 12
    country.name = 'Comoros'
    country.code = 'KM'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 13
    country.name = 'Congo'
    country.code = 'CG'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 14
    country.name = 'Djibouti'
    country.code = 'DJ'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 15
    country.name = 'Egypt'
    country.code = 'EG'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 16
    country.name = 'Equatorial Guinea'
    country.code = 'GQ'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 17
    country.name = 'Eritrea'
    country.code = 'ER'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 18
    country.name = 'Ethiopia'
    country.code = 'ET'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 19
    country.name = 'Gabon Republic'
    country.code = 'GA'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 20
    country.name = 'Gambia'
    country.code = 'GM'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 21
    country.name = 'Ghana'
    country.code = 'GH'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 22
    country.name = 'Guinea-Bissau'
    country.code = 'GW'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 23
    country.name = 'Guinea'
    country.code = 'GN'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 24
    country.name = 'Ivory Coast'
    country.code = 'CI'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 25
    country.name = 'Kenya'
    country.code = 'KE'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 26
    country.name = 'Lesotho'
    country.code = 'LS'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 27
    country.name = 'Liberia'
    country.code = 'LR'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 28
    country.name = 'Libya'
    country.code = 'LY'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 29
    country.name = 'Madagascar'
    country.code = 'MG'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 30
    country.name = 'Malawi'
    country.code = 'MW'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 31
    country.name = 'Mali Republic'
    country.code = 'ML'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 32
    country.name = 'Mauritania'
    country.code = 'MR'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 33
    country.name = 'Mauritius'
    country.code = 'MU'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 34
    country.name = 'Mayotte Island'
    country.code = 'YT'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 35
    country.name = 'Morocco'
    country.code = 'MA'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 36
    country.name = 'Mozambique'
    country.code = 'MZ'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 37
    country.name = 'Namibia'
    country.code = 'NA'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 38
    country.name = 'Niger Republic'
    country.code = 'NE'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 39
    country.name = 'Nigeria'
    country.code = 'NG'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 40
    country.name = 'Principe'
    country.code = 'ST'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 41
    country.name = 'Reunion Island'
    country.code = 'RE'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 42
    country.name = 'Rwanda'
    country.code = 'RW'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 43
    country.name = 'Sao Tome'
    country.code = 'ST'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 44
    country.name = 'Senegal Republic'
    country.code = 'SN'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 45
    country.name = 'Seychelles'
    country.code = 'SC'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 46
    country.name = 'Sierra Leone'
    country.code = 'SL'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 47
    country.name = 'Somalia Republic'
    country.code = 'SO'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 48
    country.name = 'South Africa'
    country.code = 'ZA'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 49
    country.name = 'St. Helena'
    country.code = 'SH'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 50
    country.name = 'Sudan'
    country.code = 'SD'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 51
    country.name = 'Swaziland'
    country.code = 'SZ'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 52
    country.name = 'Tanzania'
    country.code = 'TZ'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 53
    country.name = 'Togo'
    country.code = 'TG'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 54
    country.name = 'Tunisia'
    country.code = 'TN'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 55
    country.name = 'Uganda'
    country.code = 'UG'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 56
    country.name = 'Zaire'
    country.code = 'CD'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 57
    country.name = 'Zambia'
    country.code = 'ZM'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 58
    country.name = 'Zanzibar'
    country.code = 'TZ'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 59
    country.name = 'Zimbabwe'
    country.code = 'ZW'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 60
    country.name = 'South Sudan'
    country.code = 'SS'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 61
    country.name = 'Dem. Republic of the Congo'
    country.code = 'CD'
    country.continent = Continent.objects.get( pk = 1 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 62
    country.name = 'Afghanistan'
    country.code = 'AF'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 63
    country.name = 'Armenia'
    country.code = 'AM'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 64
    country.name = 'Azerbaijan'
    country.code = 'AZ'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 65
    country.name = 'Bahrain'
    country.code = 'BH'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 66
    country.name = 'Bangladesh'
    country.code = 'BD'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 67
    country.name = 'Bhutan'
    country.code = 'BT'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 68
    country.name = 'Brunei'
    country.code = 'BN'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 69
    country.name = 'Cambodia'
    country.code = 'KH'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 70
    country.name = 'China'
    country.code = 'CN'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 71
    country.name = 'Christmas Island'
    country.code = 'CX'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 72
    country.name = 'Cocos Islands'
    country.code = 'CC'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 73
    country.name = 'Diego Garcia'
    country.code = 'IO'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 74
    country.name = 'Georgia'
    country.code = 'GE'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 75
    country.name = 'Hong Kong'
    country.code = 'HK'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 76
    country.name = 'India'
    country.code = 'IN'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 77
    country.name = 'Indonesia'
    country.code = 'ID'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 78
    country.name = 'Iran'
    country.code = 'IR'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 79
    country.name = 'Iraq'
    country.code = 'IQ'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 80
    country.name = 'Israel'
    country.code = 'IL'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 81
    country.name = 'Japan'
    country.code = 'JP'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 82
    country.name = 'Jordan'
    country.code = 'JO'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 83
    country.name = 'Kazakhstan'
    country.code = 'KZ'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 84
    country.name = 'North Korea'
    country.code = 'KP'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 85
    country.name = 'South Korea'
    country.code = 'KR'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 86
    country.name = 'Kuwait'
    country.code = 'KW'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 87
    country.name = 'Kyrgyzstan'
    country.code = 'KG'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 88
    country.name = 'Laos'
    country.code = 'LA'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 89
    country.name = 'Lebanon'
    country.code = 'LB'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 90
    country.name = 'Macau'
    country.code = 'MO'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 91
    country.name = 'Malaysia'
    country.code = 'MY'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 92
    country.name = 'Maldives'
    country.code = 'MV'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 93
    country.name = 'Mongolia'
    country.code = 'MN'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 94
    country.name = 'Myanmar'
    country.code = 'MM'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 95
    country.name = 'Nepal'
    country.code = 'NP'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 96
    country.name = 'Oman'
    country.code = 'OM'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 97
    country.name = 'Macau'
    country.code = 'MO'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 98
    country.name = 'Pakistan'
    country.code = 'PK'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 99
    country.name = 'Philippines'
    country.code = 'PH'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 100
    country.name = 'Qatar'
    country.code = 'QA'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 101
    country.name = 'Saudi Arabia'
    country.code = 'SA'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 102
    country.name = 'Singapore'
    country.code = 'SG'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 103
    country.name = 'Sri Lanka'
    country.code = 'LK'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 104
    country.name = 'Syria'
    country.code = 'SY'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 105
    country.name = 'Syria'
    country.code = 'SY'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 106
    country.name = 'Taiwan'
    country.code = 'TW'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 107
    country.name = 'Tajikistan'
    country.code = 'TJ'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 108
    country.name = 'Thailand'
    country.code = 'TH'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 109
    country.name = 'Turkey'
    country.code = 'TR'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 110
    country.name = 'Turkmenistan'
    country.code = 'TM'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 111
    country.name = 'United Arab Emirates'
    country.code = 'AE'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 112
    country.name = 'Uzbekistan'
    country.code = 'UZ'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 113
    country.name = 'Vietnam'
    country.code = 'VN'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 114
    country.name = 'Yemen'
    country.code = 'YE'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 115
    country.name = 'Palestine'
    country.code = 'PS'
    country.continent = Continent.objects.get( pk = 3 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 116
    country.name = 'American Samoa'
    country.code = 'AS'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 117
    country.name = 'Australia'
    country.code = 'AU'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = True
    country.save()

    country = Country()
    country.id = 118
    country.name = 'Chatham Island, NZ'
    country.code = 'NZ'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 119
    country.name = 'Cook Islands'
    country.code = 'CK'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 120
    country.name = 'Fiji Islands'
    country.code = 'FJ'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 121
    country.name = 'French Polynesia'
    country.code = 'PF'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 122
    country.name = 'Guam'
    country.code = 'GU'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 123
    country.name = 'Kiribati'
    country.code = 'KI'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 124
    country.name = 'American'
    country.code = 'AS'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 125
    country.name = 'Mariana Islands'
    country.code = 'MI'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 126
    country.name = 'Marshall Islands'
    country.code = 'MH'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 127
    country.name = 'Federated States of Micronesia'
    country.code = 'FM'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 128
    country.name = 'Midway Islands'
    country.code = 'UM'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 129
    country.name = 'Nauru'
    country.code = 'NR'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 130
    country.name = 'New Caledonia'
    country.code = 'NC'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 131
    country.name = 'New Zealand'
    country.code = 'NZ'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = True
    country.save()

    country = Country()
    country.id = 132
    country.name = 'Niue'
    country.code = 'NU'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 133
    country.name = 'Norfolk Island'
    country.code = 'NF'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 134
    country.name = 'Palau'
    country.code = 'PW'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 135
    country.name = 'Papua New Guinea'
    country.code = 'PG'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 136
    country.name = 'Saipan'
    country.code = 'MP'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 137
    country.name = 'Solomon Islands'
    country.code = 'SB'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 138
    country.name = 'Tokelau'
    country.code = 'TK'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 139
    country.name = 'Tonga'
    country.code = 'TO'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 140
    country.name = 'Tuvalu'
    country.code = 'TV'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 141
    country.name = 'Vanuatu'
    country.code = 'VU'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 142
    country.name = 'Wake Island'
    country.code = 'UM'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 143
    country.name = 'Wallis and Futuna Islands'
    country.code = 'WF'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 144
    country.name = 'Samoa'
    country.code = 'WS'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 145
    country.name = 'East Timor'
    country.code = 'TL'
    country.continent = Continent.objects.get( pk = 6 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 146
    country.name = 'Antarctica'
    country.code = 'AQ'
    country.continent = Continent.objects.get( pk = 2 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 147
    country.name = 'Albania'
    country.code = 'AL'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 148
    country.name = 'Andorra'
    country.code = 'AD'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 149
    country.name = 'Austria'
    country.code = 'AT'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 150
    country.name = 'Belarus'
    country.code = 'BY'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 151
    country.name = 'Belgium'
    country.code = 'BE'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 152
    country.name = 'Bosnia and Herzegovina'
    country.code = 'BA'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 153
    country.name = 'Bulgaria'
    country.code = 'BG'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 154
    country.name = 'Croatia'
    country.code = 'HR'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 155
    country.name = 'Cyprus'
    country.code = 'CY'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 156
    country.name = 'Czech Republic'
    country.code = 'CZ'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 157
    country.name = 'Denmark'
    country.code = 'DK'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 158
    country.name = 'Estonia'
    country.code = 'EE'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 159
    country.name = 'Faroe Islands'
    country.code = 'FO'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 160
    country.name = 'Finland'
    country.code = 'FI'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 161
    country.name = 'France'
    country.code = 'FR'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 162
    country.name = 'Germany'
    country.code = 'DE'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 163
    country.name = 'Gibraltar'
    country.code = 'GI'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 164
    country.name = 'Greece'
    country.code = 'GR'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 165
    country.name = 'Hungary'
    country.code = 'HU'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 166
    country.name = 'Iceland'
    country.code = 'IS'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 167
    country.name = 'Ireland'
    country.code = 'IE'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 168
    country.name = 'Italy'
    country.code = 'IT'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 169
    country.name = 'Latvia'
    country.code = 'LV'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 170
    country.name = 'Liechtenstein'
    country.code = 'LI'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 171
    country.name = 'Lithuania'
    country.code = 'LT'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 172
    country.name = 'Luxembourg'
    country.code = 'LU'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 173
    country.name = 'Macedonia'
    country.code = 'MK'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 174
    country.name = 'Malta'
    country.code = 'MT'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 175
    country.name = 'Moldova'
    country.code = 'MD'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()


    country = Country()
    country.id = 176
    country.name = 'Monaco'
    country.code = 'MC'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 177
    country.name = 'Netherlands'
    country.code = 'NL'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 178
    country.name = 'Norway'
    country.code = 'NO'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 179
    country.name = 'Poland'
    country.code = 'PL'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 180
    country.name = 'Portugal'
    country.code = 'PT'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 181
    country.name = 'Romania'
    country.code = 'RO'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 182
    country.name = 'Russia'
    country.code = 'RU'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 183
    country.name = 'San Marino'
    country.code = 'SM'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 184
    country.name = 'Serbia'
    country.code = 'RS'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 185
    country.name = 'Slovakia'
    country.code = 'SK'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 186
    country.name = 'Slovenia'
    country.code = 'SL'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 187
    country.name = 'Spain'
    country.code = 'ES'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 188
    country.name = 'Sweden'
    country.code = 'SE'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 189
    country.name = 'Switzerland'
    country.code = 'CH'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 190
    country.name = 'Ukraine'
    country.code = 'UA'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 191
    country.name = 'United Kingdom'
    country.code = 'GB'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 192
    country.name = 'Vatican city'
    country.code = 'VA'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 193
    country.name = 'Yugoslavia'
    country.code = 'RS'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 194
    country.name = 'Kosovo'
    country.code = 'RS'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 195
    country.name = 'Montenegro'
    country.code = 'ME'
    country.continent = Continent.objects.get( pk = 4 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 196
    country.name = 'Anguilla'
    country.code = 'AI'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 197
    country.name = 'Antigua and Barbuda'
    country.code = 'AG'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 198
    country.name = 'Aruba'
    country.code = 'AW'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 199
    country.name = 'Bahamas'
    country.code = 'BS'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 200
    country.name = 'Barbados'
    country.code = 'BB'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 201
    country.name = 'Belize'
    country.code = 'BZ'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 202
    country.name = 'Bermuda'
    country.code = 'BM'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 203
    country.name = 'British Virgin Islands'
    country.code = 'VG'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 204
    country.name = 'Canada'
    country.code = 'CA'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = True
    country.save()

    country = Country()
    country.id = 205
    country.name = 'Cayman Islands'
    country.code = 'KY'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 206
    country.name = 'Costa Rica'
    country.code = 'CR'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 207
    country.name = 'Cuba'
    country.code = 'CU'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 208
    country.name = 'Curacao'
    country.code = 'CW'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 209
    country.name = 'Dominica'
    country.code = 'DM'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 210
    country.name = 'Dominican Republic'
    country.code = 'DO'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 211
    country.name = 'El Salvador'
    country.code = 'SV'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 212
    country.name = 'Greenland'
    country.code = 'GL'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 213
    country.name = 'Grenada and Carriacuou'
    country.code = 'GD'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 214
    country.name = 'Guadeloupe'
    country.code = 'GP'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 215
    country.name = 'Guatemala'
    country.code = 'GT'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 216
    country.name = 'Haiti'
    country.code = 'HT'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 217
    country.name = 'Honduras'
    country.code = 'HN'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 218
    country.name = 'Jamaica'
    country.code = 'JM'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 219
    country.name = 'Martinique'
    country.code = 'MQ'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 220
    country.name = 'Mexico'
    country.code = 'MX'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 221
    country.name = 'Miquelon'
    country.code = 'PM'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 222
    country.name = 'Montserrat'
    country.code = 'MS'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 223
    country.name = 'Netherlands Antilles'
    country.code = 'CW'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 224
    country.name = 'Nevis'
    country.code = 'KN'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 225
    country.name = 'Nicaragua'
    country.code = 'NI'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 226
    country.name = 'Panama'
    country.code = 'PA'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 227
    country.name = 'Puerto Rico'
    country.code = 'PR'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 228
    country.name = 'St. Kitts'
    country.code = 'KN'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 229
    country.name = 'St. Lucia'
    country.code = 'LC'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 230
    country.name = 'St. Pierre and Miquelon'
    country.code = 'PM'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 231
    country.name = 'St. Vincent'
    country.code = 'VC'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 232
    country.name = 'Trinidad and Tobago'
    country.code = 'TT'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 233
    country.name = 'Turks and Caicos Islands'
    country.code = 'TC'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 234
    country.name = 'US Virgin Islands'
    country.code = 'VI'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 235
    country.name = 'United States'
    country.code = 'US'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 236
    country.name = 'Sint Maarten'
    country.code = 'SX'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 237
    country.name = 'Bonaire'
    country.code = 'BQ'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 238
    country.name = 'Saba'
    country.code = 'SA'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 239
    country.name = 'Sint Eustatius'
    country.code = 'SE'
    country.continent = Continent.objects.get( pk = 5 )
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 240
    country.name = 'Argentina'
    country.code = 'AR'
    country.continent = Continent.objects.get( pk = 7)
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 241
    country.name = 'Bolivia'
    country.code = 'BO'
    country.continent = Continent.objects.get( pk = 7)
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 242
    country.name = 'Brazil'
    country.code = 'BR'
    country.continent = Continent.objects.get( pk = 7)
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 243
    country.name = 'Chile'
    country.code = 'CL'
    country.continent = Continent.objects.get( pk = 7)
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 244
    country.name = 'Colombia'
    country.code = 'CO'
    country.continent = Continent.objects.get( pk = 7)
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 245
    country.name = 'Ecuador'
    country.code = 'EC'
    country.continent = Continent.objects.get( pk = 7)
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 246
    country.name = 'Falkland Islands'
    country.code = 'FK'
    country.continent = Continent.objects.get( pk = 7)
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 247
    country.name = 'French Guiana'
    country.code = 'GF'
    country.continent = Continent.objects.get( pk = 7)
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 248
    country.name = 'Guiana'
    country.code = 'GY'
    country.continent = Continent.objects.get( pk = 7)
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 249
    country.name = 'Guyana'
    country.code = 'GY'
    country.continent = Continent.objects.get( pk = 7)
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 250
    country.name = 'Paraguay'
    country.code = 'PY'
    country.continent = Continent.objects.get( pk = 7)
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 251
    country.name = 'Peru'
    country.code = 'PE'
    country.continent = Continent.objects.get( pk = 7)
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 252
    country.name = 'Suriname'
    country.code = 'SR'
    country.continent = Continent.objects.get( pk = 7)
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 253
    country.name = 'Uruguay'
    country.code = 'UY'
    country.continent = Continent.objects.get( pk = 7)
    country.immigration_enabled = False
    country.save()

    country = Country()
    country.id = 254
    country.name = 'Venezuela'
    country.code = 'VE'
    country.continent = Continent.objects.get( pk = 7)
    country.immigration_enabled = False
    country.save()


#######################
# LANGUAGES
#######################
def core_language_initial_values( apps, schema_editor ):

    # Get model to use (historical version)
    Language = apps.get_model( "core", "Language" )

    # Insert data
    language = Language()
    language.id = 1
    language.name = 'Abkhazian'
    language.code = 'ab'
    language.save()

    language = Language()
    language.id = 2
    language.name = 'Afar'
    language.code = 'aa'
    language.save()

    language = Language()
    language.id = 3
    language.name = 'Afrikaans'
    language.code = 'af'
    language.save()

    language = Language()
    language.id = 4
    language.name = 'Albanian'
    language.code = 'sq'
    language.save()

    language = Language()
    language.id = 5
    language.name = 'Amharic'
    language.code = 'am'
    language.save()

    language = Language()
    language.id = 6
    language.name = 'Arabic'
    language.code = 'ar'
    language.save()

    language = Language()
    language.id = 7
    language.name = 'Aragonese'
    language.code = 'an'
    language.save()

    language = Language()
    language.id = 8
    language.name = 'Armenian'
    language.code = 'hy'
    language.save()

    language = Language()
    language.id = 9
    language.name = 'Assamese'
    language.code = 'as'
    language.save()

    language = Language()
    language.id = 10
    language.name = 'Aymara'
    language.code = 'ay'
    language.save()

    language = Language()
    language.id = 11
    language.name = 'Azerbaijani'
    language.code = 'az'
    language.save()

    language = Language()
    language.id = 12
    language.name = 'Bashkir'
    language.code = 'ba'
    language.save()

    language = Language()
    language.id = 13
    language.name = 'Basque'
    language.code = 'eu'
    language.save()

    language = Language()
    language.id = 14
    language.name = 'Bengali (Bangla)'
    language.code = 'bn'
    language.save()

    language = Language()
    language.id = 15
    language.name = 'Bhutani'
    language.code = 'dz'
    language.save()

    language = Language()
    language.id = 16
    language.name = 'Bihari'
    language.code = 'bh'
    language.save()

    language = Language()
    language.id = 17
    language.name = 'Bislama'
    language.code = 'bi'
    language.save()

    language = Language()
    language.id = 18
    language.name = 'Breton'
    language.code = 'br'
    language.save()

    language = Language()
    language.id = 19
    language.name = 'Bulgarian'
    language.code = 'bg'
    language.save()

    language = Language()
    language.id = 20
    language.name = 'Burmese'
    language.code = 'my'
    language.save()

    language = Language()
    language.id = 21
    language.name = 'Byelorussian (Belarusian)'
    language.code = 'br'
    language.save()

    language = Language()
    language.id = 22
    language.name = 'Cambodian'
    language.code = 'km'
    language.save()

    language = Language()
    language.id = 23
    language.name = 'Catalan'
    language.code = 'ca'
    language.save()

    language = Language()
    language.id = 24
    language.name = 'Cherokee'
    language.code = 'Chero'
    language.save()

    language = Language()
    language.id = 25
    language.name = 'Chewa'
    language.code = 'chewa'
    language.save()

    language = Language()
    language.id = 26
    language.name = 'Chinese'
    language.code = 'zh'
    language.save()

    language = Language()
    language.id = 27
    language.name = 'Corsican'
    language.code = 'co'
    language.save()

    language = Language()
    language.id = 28
    language.name = 'Croatian'
    language.code = 'hr'
    language.save()

    language = Language()
    language.id = 29
    language.name = 'Czech'
    language.code = 'cs'
    language.save()

    language = Language()
    language.id = 30
    language.name = 'Danish'
    language.code = 'da'
    language.save()

    language = Language()
    language.id = 31
    language.name = 'Divehi'
    language.code = 'diveh'
    language.save()

    language = Language()
    language.id = 32
    language.name = 'Dutch'
    language.code = 'nl'
    language.save()

    language = Language()
    language.id = 33
    language.name = 'Edo'
    language.code = 'edo'
    language.save()

    language = Language()
    language.id = 34
    language.name = 'English'
    language.code = 'en'
    language.save()

    language = Language()
    language.id = 35
    language.name = 'Esperanto'
    language.code = 'eo'
    language.save()

    #http://www.w3schools.com/tags/ref_language_codes.asp
    language = Language()
    language.id = 36
    language.name = 'Estonian'
    language.code = 'et'
    language.save()

    language = Language()
    language.id = 37
    language.name = 'Faeroese'
    language.code = 'fo'
    language.save()

    language = Language()
    language.id = 38
    language.name = 'Farsi'
    language.code = 'fa'
    language.save()

    language = Language()
    language.id = 39
    language.name = 'Fiji'
    language.code = 'fj'
    language.save()

    language = Language()
    language.id = 40
    language.name = 'Finnish'
    language.code = 'fi'
    language.save()

    language = Language()
    language.id = 41
    language.name = 'Flemish'
    language.code = 'flemi'
    language.save()

    language = Language()
    language.id = 42
    language.name = 'French'
    language.code = 'fr'
    language.save()

    language = Language()
    language.id = 43
    language.name = 'Frisian'
    language.code = 'fy'
    language.save()

    language = Language()
    language.id = 44
    language.name = 'Fulfulde'
    language.code = 'fulfu'
    language.save()

    language = Language()
    language.id = 45
    language.name = 'Galician'
    language.code = 'gl'
    language.save()

    language = Language()
    language.id = 46
    language.name = 'Gaelic (Scottish)'
    language.code = 'gd'
    language.save()

    language = Language()
    language.id = 47
    language.name = 'Gaelic (Manx)'
    language.code = 'gv'
    language.save()

    language = Language()
    language.id = 48
    language.name = 'Georgian'
    language.code = 'ka'
    language.save()

    language = Language()
    language.id = 49
    language.name = 'German'
    language.code = 'de'
    language.save()

    language = Language()
    language.id = 50
    language.name = 'Greek'
    language.code = 'el'
    language.save()

    language = Language()
    language.id = 51
    language.name = 'Greenlandic'
    language.code = 'kl'
    language.save()

    language = Language()
    language.id = 52
    language.name = 'Guarani'
    language.code = 'gn'
    language.save()

    language = Language()
    language.id = 53
    language.name = 'Gujarati'
    language.code = 'gu'
    language.save()

    language = Language()
    language.id = 54
    language.name = 'Haitian Creole'
    language.code = 'ht'
    language.save()

    language = Language()
    language.id = 55
    language.name = 'Hausa'
    language.code = 'ha'
    language.save()

    language = Language()
    language.id = 56
    language.name = 'Hawaiian'
    language.code = 'hawai'
    language.save()

    language = Language()
    language.id = 57
    language.name = 'Hebrew'
    language.code = 'he,iw'
    language.save()

    language = Language()
    language.id = 58
    language.name = 'Hindi'
    language.code = 'hi'
    language.save()

    language = Language()
    language.id = 59
    language.name = 'Hungarian'
    language.code = 'hu'
    language.save()

    language = Language()
    language.id = 60
    language.name = 'Ibibio'
    language.code = 'ibid'
    language.save()

    language = Language()
    language.id = 61
    language.name = 'Icelandic'
    language.code = 'is'
    language.save()

    language = Language()
    language.id = 62
    language.name = 'Ido'
    language.code = 'io'
    language.save()

    language = Language()
    language.id = 63
    language.name = 'Igbo'
    language.code = 'igbo'
    language.save()

    language = Language()
    language.id = 64
    language.name = 'Indonesian'
    language.code = 'id,in'
    language.save()

    language = Language()
    language.id = 65
    language.name = 'Interlingua'
    language.code = 'ia'
    language.save()

    language = Language()
    language.id = 66
    language.name = 'Interlingue'
    language.code = 'ie'
    language.save()

    language = Language()
    language.id = 67
    language.name = 'Inuktitut'
    language.code = 'iu'
    language.save()

    language = Language()
    language.id = 68
    language.name = 'Inupiak'
    language.code = 'ik'
    language.save()

    language = Language()
    language.id = 69
    language.name = 'Irish'
    language.code = 'ga'
    language.save()

    language = Language()
    language.id = 70
    language.name = 'Italian'
    language.code = 'it'
    language.save()

    language = Language()
    language.id = 71
    language.name = 'Japanese'
    language.code = 'ja'
    language.save()

    language = Language()
    language.id = 72
    language.name = 'Javanese'
    language.code = 'jv'
    language.save()

    language = Language()
    language.id = 73
    language.name = 'Kannada'
    language.code = 'kn'
    language.save()

    language = Language()
    language.id = 74
    language.name = 'Kanuri'
    language.code = 'kanur'
    language.save()

    language = Language()
    language.id = 75
    language.name = 'Kashmiri'
    language.code = 'ks'
    language.save()

    language = Language()
    language.id = 76
    language.name = 'Kazakh'
    language.code = 'kk'
    language.save()

    language = Language()
    language.id = 77
    language.name = 'Kinyarwanda (Ruanda)'
    language.code = 'rw'
    language.save()

    language = Language()
    language.id = 78
    language.name = 'Kirghiz'
    language.code = 'ky'
    language.save()

    language = Language()
    language.id = 79
    language.name = 'Kirundi (Rundi)'
    language.code = 'rn'
    language.save()

    language = Language()
    language.id = 80
    language.name = 'Konkani'
    language.code = 'konka'
    language.save()

    language = Language()
    language.id = 81
    language.name = 'Korean'
    language.code = 'ko'
    language.save()

    language = Language()
    language.id = 82
    language.name = 'Kurdish'
    language.code = 'ku'
    language.save()

    language = Language()
    language.id = 83
    language.name = 'Laothian'
    language.code = 'lo'
    language.save()

    language = Language()
    language.id = 84
    language.name = 'Latin'
    language.code = 'la'
    language.save()

    language = Language()
    language.id = 85
    language.name = 'Latvian (Lettish)'
    language.code = 'lv'
    language.save()

    language = Language()
    language.id = 86
    language.name = 'Limburgish ( Limburger)'
    language.code = 'li'
    language.save()

    language = Language()
    language.id = 87
    language.name = 'Lingala'
    language.code = 'ln'
    language.save()

    language = Language()
    language.id = 88
    language.name = 'Lithuanian'
    language.code = 'lt'
    language.save()

    language = Language()
    language.id = 89
    language.name = 'Macedonian'
    language.code = 'mk'
    language.save()

    language = Language()
    language.id = 90
    language.name = 'Malagasy'
    language.code = 'mg'
    language.save()

    language = Language()
    language.id = 91
    language.name = 'Malay'
    language.code = 'ms'
    language.save()

    language = Language()
    language.id = 92
    language.name = 'Malayalam'
    language.code = 'ml'
    language.save()

    language = Language()
    language.id = 93
    language.name = 'Maltese'
    language.code = 'mt'
    language.save()

    language = Language()
    language.id = 94
    language.name = 'Maori'
    language.code = 'mi'
    language.save()

    language = Language()
    language.id = 95
    language.name = 'Marathi'
    language.code = 'mr'
    language.save()

    language = Language()
    language.id = 96
    language.name = 'Moldavian'
    language.code = 'mo'
    language.save()

    language = Language()
    language.id = 97
    language.name = 'Mongolian'
    language.code = 'mn'
    language.save()

    language = Language()
    language.id = 98
    language.name = 'Nauru'
    language.code = 'na'
    language.save()

    language = Language()
    language.id = 99
    language.name = 'Nepali'
    language.code = 'ne'
    language.save()

    language = Language()
    language.id = 100
    language.name = 'Norwegian'
    language.code = 'no'
    language.save()

    language = Language()
    language.id = 101
    language.name = 'Occitan'
    language.code = 'oc'
    language.save()

    language = Language()
    language.id = 102
    language.name = 'Oriya'
    language.code = 'or'
    language.save()

    language = Language()
    language.id = 103
    language.name = 'Oromo (Afaan Oromo)'
    language.code = 'om'
    language.save()

    language = Language()
    language.id = 104
    language.name = 'Papiamentu'
    language.code = 'papia'
    language.save()

    language = Language()
    language.id = 105
    language.name = 'Pashto (Pushto)'
    language.code = 'ps'
    language.save()

    language = Language()
    language.id = 106
    language.name = 'Polish'
    language.code = 'pl'
    language.save()

    language = Language()
    language.id = 107
    language.name = 'Portuguese'
    language.code = 'pt'
    language.save()

    language = Language()
    language.id = 108
    language.name = 'Punjabi'
    language.code = 'pa'
    language.save()

    language = Language()
    language.id = 109
    language.name = 'Quechua'
    language.code = 'qu'
    language.save()

    language = Language()
    language.id = 110
    language.name = 'Rhaeto-Romance'
    language.code = 'rm'
    language.save()

    language = Language()
    language.id = 111
    language.name = 'Romanian'
    language.code = 'ro'
    language.save()

    language = Language()
    language.id = 112
    language.name = 'Russian'
    language.code = 'ru'
    language.save()

    language = Language()
    language.id = 113
    language.name = 'Sami (Lappish)'
    language.code = 'samil'
    language.save()

    language = Language()
    language.id = 114
    language.name = 'Samoan'
    language.code = 'sm'
    language.save()

    language = Language()
    language.id = 115
    language.name = 'Sangro'
    language.code = 'sg'
    language.save()

    language = Language()
    language.id = 116
    language.name = 'Sanskrit'
    language.code = 'sa'
    language.save()

    language = Language()
    language.id = 117
    language.name = 'Serbian'
    language.code = 'sr'
    language.save()

    language = Language()
    language.id = 118
    language.name = 'Serbo-Croatian'
    language.code = 'sh'
    language.save()

    language = Language()
    language.id = 119
    language.name = 'Sesotho'
    language.code = 'st'
    language.save()

    language = Language()
    language.id = 120
    language.name = 'Setswana'
    language.code = 'tn'
    language.save()

    language = Language()
    language.id = 121
    language.name = 'Shona'
    language.code = 'sn'
    language.save()

    language = Language()
    language.id = 122
    language.name = 'Sichuan Yi'
    language.code = 'ii'
    language.save()

    language = Language()
    language.id = 123
    language.name = 'Sindhi'
    language.code = 'sd'
    language.save()

    language = Language()
    language.id = 124
    language.name = 'Sinhalese'
    language.code = 'si'
    language.save()

    language = Language()
    language.id = 125
    language.name = 'Siswati'
    language.code = 'ss'
    language.save()

    language = Language()
    language.id = 126
    language.name = 'Slovak'
    language.code = 'sk'
    language.save()

    language = Language()
    language.id = 127
    language.name = 'Slovenian'
    language.code = 'sl'
    language.save()

    language = Language()
    language.id = 128
    language.name = 'Somali'
    language.code = 'so'
    language.save()

    language = Language()
    language.id = 129
    language.name = 'Spanish'
    language.code = 'es'
    language.save()

    language = Language()
    language.id = 130
    language.name = 'Sundanese'
    language.code = 'su'
    language.save()

    language = Language()
    language.id = 131
    language.name = 'Swahili (Kiswahili)'
    language.code = 'sw'
    language.save()

    language = Language()
    language.id = 132
    language.name = 'Swedish'
    language.code = 'sv'
    language.save()

    language = Language()
    language.id = 133
    language.name = 'Syriac'
    language.code = 'syria'
    language.save()

    language = Language()
    language.id = 134
    language.name = 'Tagalog'
    language.code = 'tl'
    language.save()

    language = Language()
    language.id = 135
    language.name = 'Tajik'
    language.code = 'tg'
    language.save()

    language = Language()
    language.id = 136
    language.name = 'Tamazight'
    language.code = 'tamaz'
    language.save()

    language = Language()
    language.id = 137
    language.name = 'Tamil'
    language.code = 'ta'
    language.save()

    language = Language()
    language.id = 138
    language.name = 'Tatar'
    language.code = 'tt'
    language.save()

    language = Language()
    language.id = 139
    language.name = 'Telugu'
    language.code = 'te'
    language.save()

    language = Language()
    language.id = 140
    language.name = 'Thai'
    language.code = 'th'
    language.save()

    language = Language()
    language.id = 141
    language.name = 'Tibetan'
    language.code = 'bo'
    language.save()

    language = Language()
    language.id = 142
    language.name = 'Tigrinya'
    language.code = 'ti'
    language.save()

    language = Language()
    language.id = 143
    language.name = 'Tonga'
    language.code = 'to'
    language.save()

    language = Language()
    language.id = 144
    language.name = 'Tsonga'
    language.code = 'ts'
    language.save()

    language = Language()
    language.id = 145
    language.name = 'Turkish'
    language.code = 'tr'
    language.save()

    language = Language()
    language.id = 146
    language.name = 'Turkmen'
    language.code = 'tk'
    language.save()

    language = Language()
    language.id = 147
    language.name = 'Twi'
    language.code = 'tw'
    language.save()

    language = Language()
    language.id = 148
    language.name = 'Uighur'
    language.code = 'ug'
    language.save()

    language = Language()
    language.id = 149
    language.name = 'Ukrainian'
    language.code = 'uk'
    language.save()

    language = Language()
    language.id = 150
    language.name = 'Urdu'
    language.code = 'ur'
    language.save()

    language = Language()
    language.id = 151
    language.name = 'Uzbek'
    language.code = 'uz'
    language.save()

    language = Language()
    language.id = 152
    language.name = 'Venda'
    language.code = 'venda'
    language.save()

    language = Language()
    language.id = 153
    language.name = 'Vietnamese'
    language.code = 'vi'
    language.save()

    language = Language()
    language.id = 154
    language.name = 'Volapük'
    language.code = 'vo'
    language.save()

    language = Language()
    language.id = 155
    language.name = 'Wallon'
    language.code = 'wa'
    language.save()

    language = Language()
    language.id = 156
    language.name = 'Welsh'
    language.code = 'cy'
    language.save()

    language = Language()
    language.id = 157
    language.name = 'Wolof'
    language.code = 'wo'
    language.save()

    language = Language()
    language.id = 158
    language.name = 'Xhosa'
    language.code = 'xh'
    language.save()

    language = Language()
    language.id = 159
    language.name = 'Yi'
    language.code = 'yi'
    language.save()

    language = Language()
    language.id = 160
    language.name = 'Yiddish'
    language.code = 'yi,ji'
    language.save()

    language = Language()
    language.id = 161
    language.name = 'Yoruba'
    language.code = 'yo'
    language.save()

    language = Language()
    language.id = 162
    language.name = 'Zulu'
    language.code = 'zu'
    language.save()


#######################
# QUESTIONS
#######################
def core_question_initial_values( apps, schema_editor ):

    # Get model to use (historical version)
    Question = apps.get_model( "core", "Question" )

    # Insert data
    question = Question()
    question.id = 1
    question.description = 'Do you have any family members who are citizens in the country of destination?'
    question.help_text = 'If you have a close family member who lives in CA or AU, as an example, you may get some points'
    question.save()

    question = Question()
    question.id = 2
    question.description = 'How old are you?'
    question.help_text = ''
    question.save()

    question = Question()
    question.id = 3
    question.description = 'What is your English Level?'
    question.help_text = ''
    question.save()

    question = Question()
    question.id = 4
    question.description = 'What is your French Level?'
    question.help_text = ''
    question.save()

    question = Question()
    question.id = 5
    question.description = 'What is your highest degree of education?'
    question.help_text = 'Phd, Masters, bachelors, etc..'
    question.save()

    question = Question()
    question.id = 6
    question.description = 'Do you have a written job offer on country of destination?'
    question.help_text = ''
    question.save()

    question = Question()
    question.id = 7
    question.description = 'How many years of experience in a skilled occupation outside country of destination?'
    question.help_text = ''
    question.save()

    question = Question()
    question.id = 8
    question.description = 'How many years of experience in a skilled occupation at country of destination?'
    question.help_text = ''
    question.save()

    question = Question()
    question.id = 9
    question.description = 'What is your occupation?'
    question.help_text = ''
    question.save()

    question = Question()
    question.id = 10
    question.description = 'Do you have a partner in a skilled occupation in demand?'
    question.help_text = ''
    question.save()

    question = Question()
    question.id = 11
    question.description = 'Do you plan to invest or open a business?'
    question.help_text = ''
    question.save()

    question = Question()
    question.id = 12
    question.description = 'Do you have a letter of support for a start-up venture from a canadian designated entity?'
    question.help_text = ''
    question.save()

    question = Question()
    question.id = 13
    question.description = 'Are You a U.S citizen?'
    question.help_text = ''
    question.save()

    question = Question()
    question.id = 14
    question.description = 'Did you study in regional Australia or low population growth metropolitan area?'
    question.help_text = ''
    question.save()

    question = Question()
    question.id = 15
    question.description = 'Did you complete a Professional Year (Course) in Australia?'
    question.help_text = ''
    question.save()

    question = Question()
    question.id = 16
    question.description = 'Are you willing to live and work in regional Australia?'
    question.help_text = ''
    question.save()

    question = Question()
    question.id = 17
    question.description = 'Can you be accredited as a translator or interpreter in a Credentialled community language (Australia)?'
    question.help_text = ''
    question.save()

    question = Question()
    question.id = 18
    question.description = 'Has your partner worked or studied in Canada?'
    question.help_text = ''
    question.save()

    question = Question()
    question.id = 19
    question.description = 'What is your partner English Level?'
    question.help_text = ''
    question.save()

    question = Question()
    question.id = 20
    question.description = 'What is your partner French Level?'
    question.help_text = ''
    question.save()

    question = Question()
    question.id = 21
    question.description = 'What is your partner level of education?'
    question.help_text = ''
    question.save()



#######################
# ANSWER CATEGORIES
#######################
def core_answer_category_initial_values( apps, schema_editor ):

    # Get model to use (historical version)
    AnswerCategory = apps.get_model( "core", "AnswerCategory" )
    Question = apps.get_model( "core", "Question" )

    # Insert data

    # -- What's your occupation? -----------------------------
    answer_category = AnswerCategory()
    answer_category.id = 1
    answer_category.question = Question.objects.get( pk = 9 )
    answer_category.name = 'Business / Finance / Administration / Advertising'
    answer_category.save()

    answer_category = AnswerCategory()
    answer_category.id = 2
    answer_category.question = Question.objects.get( pk = 9 )
    answer_category.name = 'Art / Culture / Recreation / Sport'
    answer_category.save()

    answer_category = AnswerCategory()
    answer_category.id = 3
    answer_category.question = Question.objects.get( pk = 9 )
    answer_category.name = 'Health'
    answer_category.save()

    answer_category = AnswerCategory()
    answer_category.id = 4
    answer_category.question = Question.objects.get( pk = 9 )
    answer_category.name = 'Engineering / Technology / Natural and Applied Sciences / Architecture'
    answer_category.save()

    answer_category = AnswerCategory()
    answer_category.id = 5
    answer_category.question = Question.objects.get( pk = 9 )
    answer_category.name = 'Education / Law / Social, community and gov. services'
    answer_category.save()

    answer_category = AnswerCategory()
    answer_category.id = 6
    answer_category.question = Question.objects.get( pk = 9 )
    answer_category.name = 'Natural Resources / Agriculture / Related Production'
    answer_category.save()

    answer_category = AnswerCategory()
    answer_category.id = 7
    answer_category.question = Question.objects.get( pk = 9 )
    answer_category.name = 'Sales / Services'
    answer_category.save()

    answer_category = AnswerCategory()
    answer_category.id = 8
    answer_category.question = Question.objects.get( pk = 9 )
    answer_category.name = 'Trades / Transports / Equipments / Manufacturing / Utilities'
    answer_category.save()



#######################
# ANSWERS
#######################
def core_answer_initial_values( apps, schema_editor ):

    # Get model to use (historical version)
    Answer = apps.get_model( "core", "Answer" )
    Question = apps.get_model( "core", "Question" )
    AnswerCategory = apps.get_model( "core", "AnswerCategory" )

    # Insert data

    # -- Family members in other countries? -----------------------------
    answer = Answer()
    answer.id = 1
    answer.question = Question.objects.get( pk = 1 )
    answer.description = 'Yes'
    answer.save()

    answer = Answer()
    answer.id = 2
    answer.question = Question.objects.get( pk = 1 )
    answer.description = 'No'
    answer.save()

    # -- How old are you? -----------------------------
    answer = Answer()
    answer.id = 3
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '1'
    answer.save()

    answer = Answer()
    answer.id = 4
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '2'
    answer.save()

    answer = Answer()
    answer.id = 5
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '3'
    answer.save()

    answer = Answer()
    answer.id = 6
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '4'
    answer.save()

    answer = Answer()
    answer.id = 7
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '5'
    answer.save()

    answer = Answer()
    answer.id = 8
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '6'
    answer.save()

    answer = Answer()
    answer.id = 9
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '7'
    answer.save()

    answer = Answer()
    answer.id = 10
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '8'
    answer.save()

    answer = Answer()
    answer.id = 11
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '9'
    answer.save()

    answer = Answer()
    answer.id = 12
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '10'
    answer.save()

    answer = Answer()
    answer.id = 13
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '11'
    answer.save()

    answer = Answer()
    answer.id = 14
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '12'
    answer.save()

    answer = Answer()
    answer.id = 15
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '13'
    answer.save()

    answer = Answer()
    answer.id = 16
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '14'
    answer.save()

    answer = Answer()
    answer.id = 17
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '15'
    answer.save()

    answer = Answer()
    answer.id = 18
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '16'
    answer.save()

    answer = Answer()
    answer.id = 19
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '17'
    answer.save()

    answer = Answer()
    answer.id = 20
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '18'
    answer.save()

    answer = Answer()
    answer.id = 21
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '19'
    answer.save()

    answer = Answer()
    answer.id = 22
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '20'
    answer.save()

    answer = Answer()
    answer.id = 23
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '21'
    answer.save()

    answer = Answer()
    answer.id = 24
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '22'
    answer.save()

    answer = Answer()
    answer.id = 25
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '23'
    answer.save()

    answer = Answer()
    answer.id = 26
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '24'
    answer.save()

    answer = Answer()
    answer.id = 27
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '25'
    answer.save()

    answer = Answer()
    answer.id = 28
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '26'
    answer.save()

    answer = Answer()
    answer.id = 29
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '27'
    answer.save()

    answer = Answer()
    answer.id = 30
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '28'
    answer.save()

    answer = Answer()
    answer.id = 31
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '29'
    answer.save()

    answer = Answer()
    answer.id = 32
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '30'
    answer.save()

    answer = Answer()
    answer.id = 33
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '31'
    answer.save()

    answer = Answer()
    answer.id = 34
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '32'
    answer.save()

    answer = Answer()
    answer.id = 35
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '33'
    answer.save()

    answer = Answer()
    answer.id = 36
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '34'
    answer.save()

    answer = Answer()
    answer.id = 37
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '35'
    answer.save()

    answer = Answer()
    answer.id = 38
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '36'
    answer.save()

    answer = Answer()
    answer.id = 39
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '37'
    answer.save()

    answer = Answer()
    answer.id = 40
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '38'
    answer.save()

    answer = Answer()
    answer.id = 41
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '39'
    answer.save()

    answer = Answer()
    answer.id = 42
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '40'
    answer.save()

    answer = Answer()
    answer.id = 43
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '41'
    answer.save()

    answer = Answer()
    answer.id = 44
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '42'
    answer.save()

    answer = Answer()
    answer.id = 45
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '43'
    answer.save()

    answer = Answer()
    answer.id = 46
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '44'
    answer.save()

    answer = Answer()
    answer.id = 47
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '45'
    answer.save()

    answer = Answer()
    answer.id = 48
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '46'
    answer.save()

    answer = Answer()
    answer.id = 49
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '47'
    answer.save()

    answer = Answer()
    answer.id = 50
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '48'
    answer.save()

    answer = Answer()
    answer.id = 51
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '49'
    answer.save()

    answer = Answer()
    answer.id = 52
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '50'
    answer.save()

    answer = Answer()
    answer.id = 53
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '51'
    answer.save()

    answer = Answer()
    answer.id = 54
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '52'
    answer.save()

    answer = Answer()
    answer.id = 55
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '53'
    answer.save()

    answer = Answer()
    answer.id = 56
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '54'
    answer.save()

    answer = Answer()
    answer.id = 57
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '55'
    answer.save()

    answer = Answer()
    answer.id = 58
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '56'
    answer.save()

    answer = Answer()
    answer.id = 59
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '57'
    answer.save()

    answer = Answer()
    answer.id = 60
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '58'
    answer.save()

    answer = Answer()
    answer.id = 61
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '59'
    answer.save()

    answer = Answer()
    answer.id = 62
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '60'
    answer.save()

    answer = Answer()
    answer.id = 63
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '61'
    answer.save()

    answer = Answer()
    answer.id = 64
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '62'
    answer.save()

    answer = Answer()
    answer.id = 65
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '63'
    answer.save()

    answer = Answer()
    answer.id = 66
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '64'
    answer.save()

    answer = Answer()
    answer.id = 67
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '65'
    answer.save()

    answer = Answer()
    answer.id = 68
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '66'
    answer.save()

    answer = Answer()
    answer.id = 69
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '67'
    answer.save()

    answer = Answer()
    answer.id = 70
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '68'
    answer.save()

    answer = Answer()
    answer.id = 71
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '69'
    answer.save()

    answer = Answer()
    answer.id = 72
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '70'
    answer.save()

    answer = Answer()
    answer.id = 73
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '71'
    answer.save()

    answer = Answer()
    answer.id = 74
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '72'
    answer.save()

    answer = Answer()
    answer.id = 75
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '73'
    answer.save()

    answer = Answer()
    answer.id = 76
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '74'
    answer.save()

    answer = Answer()
    answer.id = 77
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '75'
    answer.save()

    answer = Answer()
    answer.id = 78
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '76'
    answer.save()

    answer = Answer()
    answer.id = 79
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '77'
    answer.save()

    answer = Answer()
    answer.id = 80
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '78'
    answer.save()

    answer = Answer()
    answer.id = 81
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '79'
    answer.save()

    answer = Answer()
    answer.id = 82
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '80'
    answer.save()

    answer = Answer()
    answer.id = 83
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '81'
    answer.save()

    answer = Answer()
    answer.id = 84
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '82'
    answer.save()

    answer = Answer()
    answer.id = 85
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '83'
    answer.save()

    answer = Answer()
    answer.id = 86
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '84'
    answer.save()

    answer = Answer()
    answer.id = 87
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '85'
    answer.save()

    answer = Answer()
    answer.id = 88
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '86'
    answer.save()

    answer = Answer()
    answer.id = 89
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '87'
    answer.save()

    answer = Answer()
    answer.id = 90
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '88'
    answer.save()

    answer = Answer()
    answer.id = 91
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '89'
    answer.save()

    answer = Answer()
    answer.id = 92
    answer.question = Question.objects.get( pk = 2 )
    answer.description = '90'
    answer.save()


    # -- What is your ENGLISH level? -----------------------------
    answer = Answer()
    answer.id = 93
    answer.question = Question.objects.get( pk = 3 )
    answer.description = 'None'
    answer.save()

    answer = Answer()
    answer.id = 94
    answer.question = Question.objects.get( pk = 3 )
    answer.description = 'Basic Proficiency'
    answer.save()

    answer = Answer()
    answer.id = 95
    answer.question = Question.objects.get( pk = 3 )
    answer.description = 'Moderate Proficiency'
    answer.save()

    answer = Answer()
    answer.id = 96
    answer.question = Question.objects.get( pk = 3 )
    answer.description = 'High Proficiency'
    answer.save()


    # -- What is your FRENCH level? -----------------------------
    answer = Answer()
    answer.id = 97
    answer.question = Question.objects.get( pk = 4 )
    answer.description = 'None'
    answer.save()

    answer = Answer()
    answer.id = 98
    answer.question = Question.objects.get( pk = 4 )
    answer.description = 'Basic Proficiency'
    answer.save()

    answer = Answer()
    answer.id = 99
    answer.question = Question.objects.get( pk = 4 )
    answer.description = 'Moderate Proficiency'
    answer.save()

    answer = Answer()
    answer.id = 100
    answer.question = Question.objects.get( pk = 4 )
    answer.description = 'High Proficiency'
    answer.save()


    # -- What is your highest degree of education? -----------------------------
    answer = Answer()
    answer.id = 101
    answer.question = Question.objects.get( pk = 5 )
    answer.description = 'None'
    answer.save()

    answer = Answer()
    answer.id = 102
    answer.question = Question.objects.get( pk = 5 )
    answer.description = 'Primary Education'
    answer.save()

    answer = Answer()
    answer.id = 103
    answer.question = Question.objects.get( pk = 5 )
    answer.description = 'Secondary Education - Lower'
    answer.save()

    answer = Answer()
    answer.id = 104
    answer.question = Question.objects.get( pk = 5 )
    answer.description = 'Secondary Education - Upper (High-School)'
    answer.save()

    answer = Answer()
    answer.id = 105
    answer.question = Question.objects.get( pk = 5 )
    answer.description = 'Post Secondary Education (Trades, associate, technical)'
    answer.save()

    answer = Answer()
    answer.id = 106
    answer.question = Question.objects.get( pk = 5 )
    answer.description = 'Bachelors Level'
    answer.save()

    answer = Answer()
    answer.id = 107
    answer.question = Question.objects.get( pk = 5 )
    answer.description = 'Masters Level'
    answer.save()

    answer = Answer()
    answer.id = 108
    answer.question = Question.objects.get( pk = 5 )
    answer.description = 'Doctoral Level'
    answer.save()


    # -- Do you have a written job offer on country of destination? -----------------------------
    answer = Answer()
    answer.id = 109
    answer.question = Question.objects.get( pk = 6 )
    answer.description = 'Yes'
    answer.save()

    answer = Answer()
    answer.id = 110
    answer.question = Question.objects.get( pk = 6 )
    answer.description = 'No'
    answer.save()


    # -- How many years of experience OUTSIDE country of destination -----------------------------
    answer = Answer()
    answer.id = 111
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '1'
    answer.save()

    answer = Answer()
    answer.id = 112
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '2'
    answer.save()

    answer = Answer()
    answer.id = 113
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '3'
    answer.save()

    answer = Answer()
    answer.id = 114
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '4'
    answer.save()

    answer = Answer()
    answer.id = 115
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '5'
    answer.save()

    answer = Answer()
    answer.id = 116
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '6'
    answer.save()

    answer = Answer()
    answer.id = 117
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '7'
    answer.save()

    answer = Answer()
    answer.id = 118
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '8'
    answer.save()

    answer = Answer()
    answer.id = 119
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '9'
    answer.save()

    answer = Answer()
    answer.id = 120
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '10'
    answer.save()

    answer = Answer()
    answer.id = 121
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '11'
    answer.save()

    answer = Answer()
    answer.id = 122
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '12'
    answer.save()

    answer = Answer()
    answer.id = 123
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '13'
    answer.save()

    answer = Answer()
    answer.id = 124
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '14'
    answer.save()

    answer = Answer()
    answer.id = 125
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '15'
    answer.save()

    answer = Answer()
    answer.id = 126
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '16'
    answer.save()

    answer = Answer()
    answer.id = 127
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '17'
    answer.save()

    answer = Answer()
    answer.id = 128
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '18'
    answer.save()

    answer = Answer()
    answer.id = 129
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '19'
    answer.save()

    answer = Answer()
    answer.id = 130
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '20'
    answer.save()

    answer = Answer()
    answer.id = 131
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '21'
    answer.save()

    answer = Answer()
    answer.id = 132
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '22'
    answer.save()

    answer = Answer()
    answer.id = 133
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '23'
    answer.save()

    answer = Answer()
    answer.id = 134
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '24'
    answer.save()

    answer = Answer()
    answer.id = 135
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '25'
    answer.save()

    answer = Answer()
    answer.id = 136
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '26'
    answer.save()

    answer = Answer()
    answer.id = 137
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '27'
    answer.save()

    answer = Answer()
    answer.id = 138
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '28'
    answer.save()

    answer = Answer()
    answer.id = 139
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '29'
    answer.save()

    answer = Answer()
    answer.id = 140
    answer.question = Question.objects.get( pk = 7 )
    answer.description = '30'
    answer.save()


    # -- How many years of experience AT country of destination -----------------------------
    answer = Answer()
    answer.id = 141
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '1'
    answer.save()

    answer = Answer()
    answer.id = 142
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '2'
    answer.save()

    answer = Answer()
    answer.id = 143
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '3'
    answer.save()

    answer = Answer()
    answer.id = 144
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '4'
    answer.save()

    answer = Answer()
    answer.id = 145
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '5'
    answer.save()

    answer = Answer()
    answer.id = 146
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '6'
    answer.save()

    answer = Answer()
    answer.id = 147
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '7'
    answer.save()

    answer = Answer()
    answer.id = 148
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '8'
    answer.save()

    answer = Answer()
    answer.id = 149
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '9'
    answer.save()

    answer = Answer()
    answer.id = 150
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '10'
    answer.save()

    answer = Answer()
    answer.id = 151
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '11'
    answer.save()

    answer = Answer()
    answer.id = 152
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '12'
    answer.save()

    answer = Answer()
    answer.id = 153
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '13'
    answer.save()

    answer = Answer()
    answer.id = 154
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '14'
    answer.save()

    answer = Answer()
    answer.id = 155
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '15'
    answer.save()

    answer = Answer()
    answer.id = 156
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '16'
    answer.save()

    answer = Answer()
    answer.id = 157
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '17'
    answer.save()

    answer = Answer()
    answer.id = 158
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '18'
    answer.save()

    answer = Answer()
    answer.id = 159
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '19'
    answer.save()

    answer = Answer()
    answer.id = 160
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '20'
    answer.save()

    answer = Answer()
    answer.id = 161
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '21'
    answer.save()

    answer = Answer()
    answer.id = 162
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '22'
    answer.save()

    answer = Answer()
    answer.id = 163
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '23'
    answer.save()

    answer = Answer()
    answer.id = 164
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '24'
    answer.save()

    answer = Answer()
    answer.id = 165
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '25'
    answer.save()

    answer = Answer()
    answer.id = 166
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '26'
    answer.save()

    answer = Answer()
    answer.id = 167
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '27'
    answer.save()

    answer = Answer()
    answer.id = 168
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '28'
    answer.save()

    answer = Answer()
    answer.id = 169
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '29'
    answer.save()

    answer = Answer()
    answer.id = 170
    answer.question = Question.objects.get( pk = 8 )
    answer.description = '30'
    answer.save()


    # -- What' your occupation -----------------------------
    answer = Answer()
    answer.id = 171
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Accountant (General)'
    answer.save()

    answer = Answer()
    answer.id = 172
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Financial Auditor'
    answer.save()

    answer = Answer()
    answer.id = 173
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Management Accountant'
    answer.save()

    answer = Answer()
    answer.id = 174
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Taxation Accountant'
    answer.save()

    answer = Answer()
    answer.id = 175
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'External Auditor'
    answer.save()

    answer = Answer()
    answer.id = 176
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Internal Auditor'
    answer.save()

    answer = Answer()
    answer.id = 177
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Actuary'
    answer.save()

    answer = Answer()
    answer.id = 178
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Financial and investment analysts'
    answer.save()

    answer = Answer()
    answer.id = 179
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Financial Managers'
    answer.save()

    answer = Answer()
    answer.id = 180
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Insurance, real estate and financial brokerage managers'
    answer.save()

    answer = Answer()
    answer.id = 181
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Financial Market Dealer'
    answer.save()

    answer = Answer()
    answer.id = 182
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Other Financial Officers/Dealers'
    answer.save()

    answer = Answer()
    answer.id = 183
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Supervisors, finance and insurance office workers'
    answer.save()

    answer = Answer()
    answer.id = 184
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Financial Investment Adviser'
    answer.save()

    answer = Answer()
    answer.id = 185
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Financial Investment Manager'
    answer.save()

    answer = Answer()
    answer.id = 186
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Securities agents, investment dealers and brokers'
    answer.save()

    answer = Answer()
    answer.id = 187
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Financial Institution Branch Manager'
    answer.save()

    answer = Answer()
    answer.id = 188
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Land Economist'
    answer.save()

    answer = Answer()
    answer.id = 189
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Economist'
    answer.save()

    answer = Answer()
    answer.id = 190
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Valuer'
    answer.save()

    answer = Answer()
    answer.id = 191
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Stockbroking Dealer'
    answer.save()

    answer = Answer()
    answer.id = 192
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Antique Dealer'
    answer.save()

    answer = Answer()
    answer.id = 193
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Insurance Broker'
    answer.save()

    answer = Answer()
    answer.id = 194
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Business Broker'
    answer.save()

    answer = Answer()
    answer.id = 195
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Insurance Agent'
    answer.save()

    answer = Answer()
    answer.id = 196
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Insurance Investigator'
    answer.save()

    answer = Answer()
    answer.id = 197
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Insurance Loss Adjuster'
    answer.save()

    answer = Answer()
    answer.id = 198
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Insurance Risk Surveyor'
    answer.save()

    answer = Answer()
    answer.id = 199
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Property Administrators'
    answer.save()

    answer = Answer()
    answer.id = 200
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Contract Administrator'
    answer.save()

    answer = Answer()
    answer.id = 201
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Program or Project Administrator'
    answer.save()

    answer = Answer()
    answer.id = 202
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Actor'
    answer.save()

    answer = Answer()
    answer.id = 203
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Dancers and Other Entertainers'
    answer.save()

    answer = Answer()
    answer.id = 204
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Librarian'
    answer.save()

    answer = Answer()
    answer.id = 205
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Library Technician'
    answer.save()

    answer = Answer()
    answer.id = 206
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Gallery or Museum Curator'
    answer.save()

    answer = Answer()
    answer.id = 207
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Gallery or Museum Technician'
    answer.save()

    answer = Answer()
    answer.id = 208
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Conservation Officer'
    answer.save()

    answer = Answer()
    answer.id = 209
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Conservator'
    answer.save()

    answer = Answer()
    answer.id = 210
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Archivist'
    answer.save()

    answer = Answer()
    answer.id = 211
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Author'
    answer.save()

    answer = Answer()
    answer.id = 212
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Copywriter'
    answer.save()

    answer = Answer()
    answer.id = 213
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Journalists and Other Writers'
    answer.save()

    answer = Answer()
    answer.id = 214
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Technical Writer'
    answer.save()

    answer = Answer()
    answer.id = 215
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Signwriter'
    answer.save()

    answer = Answer()
    answer.id = 216
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Film and Video Editor'
    answer.save()

    answer = Answer()
    answer.id = 217
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Newspaper or Periodical Editor'
    answer.save()

    answer = Answer()
    answer.id = 218
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Book or Script Editor'
    answer.save()

    answer = Answer()
    answer.id = 219
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Print Journalist'
    answer.save()

    answer = Answer()
    answer.id = 220
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Radio Journalist'
    answer.save()

    answer = Answer()
    answer.id = 221
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Television Journalist'
    answer.save()

    answer = Answer()
    answer.id = 222
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Translators, terminologists and interpreters'
    answer.save()

    answer = Answer()
    answer.id = 223
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Video Producer'
    answer.save()

    answer = Answer()
    answer.id = 224
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Media Producer (excluding Video)'
    answer.save()

    answer = Answer()
    answer.id = 225
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Director (Film, Television, Radio or Stage)'
    answer.save()

    answer = Answer()
    answer.id = 226
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Director of Photography'
    answer.save()

    answer = Answer()
    answer.id = 227
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Dancer or Choreographer'
    answer.save()

    answer = Answer()
    answer.id = 228
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Composer'
    answer.save()

    answer = Answer()
    answer.id = 229
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Musician (Instrumental)'
    answer.save()

    answer = Answer()
    answer.id = 230
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Musical Instrument Maker or Repairer'
    answer.save()

    answer = Answer()
    answer.id = 231
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Music Director'
    answer.save()

    answer = Answer()
    answer.id = 232
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Music Professionals (Others)'
    answer.save()

    answer = Answer()
    answer.id = 233
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Music Teacher (Private Tuition)'
    answer.save()

    answer = Answer()
    answer.id = 234
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Singer'
    answer.save()

    answer = Answer()
    answer.id = 235
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Painter (Visual Arts)'
    answer.save()

    answer = Answer()
    answer.id = 236
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Sculptor'
    answer.save()

    answer = Answer()
    answer.id = 237
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Visual Arts and Crafts Professionals (Others)'
    answer.save()

    answer = Answer()
    answer.id = 238
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Art Director (Film, Television or Stage)'
    answer.save()

    answer = Answer()
    answer.id = 239
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Art Teacher (Private Tuition)'
    answer.save()

    answer = Answer()
    answer.id = 240
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Artistic Director'
    answer.save()

    answer = Answer()
    answer.id = 241
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Arts Administrator or Manager'
    answer.save()

    answer = Answer()
    answer.id = 242
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Community Arts Worker'
    answer.save()

    answer = Answer()
    answer.id = 243
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Entertainer or Variety Artist'
    answer.save()

    answer = Answer()
    answer.id = 244
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Potter or Ceramic Artist'
    answer.save()

    answer = Answer()
    answer.id = 245
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Performing Arts Technicians (Others)'
    answer.save()

    answer = Answer()
    answer.id = 246
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Make Up Artist'
    answer.save()

    answer = Answer()
    answer.id = 247
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Dance Teacher (Private Tuition)'
    answer.save()

    answer = Answer()
    answer.id = 248
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Drama Teacher (Private Tuition)'
    answer.save()

    answer = Answer()
    answer.id = 249
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Recreation Coordinator'
    answer.save()

    answer = Answer()
    answer.id = 250
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Photographers Assistant'
    answer.save()

    answer = Answer()
    answer.id = 251
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Photographer'
    answer.save()

    answer = Answer()
    answer.id = 252
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Camera Operator (Film, Television or Video)'
    answer.save()

    answer = Answer()
    answer.id = 253
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Graphic Pre-press Trades Worker'
    answer.save()

    answer = Answer()
    answer.id = 254
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Broadcast Transmitter Operator'
    answer.save()

    answer = Answer()
    answer.id = 255
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Records Manager'
    answer.save()

    answer = Answer()
    answer.id = 256
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Radio Communications Technician'
    answer.save()

    answer = Answer()
    answer.id = 257
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Program Director (Television or Radio)'
    answer.save()

    answer = Answer()
    answer.id = 258
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Radio Presenter'
    answer.save()

    answer = Answer()
    answer.id = 259
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Radiocommunications Technician'
    answer.save()

    answer = Answer()
    answer.id = 260
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Graphic Designer'
    answer.save()

    answer = Answer()
    answer.id = 261
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Fashion Designer'
    answer.save()

    answer = Answer()
    answer.id = 262
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Interior Designer'
    answer.save()

    answer = Answer()
    answer.id = 263
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Jewellery Designer'
    answer.save()

    answer = Answer()
    answer.id = 264
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Marine Designer'
    answer.save()

    answer = Answer()
    answer.id = 265
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Multimedia Designer'
    answer.save()

    answer = Answer()
    answer.id = 266
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Web Designer'
    answer.save()

    answer = Answer()
    answer.id = 267
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Industrial Designer'
    answer.save()

    answer = Answer()
    answer.id = 268
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Illustrator'
    answer.save()

    answer = Answer()
    answer.id = 269
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Interior Decorator'
    answer.save()

    answer = Answer()
    answer.id = 270
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Operating Theatre Technician'
    answer.save()

    answer = Answer()
    answer.id = 271
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Cinema or Theatre Manager'
    answer.save()

    answer = Answer()
    answer.id = 272
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Clothing Patternmaker'
    answer.save()

    answer = Answer()
    answer.id = 273
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Gymnastics Coach or Instructor'
    answer.save()

    answer = Answer()
    answer.id = 274
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Horse Riding Coach or Instructor'
    answer.save()

    answer = Answer()
    answer.id = 275
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Other Sports Coach or Instructor'
    answer.save()

    answer = Answer()
    answer.id = 276
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Swimming Coach or Instructor'
    answer.save()

    answer = Answer()
    answer.id = 277
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Tennis Coach'
    answer.save()

    answer = Answer()
    answer.id = 278
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Sports Administrator'
    answer.save()

    answer = Answer()
    answer.id = 279
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Sports Centre Manager'
    answer.save()

    answer = Answer()
    answer.id = 280
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Sports Centre Manager'
    answer.save()

    answer = Answer()
    answer.id = 281
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Sports Development Officer'
    answer.save()

    answer = Answer()
    answer.id = 282
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Other Sports Official'
    answer.save()

    answer = Answer()
    answer.id = 283
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Snowsport Instructor'
    answer.save()

    answer = Answer()
    answer.id = 284
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Sports Umpire'
    answer.save()

    answer = Answer()
    answer.id = 285
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Sportspersons (Others)'
    answer.save()

    answer = Answer()
    answer.id = 286
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Fitness Centre Manager'
    answer.save()

    answer = Answer()
    answer.id = 287
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Horse Trainer'
    answer.save()

    answer = Answer()
    answer.id = 288
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Jockey'
    answer.save()

    answer = Answer()
    answer.id = 289
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Diving Instructor (Open Water)'
    answer.save()

    answer = Answer()
    answer.id = 290
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Audiologists'
    answer.save()

    answer = Answer()
    answer.id = 291
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Licensed practical nurses'
    answer.save()

    answer = Answer()
    answer.id = 292
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Nursing co-ordinators and supervisors'
    answer.save()

    answer = Answer()
    answer.id = 293
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Registered nurses and registered psychiatric nurses'
    answer.save()

    answer = Answer()
    answer.id = 294
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Nurse Practitioner'
    answer.save()

    answer = Answer()
    answer.id = 295
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Nursing Clinical Director'
    answer.save()

    answer = Answer()
    answer.id = 296
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Registered Nurse (Aged Care)'
    answer.save()

    answer = Answer()
    answer.id = 297
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Registered Nurse (Child and Family Health)'
    answer.save()

    answer = Answer()
    answer.id = 298
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Registered Nurse (Community Health)'
    answer.save()

    answer = Answer()
    answer.id = 299
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Registered Nurse (Critical Care and Emergency)'
    answer.save()

    answer = Answer()
    answer.id = 300
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Registered Nurse (Developmental Disability)'
    answer.save()

    answer = Answer()
    answer.id = 301
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Registered Nurse (Disability and Rehabilitation)'
    answer.save()

    answer = Answer()
    answer.id = 302
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Registered Nurse (Medical Practice)'
    answer.save()

    answer = Answer()
    answer.id = 303
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Registered Nurse (Medical)'
    answer.save()

    answer = Answer()
    answer.id = 304
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Registered Nurse (Mental Health)'
    answer.save()

    answer = Answer()
    answer.id = 305
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Registered Nurse (Paediatrics)'
    answer.save()

    answer = Answer()
    answer.id = 306
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Registered Nurse (Perioperative)'
    answer.save()

    answer = Answer()
    answer.id = 307
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Registered Nurse (Surgical)'
    answer.save()

    answer = Answer()
    answer.id = 308
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Registered Nurses (Others)'
    answer.save()

    answer = Answer()
    answer.id = 309
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Nurse Educator'
    answer.save()

    answer = Answer()
    answer.id = 310
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Nurse Manager'
    answer.save()

    answer = Answer()
    answer.id = 311
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Nurse Researcher'
    answer.save()

    answer = Answer()
    answer.id = 312
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Enrolled Nurse'
    answer.save()

    answer = Answer()
    answer.id = 313
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Mothercraft Nurse'
    answer.save()

    answer = Answer()
    answer.id = 314
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'General practitioners and family physicians'
    answer.save()

    answer = Answer()
    answer.id = 315
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Specialist physicians (General Medicine)'
    answer.save()

    answer = Answer()
    answer.id = 316
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Specialist Physicians (Others)'
    answer.save()

    answer = Answer()
    answer.id = 317
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Medical Practitioners (Others)'
    answer.save()

    answer = Answer()
    answer.id = 318
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Traditional Chinese Medicine Practitioner'
    answer.save()

    answer = Answer()
    answer.id = 319
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Traditional Maori Health Practitioner'
    answer.save()

    answer = Answer()
    answer.id = 320
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Dentist'
    answer.save()

    answer = Answer()
    answer.id = 321
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Dental Hygienist'
    answer.save()

    answer = Answer()
    answer.id = 322
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Dental Prosthetist'
    answer.save()

    answer = Answer()
    answer.id = 323
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Dental Specialist'
    answer.save()

    answer = Answer()
    answer.id = 324
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Dental Technician'
    answer.save()

    answer = Answer()
    answer.id = 325
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Dental Therapist'
    answer.save()

    answer = Answer()
    answer.id = 326
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Veterinarian'
    answer.save()

    answer = Answer()
    answer.id = 327
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Veterinary Nurse'
    answer.save()

    answer = Answer()
    answer.id = 328
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Optometrist'
    answer.save()

    answer = Answer()
    answer.id = 329
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Chiropractor'
    answer.save()

    answer = Answer()
    answer.id = 330
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Inspectors in public and environmental health and occupational health and safety'
    answer.save()

    answer = Answer()
    answer.id = 331
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Hospital Pharmacist'
    answer.save()

    answer = Answer()
    answer.id = 332
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Industrial Pharmacist'
    answer.save()

    answer = Answer()
    answer.id = 333
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Retail Pharmacist'
    answer.save()

    answer = Answer()
    answer.id = 334
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Pharmacy Technician'
    answer.save()

    answer = Answer()
    answer.id = 335
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Dietitians'
    answer.save()

    answer = Answer()
    answer.id = 336
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Nutritionists'
    answer.save()

    answer = Answer()
    answer.id = 337
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Speech Pathologist'
    answer.save()

    answer = Answer()
    answer.id = 338
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Speech Language Therapist'
    answer.save()

    answer = Answer()
    answer.id = 339
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Physiotherapists'
    answer.save()

    answer = Answer()
    answer.id = 340
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Occupational Therapists'
    answer.save()

    answer = Answer()
    answer.id = 341
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Respiratory therapists, clinical perfusionists and cardiopulmonary technologists'
    answer.save()

    answer = Answer()
    answer.id = 342
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Complementary Health Therapists (Others)'
    answer.save()

    answer = Answer()
    answer.id = 343
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Psychotherapist'
    answer.save()

    answer = Answer()
    answer.id = 344
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Massage Therapist'
    answer.save()

    answer = Answer()
    answer.id = 345
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Diversional Therapist'
    answer.save()

    answer = Answer()
    answer.id = 346
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Medical Radiation Technologist'
    answer.save()

    answer = Answer()
    answer.id = 347
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Medical Sonographer'
    answer.save()

    answer = Answer()
    answer.id = 348
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Paramedical occupations'
    answer.save()

    answer = Answer()
    answer.id = 349
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Medical Administrator'
    answer.save()

    answer = Answer()
    answer.id = 350
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Medical Diagnostic Radiographer'
    answer.save()

    answer = Answer()
    answer.id = 351
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Medical Laboratory Scientist'
    answer.save()

    answer = Answer()
    answer.id = 352
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Medical Oncologist'
    answer.save()

    answer = Answer()
    answer.id = 353
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Medical Radiation Therapist'
    answer.save()

    answer = Answer()
    answer.id = 354
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Physicist (Medical Physicist only)'
    answer.save()

    answer = Answer()
    answer.id = 355
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Medical Superintendent'
    answer.save()

    answer = Answer()
    answer.id = 356
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Resident Medical Officer'
    answer.save()

    answer = Answer()
    answer.id = 357
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Medical Laboratory Technician'
    answer.save()

    answer = Answer()
    answer.id = 358
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Medical Technicians (Others)'
    answer.save()

    answer = Answer()
    answer.id = 359
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Pathologist'
    answer.save()

    answer = Answer()
    answer.id = 360
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Clinical Haematologist'
    answer.save()

    answer = Answer()
    answer.id = 361
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Clinical Psychologist'
    answer.save()

    answer = Answer()
    answer.id = 362
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Clinical Haematologist'
    answer.save()

    answer = Answer()
    answer.id = 363
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Clinical Coder'
    answer.save()

    answer = Answer()
    answer.id = 364
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Cardiologist'
    answer.save()

    answer = Answer()
    answer.id = 365
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Cardiothoracic Surgeon'
    answer.save()

    answer = Answer()
    answer.id = 366
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Radiation Oncologist'
    answer.save()

    answer = Answer()
    answer.id = 367
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Diagnostic and Interventional Radiologist'
    answer.save()

    answer = Answer()
    answer.id = 368
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Health Diagnostic and Promotion Professionals (Others)'
    answer.save()

    answer = Answer()
    answer.id = 369
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Dermatologist'
    answer.save()

    answer = Answer()
    answer.id = 370
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Neurosurgeon'
    answer.save()

    answer = Answer()
    answer.id = 371
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Orthopaedic Surgeon'
    answer.save()

    answer = Answer()
    answer.id = 372
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Paediatric Surgeon'
    answer.save()

    answer = Answer()
    answer.id = 373
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Plastic and Reconstructive Surgeon'
    answer.save()

    answer = Answer()
    answer.id = 374
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Surgeon (General)'
    answer.save()

    answer = Answer()
    answer.id = 375
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Vascular Surgeon'
    answer.save()

    answer = Answer()
    answer.id = 376
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Paediatrician'
    answer.save()

    answer = Answer()
    answer.id = 377
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Psychologists'
    answer.save()

    answer = Answer()
    answer.id = 378
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Educational Psychologist'
    answer.save()

    answer = Answer()
    answer.id = 379
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Organisational Psychologist'
    answer.save()

    answer = Answer()
    answer.id = 380
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Psychiatrist'
    answer.save()

    answer = Answer()
    answer.id = 381
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Emergency Medicine Specialist'
    answer.save()

    answer = Answer()
    answer.id = 382
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Nuclear Medicine Technologist'
    answer.save()

    answer = Answer()
    answer.id = 383
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Renal Medicine Specialist'
    answer.save()

    answer = Answer()
    answer.id = 384
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Thoracic Medicine Specialist'
    answer.save()

    answer = Answer()
    answer.id = 385
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Endocrinologist'
    answer.save()

    answer = Answer()
    answer.id = 386
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Gastroenterologist'
    answer.save()

    answer = Answer()
    answer.id = 387
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Rheumatologist'
    answer.save()

    answer = Answer()
    answer.id = 388
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Neurologist'
    answer.save()

    answer = Answer()
    answer.id = 389
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Obstetrician and Gynaecologist'
    answer.save()

    answer = Answer()
    answer.id = 390
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Ophthalmologist'
    answer.save()

    answer = Answer()
    answer.id = 391
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Orthoptist'
    answer.save()

    answer = Answer()
    answer.id = 392
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Orthotist or Prosthetist'
    answer.save()

    answer = Answer()
    answer.id = 393
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Otorhinolaryngologist'
    answer.save()

    answer = Answer()
    answer.id = 394
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Rehabilitation Counsellor'
    answer.save()

    answer = Answer()
    answer.id = 395
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Urologist'
    answer.save()

    answer = Answer()
    answer.id = 396
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Cardiac Technician'
    answer.save()

    answer = Answer()
    answer.id = 397
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Exercise Physiologist'
    answer.save()

    answer = Answer()
    answer.id = 398
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Health Information Manager'
    answer.save()

    answer = Answer()
    answer.id = 399
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Health Promotion Officer'
    answer.save()

    answer = Answer()
    answer.id = 400
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Midwife'
    answer.save()

    answer = Answer()
    answer.id = 401
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Ambulance Officer'
    answer.save()

    answer = Answer()
    answer.id = 402
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Ambulance Paramedic'
    answer.save()

    answer = Answer()
    answer.id = 403
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Health Practice Manager'
    answer.save()

    answer = Answer()
    answer.id = 404
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Lifeguard'
    answer.save()

    answer = Answer()
    answer.id = 405
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Primary Health Organisation Manager'
    answer.save()

    answer = Answer()
    answer.id = 406
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Health and Welfare Services Managers (Others)'
    answer.save()

    answer = Answer()
    answer.id = 407
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Aboriginal and Torres Strait Islander Health Worker'
    answer.save()

    answer = Answer()
    answer.id = 408
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Kaiawhina (Hauora) (Maori Health Assistant)'
    answer.save()

    answer = Answer()
    answer.id = 409
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Managers in health care'
    answer.save()

    answer = Answer()
    answer.id = 410
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Civil Engineer'
    answer.save()

    answer = Answer()
    answer.id = 411
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Aeronautical Engineer'
    answer.save()

    answer = Answer()
    answer.id = 412
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Agricultural Engineer'
    answer.save()

    answer = Answer()
    answer.id = 413
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Electrical and Electronics Engineering Technologists and Technicians'
    answer.save()

    answer = Answer()
    answer.id = 414
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Electrical Engineer'
    answer.save()

    answer = Answer()
    answer.id = 415
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Biomedical Engineer'
    answer.save()

    answer = Answer()
    answer.id = 416
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Chemical Engineer'
    answer.save()

    answer = Answer()
    answer.id = 417
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Civil Engineering Draftsperson'
    answer.save()

    answer = Answer()
    answer.id = 418
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Civil Engineering Technician'
    answer.save()

    answer = Answer()
    answer.id = 419
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Mechanical Engineering Technologists and Technicians'
    answer.save()

    answer = Answer()
    answer.id = 420
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Mechanical engineers'
    answer.save()

    answer = Answer()
    answer.id = 421
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Petroleum Engineer'
    answer.save()

    answer = Answer()
    answer.id = 422
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Electrical Engineering Draftsperson'
    answer.save()

    answer = Answer()
    answer.id = 423
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Electrical Engineering Technician'
    answer.save()

    answer = Answer()
    answer.id = 424
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Electronics Engineer'
    answer.save()

    answer = Answer()
    answer.id = 425
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Engineering Manager'
    answer.save()

    answer = Answer()
    answer.id = 426
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Engineering Technologist'
    answer.save()

    answer = Answer()
    answer.id = 427
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Environmental Engineer'
    answer.save()

    answer = Answer()
    answer.id = 428
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Geotechnical Engineer'
    answer.save()

    answer = Answer()
    answer.id = 429
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Industrial Engineer'
    answer.save()

    answer = Answer()
    answer.id = 430
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Materials Engineer'
    answer.save()

    answer = Answer()
    answer.id = 431
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Engineering Professionals (Others)'
    answer.save()

    answer = Answer()
    answer.id = 432
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Mining Engineer (Excluding Petroleum)'
    answer.save()

    answer = Answer()
    answer.id = 433
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Production or Plant Engineer'
    answer.save()

    answer = Answer()
    answer.id = 434
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Ships Engineer'
    answer.save()

    answer = Answer()
    answer.id = 435
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Structural Engineer'
    answer.save()

    answer = Answer()
    answer.id = 436
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Telecommunications Engineer'
    answer.save()

    answer = Answer()
    answer.id = 437
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Telecommunications Field Engineer'
    answer.save()

    answer = Answer()
    answer.id = 438
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Telecommunications Network Engineer'
    answer.save()

    answer = Answer()
    answer.id = 439
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Transport Engineer'
    answer.save()

    answer = Answer()
    answer.id = 440
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Building and Engineering Technicians (Others)'
    answer.save()

    answer = Answer()
    answer.id = 441
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Electronic Engineering Draftsperson'
    answer.save()

    answer = Answer()
    answer.id = 442
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Electronic Engineering Technician'
    answer.save()

    answer = Answer()
    answer.id = 443
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Mechanical Engineering Draftsperson'
    answer.save()

    answer = Answer()
    answer.id = 444
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Mechanical Engineering Technician'
    answer.save()

    answer = Answer()
    answer.id = 445
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - Computer Network Technician'
    answer.save()

    answer = Answer()
    answer.id = 446
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - Web Developer'
    answer.save()

    answer = Answer()
    answer.id = 447
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - Computer Network and Systems Engineer'
    answer.save()

    answer = Answer()
    answer.id = 448
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - Analyst Programmer'
    answer.save()

    answer = Answer()
    answer.id = 449
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - Developer Programmer'
    answer.save()

    answer = Answer()
    answer.id = 450
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - Software and Applications Programmers (Others)'
    answer.save()

    answer = Answer()
    answer.id = 451
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - Web Administrator'
    answer.save()

    answer = Answer()
    answer.id = 452
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - Software Engineer or Designer'
    answer.save()

    answer = Answer()
    answer.id = 453
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - Software Tester'
    answer.save()

    answer = Answer()
    answer.id = 454
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - Information Systems Analysts and Consultants'
    answer.save()

    answer = Answer()
    answer.id = 455
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - ICT business Analyst'
    answer.save()

    answer = Answer()
    answer.id = 456
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - ICT Account Manager'
    answer.save()

    answer = Answer()
    answer.id = 457
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - ICT Business Development Manager'
    answer.save()

    answer = Answer()
    answer.id = 458
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - ICT Managers (Others)'
    answer.save()

    answer = Answer()
    answer.id = 459
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - ICT Project Manager'
    answer.save()

    answer = Answer()
    answer.id = 460
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - ICT Quality Assurance Engineer'
    answer.save()

    answer = Answer()
    answer.id = 461
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - ICT Sales Representative'
    answer.save()

    answer = Answer()
    answer.id = 462
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - ICT Security Specialist'
    answer.save()

    answer = Answer()
    answer.id = 463
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - ICT Support and Test Engineers (Others)'
    answer.save()

    answer = Answer()
    answer.id = 464
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - ICT Support Engineer'
    answer.save()

    answer = Answer()
    answer.id = 465
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - ICT Systems Test Engineer'
    answer.save()

    answer = Answer()
    answer.id = 466
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - ICT Trainer'
    answer.save()

    answer = Answer()
    answer.id = 467
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - ICT Customer Support Officer'
    answer.save()

    answer = Answer()
    answer.id = 468
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - ICT Support Technicians (Others)'
    answer.save()

    answer = Answer()
    answer.id = 469
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - Chief Information Officer'
    answer.save()

    answer = Answer()
    answer.id = 470
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - Multimedia Specialist'
    answer.save()

    answer = Answer()
    answer.id = 471
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - Database Analysts and Administrators'
    answer.save()

    answer = Answer()
    answer.id = 472
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - Systems Analyst'
    answer.save()

    answer = Answer()
    answer.id = 473
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - Systems Administrator'
    answer.save()

    answer = Answer()
    answer.id = 474
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - Network Administrator'
    answer.save()

    answer = Answer()
    answer.id = 475
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Computing professionals - Network Analyst'
    answer.save()

    answer = Answer()
    answer.id = 476
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Physicist'
    answer.save()

    answer = Answer()
    answer.id = 477
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Biochemist'
    answer.save()

    answer = Answer()
    answer.id = 478
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Chemist'
    answer.save()

    answer = Answer()
    answer.id = 479
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Chemistry Technician'
    answer.save()

    answer = Answer()
    answer.id = 480
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Agricultural Scientist'
    answer.save()

    answer = Answer()
    answer.id = 481
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Geoscientists and Oceanographers'
    answer.save()

    answer = Answer()
    answer.id = 482
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Other Spatial Scientist'
    answer.save()

    answer = Answer()
    answer.id = 483
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Forest Scientist'
    answer.save()

    answer = Answer()
    answer.id = 484
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Life Scientist (General)'
    answer.save()

    answer = Answer()
    answer.id = 485
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Life Scientists (Others)'
    answer.save()

    answer = Answer()
    answer.id = 486
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Geophysicist'
    answer.save()

    answer = Answer()
    answer.id = 487
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Natural and Physical Science Professionals (Others)'
    answer.save()

    answer = Answer()
    answer.id = 488
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Biotechnologist'
    answer.save()

    answer = Answer()
    answer.id = 489
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Marine Biologist'
    answer.save()

    answer = Answer()
    answer.id = 490
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Microbiologist'
    answer.save()

    answer = Answer()
    answer.id = 491
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Agricultural Consultant'
    answer.save()

    answer = Answer()
    answer.id = 492
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Agricultural Technician'
    answer.save()

    answer = Answer()
    answer.id = 493
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Geologist'
    answer.save()

    answer = Answer()
    answer.id = 494
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Hydrogeologist'
    answer.save()

    answer = Answer()
    answer.id = 495
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Architect'
    answer.save()

    answer = Answer()
    answer.id = 496
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Landscape Architect'
    answer.save()

    answer = Answer()
    answer.id = 497
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Naval Architect'
    answer.save()

    answer = Answer()
    answer.id = 498
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Architectural, Building and Surveying Technicians (Others)'
    answer.save()

    answer = Answer()
    answer.id = 499
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Architectural Draftsperson'
    answer.save()

    answer = Answer()
    answer.id = 500
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Urban and Regional Planner'
    answer.save()

    answer = Answer()
    answer.id = 501
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Mathematician'
    answer.save()

    answer = Answer()
    answer.id = 502
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Statistician'
    answer.save()

    answer = Answer()
    answer.id = 503
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Earth Science Technician'
    answer.save()

    answer = Answer()
    answer.id = 504
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Quantity Surveyor'
    answer.save()

    answer = Answer()
    answer.id = 505
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Surveyor'
    answer.save()

    answer = Answer()
    answer.id = 506
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Marine Surveyor'
    answer.save()

    answer = Answer()
    answer.id = 507
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Construction estimators'
    answer.save()

    answer = Answer()
    answer.id = 508
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Construction Managers or Construction Project Managers'
    answer.save()

    answer = Answer()
    answer.id = 509
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Aeroplane Pilot'
    answer.save()

    answer = Answer()
    answer.id = 510
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Helicopter Pilot'
    answer.save()

    answer = Answer()
    answer.id = 511
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Flying Instructor'
    answer.save()

    answer = Answer()
    answer.id = 512
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Air Traffic Controller'
    answer.save()

    answer = Answer()
    answer.id = 513
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Building Inspector'
    answer.save()

    answer = Answer()
    answer.id = 514
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Building Associate'
    answer.save()

    answer = Answer()
    answer.id = 515
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Environmental Consultant'
    answer.save()

    answer = Answer()
    answer.id = 516
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Environmental Manager'
    answer.save()

    answer = Answer()
    answer.id = 517
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Environmental Research Scientist'
    answer.save()

    answer = Answer()
    answer.id = 518
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Environmental Scientists (Others)'
    answer.save()

    answer = Answer()
    answer.id = 519
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Life Science Technicia'
    answer.save()

    answer = Answer()
    answer.id = 520
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Science Technicians (Others)'
    answer.save()

    answer = Answer()
    answer.id = 521
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Surveying or Spatial Science Technician'
    answer.save()

    answer = Answer()
    answer.id = 522
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'University Professor or lecturer'
    answer.save()

    answer = Answer()
    answer.id = 523
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Early Childhood (Pre-primary School) Teacher'
    answer.save()

    answer = Answer()
    answer.id = 524
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Secondary School Teacher'
    answer.save()

    answer = Answer()
    answer.id = 525
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Special Education Teachers (Others)'
    answer.save()

    answer = Answer()
    answer.id = 526
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Special Needs Teacher'
    answer.save()

    answer = Answer()
    answer.id = 527
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Intermediate School Teacher'
    answer.save()

    answer = Answer()
    answer.id = 528
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Kaiako Kohanga Reo (Maori Language Nest Teacher)'
    answer.save()

    answer = Answer()
    answer.id = 529
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Kaiako Kura Kaupapa Maori (Maori-medium Primary School Teacher)'
    answer.save()

    answer = Answer()
    answer.id = 530
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Teacher of the Hearing Impaired'
    answer.save()

    answer = Answer()
    answer.id = 531
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Teacher of the Sight Impaired'
    answer.save()

    answer = Answer()
    answer.id = 532
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Polytechnic Teacher'
    answer.save()

    answer = Answer()
    answer.id = 533
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Pouako Kura Kaupapa Maori (Maori-medium Primary School Senior Teacher)'
    answer.save()

    answer = Answer()
    answer.id = 534
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Primary School Teacher'
    answer.save()

    answer = Answer()
    answer.id = 535
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Private Tutors and Teachers (Others)'
    answer.save()

    answer = Answer()
    answer.id = 536
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Secondary School Teacher'
    answer.save()

    answer = Answer()
    answer.id = 537
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Teacher of English to Speakers of Other Languages'
    answer.save()

    answer = Answer()
    answer.id = 538
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'School Principal'
    answer.save()

    answer = Answer()
    answer.id = 539
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'School Laboratory Technician'
    answer.save()

    answer = Answer()
    answer.id = 540
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'University Tutor'
    answer.save()

    answer = Answer()
    answer.id = 541
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Early Childhood (Pre-primary school) Assistants'
    answer.save()

    answer = Answer()
    answer.id = 542
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Education Adviser'
    answer.save()

    answer = Answer()
    answer.id = 543
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Education Managers (Others)'
    answer.save()

    answer = Answer()
    answer.id = 544
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Education Reviewer'
    answer.save()

    answer = Answer()
    answer.id = 545
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Regional Education Manager'
    answer.save()

    answer = Answer()
    answer.id = 546
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Judge'
    answer.save()

    answer = Answer()
    answer.id = 547
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Intellectual Property Lawyer'
    answer.save()

    answer = Answer()
    answer.id = 548
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Law Clerk'
    answer.save()

    answer = Answer()
    answer.id = 549
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Judicial and Other Legal Professionals (Others)'
    answer.save()

    answer = Answer()
    answer.id = 550
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Legal Executive'
    answer.save()

    answer = Answer()
    answer.id = 551
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Legal Secretary'
    answer.save()

    answer = Answer()
    answer.id = 552
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Legislators (Others)'
    answer.save()

    answer = Answer()
    answer.id = 553
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Local Government Legislator'
    answer.save()

    answer = Answer()
    answer.id = 554
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Magistrate'
    answer.save()

    answer = Answer()
    answer.id = 555
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Social Worker'
    answer.save()

    answer = Answer()
    answer.id = 556
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Social Professionals (Others)'
    answer.save()

    answer = Answer()
    answer.id = 557
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Family Support Worker'
    answer.save()

    answer = Answer()
    answer.id = 558
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Family and Marriage Counsellor'
    answer.save()

    answer = Answer()
    answer.id = 559
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Student Counsellor'
    answer.save()

    answer = Answer()
    answer.id = 560
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Careers Counsellor'
    answer.save()

    answer = Answer()
    answer.id = 561
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Counsellors (Others)'
    answer.save()

    answer = Answer()
    answer.id = 562
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Drug and Alcohol Counsellor'
    answer.save()

    answer = Answer()
    answer.id = 563
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Minister of Religion'
    answer.save()

    answer = Answer()
    answer.id = 564
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Parole or Probation Officer'
    answer.save()

    answer = Answer()
    answer.id = 565
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Community Worker'
    answer.save()

    answer = Answer()
    answer.id = 566
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Policy Analyst'
    answer.save()

    answer = Answer()
    answer.id = 567
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Policy and Planning Manager'
    answer.save()

    answer = Answer()
    answer.id = 568
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Police Officer'
    answer.save()

    answer = Answer()
    answer.id = 569
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Commissioned Police Officer'
    answer.save()

    answer = Answer()
    answer.id = 570
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Commissioned Defence Force Officer'
    answer.save()

    answer = Answer()
    answer.id = 571
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Commissioned Fire Officer'
    answer.save()

    answer = Answer()
    answer.id = 572
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Disabilities Services Officer'
    answer.save()

    answer = Answer()
    answer.id = 573
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Detective'
    answer.save()

    answer = Answer()
    answer.id = 574
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Defence Force Senior Officer'
    answer.save()

    answer = Answer()
    answer.id = 575
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Electorate Officer'
    answer.save()

    answer = Answer()
    answer.id = 576
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Intelligence Officer'
    answer.save()

    answer = Answer()
    answer.id = 577
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Liaison Officer'
    answer.save()

    answer = Answer()
    answer.id = 578
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Residential Care Officer'
    answer.save()

    answer = Answer()
    answer.id = 579
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Court Collections Officer'
    answer.save()

    answer = Answer()
    answer.id = 580
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Court Registry Officer'
    answer.save()

    answer = Answer()
    answer.id = 581
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Clerk of Court'
    answer.save()

    answer = Answer()
    answer.id = 582
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Fire Fighter'
    answer.save()

    answer = Answer()
    answer.id = 583
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Child Care Centre Manager'
    answer.save()

    answer = Answer()
    answer.id = 584
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Welfare Worker'
    answer.save()

    answer = Answer()
    answer.id = 585
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Welfare Centre Manager'
    answer.save()

    answer = Answer()
    answer.id = 586
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Conveyancer'
    answer.save()

    answer = Answer()
    answer.id = 587
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Barrister'
    answer.save()

    answer = Answer()
    answer.id = 588
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Solicitor'
    answer.save()

    answer = Answer()
    answer.id = 589
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Forester'
    answer.save()

    answer = Answer()
    answer.id = 590
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Market Gardener'
    answer.save()

    answer = Answer()
    answer.id = 591
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Production Manager (Mining)'
    answer.save()

    answer = Answer()
    answer.id = 592
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Production Manager (Forestry)'
    answer.save()

    answer = Answer()
    answer.id = 593
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Crop Farmers (Others)'
    answer.save()

    answer = Answer()
    answer.id = 594
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Field Crop Grower'
    answer.save()

    answer = Answer()
    answer.id = 595
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Mixed Crop and Livestock Farmer'
    answer.save()

    answer = Answer()
    answer.id = 596
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Mixed Crop Farmer'
    answer.save()

    answer = Answer()
    answer.id = 597
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Dairy Cattle Farmer'
    answer.save()

    answer = Answer()
    answer.id = 598
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Deer Farmer'
    answer.save()

    answer = Answer()
    answer.id = 599
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Goat Farmer'
    answer.save()

    answer = Answer()
    answer.id = 600
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Livestock Farmers (Others)'
    answer.save()

    answer = Answer()
    answer.id = 601
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Mixed Livestock Farmer'
    answer.save()

    answer = Answer()
    answer.id = 602
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Pig Farmer'
    answer.save()

    answer = Answer()
    answer.id = 603
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Poultry Farmer'
    answer.save()

    answer = Answer()
    answer.id = 604
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Sheep Farmer'
    answer.save()

    answer = Answer()
    answer.id = 605
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Aquaculture Farmer'
    answer.save()

    answer = Answer()
    answer.id = 606
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Beef Cattle Farmer'
    answer.save()

    answer = Answer()
    answer.id = 607
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Managers in natural resources production and fishing'
    answer.save()

    answer = Answer()
    answer.id = 608
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Master Fisher'
    answer.save()

    answer = Answer()
    answer.id = 609
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Fisheries Officer'
    answer.save()

    answer = Answer()
    answer.id = 610
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Botanist'
    answer.save()

    answer = Answer()
    answer.id = 611
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Drainer'
    answer.save()

    answer = Answer()
    answer.id = 612
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Cotton Grower'
    answer.save()

    answer = Answer()
    answer.id = 613
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Fruit or Nut Grower'
    answer.save()

    answer = Answer()
    answer.id = 614
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Grape Grower'
    answer.save()

    answer = Answer()
    answer.id = 615
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Sugar Cane Grower'
    answer.save()

    answer = Answer()
    answer.id = 616
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Turf Grower'
    answer.save()

    answer = Answer()
    answer.id = 617
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Wine Maker'
    answer.save()

    answer = Answer()
    answer.id = 618
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Sales and Marketing Manager'
    answer.save()

    answer = Answer()
    answer.id = 619
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Sales Representative (Industrial Products)'
    answer.save()

    answer = Answer()
    answer.id = 620
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Sales Representative (Medical and Pharmaceutical Products)'
    answer.save()

    answer = Answer()
    answer.id = 621
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Technical Sales Representatives (Others)'
    answer.save()

    answer = Answer()
    answer.id = 622
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Real Estate Agency Licensee'
    answer.save()

    answer = Answer()
    answer.id = 623
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Real Estate Agent'
    answer.save()

    answer = Answer()
    answer.id = 624
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Real Estate Representative'
    answer.save()

    answer = Answer()
    answer.id = 625
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Accommodation and Hospitality Managers (Others)'
    answer.save()

    answer = Answer()
    answer.id = 626
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Hospitality, Retail and Service Managers (Others)'
    answer.save()

    answer = Answer()
    answer.id = 627
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Travel Agency Manager'
    answer.save()

    answer = Answer()
    answer.id = 628
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Travel Attendants (Others)'
    answer.save()

    answer = Answer()
    answer.id = 629
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Customer Service Manager'
    answer.save()

    answer = Answer()
    answer.id = 630
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Chef'
    answer.save()

    answer = Answer()
    answer.id = 631
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Cook'
    answer.save()

    answer = Answer()
    answer.id = 632
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Pastrycook'
    answer.save()

    answer = Answer()
    answer.id = 633
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Butcher or Smallgoods Maker'
    answer.save()

    answer = Answer()
    answer.id = 634
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Meat Inspector'
    answer.save()

    answer = Answer()
    answer.id = 635
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Baker'
    answer.save()

    answer = Answer()
    answer.id = 636
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Hairdresser'
    answer.save()

    answer = Answer()
    answer.id = 637
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Hair or Beauty Salon Manager'
    answer.save()

    answer = Answer()
    answer.id = 638
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Dressmaker or Tailor'
    answer.save()

    answer = Answer()
    answer.id = 639
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Shoemaker'
    answer.save()

    answer = Answer()
    answer.id = 640
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Jeweller'
    answer.save()

    answer = Answer()
    answer.id = 641
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Watch and Clock Maker and Repairer'
    answer.save()

    answer = Answer()
    answer.id = 642
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Funeral Director'
    answer.save()

    answer = Answer()
    answer.id = 643
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Funeral Workers (Others)'
    answer.save()

    answer = Answer()
    answer.id = 644
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Security Consultant'
    answer.save()

    answer = Answer()
    answer.id = 645
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Pet Groomer'
    answer.save()

    answer = Answer()
    answer.id = 646
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Animal Attendants and Trainers (Others)'
    answer.save()

    answer = Answer()
    answer.id = 647
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Podiatrist'
    answer.save()

    answer = Answer()
    answer.id = 648
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Supply and Distribution Manager'
    answer.save()

    answer = Answer()
    answer.id = 649
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Wholesaler'
    answer.save()

    answer = Answer()
    answer.id = 650
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Amusement Centre Manager'
    answer.save()

    answer = Answer()
    answer.id = 651
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Cafe or Restaurant Manager'
    answer.save()

    answer = Answer()
    answer.id = 652
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Bed and Breakfast Operator'
    answer.save()

    answer = Answer()
    answer.id = 653
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Betting Agency Manager'
    answer.save()

    answer = Answer()
    answer.id = 654
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Boarding Kennel or Cattery Operator'
    answer.save()

    answer = Answer()
    answer.id = 655
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Caravan Park and Camping Ground Manager'
    answer.save()

    answer = Answer()
    answer.id = 656
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Hotel or Motel Manager'
    answer.save()

    answer = Answer()
    answer.id = 657
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Licensed Club Manager'
    answer.save()

    answer = Answer()
    answer.id = 658
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Retail Manager (General)'
    answer.save()

    answer = Answer()
    answer.id = 659
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Metal Fabricator'
    answer.save()

    answer = Answer()
    answer.id = 660
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Metal Machinist (First Class)'
    answer.save()

    answer = Answer()
    answer.id = 661
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Metallurgist'
    answer.save()

    answer = Answer()
    answer.id = 662
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Sheetmetal Trades Worker'
    answer.save()

    answer = Answer()
    answer.id = 663
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Metallurgical or Materials Technician'
    answer.save()

    answer = Answer()
    answer.id = 664
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Metal Casting Trades Worker'
    answer.save()

    answer = Answer()
    answer.id = 665
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Metal Fitters and Machinists (Others)'
    answer.save()

    answer = Answer()
    answer.id = 666
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Metal Polisher'
    answer.save()

    answer = Answer()
    answer.id = 667
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Sheetmetal Trades Worker'
    answer.save()

    answer = Answer()
    answer.id = 668
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Electrical Line Mechanic'
    answer.save()

    answer = Answer()
    answer.id = 669
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Electrical Linesworker'
    answer.save()

    answer = Answer()
    answer.id = 670
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Technical Cable Jointer'
    answer.save()

    answer = Answer()
    answer.id = 671
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Printing Machinist'
    answer.save()

    answer = Answer()
    answer.id = 672
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Wood Machinist'
    answer.save()

    answer = Answer()
    answer.id = 673
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Wood Machinists and Other Wood Trades Workers (Others)'
    answer.save()

    answer = Answer()
    answer.id = 674
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Toolmaker'
    answer.save()

    answer = Answer()
    answer.id = 675
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Fitter-Welder'
    answer.save()

    answer = Answer()
    answer.id = 676
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Pressure Welder'
    answer.save()

    answer = Answer()
    answer.id = 677
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Welder (First Class)'
    answer.save()

    answer = Answer()
    answer.id = 678
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Cabler (Data and Telecommunications)'
    answer.save()

    answer = Answer()
    answer.id = 679
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Telecommunications Cable Jointer'
    answer.save()

    answer = Answer()
    answer.id = 680
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Airconditioning and Mechanical Services Plumber'
    answer.save()

    answer = Answer()
    answer.id = 681
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Plumber (General)'
    answer.save()

    answer = Answer()
    answer.id = 682
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Roof plumber'
    answer.save()

    answer = Answer()
    answer.id = 683
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Carpenter'
    answer.save()

    answer = Answer()
    answer.id = 684
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Carpenter and Joiner'
    answer.save()

    answer = Answer()
    answer.id = 685
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Bricklayer'
    answer.save()

    answer = Answer()
    answer.id = 686
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Fibrous Plasterer'
    answer.save()

    answer = Answer()
    answer.id = 687
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Solid Plasterer'
    answer.save()

    answer = Answer()
    answer.id = 688
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Print Finisher'
    answer.save()

    answer = Answer()
    answer.id = 689
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Floor Finisher'
    answer.save()

    answer = Answer()
    answer.id = 690
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Furniture Finisher'
    answer.save()

    answer = Answer()
    answer.id = 691
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Glazier'
    answer.save()

    answer = Answer()
    answer.id = 692
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Vehicle Painter'
    answer.save()

    answer = Answer()
    answer.id = 693
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Wall and Floor Tiler'
    answer.save()

    answer = Answer()
    answer.id = 694
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Airconditioning and Refrigeration Mechanic'
    answer.save()

    answer = Answer()
    answer.id = 695
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Diesel Motor Mechanic'
    answer.save()

    answer = Answer()
    answer.id = 696
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Lift Mechanic'
    answer.save()

    answer = Answer()
    answer.id = 697
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Motor Mechanic (General)'
    answer.save()

    answer = Answer()
    answer.id = 698
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Motorcycle Mechanic'
    answer.save()

    answer = Answer()
    answer.id = 699
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Small Engine Mechanic'
    answer.save()

    answer = Answer()
    answer.id = 700
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Aircraft Maintenance Engineer (Mechanical)'
    answer.save()

    answer = Answer()
    answer.id = 701
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Aircraft Maintenance Engineer (Avionics)'
    answer.save()

    answer = Answer()
    answer.id = 702
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Business Machine Mechanic'
    answer.save()

    answer = Answer()
    answer.id = 703
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Optical Mechanic'
    answer.save()

    answer = Answer()
    answer.id = 704
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Telecommunications Line Mechanic'
    answer.save()

    answer = Answer()
    answer.id = 705
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Automotive Electrician'
    answer.save()

    answer = Answer()
    answer.id = 706
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Air Transport Professionals (Others)'
    answer.save()

    answer = Answer()
    answer.id = 707
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Boat Builder and Repairer'
    answer.save()

    answer = Answer()
    answer.id = 708
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Electrician (General)'
    answer.save()

    answer = Answer()
    answer.id = 709
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Electrician (Special Class)'
    answer.save()

    answer = Answer()
    answer.id = 710
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Electronic Equipment Trades Worker'
    answer.save()

    answer = Answer()
    answer.id = 711
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Electronic Instrument Trades Worker (General)'
    answer.save()

    answer = Answer()
    answer.id = 712
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Electronic Instrument Trades Worker (Special Class)'
    answer.save()

    answer = Answer()
    answer.id = 713
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Fitter (General)'
    answer.save()

    answer = Answer()
    answer.id = 714
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Fitter and Turner'
    answer.save()

    answer = Answer()
    answer.id = 715
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Gasfitter'
    answer.save()

    answer = Answer()
    answer.id = 716
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Joiner'
    answer.save()

    answer = Answer()
    answer.id = 717
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Locksmith'
    answer.save()

    answer = Answer()
    answer.id = 718
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Painting trades workers'
    answer.save()

    answer = Answer()
    answer.id = 719
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Ships Master'
    answer.save()

    answer = Answer()
    answer.id = 720
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Ships Officer'
    answer.save()

    answer = Answer()
    answer.id = 721
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Shipwright'
    answer.save()

    answer = Answer()
    answer.id = 722
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Stonemason'
    answer.save()

    answer = Answer()
    answer.id = 723
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Manufacturer'
    answer.save()

    answer = Answer()
    answer.id = 724
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Marine Transport Professionals (Others)'
    answer.save()

    answer = Answer()
    answer.id = 725
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Production Manager (Manufacturing)'
    answer.save()

    answer = Answer()
    answer.id = 726
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Equipment Hire Manager'
    answer.save()

    answer = Answer()
    answer.id = 727
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Fleet Manager'
    answer.save()

    answer = Answer()
    answer.id = 728
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Transport Company Manager'
    answer.save()

    answer = Answer()
    answer.id = 729
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Apparel Cutter'
    answer.save()

    answer = Answer()
    answer.id = 730
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Automotive Electrician'
    answer.save()

    answer = Answer()
    answer.id = 731
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Blacksmith'
    answer.save()

    answer = Answer()
    answer.id = 732
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Boat Builder and Repairer'
    answer.save()

    answer = Answer()
    answer.id = 733
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Cabinetmaker'
    answer.save()

    answer = Answer()
    answer.id = 734
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Canvas Goods Fabricator'
    answer.save()

    answer = Answer()
    answer.id = 735
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Chemical Plant Operator'
    answer.save()

    answer = Answer()
    answer.id = 736
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Communications Operator'
    answer.save()

    answer = Answer()
    answer.id = 737
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Drainlayer'
    answer.save()

    answer = Answer()
    answer.id = 738
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Electroplater'
    answer.save()

    answer = Answer()
    answer.id = 739
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Farrier'
    answer.save()

    answer = Answer()
    answer.id = 740
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Fire Protection Equipment Technician'
    answer.save()

    answer = Answer()
    answer.id = 741
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Gas or Petroleum Operator'
    answer.save()

    answer = Answer()
    answer.id = 742
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Leather Goods Maker'
    answer.save()

    answer = Answer()
    answer.id = 743
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Light Technician'
    answer.save()

    answer = Answer()
    answer.id = 744
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Panelbeater'
    answer.save()

    answer = Answer()
    answer.id = 745
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Picture Framer'
    answer.save()

    answer = Answer()
    answer.id = 746
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Plastics Technician'
    answer.save()

    answer = Answer()
    answer.id = 747
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Power Generation Plant Operator'
    answer.save()

    answer = Answer()
    answer.id = 748
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Precision Instrument Maker and Repairer'
    answer.save()

    answer = Answer()
    answer.id = 749
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Roof Tiler'
    answer.save()

    answer = Answer()
    answer.id = 750
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Sail Maker'
    answer.save()

    answer = Answer()
    answer.id = 751
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Saw Maker and Repairer'
    answer.save()

    answer = Answer()
    answer.id = 752
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Screen Printer'
    answer.save()

    answer = Answer()
    answer.id = 753
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Small Offset Printer'
    answer.save()

    answer = Answer()
    answer.id = 754
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Sound Technician'
    answer.save()

    answer = Answer()
    answer.id = 755
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Technicians and Trades Workers (Others)'
    answer.save()

    answer = Answer()
    answer.id = 756
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Telecommunications Technician'
    answer.save()

    answer = Answer()
    answer.id = 757
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Television Equipment Operator'
    answer.save()

    answer = Answer()
    answer.id = 758
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Textile, Clothing and Footwear Mechanic'
    answer.save()

    answer = Answer()
    answer.id = 759
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Upholsterer'
    answer.save()

    answer = Answer()
    answer.id = 760
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Vehicle Body Builder'
    answer.save()

    answer = Answer()
    answer.id = 761
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Vehicle Trimmer'
    answer.save()

    answer = Answer()
    answer.id = 762
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Wood Turner'
    answer.save()

    answer = Answer()
    answer.id = 763
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Arborist'
    answer.save()

    answer = Answer()
    answer.id = 764
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Clothing Trades Workers (Others)'
    answer.save()

    answer = Answer()
    answer.id = 765
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Florist'
    answer.save()

    answer = Answer()
    answer.id = 766
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Gardener (General)'
    answer.save()

    answer = Answer()
    answer.id = 767
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Greenkeeper'
    answer.save()

    answer = Answer()
    answer.id = 768
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Kennel Hand'
    answer.save()

    answer = Answer()
    answer.id = 769
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Landscape Gardener'
    answer.save()

    answer = Answer()
    answer.id = 770
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Nurseryperson'
    answer.save()

    answer = Answer()
    answer.id = 771
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments / Manufacturing / Utilities
    answer.description = 'Wool Classer'
    answer.save()


    ######### ADDITIONAL ######################################################
    answer = Answer()
    answer.id = 772
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Advertising Manager'
    answer.save()

    answer = Answer()
    answer.id = 773
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Advertising Specialist'
    answer.save()

    answer = Answer()
    answer.id = 774
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Home building and renovation managers'
    answer.save()

    answer = Answer()
    answer.id = 775
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Human resources managers'
    answer.save()

    answer = Answer()
    answer.id = 776
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Professional occupations in advertising, marketing and public relations (Others)'
    answer.save()

    answer = Answer()
    answer.id = 777
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Purchasing managers'
    answer.save()

    answer = Answer()
    answer.id = 778
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Chief Executive or Managing Director'
    answer.save()

    answer = Answer()
    answer.id = 779
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Senior managers – financial, communications and other business services'
    answer.save()

    answer = Answer()
    answer.id = 780
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Senior managers – trade, broadcasting and other services (Others)'
    answer.save()

    answer = Answer()
    answer.id = 781
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Company Secretary'
    answer.save()

    answer = Answer()
    answer.id = 782
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Corporate General Manager'
    answer.save()

    answer = Answer()
    answer.id = 783
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Corporate Services Manager'
    answer.save()

    answer = Answer()
    answer.id = 784
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Corporate Treasurer'
    answer.save()

    answer = Answer()
    answer.id = 785
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Futures Trader'
    answer.save()

    answer = Answer()
    answer.id = 786
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Project Builder'
    answer.save()

    answer = Answer()
    answer.id = 787
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Human Resource Adviser'
    answer.save()

    answer = Answer()
    answer.id = 788
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Human Resource Manager'
    answer.save()

    answer = Answer()
    answer.id = 789
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Importer or Exporter'
    answer.save()

    answer = Answer()
    answer.id = 790
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Information and Organisation Professionals (Others)'
    answer.save()

    answer = Answer()
    answer.id = 791
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Management Consultant'
    answer.save()

    answer = Answer()
    answer.id = 792
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Market Research Analyst'
    answer.save()

    answer = Answer()
    answer.id = 793
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Marketing Specialist'
    answer.save()

    answer = Answer()
    answer.id = 794
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Organisation and Methods Analyst'
    answer.save()

    answer = Answer()
    answer.id = 795
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Procurement Manager'
    answer.save()

    answer = Answer()
    answer.id = 796
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Public Relations Manager'
    answer.save()

    answer = Answer()
    answer.id = 797
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Public Relations Professional'
    answer.save()

    answer = Answer()
    answer.id = 798
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Quality Assurance Manager'
    answer.save()

    answer = Answer()
    answer.id = 799
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Recruitment Consultant'
    answer.save()

    answer = Answer()
    answer.id = 800
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Research and Development Manager'
    answer.save()

    answer = Answer()
    answer.id = 801
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Specialist Managers (Others)'
    answer.save()

    answer = Answer()
    answer.id = 802
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Technical Director'
    answer.save()

    answer = Answer()
    answer.id = 803
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Training and Development Professional'
    answer.save()

    answer = Answer()
    answer.id = 804
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Call or Contact Centre Manager'
    answer.save()

    answer = Answer()
    answer.id = 805
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Commodities Trader'
    answer.save()

    answer = Answer()
    answer.id = 806
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Conference and Event Organiser'
    answer.save()

    answer = Answer()
    answer.id = 807
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Facilities Manager'
    answer.save()

    answer = Answer()
    answer.id = 808
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Maintenance Planner'
    answer.save()

    answer = Answer()
    answer.id = 809
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Office Manager'
    answer.save()

    answer = Answer()
    answer.id = 810
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Post Office Manager'
    answer.save()

    answer = Answer()
    answer.id = 811
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Practice Managers (Others)'
    answer.save()

    answer = Answer()
    answer.id = 812
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Railway Station Manager'
    answer.save()

    answer = Answer()
    answer.id = 813
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Retirement Village Manager'
    answer.save()

    answer = Answer()
    answer.id = 814
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Call or Contact Centre Team Leader'
    answer.save()

    answer = Answer()
    answer.id = 815
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Personal Assistant'
    answer.save()

    answer = Answer()
    answer.id = 816
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Retail Buyer'
    answer.save()

    answer = Answer()
    answer.id = 817
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Secretary (General)'
    answer.save()

    answer = Answer()
    answer.id = 818
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 1 ) # Business / Finance / Administration / Advertising
    answer.description = 'Trust Officer'
    answer.save()

    answer = Answer()
    answer.id = 819
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Stage Manager'
    answer.save()

    answer = Answer()
    answer.id = 820
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Television Presenter'
    answer.save()

    answer = Answer()
    answer.id = 821
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Dog or Horse Racing Official'
    answer.save()

    answer = Answer()
    answer.id = 822
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Footballer'
    answer.save()

    answer = Answer()
    answer.id = 823
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 2 ) # Art / Culture / Recreation / Sport
    answer.description = 'Golfer'
    answer.save()

    answer = Answer()
    answer.id = 824
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Acupuncturist'
    answer.save()

    answer = Answer()
    answer.id = 825
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Anaesthetist'
    answer.save()

    answer = Answer()
    answer.id = 826
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Environmental Health Officer'
    answer.save()

    answer = Answer()
    answer.id = 827
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Intensive Care Specialist'
    answer.save()

    answer = Answer()
    answer.id = 828
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Osteopath'
    answer.save()

    answer = Answer()
    answer.id = 829
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Podiatrist'
    answer.save()

    answer = Answer()
    answer.id = 830
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Naturopath'
    answer.save()

    answer = Answer()
    answer.id = 831
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Anaesthetic Technician'
    answer.save()

    answer = Answer()
    answer.id = 832
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Quarantine Officer'
    answer.save()

    answer = Answer()
    answer.id = 833
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'First Aid Trainer'
    answer.save()

    answer = Answer()
    answer.id = 834
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 3 ) # Health
    answer.description = 'Phlebotomist'
    answer.save()

    answer = Answer()
    answer.id = 835
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Industrial instrument technicians and mechanics'
    answer.save()

    answer = Answer()
    answer.id = 836
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Cartographer'
    answer.save()

    answer = Answer()
    answer.id = 837
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Food Technologist'
    answer.save()

    answer = Answer()
    answer.id = 838
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Laboratory Manager'
    answer.save()

    answer = Answer()
    answer.id = 839
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Telecommunications Network Planner'
    answer.save()

    answer = Answer()
    answer.id = 840
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Telecommunications Technical Officer or Technologist'
    answer.save()

    answer = Answer()
    answer.id = 841
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Meteorologist'
    answer.save()

    answer = Answer()
    answer.id = 842
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Patents Examiner'
    answer.save()

    answer = Answer()
    answer.id = 843
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Zoologist'
    answer.save()

    answer = Answer()
    answer.id = 844
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Hydrographer'
    answer.save()

    answer = Answer()
    answer.id = 845
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 4 ) # Engineering / Technology / Natural and Applied Sciences / Architecture
    answer.description = 'Mine Deputy'
    answer.save()

    answer = Answer()
    answer.id = 846
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Archaeologist'
    answer.save()

    answer = Answer()
    answer.id = 847
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Faculty Head'
    answer.save()

    answer = Answer()
    answer.id = 848
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Historian'
    answer.save()

    answer = Answer()
    answer.id = 849
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Migration Agent'
    answer.save()

    answer = Answer()
    answer.id = 850
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Member of Parliament'
    answer.save()

    answer = Answer()
    answer.id = 851
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Park Ranger'
    answer.save()

    answer = Answer()
    answer.id = 852
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Senior Non-commissioned Defence Force'
    answer.save()

    answer = Answer()
    answer.id = 853
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Tribunal Member'
    answer.save()

    answer = Answer()
    answer.id = 854
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Workplace Relations Adviser'
    answer.save()

    answer = Answer()
    answer.id = 855
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Youth Worker'
    answer.save()

    answer = Answer()
    answer.id = 856
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Defence Force Member - Other Ranks'
    answer.save()

    answer = Answer()
    answer.id = 857
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 5 ) # Education / Law / Social, community and gov. services
    answer.description = 'Emergency Service Worker'
    answer.save()

    answer = Answer()
    answer.id = 858
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Apiarist'
    answer.save()

    answer = Answer()
    answer.id = 859
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Horse Breeder'
    answer.save()

    answer = Answer()
    answer.id = 860
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Primary Products Inspectors (Others)'
    answer.save()

    answer = Answer()
    answer.id = 861
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Shearer'
    answer.save()

    answer = Answer()
    answer.id = 862
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Stock and Station Agent'
    answer.save()

    answer = Answer()
    answer.id = 863
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 6 ) # Natural Resources / Agriculture / Related Production
    answer.description = 'Wool Buyer'
    answer.save()

    answer = Answer()
    answer.id = 864
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Diver'
    answer.save()

    answer = Answer()
    answer.id = 865
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Auctioneer'
    answer.save()

    answer = Answer()
    answer.id = 866
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Dispensing Optician'
    answer.save()

    answer = Answer()
    answer.id = 867
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Dog Handler or Trainer'
    answer.save()

    answer = Answer()
    answer.id = 868
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Driving Instructor'
    answer.save()

    answer = Answer()
    answer.id = 869
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Hotel Service Manager'
    answer.save()

    answer = Answer()
    answer.id = 870
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Property Manager'
    answer.save()

    answer = Answer()
    answer.id = 871
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 7 ) # Sales / Services
    answer.description = 'Zookeeper'
    answer.save()

    answer = Answer()
    answer.id = 872
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments
    answer.description = 'Flower Grower'
    answer.save()

    answer = Answer()
    answer.id = 873
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments
    answer.description = 'Hardware Technician'
    answer.save()

    answer = Answer()
    answer.id = 874
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments
    answer.description = 'Plumbing Inspector'
    answer.save()

    answer = Answer()
    answer.id = 875
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments
    answer.description = 'Engineering Patternmaker'
    answer.save()

    answer = Answer()
    answer.id = 876
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments
    answer.description = 'Engraver'
    answer.save()

    answer = Answer()
    answer.id = 877
    answer.question = Question.objects.get( pk = 9 )
    answer.answer_category = AnswerCategory.objects.get( pk = 8 ) # Trades / Transports / Equipments
    answer.description = 'Flight Attendant'
    answer.save()

    # -- Partner Skills? -----------------------------
    answer = Answer()
    answer.id = 878
    answer.question = Question.objects.get( pk = 10 )
    answer.description = 'Yes'
    answer.save()

    answer = Answer()
    answer.id = 879
    answer.question = Question.objects.get( pk = 10 )
    answer.description = 'No'
    answer.save()


    # -- Invest or open a business? -----------------------------
    answer = Answer()
    answer.id = 880
    answer.question = Question.objects.get( pk = 11 )
    answer.description = 'Yes'
    answer.save()

    answer = Answer()
    answer.id = 881
    answer.question = Question.objects.get( pk = 11 )
    answer.description = 'No'
    answer.save()


    # -- Letter from startup canadian venture? -----------------------------
    answer = Answer()
    answer.id = 882
    answer.question = Question.objects.get( pk = 12 )
    answer.description = 'Yes'
    answer.save()

    answer = Answer()
    answer.id = 883
    answer.question = Question.objects.get( pk = 12 )
    answer.description = 'No'
    answer.save()


    # -- US Citizen? -----------------------------
    answer = Answer()
    answer.id = 884
    answer.question = Question.objects.get( pk = 13 )
    answer.description = 'Yes'
    answer.save()

    answer = Answer()
    answer.id = 885
    answer.question = Question.objects.get( pk = 13 )
    answer.description = 'No'
    answer.save()


    # -- Studied in Regional Australia? -----------------------------
    answer = Answer()
    answer.id = 886
    answer.question = Question.objects.get( pk = 14 )
    answer.description = 'Yes'
    answer.save()

    answer = Answer()
    answer.id = 887
    answer.question = Question.objects.get( pk = 14 )
    answer.description = 'No'
    answer.save()


    # -- Professional year in Australia? -----------------------------
    answer = Answer()
    answer.id = 888
    answer.question = Question.objects.get( pk = 15 )
    answer.description = 'Yes'
    answer.save()

    answer = Answer()
    answer.id = 889
    answer.question = Question.objects.get( pk = 15 )
    answer.description = 'No'
    answer.save()


    # -- Willing to live and work in Australia? -----------------------------
    answer = Answer()
    answer.id = 890
    answer.question = Question.objects.get( pk = 16 )
    answer.description = 'Yes'
    answer.save()

    answer = Answer()
    answer.id = 891
    answer.question = Question.objects.get( pk = 16 )
    answer.description = 'No'
    answer.save()


    # -- Credentialled community language in Australia? -----------------------------
    answer = Answer()
    answer.id = 892
    answer.question = Question.objects.get( pk = 17 )
    answer.description = 'Yes'
    answer.save()

    answer = Answer()
    answer.id = 893
    answer.question = Question.objects.get( pk = 17 )
    answer.description = 'No'
    answer.save()

    # -- Partner studied or worked in CANADA? -----------------------------
    answer = Answer()
    answer.id = 894
    answer.question = Question.objects.get( pk = 18 )
    answer.description = 'Yes'
    answer.save()

    answer = Answer()
    answer.id = 895
    answer.question = Question.objects.get( pk = 18 )
    answer.description = 'No'
    answer.save()


    # -- What is your PARTNER ENGLISH level? -----------------------------
    answer = Answer()
    answer.id = 896
    answer.question = Question.objects.get( pk = 19 )
    answer.description = 'None'
    answer.save()

    answer = Answer()
    answer.id = 897
    answer.question = Question.objects.get( pk = 19 )
    answer.description = 'Basic Proficiency'
    answer.save()

    answer = Answer()
    answer.id = 898
    answer.question = Question.objects.get( pk = 19 )
    answer.description = 'Moderate Proficiency'
    answer.save()

    answer = Answer()
    answer.id = 899
    answer.question = Question.objects.get( pk = 19 )
    answer.description = 'High Proficiency'
    answer.save()


    # -- What is your PARTNER FRENCH level? -----------------------------
    answer = Answer()
    answer.id = 900
    answer.question = Question.objects.get( pk = 20 )
    answer.description = 'None'
    answer.save()

    answer = Answer()
    answer.id = 901
    answer.question = Question.objects.get( pk = 20 )
    answer.description = 'Basic Proficiency'
    answer.save()

    answer = Answer()
    answer.id = 902
    answer.question = Question.objects.get( pk = 20 )
    answer.description = 'Moderate Proficiency'
    answer.save()

    answer = Answer()
    answer.id = 903
    answer.question = Question.objects.get( pk = 20 )
    answer.description = 'High Proficiency'
    answer.save()


    # -- What is your PARTNER'S highest degree of education? -----------------------------
    answer = Answer()
    answer.id = 904
    answer.question = Question.objects.get( pk = 21 )
    answer.description = 'None'
    answer.save()

    answer = Answer()
    answer.id = 905
    answer.question = Question.objects.get( pk = 21 )
    answer.description = 'Primary Education'
    answer.save()

    answer = Answer()
    answer.id = 906
    answer.question = Question.objects.get( pk = 21 )
    answer.description = 'Secondary Education - Lower'
    answer.save()

    answer = Answer()
    answer.id = 907
    answer.question = Question.objects.get( pk = 21 )
    answer.description = 'Secondary Education - Upper (High-School)'
    answer.save()

    answer = Answer()
    answer.id = 908
    answer.question = Question.objects.get( pk = 21 )
    answer.description = 'Post Secondary Education (Trades, associate, technical)'
    answer.save()

    answer = Answer()
    answer.id = 909
    answer.question = Question.objects.get( pk = 21 )
    answer.description = 'Bachelors Level'
    answer.save()

    answer = Answer()
    answer.id = 910
    answer.question = Question.objects.get( pk = 21 )
    answer.description = 'Masters Level'
    answer.save()

    answer = Answer()
    answer.id = 911
    answer.question = Question.objects.get( pk = 21 )
    answer.description = 'Doctoral Level'
    answer.save()


#######################
# MIGRATION CLASS
#######################
class Migration( migrations.Migration ):

    dependencies = [
        ( 'core', '0001_initial' ),
    ]

    operations = [
        migrations.RunPython( auth_group_initial_values ),
        migrations.RunPython( core_continent_initial_values ),
        migrations.RunPython( core_country_initial_values ),
        migrations.RunPython( core_language_initial_values ),
        migrations.RunPython( core_question_initial_values ),
        migrations.RunPython( core_answer_category_initial_values ),
        migrations.RunPython( core_answer_initial_values ),
    ]