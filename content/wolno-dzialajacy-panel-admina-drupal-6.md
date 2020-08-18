Title: Wolno działający panel admina Drupal 6
Date: 2012-01-29 13:50
Author: filipgorczynski
Category: Programowanie, Rozwiązania
Tags: Drupal, drupal długo wczytuje strony, firefox, hosts, ipv6, panel administratora, wolne działanie
Slug: wolno-dzialajacy-panel-admina-drupal-6
Status: published

[![](http://filipgorczynski.files.wordpress.com/2011/11/drupal-logo-application_logo.png?w=131 "Drupal-Logo.application_logo"){.alignleft .wp-image-473 width="47" height="54"}](http://filipgorczynski.files.wordpress.com/2011/11/drupal-logo-application_logo.png)

Od pewnego czasu katowałem się bardzo wolno działającym panelem administracyjnym Drupala w przeglądarce Firefox nawet przy czystej instalacji. Dzięki pomocy  [znajomego](http://niekoduj.pl/ "d3x") okazało się, że problemem jest ustawienie na podstronie konfiguracji odpowiedniej wartości dla zmiennej.  
W Firefoxie w pasku adresu wpisujemy  
\[code language="text"\]about:config\[/code\]

Potwierdzamy, że zgadzamy się z warunkami.  
Na otwartej podstronie wyszukujemy:  
\[code language="text"\]network.dns.disableIPv6\[/code\]

i zmieniamy ją na **TRUE**.  
Dodatkowo, spotkałem się także z zaleceniami wykomentowania (znak \#) linijki  
\[code language="text"\]  
::1 localhost  
\[/code\]

w pliku  
\[code language="text"\]  
c:\\Windows\\System32\\drivers\\etc\\hosts  
\[/code\]

Panel administracyjny powinien znacznie przyspieszyć.
