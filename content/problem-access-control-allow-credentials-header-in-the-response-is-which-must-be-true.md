Title: Problem: 'Access-Control-Allow-Credentials' header in the response is '' which must be 'true'
Date: 2018-10-19 10:59
Author: filipgorczynski
Category: Tech
Slug: problem-access-control-allow-credentials-header-in-the-response-is-which-must-be-true
Status: draft

![Django Logo](https://filipgorczynski.files.wordpress.com/2015/10/django-logo-positive.png?w=128){.alignleft .wp-image-1153 .size-thumbnail width="128" height="45"}Natknąłem się na problem z odpowiedzią z Django REST framework; zakładka **Sieć** w Chrome radośnie pokazuje, że żądanie GET do serwera zakończyło się pomyślnie, **Podgląd** odpowiedzi pokazuje zwrócony obiekt (dokładnie to czego oczekiwałem), ale część frontendowa trafia do funkcji obsługi błędu. Zakładka **Konsola** w Chrome wyrzuca na czerwono:

\[code\]

'Access-Control-Allow-Credentials' header in the response is '' which must be 'true'

\[/code\]

O ile w samym Django zainstalowana i skonfigurowana jest biblioteka [django-cors-headers](https://pypi.org/project/django-cors-headers/) to w odpowiedzi nadal brakowało: `Access-Control-Allow-Credentials`

Niestety`Access-Control-Allow-Credentials` nigdzie w Google nie dało się wyszukać (w kontekście django-cors-headers), a wszystkie wyniki dotyczyły problemów z `Access-Control-Allow-Origin`.

Okazuje się, że rozwiązaniem jest po prostu ustawienie zmiennej:

\[code language="python"\]

CORS\_ALLOW\_CREDENTIALS = True

\[/code\]

w pliku `settings.py`

**Wniosek:** Najlepszą dokumentacją jest sam kod. :)
