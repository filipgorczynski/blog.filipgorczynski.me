Title: Python i błąd R6034: An application has made an attempt to load the C runtime library incorrectly
Date: 2011-11-14 21:09
Author: filipgorczynski
Category: Programowanie, Rozwiązania, Systemy Operacyjne
Tags: An application has made an attempt to load the C runtime library incorrectly, C runtime library, Python, R6034, Windows 7
Slug: python-i-blad-r6034-an-application-has-made-an-attempt-to-load-the-c-runtime-library-incorrectly
Status: hidden

Od kilku dni próba uruchomienia jakiegokolwiek modułu Pythona pobranego z sieci kończyła się poniższym komunikatem:

\[code language="text"\]  
R6034  
An application has made an attempt to load the C runtime library incorrectly.  
Please contact the application's support team for more information.  
\[/code\]

Ciężko cokolwiek konkretnego na ten temat znaleźć w sieci, jednak warto spróbować poniższego rozwiązania. Trudno określić, co może być konkretną przyczyną takiego stanu rzeczy - problem pojawiał się praktycznie w każdym module - dlatego przedstawię wszystko co zrobiłem w kierunku poprawienia tego dziwnego zachowania.

1.  Usunięcie ze zmiennej systemowej PATH wszystkich nawiązań do innych wersji Pythona
2.  Instalacja MinGW oraz dodanie ścieżki do zmiennej systemowej PATH
3.  Dodanie zmiennej PYTHONPATH do zmiennych użytkownika
4.  Dodanie ścieżki do Pythona do zmiennej systemowej PATH

Opis dotyczy Windows 7 oraz Pythona w wersji 2.7.2 dla systemów 32 bitowych - istniał częsty problem z dostępnością modułów 64 bitowych.

1\. Usunięcie ze zmiennej systemowej PATH wszystkich nawiązań do innych wersji Pythona  
Na początku proponuję wyrzucić ze zmiennej PATH wszystkie odwołania do innych wersji Pythona. Może to być cokolwiek, np.: Panda3D czy Blender - dostarczany jest z nimi ich Python, co może powodować konflikty. Tymczasowo wszystkie odwołania wyrzucamy, w razie potrzeby jeśli wszystko przejdzie pomyślnie, będziemy mogli przywrócić dodatkowe wpisy w zmiennej PATH. Modyfikację zmiennych systemowych dokonać możemy w poniższy sposób:  
Wciskamy jednocześnie WIN+Pause/Break aby otworzyć informacje o Systemie Windows. W otwartym oknie wybieramy "Zaawansowane ustawienia systemu", zakładka "Zaawansowane" i przycisk "Zmienne środowiskowe".

2\. Instalacja MinGW oraz dodanie ścieżki do zmiennej systemowej PATH.  
Ze strony [SourceForge.net](http://sourceforge.net/projects/mingw/files/latest/download?source=files "SourceForge.net") pobieramy mingw-get-inst.exe który zatroszczy się o pobranie odpowiednich komponentów i całą instalację. Zakładam, że zostanie zainstalowany w C:\\MinGW. Do zmiennej systemowej PATH dodajemy na samym początku ścieżkę do instalacji MinGW (C:\\MinGW\\bin).

3\. Dodanie zmiennej PYTHONPATH do zmiennych systemowych.  
Okno edycji zmiennych wywołujemy jak w punkcie 1. W otwartym oknie w sekcji "Zmienne użytkownika dla \[nazwa użytkownika\]" jeśli nie istnieje, dodajemy nową zmienną PYTHONPATH i nadajemy jej wartość w postaci ścieżki instalacji Pythona - dla mnie jest to C:\\Python27\\.

4\. Dodanie ścieżki do Pythona do zmiennej systemowej PATH.  
Wszystko wykonujemy jak powyżej, jednak tym razem modyfikacja dotyczy zmiennej PATH/Path w sekcji "Zmienne systemowe". Dodajemy ścieżkę do naszej instalacji Pythona do tej zmiennej - najlepiej zaraz za ścieżką do MinGW.

Proszę o informację, czy pomogło w Waszym przypadku.
