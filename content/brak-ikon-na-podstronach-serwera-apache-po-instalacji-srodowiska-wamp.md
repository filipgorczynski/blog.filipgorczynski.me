Title: Brak ikon na podstronach serwera Apache po instalacji środowiska WAMP
Date: 2012-02-12 19:36
Author: filipgorczynski
Category: Rozwiązania, Systemy Operacyjne
Tags: Apache, brak ikon, conf, httpd-autoindex.conf, icons, ikony, MySQL, PHP, serwer, wamp, Windows
Slug: brak-ikon-na-podstronach-serwera-apache-po-instalacji-srodowiska-wamp
Status: published

[![](http://filipgorczynski.files.wordpress.com/2011/11/wamp-server-small.png?w=150 "wamp-server-small"){.alignleft .wp-image-476 width="90" height="90"}](http://filipgorczynski.files.wordpress.com/2011/11/wamp-server-small.png)Instalacja środowiska WAMP to dopiero początek. Z czasem przychodzi potrzeba konfigurowania i poprawiania jego sposobu działania. Jednym z problemów na które natrafiłem jest brak wyświetlania ikonek na podstronach serwera Apache podczas przeglądania struktury katalogów. W miejsce katalogów pojawiał się np. napis \[DIR\]. Same ikonki znaleźć możemy w katalogu serwera Apache, w moim przypadku jest to **C:\\wamp\\bin\\apache\\Apache2.2.17**. Oczywiście chodzi o katalog **icons**. Aby wyświetlać ikonki poprawnie - lub ewentualnie podmienić ikonki na własne - musimy poprawić ścieżkę do katalogu z ikonkami.

Plik z odpowiednią konfiguracją znajdziemy w C:\\wamp\\bin\\apache\\Apache2.2.17\\conf\\extra. Interesuje nas plik **httpd-autoindex.conf.**

\[code language="text"\]  
Alias /icons/ "C:/wamp/bin/apache/Apache2.2.17/icons/"

\<Directory "C:/wamp/bin/apache/Apache2.2.17/icons"\>  
Options Indexes MultiViews  
AllowOverride None  
Order allow,deny  
Allow from all  
\</Directory\>  
\[/code\]

Jedyną czynnością jaką musimy wykonać jest określenie w obu miejscach prawidłowych ścieżek do naszego katalogu z ikonkami oraz restart serwera.
