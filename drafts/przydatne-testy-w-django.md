Title: Przydatne testy w Django
Date: 2019-04-25 13:42
Author: filipgorczynski
Category: Tech
Slug: przydatne-testy-w-django
Status: draft

self.assertEquals(  
response.get('Content-Disposition'),  
"attachment; filename=somefile.jpg"  
)
