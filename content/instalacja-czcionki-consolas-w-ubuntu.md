Title: Instalacja fontu Consolas w Ubuntu
Date: 2017-06-16 06:33
Author: filipgorczynski
Category: Programowanie, Rozwiązania
Tags: Cabextract, Consolas, Consolas Bold Italic, Font, Font Manager, Ubuntu
Slug: instalacja-czcionki-consolas-w-ubuntu
Status: published

[![Ubuntu Logo](https://filipgorczynski.files.wordpress.com/2017/06/ubuntulogo.png?w=150){.alignleft .wp-image-1313 .size-thumbnail width="150" height="150"}](https://filipgorczynski.files.wordpress.com/2017/06/ubuntulogo.png)Instalacja fontu Consolas w Ubuntu została bardzo dobrze opisana na [kilku stronach](https://goo.gl/G5i0Yg), ale dla kompletności pozwolę sobie powtórzyć i skrócić.

Instalujemy odpowiednie pakiety

\[code language="bash"\]

\$ sudo apt-get install font-manager

\$ sudo apt-get install cabextract

\[/code\]

Do pliku `~/Pulpit/consolas.sh` wrzucamy:

\[code language="bash"\]

\#!/bin/sh  
set -e  
set -x  
mkdir temp  
cd temp  
wget http://download.microsoft.com/download/E/6/7/E675FFFC-2A6D-4AB0-B3EB-27C9F8C8F696/PowerPointViewer.exe  
cabextract -L -F ppviewer.cab PowerPointViewer.exe  
cabextract ppviewer.cab

\[/code\]

Otwieramy terminal `ctrl+alt+t` i przechodzimy do katalogu z naszym plikiem (Pulpit). Nadajmy prawo do wykonania `chmod +x consolas.sh` i uruchamiamy `./consolas.sh`.

Chwilę pomieli wyrzucając na ekran wykonywane instrukcje, zaciągnie archiwum CAB z fontami od Microsoftu i zapisze w katalogu `temp` na Pulpicie.

W terminalu wpisujemy `font-manager` i uruchomi się niewielkie okienko:

[![](https://filipgorczynski.files.wordpress.com/2017/06/zrzut-ekranu-z-2017-06-15-15-44-49.png?w=300){.alignleft .wp-image-1318 .size-medium width="300" height="215"}](https://filipgorczynski.files.wordpress.com/2017/06/zrzut-ekranu-z-2017-06-15-15-44-49.png)

 

 

 

 

 

 

 

Na dole z lewej strony znajdziemy 5 przycisków; pierwszy z prawej strony pozwoli nam zainstalować nowe fonty. Wybierzemy katalog `~/Pulpit/temp` gdzie powinien znaleźć kilka - między innymi te z rodziny Consolas. Wybieramy pliki pasujące do `CONSOLA*.TTF`, pozwalamy `Font Manager` na przeładowanie biblioteki i już powinniśmy mieć wybrane fonty w systemie.

Po zainstalowaniu wszystko jest niby super, ale gdy wejdziemy np. na StackOverflow zauważymy, że przykładowe źródła przedstawiane są fontem `"Consolas Bold Italic"` , która wskazuje na plik `CONSOLAZ.TTF` - mimo, że w CSS określone jest jasno "Consolas". Nie znam dokładnej przyczyny takiego zachowania, ale rozwiązaniem tego problemu jest po prostu zmiana nazw plików w katalogu `/home/USER/.fonts/Library/C/`z:

\[code language="text"\]

CONSOLAB.TTF  
CONSOLAI.TTF  
CONSOLA.TTF  
CONSOLAZ.TTF

\[/code\]

na

\[code language="text"\]

CONSOLASB.TTF  
CONSOLASI.TTF  
CONSOLAS.TTF  
CONSOLASZ.TTF

\[/code\]

czyli po prostu dodanie literki `S`w nazwie.
