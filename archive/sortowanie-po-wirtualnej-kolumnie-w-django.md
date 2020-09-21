Title: Sortowanie po wirtualnej kolumnie w Django
Date: 2018-03-07 17:14
Author: filipgorczynski
Category: Dobre praktyki, Programowanie
Tags: case, django, django rest framework, drf, order_by, when
Slug: sortowanie-po-wirtualnej-kolumnie-w-django
Status: archive

![Django Logo](https://filipgorczynski.files.wordpress.com/2015/10/django-logo-positive.png?w=128){.alignleft .wp-image-1153 .size-thumbnail width="128" height="45"}

Nie tak dawno temu w ramach jednego z zadań w Django było uporządkowanie wyników wg innego klucza niż najprostsze `ORDER BY`. Chodziło o nadanie pewnego rodzaju wag dla wierszy, które możliwie najlepiej wpasowały się w poniższe kryteria:

-   pierwszeństwo miały wiersze, które zawierały dokładne dopasowanie szukanej frazy
-   następnie wiersze, które od szukanej frazy się zaczynały
-   kolejno wiersze, które na podaną frazę się kończyły
-   kończąc wierszami, które podaną frazę zawierały w dowolnym miejscu
-   opcjonalnie pozostałe wiersze, jeśli `query` nie było jedynym kryterium filtrowania.

Przydatny okazał się poniższy kawałek kodu tworzący nieistniejącą w modelu `CaseWhen` columnę `exact` w postaci nowych warunków w obiekcie `QuerySet`  - po której następnie sortował:

https://gist.github.com/filipgorczynski/b7bf3367d832dfccff9eb9ad81ffa184

Dodatkowe porządkowanie wg kolumny `name` służy do alfabetycznego uporządkowania wierszy, którym została nadana ta sama waga.

Jeśli nie zostanie przekazana fraza do szukania (parametr `q)` używana jest fraza `beer`. Żeby mieć pogląd jakie rzeczywiście wyniki są zwracane - w migracji aplikacji `casewhen` dodaję kilka wierszy do bazy.

Rozwiązanie zostało wdrożone w ramach integracji z [Django REST Framework](http://www.django-rest-framework.org/), ale chodzi tylko o zasadę działania, więc kod można wykorzystać także bez DRF.

Oczywiście całość do przejrzenia bezpośrednio na [GitHub](https://github.com/filipgorczynski/django-virtual-column-sort).
