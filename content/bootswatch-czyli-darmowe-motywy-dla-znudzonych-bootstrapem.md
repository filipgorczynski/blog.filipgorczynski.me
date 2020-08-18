Title: Bootswatch, czyli darmowe motywy dla znudzonych Bootstrapem
Date: 2018-02-16 18:09
Author: filipgorczynski
Category: Programowanie, Rozwiązania
Tags: angular, bootstrap, bootswatch, flatly, motyw, ng, themes
Slug: bootswatch-czyli-darmowe-motywy-dla-znudzonych-bootstrapem
Status: published

![](https://filipgorczynski.files.wordpress.com/2018/02/angular_full_color_logo.png){.alignleft .wp-image-1599 .size-full width="120" height="128"}

Ciężko znaleźć w branży webowej programistę, który nie słyszał o [Bootstrapie](https://getbootstrap.com/). Podejrzewam jednak, że mniej osób słyszało o kolekcji darmowych motywów - [Bootswatch](https://bootswatch.com/).  
Na przykładzie prostej aplikacji w Angularze chciałbym przedstawić instalację jednego z tych darmowych motywów.

Początek nie odbiega od tego, co zwykle robimy. Generujemy czysty projekt Angular, np. narzędziem [ng-cli](https://cli.angular.io/), dodajemy wymagane zależności i instalujemy paczki potrzebne do uruchomienia projektu.

https://gist.github.com/filipgorczynski/f5e6b1ca9ad3becc4783cf2ec44bb7c8

Po krótkiej chwili, gdy otrzymamy informację, że wszystkie zależności zostały zainstalowane poprawnie dodajemy styl wybranego przez nas motywu do globalnych stylów ładowanych w aplikacji - w pliku `.angular-cli.json` zmieniamy sekcję `styles`:

https://gist.github.com/filipgorczynski/b2020c9abbc47946be3c4cfbd2da8a4c

Gdyby nie było to widoczne na pierwszy rzut oka, użyłem motywu [flatly](https://bootswatch.com/flatly/).

Oczywiście, żeby nie było zbyt pięknie musiałem też "podkraść" fragment zawartości pliku `custom.min.css` - był w postaci skompresowanej, ale po rozplątaniu dostajemy mniej więcej coś takiego jak poniżej. W dużej mierze chodzi o odstępy pionowe pomiędzy komponentami.

https://gist.github.com/filipgorczynski/0874521e5849d6701e929351bd29f392

"Zainspirowany" szablonem HTML z przykładu tego motywu wybrałem tylko kilka jego fragmentów żeby pokazać, że jednak coś tam działa:

https://gist.github.com/filipgorczynski/883ac210c08e3b40d1a6a102ee7976e3

I to by było wszystko co należy zrobić. Oczywiście można pokusić się o dodanie kilku plików JavaScript, które obsługują takie działania jak *popovery* czy okienka modalne, ale to może innym razem.

Całość dostępna w repozytorium [GitHub](https://github.com/filipgorczynski/ng-bootswatch-boilerplate).
