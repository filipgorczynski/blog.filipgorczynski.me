Title: Wymuszenie zatrzymania wbudowanego serwera Django na konkretnym porcie
Date: 2015-10-01 07:36
Author: filipgorczynski
Category: Rozwiązania
Tags: 8000, django, fuser, pdb, serwer wbudowany, zatrzymanie
Slug: wymuszenie-zatrzymania-wbudowanego-serwera-django-na-konkretnym-porcie
Status: published

[![Djanglo Logo](https://filipgorczynski.files.wordpress.com/2015/10/django-logo-positive.png?w=150){.alignleft .wp-image-1153 .size-thumbnail width="150" height="52"}](https://filipgorczynski.files.wordpress.com/2015/10/django-logo-positive.png)Korzystając z wbudowanego serwera Django oraz debuggera pdb doprowadziłem do sytuacji, w której w żadnej konsoli ten serwer nie był uruchomiony - próba jego ponownego odpalenia skutkowała komunikatem:

\[code language="bash"\]  
Performing system checks...

System check identified no issues (0 silenced).  
September 29, 2015 - 07:47:36  
Django version 1.8, using settings 'project.settings'  
Starting development server at http://127.0.0.1:8000/  
Quit the server with CONTROL-C.  
Error: That port is already in use.  
\[/code\]

Próba otwierania strony w przeglądarce nic nie dawała, reagowało to tak, jak by zatrzymywało się grzecznie na pdb - przy czym żadnych informacji nigdzie o tym nie było.

Przydało się polecenie:

\[code language="bash"\]  
fuser -n tcp -k 8000  
\[/code\]
