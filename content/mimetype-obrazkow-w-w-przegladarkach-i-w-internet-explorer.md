Title: MimeType obrazków w przeglądarkach i w Internet Explorer
Date: 2010-05-02 13:11
Author: filipgorczynski
Category: Programowanie
Slug: mimetype-obrazkow-w-w-przegladarkach-i-w-internet-explorer
Status: published

Jakiś czas temu w związku ze zgłoszeniem przez klienta informacji, że "nie działa dodawanie obrazków", okazało się, że należy sprawdzać oddzielne mime-type dla przeglądarek oraz dla Internet Explorera (pomimo wysłania tego samego obrazka). Dlatego, aby w Internet Explorer działało dodawanie obrazków png czy jpg (czasem działało, czasem nie), należy użyć:

\[sourcecode language="php"\]  
\$aMimeTypes = array('image/gif', 'image/jpeg', 'image/png', 'image/pjpeg', 'image/x-png', 'image/bmp');  
\[/sourcecode\]

czyli jakiegoś tajemniczego image/pjpeg oraz image/x-png.

Dlaczego Microsoft zawsze lubi rzucać ludziom kłody pod nogi?
