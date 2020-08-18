Title: Dodawanie pliku .xxx w Windows
Date: 2015-02-10 20:09
Author: filipgorczynski
Category: Rozwiązania, Systemy Operacyjne
Tags: .gitignore, .hgignore, .htaccess, nowy plik, plik, Windows
Slug: dodawanie-pliku-xxx-w-windows
Status: published

Często spotykam się z różnymi proponowanymi obejściami (tworzenia z linii poleceń) albo tłumaczeniami, że jest to wyjątkowo trudne podczas próby stworzenia w Windows pliku, którego nazwa znajduje się dopiero po kropce. W systemach pochodnych od Unix można to zrobić poprzez proste:

\[code language="text"\]touch .gitignore\[/code\]

\[code language="text"\]touch .htaccess\[/code\]

Windows domyślnie nie dostarcza narzędzia touch, a próba utworzenia pliku o podanej wcześniej nazwie kończy się nieprzyjemnym komunikatem *"Zmień nazwę"* - *"Wpisz nazwę pliku"*.

**Rozwiązanie:**

Wpisując nazwę pliku dodajemy kropkę na końcu nazwy pliku, przykładowo przy tworzeniu nowego pliku (klikamy prawym przyciskiem myszy \> Nowy \> Dokument Tekstowy):

\[code language="text"\].gitignore.\[/code\]

Zostaniemy zapytani, czy chcemy zmienić nazwę pliku - oczywiście, że tak.

Powstanie plik .gitignore

Dlaczego? Nie mam bladego pojęcia.
