Title: Django - zwracanie pustego zbioru
Date: 2018-02-22 09:49
Author: filipgorczynski
Category: Bazy danych, Dobre praktyki, Programowanie, Rozwiązania
Tags: django, empty, filter, get_queryset, none, params, pusty wynik, queryset
Slug: django-zwracanie-pustego-zbioru
Status: published

![](https://filipgorczynski.files.wordpress.com/2015/10/django-logo-positive.png?w=150){.alignleft .wp-image-1153 .size-thumbnail width="150" height="52"}[QuerySet](https://docs.djangoproject.com/en/dev/ref/models/querysets/#django.db.models.query.QuerySet) to jedna z podstawowych klas, z którą będziemy pracować w trakcie pisania aplikacji w Django. Trafiłem ostatnio na problem, w którym należało zwrócić inne wyniki w zależności od tego, czy w żądaniu do serwera przesłana została zmienna w postaci pustego łańcucha znaków czy nie została wysłana w ogóle. Drobna różnica mająca ogromne znaczenie. Aby dokładniej zobrazować zaistniały problem postaram się to opisać z przykładami:

Żądany adres `http://127.0.0.1/` skutkuje zwróceniem wszystkich wyników - brak jakiegokolwiek filtrowania

Żądany adres `http://127.0.0.1/?q=` skutkuje brakiem wyników - filtrowanie jest, ale wyszukiwanie po pustym łańcuchu - który de facto pasuje do każdego dowolnego łańcucha znaków też zwróciłoby wszystkie wyniki - a tutaj potrzebowałem zwrócić pusty zbiór.

Żądany adres `http://127.0.0.1/q=abc` skutkuje zwróceniem wszystkich wyników, które w swojej treści zawierają łańcuch znaków "abc" - tutaj sprawa jest oczywista.

Ponieważ zwrócić musiałem obiekt QuerySet sprawa się komplikowała - a rozwiązaniem okazał się taki prosty kawałek kodu:

https://gist.github.com/filipgorczynski/84e8438972582e355e95e89f7a340c53
