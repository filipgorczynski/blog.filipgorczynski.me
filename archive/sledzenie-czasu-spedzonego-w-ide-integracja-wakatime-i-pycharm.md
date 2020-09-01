Title: Śledzenie czasu spędzonego w IDE - integracja WakaTime i PyCharm
Date: 2018-03-01 08:27
Author: filipgorczynski
Category: Dobre praktyki, Programowanie, Rozwiązania
Tags: PyCharm, timetracking, wakatime, śledzenie czasu
Slug: sledzenie-czasu-spedzonego-w-ide-integracja-wakatime-i-pycharm
Status: archive

![WakaTime Logo](https://filipgorczynski.files.wordpress.com/2018/03/wakatime_logo1.png){.alignleft .wp-image-1679 .size-full width="128" height="128"}

Nie tak dawno temu w ramach kolejnych prób ze śledzeniem swojego czasu spędzonego na pisaniu kodu trafiłem na [WakaTime](https://wakatime.com/).  
Dla moich potrzeb wystarczyła instalacja w PyCharm, ale inne wspierane środowiska programowania wraz z instrukcjami instalacji przejrzeć możemy na stronie [WakaTime Editors](https://wakatime.com/editors).

Sama instalacja w PyCharm to tak naprawdę znalezienie i zainstalowanie wtyczki o nazwie - zgadza się - WakaTime. W opisie wtyczki jest dokładna instrukcja instalacji.

I w sumie to tyle. Po kilku godzinach pisania kodu możemy wejść na [dashboard](https://wakatime.com/dashboard), gdzie zaprezentują nam się ładne statystyki, jakich języków używaliśmy najczęściej, w jakich projektach czy ile czasu danego dnia spędziliśmy w IDE.

Jak spora część narzędzi online także to ma swoje plany cenowe. Nam może wystarczyć darmowy, który pozwala m. in. na statystyki z ostatnich 2 tygodni. Otrzymujemy jednak narzędzie [wakadump](https://github.com/wakatime/wakadump), które pozwala nam pobierać statystyki na wypadek, gdybyśmy chcieli je dalej wykorzystać.

Warto wspomnieć, że gdy z jakichś powodów coś się posypie ze środowiskiem lub będziemy chcieli zmienić klucz API to zmiany wystarczy wprowadzić w pliku: `~/.wakatime.cfg`
