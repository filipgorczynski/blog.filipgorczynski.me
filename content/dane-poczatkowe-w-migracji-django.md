Title: Dane początkowe w migracji Django
Date: 2018-03-07 16:47
Author: filipgorczynski
Category: Tech
Tags: django, initial data, makemigrations, migracje, Python
Slug: dane-poczatkowe-w-migracji-django
Status: draft

[![Djanglo Logo](https://filipgorczynski.files.wordpress.com/2015/10/django-logo-positive.png?w=150){.alignleft .wp-image-1153 .size-thumbnail width="150" height="52"}](https://filipgorczynski.files.wordpress.com/2015/10/django-logo-positive.png)

 

 

\[code language="bash"\]  
python ../manage.py makemigrations --empty \<APLIKACJA\>  
\[/code\]

i w świeżo utworzonym pliku z migracją...

\[code language="python"\]  
\# -\*- coding: utf-8 -\*-  
from \_\_future\_\_ import unicode\_literals

from django.db import models, migrations

def populate\_badges(apps, schema\_editor):  
Badge = apps.get\_model('volontulo', 'Badge')  
records = Badge.objects.all().count()  
initial = \[  
{  
'name': 'Wolontariusz',  
'slug': 'volunteer',  
'priority': 1,  
},  
{  
'name': 'Uczestnik',  
'slug': 'participant',  
'priority': 2,  
},  
{  
'name': 'Wybitny uczestnik',  
'slug': 'prominent-participant',  
'priority': 3,  
}  
\]  
if records != 3:  
for row in initial:  
Badge(\*\*row).save()

class Migration(migrations.Migration):

dependencies = \[  
('volontulo', '0005\_auto\_20150930\_1130'),  
\]

operations = \[  
migrations.RunPython(populate\_badges),  
\]  
\[/code\]

 
