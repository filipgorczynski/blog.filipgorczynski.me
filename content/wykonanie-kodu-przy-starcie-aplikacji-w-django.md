Title: Wykonanie kodu przy starcie aplikacji w Django
Date: 2018-03-05 09:11
Author: filipgorczynski
Category: Programowanie, Rozwiązania
Tags: application, apps, django, format_html, has_change_permissions, has_delete_permission, migracja, ready, short_description
Slug: wykonanie-kodu-przy-starcie-aplikacji-w-django
Status: published

![Django Logo](https://filipgorczynski.files.wordpress.com/2015/10/django-logo-positive.png?w=128){.alignleft .wp-image-1153 .size-thumbnail width="128" height="45"}

Wielokrotnie zdarzyło mi się (i pewnie nie tylko mi) musieć uzupełnić jakimiś wartościami bazę danych w trakcie zmian w projekcie. Chodziło konkretnie o dane, które powinny się pojawić po wdrożeniu zmian i nie powinny dawać możliwości ich zmiany bądź usunięcia ze względu na potencjalny wpływ na działanie całej aplikacji.

Pierwszy pomysł tego rozwiązania to użycie migracji, jak w poniższym przykładzie:

https://gist.github.com/filipgorczynski/2c9b7f4f4db5adcf8827204e3a2bf676

Po wykonaniu migracji w bazie pojawią nam się wymagane wpisy. Jednak istotnym minusem tego rozwiązania jest to, że nadal można usunąć je bezpośrednio w bazie czy nawet w panelu administracyjnym Django i nie zostaną one odtworzone.

Kolejne podejście do problemu to przeniesienie kodu odpowiedzialnego za dodawanie wpisów do bazy do pliku `apps.py`, który uruchamiany jest przy starcie aplikacji - czyli praktycznie zawsze po restarcie serwera. Wrzucenie kodu do metody `ready` pozwoli nam obejść w całkiem elegancki sposób wspomniany wcześniej problem:

https://gist.github.com/filipgorczynski/fab9a8a0b6bdf3bb8981e0e90ab07978

Na co zwrócić musimy uwagę, w pliku \_\_init\_\_.py naszej aplikacji musimy jawnie wskazać ścieżkę do pliku konfiguracyjnego aplikacji, jako że plik ten jest opcjonalny:

https://gist.github.com/filipgorczynski/9c8f15c4b644e7d46c10f5aefb0f004d

Warto także zerknąć na kilka innych kawałków kodu, m. in. uniemożliwienie edytowania kluczowych informacji w panelu administracyjnym Django czy usuwanie tych danych. Zauważyć też można 2 drobne usprawnienia: 1) wizualna reprezentacja zapisanego koloru w panelu administracyjnym dzięki użyciu funkcji `format_html` oraz 2) zmiana tytułu kolumny w panelu administracyjnym poprzez właściwość `short_description`.

Kawałek kodu związany z synchronizacją modeli z bazą danych został zaczerpnięty ze [StackOverflow](https://stackoverflow.com/a/31847406/273283), a błąd dotyczący braku synchronizacji ujawnił się dopiero przy uruchomieniu testów.

Cały kod do pobrania i przejrzenia znaleźć można na [GitHub.](https://github.com/filipgorczynski/django-model-pre-data)
