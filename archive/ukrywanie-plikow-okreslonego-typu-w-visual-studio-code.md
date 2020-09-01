Title: Ukrywanie plików określonego typu w Visual Studio Code
Date: 2018-03-01 07:54
Author: filipgorczynski
Category: Dobre praktyki, Programowanie
Tags: TypeScript, ukrywanie plików, vscode
Slug: ukrywanie-plikow-okreslonego-typu-w-visual-studio-code
Status: archive

![](https://filipgorczynski.files.wordpress.com/2018/03/visual_studio_code_1-18_icon.png){.alignleft .wp-image-1664 .size-full width="128" height="128"}

O ile jestem wielkim zwolennikiem narzędzi ze stajni [JetBrains](https://www.jetbrains.com/) to od czasu do czasu - gdy potrzebuję zapisać coś na szybko - zdarza mi się korzystać z innego całkiem przyjemnego edytora - [VSCode](https://code.visualstudio.com/).

Narzędzie to ma to do siebie, że realne przyjemności zaczynają się dopiero, gdy skonfigurujemy je po swojemu i na szczęście sprawa jest dużo prostsza niż w Vim-ie :).

Po otwarciu w edytorze jakiegokolwiek projektu możemy zauważyć (albo raczej nie zauważyć), że w strukturze katalogów nie pojawiają się katalogi kilku powszechnie używanych systemów kontroli wersji: `.git`, `.svn`, `.hg`. Ukrywane są też pliki `.DS_Store`. Sprawa fajna i przydatna, ale jeśli zdarzy nam się pisać projekt, np. w Angularze to szybko dojdziemy do wniosku, że drzewo katalogów jest zaśmiecone i nieczytelne, m.in. ze względu na automatycznie generowane pliki - których w edytorze i tak najczęściej nie wykorzystamy.

Pozostaje nam zmienić odrobinę ustawienia edytora. Sama konfiguracja to po prostu edycja plików; dostęp do mich uzyskujemy poprzez `File > Preferences > Settings` (lub bezpośrednio z klawiatury `Ctrl + ,`).  
W lewym panelu znajdziemy listę ustawień domyślnych, z prawej - ustawienia użytkownika. I właśnie ta prawa część interesuje nas najbardziej. A to co chcemy zrobić to nadpisać wartość dla atrybutu `"files.exclude"`.

Z mojej strony chciałbym zaproponować ukrycie w drzewie katalogów dodatkowych 2 typów plików: `*.js.map` oraz plików `*.js` - o ile istnieje dla nich plik o takiej samej nazwie ale rozszerzeniu `*.ts`.

https://gist.github.com/filipgorczynski/244045502e30fad88e45f05dc63c477f

Dla kompletnie zielonych - interesują nas linie 9 i 10 :).

I jeszcze na koniec taka mała wskazówka, jeśli posiadamy otwartego, np. PyCharma (nie wiem jeszcze, czy inne IDE JetBrains posiadają taki sam skrót klawiaturowy) to - dzięki tylko 4 palcom - możemy otworzyć edytor-notatkę z konkretnym podświetlaniem składni bez tworzenia nowego pliku w strukturze projektu: `Ctrl + Alt + Shift + Insert`.
