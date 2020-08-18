Title: cd na sterydach - narzędzie do szybkiej zmiany katalogów w konsoli
Date: 2013-02-28 23:43
Author: filipgorczynski
Category: Dobre praktyki, Rozwiązania
Tags: cd, cmd, go-tool
Slug: cd-na-sterydach-narzedzie-do-szybkiej-zmiany-katalogow-w-konsoli
Status: published

Przeglądając dziś RSSy natrafiłem na genialne w swej prostocie narzędzie - przydatne szczególnie dla osób spędzających dużo czasu w konsoli. Narzędzie to nosi prostą nazwę "go-tool" i dostępne jest pod adresem <http://code.google.com/p/go-tool/>, a jego jedynym zadaniem jest skrócić czas dostępu do najczęściej odwiedzanych katalogów poprzez tworzenie skrótów.

Instalacja narzędzia jest dość prosta - o ile posiadamy zainstalowanego Pythona:  
1. Pobranie archiwum.  
2. Rozpakowanie.  
3. Przejście do rozpakowanego katalogu z poziomu konsoli.  
4. Uruchomienie polecenia: python setup.py install.  
5. Uruchomienie pliku go.py w nowo utworzonym katalogu: build/lib/go.py.  
6. Wybranie lokalizacji umieszczenia pliku go.bat poprzez wybranie z listy ścieżek.  
7. Konfiguracja skrótów już w trakcie korzystania z narzędzia.

Instrukcja obsługi dostępna jest po wywołaniu (<http://code.google.com/p/go-tool/wiki/GettingStarted>):

\[code language="text"\]  
\$ go --help  
Quick directory changing.

Usage:  
go \<shortcut\>\[/sub/dir/path\]    \# change directories  
\# same as "go -c ..."  
go -c\|-o\|-a\|-d\|-s ...           \# cd, open, add, delete, set  
go --list \[\<pattern\>\]           \# list matching shortcuts

Options:  
-h, --help                      print this help and exit  
-V, --version                   print verion info and exit

-c, --cd \<path\>                 cd to shortcut path in shell  
-s, --set \<shortcut\> \<dir\>      set a shortcut to \<dir\>  
-a, --add-current \<shortcut\>    add shortcut to current directory  
-d, --delete \<shortcut\>         delete the named shortcut  
-o, --open \<path\>               open the given shortcut path in  
explorer (Windows only)  
-l, --list \[\<pattern\>\]          list current shortcuts  
\[/code\]

Ciekawą opcją - dostępną tylko w Windows - jest przełącznik -o, który w momencie użycia:

\[code language="text"\]  
go -o \<SKRÓT\>  
\[/code\]

powoduje otwarcie okna w Eksplorerze Windows z katalogiem wskazywanym na \<SKRÓT\>.
