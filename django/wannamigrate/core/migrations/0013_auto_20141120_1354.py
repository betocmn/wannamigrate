# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


#######################
# LANGUAGES
#######################
def core_language_aditional_values( apps, schema_editor ):

    # Get model to use (historical version)
    Language = apps.get_model( "core", "Language" )

    # Insert data
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




#######################
# MIGRATION CLASS
#######################
class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20141119_1752'),
    ]

    operations = [
        migrations.RunPython( core_language_aditional_values ),
    ]
