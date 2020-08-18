Title: Instalować można tylko jeden produkt Adobe w tym samym czasie. Przed rozpoczęciem instalacji programu Adobe Photoshop CS3, proszę dokończyć poprzednią instalację.
Date: 2010-10-30 20:08
Author: filipgorczynski
Category: Rozwiązania
Slug: instalowac-mozna-tylko-jeden-produkt-adobe-w-tym-samym-czasie-przed-rozpoczeciem-instalacji-programu-adobe-photoshop-cs3-prosze-dokonczyc-poprzednia-instalacje
Status: published

Istnieje niewielkie prawdopodobieństwo, że kiedyś uda Wam się otrzymać komunikat **Instalować można tylko jeden produkt Adobe w tym samym czasie. Przed rozpoczęciem instalacji programu Adobe Photoshop CS3, proszę dokończyć poprzednią instalację.** podczas instalacji programy Adobe Photoshop CS3 Extended PL (nie wiem, czy inne wersje/języki też robią takie problemy).  
W moim przypadku pomogły poniższe zabiegi.  
Kilka programików nam potrzebnych podczas sprzątania (przydałoby się takie narzędzie do sprzątania pokoju ;)):

-   [Revo Uninstaller](http://www.revouninstaller.com/revo_uninstaller_free_download.html)
-   [CCleaner](http://www.piriform.com/)
-   [Windows Installer CleanUp](http://www.sciagnij.pl/programy/p/Windows-Narzedzia-Usuwanie_programow-Windows_Installer_CleanUp/9263)

Oczywiście, zawsze warto rozejrzeć się za aktualniejszymi wersjami. Powyższe oprogramowanie instalujemy.  
Kolejno wykonujemy.

1.  Kopiujemy zawartość płyty z Adobe Photoshop CS3 na dysk, powiedzmy do katalogu *c:/temp/*; wydaje mi się, że tak będzie najbezpieczniej
2.  Uruchamiany Windows Installer CleanUp
3.  Wyszukujemy na liście pozycje związane z Photoshop; jeśli nie ma szukamy Adobe Setup. [![Windows Install CleanUp - Adobe Setup](http://filipgorczynski.files.wordpress.com/2010/10/2010-10-30_194010.jpg?w=150 "Windows Install CleanUp - Adobe Setup"){.alignnone .size-thumbnail .wp-image-135 width="150" height="148"}](http://filipgorczynski.files.wordpress.com/2010/10/2010-10-30_194010.jpg) i [![Windows Install CleanUp - Adobe Photoshop CS3](http://filipgorczynski.files.wordpress.com/2010/10/2010-10-30_193935.jpg?w=150 "Windows Install CleanUp - Adobe Photoshop CS3"){.alignnone .size-thumbnail .wp-image-136 width="150" height="148"}](http://filipgorczynski.files.wordpress.com/2010/10/2010-10-30_193935.jpg)
4.  Oczywiście pozycje te usuwamy klikając Remove
5.  Odpalamy program Revo Uninstaller, czekamy aż wypełni się lista aplikacji, wyszukujemy Adobe Photoshop CS3 i prawym przyciskiem myszy - Odinstaluj [![Revo Uninstaller - Adobe Photoshop CS3](http://filipgorczynski.files.wordpress.com/2010/10/2010-10-30_195157.jpg?w=150 "Revo Uninstaller - Adobe Photoshop CS3"){.alignnone .size-thumbnail .wp-image-137 width="150" height="55"}](http://filipgorczynski.files.wordpress.com/2010/10/2010-10-30_195157.jpg)
6.  Po zakończeniu działań Revo Uninstallera, wyrzucenia wszystkich plików i wpisów z rejestru, na wszelki wypadek uruchamiamy jeszcze CCleaner [![CCleaner - czyszczenie rejestru](http://filipgorczynski.files.wordpress.com/2010/10/2010-10-30_195605.jpg?w=82 "CCleaner - czyszczenie rejestru"){.alignnone .size-thumbnail .wp-image-138 width="82" height="150"}](http://filipgorczynski.files.wordpress.com/2010/10/2010-10-30_195605.jpg)
7.  Trzej królowie <kbd>CTRL+ALT+DEL</kbd>, na wszelki wypadek - szukamy wpisu *msiexec.exe*, który oczywiście ubijamy
8.  Odpalamy ponownie instalację Adobe Photoshop CS3 i powinno wszystko bez problemów przejść. Na końcu uruchamiamy komputer ponownie i wracamy do gier :)

Życzę powodzenia.
