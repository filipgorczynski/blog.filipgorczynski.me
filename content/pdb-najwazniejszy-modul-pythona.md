Title: PDB - najważniejszy moduł Pythona
Date: 2015-08-08 11:16
Author: filipgorczynski
Category: Programowanie
Tags: debugger, ipdb, pdb, pdbpp, Python, traceback
Slug: pdb-najwazniejszy-modul-pythona
Status: draft

![python](https://filipgorczynski.files.wordpress.com/2015/04/python1.png){.alignleft .wp-image-1002 .size-full width="128" height="128"}

Pisząc w temacie o PDB jako najważniejszym module Pythona miałem na myśli jego istotność z punktu widzenia programisty. Także jeśli chodzi o sposób debugowania kodu. Jednym z najczęstszych sposobów "debugowania" jest wstawianie funkcji `print` w każde możliwe miejsce i "sprawdzanie" co zawiera kod w tym miejscu. To rozwiązanie jest znośne dla niewielkich i wyjątkowo prostych skryptów. W przypadku rozbudowanych aplikacji np. webowych sprawa się komplikuje ze względu na rosnący stos warstw - zanim dotrzemy do miejsca, w którym chcemy wyszukiwać/podejrzewamy błąd wiele się dzieje - konwersje adresów na ścieżki w aplikacji, cała komunikacja ze źródłem danych, generowanie szablonów - a to może mieć wpływ na nasz kod.

I właśnie tutaj z pomocą przychodzi nam moduł o wyjątkowo krótkiej nazwie pdb - Python Debugger. Jego niewątpliwą zaletą jest jego dostępność - jeśli mamy Pythona to najpewniej mamy też pdb.

Jego użycie w kodzie także jest banalne:

\[code language="python"\]  
import pdb; pdb.set\_trace()  
\[/code\]

Świetnym pomysłem jest ustawienie sobie szablonu dla 'pdb' + znak tabulacji, aby nasz edytor rozszerzał automatycznie do całej powyższej linijki.  
Co więcej, moduł pdb możemy uruchomić bezpośrednio w linii poleceń:

\[code language="text"\]  
\$ python -m pdb skrypt.py  
\[/code\]

Efektem wstawienia `import pdb; pdb.set_trace()` jest zatrzymanie się w tym miejscu wykonywania programu i zwrócenie sterowania do linii poleceń.

Najlepsze dopiero nadchodzi - ponieważ dostajemy kompletny debugger i poza najprostszym "printowaniem" zawartości zmiennych możemy się przemieszczać w dowolnym kierunku wykonywania kodu, wpływać na aktualny kod modyfikując zawartość zmiennych, zrzucenie całego stosu wywołań.

 

pdb doczekał się kilku następców - warto wspomnieć o pdbpp czy ipdb.  
Instalując pdbpp (pdb plus plus) otrzymujemy świetne polecenia dostępne od wersji 3 Pythona. Najczęściej używane z nich to sticky, ll (long list), pp (pretty print).
