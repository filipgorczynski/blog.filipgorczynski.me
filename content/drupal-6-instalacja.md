Title: Drupal 6 - Instalacja
Date: 2012-06-27 20:21
Author: filipgorczynski
Category: Programowanie, Rozwiązania
Tags: CMF, CMS, Drupal, Drupal 6, Garland, instalacja, moduły, Open Source, PHP
Slug: drupal-6-instalacja
Status: published

[![](http://filipgorczynski.files.wordpress.com/2011/11/drupal-logo-application_logo.png?w=131 "Drupal-Logo.application_logo"){.wp-image-473 .alignleft width="79" height="89"}](http://filipgorczynski.files.wordpress.com/2011/11/drupal-logo-application_logo.png)W związku z tym, że od pewnego czasu próbuję nauczyć się Drupala na poziomie "początkujący" postaram się opisywać różne rozwiązania potencjalnych problemów, konfiguracje oraz opisy modułów. Wpis ten (mam nadzieję, że kolejne się także pojawią) dotyczy aktualnie stabilnej wersji 6.25 ze względu na ogromną ilość materiałów i  modułów dostępnych w sieci. Proszę o wyrozumiałość, gdyż sam jestem na etapie nauki i do kompletnego opanowania tego CMSa dużo mi jeszcze brakuje. Powstające wpisy nie są kompletnym opisem możliwości Drupala ani rozwiązań użytych przy budowie stron - mają być dla mnie jedynie materiałem do przypominania róznych zagadnień.

Pierwszym krokiem, jaki należy wykonać jest sprawdzenie wymagań jakie stawia nam Drupal. Dokładne informacje znajdują się na stronie <http://drupal.org/requirements>. W skrócie są to:

Miejsce na dysku 15 MB - zalecałbym więcej (moduły, skórki, dodatkowe pliki),  
Serwer WWW:  Apache 1.3, Apache 2.x lub Microsoft IIS,  
Serwer baz danych: MySQL 4.1 lub nowszy,  
PHP 4.4.0 lub nowszy (5.2 zalecany) - warto także włączyć np.: APC  
[  
Jeśli spełniamy wymagania kroku pierwszego, to...]{style="text-align:justify;"}

[Drugi krok to pobranie aktualnej wersji Drupala ze strony projektu <http://drupal.org/project/drupal>. Adres ten używany jest także do określania lokalizacji modułów Drupala. Sam Drupal jak i jego moduły traktowane są w tym wypadku tak samo. Moduły dostępne są więc pod adresem http://drupal.org/project/NAZWA\_MODUŁU. Pobrane archiwum instalacyjne Drupala należy rozpakować w katalogu głównym serwera lub odpowiednio do katalogu - w moim przypadku jest to katalog drupal\_install (ścieżka *c:/htdocs/drupal\_install*).]{style="text-align:justify;"}

Tworzymy bazę danych (dowolny klient MySQL, np. phpMyAdmin), która zostanie wykorzystana przez Drupala - także nazwałem ją *drupal\_install*. Jako metodę porównywania napisów utf8\_general\_ci.

Instalacja CMS rozpoczyna się od przejścia pod adres http://localhost/drupal\_install, co zaowocuje pojawieniem się pierwszego ekranu, w którym będzie można wybrać język instalacji. Tutaj wybrałem język angielski jako domyślny. Wybranie innego języka do instalacji przedstawię w innym wpisie.

[![Drupal 6 - Instalacja: Ekran powitalny](http://filipgorczynski.files.wordpress.com/2012/04/step_01.png "Krok 1"){.aligncenter .size-full .wp-image-583 width="700" height="294"}](http://filipgorczynski.files.wordpress.com/2012/04/step_01.png)

Wybieramy więc opcję *"Install Drupal in English"*. Pojawia się kolejny ekran z nieprzyjemnym czerwonym komunikatem informującym o braku pliku z ustawieniami oraz przedstawia sposób jego utworzenia.

[![Drupal 6 - Instalacja: Plik z konfiguracją](http://filipgorczynski.files.wordpress.com/2012/04/step_02.png "Krok 2"){.aligncenter .size-full .wp-image-584 width="700" height="358"}](http://filipgorczynski.files.wordpress.com/2012/04/step_02.png)

Postępując zgodnie z zaleceniami przechodzimy do katalogu ./sites/default gdzie znajdziemy plik *default.settings.php*, który **zaleca** się skopiować pod nową nazwą *settings.php* oraz nadajemy mu prawa do zapisu przez serwer www (w Windowsie nie jest to wymagane). Następnie odświeżamy stronę lub klikamy w link na dole strony "try again" co przeniesie nas do ekranu konfiguracji bazy danych.

[![Drupal 6 - Instalacja: Konfiguracja bazy danych](http://filipgorczynski.files.wordpress.com/2012/04/step_03.png "Krok 3"){.aligncenter .size-full .wp-image-585 width="700" height="712"}](http://filipgorczynski.files.wordpress.com/2012/04/step_03.png)

Wypełniamy wymagane pola - w domyślnej instalacji MySQL wypełnić musimy tylko nazwę bazy danych (Database name) oraz nazwę użytkownika (Database username). Jeśli MySQL został wcześniej skonfigurowany, podajemy także odpowiednie hasło, ewentualnie port (jeśli inny niż domyślny 3306) oraz prefiks w tabeli, jeśli chcemy w jakiś sposób wyróżnić aktualną instalację Drupala lub jeśli wymaga tego środowisko. Jeśli wprowadzone informacje nie pozwolą połączyć się z bazą danych zostaniemy poproszeni o ich weryfikację.

W przedostatnim kroku określamy podstawową konfigurację strony - jej nazwę, główny adres e-mail oraz co najważniejsze nazwę i hasło głównego administratora. Jest to osoba o praktycznie nieograniczonej potędze w środowisku Drupala - użytkownik o ID = 1. Ze względów bezpieczeństwa warto określić dla niego skomplikowane hasło.  
Jedną z bardzo przydatnych opcji - zalecanych do włączenia - jest Clean URLs. Pozwala ona wykorzystać możliwości mod\_rewrite w serwerze Apache - co ostatecznie przekłada się na ładne adresy URL, np.: *serwer.com/to-jest-nowa-strona* zamiast serwer.com zamiast *serwer.com/?q=node/1.*

[![Drupal 6 - Instalacja: Konfiguracja strony](http://filipgorczynski.files.wordpress.com/2012/04/step_04.png "Krok 4"){.aligncenter .size-full .wp-image-586 width="700" height="1149"}](http://filipgorczynski.files.wordpress.com/2012/04/step_04.png)

Dobrze jest także pozostawić zaznaczoną opcję *Check for updates automatically* ponieważ dzięki temu Drupal co jakiś czas będzie informował nas o pojawiających się aktualizacjach - zarówno w samym jądrze Drupala jak i w zainstalowanych modułach. Kliknięcie przycisku *Save and continue* spowoduje wyświetlenie paska postępu informującego o  tworzeniu struktury bazy danych oraz przebiegu instalacji.

[![Drupal 6 - Instalacja: Podsumowanie instalacji](http://filipgorczynski.files.wordpress.com/2012/04/step_05.png "Krok 5"){.aligncenter .size-full .wp-image-587 width="700" height="300"}](http://filipgorczynski.files.wordpress.com/2012/04/step_05.png)

Gdy pasek postępu osiągnie magiczne 100% otrzymamy podsumowanie instalacji oraz możliwość odwiedzenia strony świeżo zainstalowanej wersji Drupala. Automatycznie zostaniemy także zalogowani na konto administratora (które utworzyliśmy w kroku *Configure site*).

[![Drupal 6 - Instalacja: Koniec instalacji](http://filipgorczynski.files.wordpress.com/2012/04/step_06.png "Krok 6"){.aligncenter .size-full .wp-image-588 width="700" height="603"}](http://filipgorczynski.files.wordpress.com/2012/04/step_06.png)

Dobrym pomysłem jest także usunięcie kilku plików z katalogu głównego Drupala, m. in.: INSTALL.mysql.txt, INSTALL.pgsql.txt, install.php.

Powyższy proces instalacji opisany jest także (po angielsku) w pliku INSTALL.txt .
