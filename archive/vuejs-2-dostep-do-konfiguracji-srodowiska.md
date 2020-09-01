Title: VueJS 2 - dostęp do konfiguracji środowiska
Date: 2018-02-26 16:50
Author: filipgorczynski
Category: Dobre praktyki, Programowanie, Rozwiązania
Tags: config, development, env, production, vue, vuejs
Slug: vuejs-2-dostep-do-konfiguracji-srodowiska
Status: archive

![vuejs logo](https://filipgorczynski.files.wordpress.com/2017/11/vuejs_logo-e1519284315108.png){.alignleft .wp-image-1359 .size-full width="64" height="64"}W każdym co bardziej złożonym projekcie zachodzi potrzeba przechowywania różnych konfiguracji w zależności od środowiska: developerskiego, produkcyjnego, testowego, eksperymentalnego, niebieskiego i każdego innego. Oczywiście framework VueJS nie odstaje od normy i również oferuje możliwość takiej konfiguracji.

Na początku od razu zaznaczam, że zmiany w plikach konfiguracyjnych lub tworzenie nowych plików wymaga ponownego przebudowania i uruchomienia aplikacji - brak odzwierciedlania jakichkolwiek zmian w aplikacji może się okazać dość frustrujące jeśli zapomnimy o tej czynności - a często w konsoli widzimy, że się przebudowało - tylko jednak coś zmian z konfiguracji nie chwycił.

Konfiguracja dla różnych środowisk przechowywana jest domyślnie w 3 plikach (po utworzeniu czystego projektu):

https://gist.github.com/filipgorczynski/5dae2ae766277b4c721ff1bdb0fb1bb6

Wyżej wymienione pliki ładowane są dokładnie w tej kolejności ewentualnie rozszerzając lub nadpisując dotychczasowe wartości zmiennych, więc w czystej instalacji na początku wczytywany jest plik `prod.env.js`, stałe w nim zawarte nadpisywane są plikiem `dev.env.js` a te z kolei `test.env.js`. Proste i logiczne (...długie jak drzewo genealogiczne naszej rasy...)

Oczywiście nic nie stoi na przeszkodzie aby, jeśli zajdzie taka potrzeba, dodawać swoje pliki konfiguracyjne definiujące ustawienia dla nowych środowisk. Np. staging - dodając przykładowo plik `staging.env.js` o przykładowej treści:

https://gist.github.com/filipgorczynski/9f650395b25328cacd5a2c200f10a80d

i wtedy np. w pliku `dev.env.js` rozszerzamy środowisko `stagingEnv` - a nie `prodEnv` jak to jest domyślnie.

Samo ustawienie bieżącego środowiska - wg którego budowany i uruchamiany jest VueJS odbywa się w pliku `./projekt/src/main.js` w linijce:

https://gist.github.com/filipgorczynski/7f2c9207c08a855ee362d72448142718

chociaż lepszą z praktycznego punktu widzenia wersją byłaby poniższa:

https://gist.github.com/filipgorczynski/65edc1685f33839f7a6b80fe208d088f

I teraz, jeśli zawsze (we wszystkich środowiskach) potrzebujemy w aplikacji jakieś stałe to definiujemy je w pliku `prod.env.js` odpowiednio nadpisując w pozostałych plikach, jeśli oczywiście jakieś zmiany będą potrzebne.

W komponentach nic nie musimy importować, a dostęp do zmiennej jest wygląda w taki sposób: `process.env.API_URL`

Jeśli zbudujemy teraz projekt dla odpowiedniego środowiska, np.: dla produkcji `npm run build` otrzymamy katalog `dist`, w którym to znajduje się zbudowana chwilę temu aplikacja. Przechodząc w linii poleceń do tego katalogu `cd ./projekt/dist` i uruchamiając tymczasowy serwer `python3 -m http.server 8181`, w przeglądarce pod adresem `127.0.0.1:8181` powinna być dostępna nasza aplikacja - warto w tym miejscu potwierdzić różniące się między środowiskami zmienne, żeby nie było nieprzyjemnych niespodzianek.
