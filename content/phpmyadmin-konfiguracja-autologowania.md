Title: PhpMyAdmin - konfiguracja autologowania
Date: 2012-09-08 20:36
Author: filipgorczynski
Category: Bazy danych, Dobre praktyki, Programowanie, Rozwiązania
Tags: autologin, autologowanie, config, host, konfiguracja, logowanie, logowanie automatyczne, password, phpmyadmin, pma, port, username
Slug: phpmyadmin-konfiguracja-autologowania
Status: published

![](http://filipgorczynski.files.wordpress.com/2012/08/phpmyadmin_logo.png?w=150 "PhpMyAdmin_logo"){.alignleft .wp-image-648 width="90" height="52"} Po ściągnięciu najnowszej wersji PhpMyAdmin praktycznie każda próba wejścia do panelu będzie wymagała od nas podania loginu i hasła. Na komputerach developerskich często jest to niewielkie utrudnienie. Aby logowanie następowało automatycznie należy:  
1. Otwieramy plik PhpMyAdmin/libraries/config.default.php, gdzie PhpMyAdmin to lokalizacja panelu na serwerze.  
2. Zmieniamy wartość:

\[code language="php"\]  
\$cfg\['Servers'\]\[\$i\]\['host'\] = 'localhost'; // lub odpowiednia nazwa hosta, o ile wcześniej nie była ustawiona  
\[/code\]

3\. Zmieniamy wartość:

\[code language="php"\]  
\$cfg\['Servers'\]\[\$i\]\['auth\_type'\] = 'config'; // wcześniej cookie  
\[/code\]

4\. Zmieniamy wartość:

\[code language="php"\]  
\$cfg\['Servers'\]\[\$i\]\['user'\] = 'mysql\_username'; // nazwa użytkownika, najczęściej root  
\[/code\]

5\. Zmieniamy wartość:

\[code language="php"\]  
\$cfg\['Servers'\]\[\$i\]\['password'\] = 'mysql\_password'; // hasło użytkownika, najczęściej użytkownika root  
\[/code\]

6\. Wchodzimy na stronę PhpMyAdmin na naszym serwerze i powinniśmy automatycznie być zalogowani.
