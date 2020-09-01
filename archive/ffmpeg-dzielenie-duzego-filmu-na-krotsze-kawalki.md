Title: ffmpeg - dzielenie dużego filmu na krótsze kawałki
Date: 2017-06-14 07:57
Author: filipgorczynski
Category: Programowanie, Rozwiązania, Systemy Operacyjne
Tags: cięcie filmu, ffmpeg, konwersja wideo, podział filmu
Slug: ffmpeg-dzielenie-duzego-filmu-na-krotsze-kawalki
Status: archive

[![ffmpeg](https://filipgorczynski.files.wordpress.com/2017/06/ffmpeg-logo.png?w=150){.alignleft .wp-image-1307 .size-thumbnail width="150" height="108"}](https://filipgorczynski.files.wordpress.com/2017/06/ffmpeg-logo.png)Z nieznanych mi do końca przyczyn tańsze odtwarzacze DVD (ale te posiadające port USB) nie radzą sobie za dobrze z systemami plików innymi niż FAT32. Oczywiście, nie byłoby to aż tak problematyczne, gdyby nie fakt, że w takim systemie plików nie da się umieścić pliku większego niż 4 GB. Jak wiadomo filmy w dobrej jakości to dużo gigabajtów. Jedną z alternatyw jest podłączenie do telewizora laptopa lub Raspberry Pi i odtwarzanie bezpośrednio z tego urządzenia - większość ludzi posiada już NTFS lub ext3/ext4, więc większy plik nie będzie problemem.

Gdy jednak mimo wszystkich sprzyjających okoliczności nadal chcielibyśmy podzielić plik z filmem (np. gdybyśmy chcieli go na dyskietkach wysłać do ZUS) z pomocą przyjść może narzędzie `ffmpeg` i poniższe polecenia:

[code language="bash"]

$ ffmpeg -i ~/The.Greatest.Movie.Ever.Sold.avi -ss 00:00:00 -t 01:00:00 -async 1 -c copy ~/The.Greatest.Movie.Ever.Sold-part.1.avi  
$ ffmpeg -i \~/The.Greatest.Movie.Ever.Sold.avi -ss 01:00:00 -t 01:55:23 -async 1 -c copy \~/The.Greatest.Movie.Ever.Sold-part.2.avi

[/code]

Parametr `-ss HH:MM:SS` określa początek - moment, od którego chcemy zacząć wycinać.

Parametr `-t HH:MM:SS` określa nam czas, jaki chcemy wyciąć. W przypadku pierwszego polecenia będzie to 1 godzina od początku filmu.

Parametr `-async` to synchronizacja audio - wartość 1 wg dokumentacji oznacza "wypełnienie i przycinanie" - w praktyce jak to działa - nie mam pojęcia :).

Parametr `-c` określa kodek, w przypadku podania wartości `copy` zostanie on skopiowany z pliku źródłowego. O ile dobrze kojarzę, możemy to zamienić na odpowiednie -`vcodec` i -`acodec`.

Inna sprawa, że nie każdy odtwarzacz DVD radzi sobie z różnymi formatami plików (np. mkv, mp4) i aby skonwertować plik z filmem z formatu MP4 do AVI może się przydać polecenie:

\[code language="bash"\]

\$ ffmpeg -i \~/The.Greatest.Movie.Ever.Sold.mp4 -qscale 0 -vcodec mpeg4 -acodec ac3 \~/The.Greatest.Movie.Ever.Sold.avi

\[/code\]

gdzie parametr `-i` określa nasz plik wejściowy, `-qscale 0` to ewentualna utrata jakości - nas interesuje konwersja bezstratna. `-vcodec mpeg4` to kodek wideo i `-acodec ac3` to kodek audio. Nie możemy podać wartości `copy` jak w poprzednich poleceniach ponieważ konwertujemy na inny format pliku, a przez to interesują nas inne kodeki. Na końcu podajemy nazwę pliku wyjściowego, którego docelowy rozmiar zapewne będzie trochę większy od pliku wejściowego.

Samo ffmpeg to nie tylko cięcie czy konwersja filmów, dlatego po więcej możliwości warto skierować się do pomocy tego narzędzia: `ffmpeg -h full` lub stronę projektu [ffmpeg.org](https://ffmpeg.org/)
