Title: Fedora OSError libgdal.so undefined symbol GEOSMakeValid_r
Date: 2019-11-14 11:13
Author: filipgorczynski
Category: Tech
Tags: dnf, dnf history, fedora, Fedora 29, gdal, gdal30, GEOSMakeValid_r, libgdal, OSError
Slug: fedora-oserror-libgdal-so-undefined-symbol-geosmakevalid_r
Status: archive

![Fedora Logo](https://filipgorczynski.files.wordpress.com/2019/11/fedora_logo-e1573723036788.png){.alignleft .wp-image-2381 .size-full width="128" height="128"}

Kilka dni temu nagle przestał mi się uruchamiać lokalnie projekt w Pythonie, rzucając nie do końca przyjemnym błędem: `OSError: /usr/gdal30/lib/libgdal.so.26: undefined symbol: GEOSMakeValid_r`. Pierwsze - z jakiegoś dziwnego powodu - co przyszło mi do głowy, to aktualizacja paczek Pythona. Ale nawet odtworzenie czystego venv-a nie rozwiązało problemu. <!--more-->No to nadszedł czas aby wysilić pozostałe dwa zwoje mózgowe trochę bardziej. OSError, OSError... co może być przyczyną błędu związanego z systemem operacyjnym? Ciężko jednoznacznie określić, ale może to system operacyjny? Warto popatrzeć, co tam się ostatnio zmieniło w ramach aktualizacji. Na szczęście Fedora urzekła mnie swoim menedżerem pakietów `dnf`, mimo że jeszcze rok temu `apt-get install` było dla mnie synonimem "dwukliku" na plikach \*.exe w systemach Windows.  
`dnf` jednak okazał się wyjątkowo pomocny w problematycznej kwestii. (Pamiętać musimy, że poniższe polecenia wywoływane są z wyższymi uprawnieniami, więc uruchamiamy je przez `sudo`):

https://gist.github.com/filipgorczynski/b6a361edbc264f8dc0187967b04b49bb

Do rzeczy. Skoro błąd dotyczył biblioteki `gdal`, to warto było sprawdzić szczegóły tej biblioteki zainstalowanej obecnie w systemie, czyli właśnie: `dnf list installed | grep -i gdal`. To dało wersję zainstalowanej biblioteki. Kolejne polecenie, `dnf history` pozwoliło podejrzeć ostatnio wykonywane akcje związane z aktualizacjami. Każda z tych akcji określana jest przez swój numerek, dzięki czemu byliśmy w stanie zajrzeć w szczegóły konkretnej aktualizacji `dnf history info <NUMER>`. Szaro na czarnym -(w zależności od ustawionych kolorów terminala) widać, z jakiej wersji biblioteka `gdal30` została podniesiona do nowszej. Aby wrzucić poprzednią wersję, wystarczyło rozkazać `dnf` instalację tej konkretnej, poprzedniej wersji `dnf install gdal30-libs-3.0.1-4.f29.x86_64`, co automagicznie pociągnęło w dół odpowiednie biblioteki zależne - czego szczegóły możemy ponownie zbadać poleceniem `dnf history`.
