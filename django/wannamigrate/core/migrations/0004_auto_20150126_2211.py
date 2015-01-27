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

    language = Language()
    language.id = 163
    language.name = 'Assyrian'
    language.code = 'assyri'
    language.save()

    language = Language()
    language.id = 164
    language.name = 'Auslan'
    language.code = 'auslan'
    language.save()

    language = Language()
    language.id = 165
    language.name = 'Bangla'
    language.code = 'bangla'
    language.save()

    language = Language()
    language.id = 166
    language.name = 'Bosnian'
    language.code = 'bosnia'
    language.save()

    language = Language()
    language.id = 167
    language.name = 'Cantonese'
    language.code = 'canton'
    language.save()

    language = Language()
    language.id = 168
    language.name = 'Dari'
    language.code = 'dari'
    language.save()

    language = Language()
    language.id = 169
    language.name = 'Dinka'
    language.code = 'dinka'
    language.save()

    language = Language()
    language.id = 170
    language.name = 'Filipino'
    language.code = 'filipi'
    language.save()

    language = Language()
    language.id = 171
    language.name = 'Hakka (Chinese)'
    language.code = 'hakka'
    language.save()

    language = Language()
    language.id = 172
    language.name = 'Hazaragi'
    language.code = 'hazara'
    language.save()

    language = Language()
    language.id = 173
    language.name = 'Khmer'
    language.code = 'khmer'
    language.save()

    language = Language()
    language.id = 174
    language.name = 'Lao'
    language.code = 'lao'
    language.save()

    language = Language()
    language.id = 175
    language.name = 'Mandarin'
    language.code = 'mandar'
    language.save()

    language = Language()
    language.id = 176
    language.name = 'Nuer'
    language.code = 'nuer'
    language.save()

    language = Language()
    language.id = 177
    language.name = 'Oromo'
    language.code = 'oromo'
    language.save()

    language = Language()
    language.id = 178
    language.name = 'Persian'
    language.code = 'persia'
    language.save()

    language = Language()
    language.id = 179
    language.name = 'Pushto'
    language.code = 'pushto'
    language.save()

    language = Language()
    language.id = 180
    language.name = 'Swahili'
    language.code = 'swahil'
    language.save()

    language = Language()
    language.id = 181
    language.name = 'Tetum'
    language.code = 'tetum'
    language.save()

    language = Language()
    language.id = 182
    language.name = 'Tongan'
    language.code = 'tongan'
    language.save()





class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_goal_language_message_usereducation_usereducationhistory_usergoal_userlanguage_userlanguageproficien'),
    ]

    operations = [
        migrations.RunPython( auth_group_initial_values ),
        migrations.RunPython( core_continent_initial_values ),
        migrations.RunPython( core_country_initial_values ),
        migrations.RunPython( core_language_initial_values ),
    ]
