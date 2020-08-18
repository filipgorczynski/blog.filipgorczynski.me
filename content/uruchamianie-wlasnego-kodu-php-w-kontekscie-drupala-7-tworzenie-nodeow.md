Title: Uruchamianie własnego kodu PHP w kontekście Drupala 7 + tworzenie node'ów
Date: 2012-06-29 19:10
Author: filipgorczynski
Category: Programowanie, Rozwiązania
Tags: Drupal, drupal 7, kontekst, LANGUAGE_NONE, module_load_include, node, node_object_prepare, node_save, pathauto_cleanstring, tworzenie node
Slug: uruchamianie-wlasnego-kodu-php-w-kontekscie-drupala-7-tworzenie-nodeow
Status: published

Kilka dni temu pojawiła się potrzeba zaimportowania z przygotowanego pliku kilku wpisów do postaci node'ów. Oprócz oczywistego faktu wczytywania z pliku i modyfikacji treści należało uruchomić własny skrypt w sposób, który pozwalałby m.in. na korzystanie z modułów Drupala - stworzenie i zapisanie node'ów do bazy.

Samo uruchomienie własnego kodu PHP w kontekście Drupala 7 z dostępem do modułów wymaga poniższych linijek. Jak łatwo zauważyć, jest t kod żywcem skopiowany z pliku index.php z katalogu głównego Drupala.

\[code language="php"\]  
\<?php  
define('DRUPAL\_ROOT', getcwd());  
require\_once DRUPAL\_ROOT . '/includes/bootstrap.inc';  
drupal\_bootstrap(DRUPAL\_BOOTSTRAP\_FULL);  
\[/code\]

Kolejnym wyzwaniem jest stworzenie obiektu node'a oraz zapisanie go do bazy Drupala.

\[code language="php"\]  
\$node = new stdClass();  
\$node-\>type = 'content\_type'; // typ node'a jaki chcemy stworzyć (page, article, ...)  
\$node-\>title = \$details\['name'\];  
\$node-\>language = LANGUAGE\_NONE;  
\$node-\>field\_country\[LANGUAGE\_NONE\]\[0\]\['tid'\] = \$term-\>tid;  
\$node-\>field\_city\[LANGUAGE\_NONE\]\[0\]\['value'\] = \$\_details\['city'\];  
\$node-\>field\_street\[LANGUAGE\_NONE\]\[0\]\['value'\] = \$details\['street'\];  
\$node-\>field\_zip\[LANGUAGE\_NONE\]\[0\]\['value'\] = \$details\['zip'\];  
\$node-\>field\_website\[LANGUAGE\_NONE\]\[0\]\['url'\] = \$details\['www'\];  
\$node-\>field\_phone\[LANGUAGE\_NONE\]\[0\]\['value'\] = \$details\['phone'\];  
\$node-\>field\_email\[LANGUAGE\_NONE\]\[0\]\['value'\] = \$details\['email'\];

node\_object\_prepare(\$node);  
module\_load\_include('inc', 'pathauto');  
\$node-\>path\['alias'\] = preg\_replace('/\[\^a-z0-9\_\]/i', '-', pathauto\_cleanstring(\$title));  
node\_save(\$node);  
\[/code\]

Zasada jest dość prosta. Tworzymy prosty obiekt w PHP i nadajemy wszystkie wymagane wartości. Nazewnictwo pól w tworzonym obiekcie (np.: field\_email)  
musi być takie jak pól określanych przy tworzeniu danego typu treści.  
Stała [LANGUAGE\_NONE](http://api.drupal.org/api/drupal/includes!bootstrap.inc/constant/LANGUAGE_NONE/7) jest określa dowolny język (wartość 'und') i zaleca się zawsze podawanie tej wartości - oczywiście stosownie zmieniając ją, jeśli node ma zostać dodany w określonym języku.  
Funkcja node\_object\_prepare opakowuje obiekt w dodatkowe pola, które są wymagane do poprawnego zapisania node'a do bazy.  
Wykorzystując module\_load\_include - będącą funkcją znajdującą się w jądrze Drupala wczytujemy wymagane moduły - zabezpieczając się przed dostępem do funkcji, których definicji jeszcze nie udało się załadować do pamięci. W naszym wypadku wczytujemy moduł [Pathauto](http://drupal.org/project/pathauto) aby wygenerować alias dla naszego node'a - ładniej wyglądał będzie adres /nasz-nowy-node niż node/123.

Wykorzystane funkcje:  
[drupal\_bootstrap](http://api.drupal.org/api/drupal/includes!bootstrap.inc/function/drupal_bootstrap/7)  
[node\_object\_prepare](http://api.drupal.org/api/drupal/modules!node!node.module/function/node_object_prepare/7)  
[module\_load\_include](http://api.drupal.org/api/drupal/includes!module.inc/function/module_load_include/7)  
[pathauto\_cleanstring](http://drupal.org/project/pathauto)  
[node\_save](http://api.drupal.org/api/drupal/modules!node!node.module/function/node_save/7)
