Title: Flask - podstawy programowania webowego w Pythonie
Date: 2015-07-29 20:28
Author: filipgorczynski
Category: Tech
Tags: flask, framework, Python
Slug: flask-podstawy-programowania-webowego-w-pythonie
Status: draft

![Flask - logo](https://filipgorczynski.files.wordpress.com/2015/04/flask.png?w=150){.alignleft .wp-image-969 .size-thumbnail width="150" height="134"}Od zawsze z dużym dystansem podchodziłem do mikroframeworków. Rozwiązania oparte na bibliotekach tworzonych przez różnych ludzi/zespoły były dla mnie synonimem braku jakości/spójności. Kilka miesięcy temu, gdy już zapadła poważna decyzja i postanowiłem przesiąść się na Python na dzień dobry zostałem wrzucony do mikroframeworka Flask - w celu wdrożenia się w nowy sposób myślenia. Do tej pory słyszałem o Django jako o dominującym rozwiązaniu wśród frameworków webowych w Pythonie - out of the box dostajemy ORM, system szablonów, routing, obsługę sesji, użytkowników, migracji i ogólnie wszystkiego co nam tylko przyjdzie do głowy. Trochę czasu z Flaskiem przekonało mnie, że małe rozwiązania nie koniecznie muszą być złe.

W ramach wpisów dotyczących Flaska chciałbym przedstawić ogólnodostępne i najczęściej używane rozszerzenia tego frameworka:

-   Routing Werkzeug i szablony Jinja2
-   Flask-WTF - formularze
-   Flask-SQLAlchemy - bazy danych
-   Flask-Login - uwierzytelnianie użytkowników
-   Flask-Mail - wysyłanie maili
-   Flask-Assets - zarządzanie zasobami (CSS, JavaScrip, itp)
-   Flask-Babel - aplikacje wielojęzyczne
-   Flask-Admin - panel administracyjny
-   Flask-Uploads - upload plików

W ramach tego artykułu chciałbym opisać podstawy Flaska czyli tak naprawdę routing i proste szablony, które mam nadzieję staną się bazą do bardziej rozbudowanych aplikacji oraz własnych eksperymentów.

Zaczynamy - środowisko wirtualne i instalacja Flask
---------------------------------------------------

Tak jak ma to miejsce w przypadku większości projektów, najlepiej utworzyć środowisko wirtualne, aby nie zaśmiecać systemowej instalacji Pythona kolejnymi modułami.  
Poniżej przedstawiam sposób w jaki zazwyczaj do tego podchodzę przy prostych projektach oraz ewentualnych eksperymentach z kodem. (Znak \$ oznacza w tym wypadku systemowy znak zachęty)

\[code language="bash"\]  
\$ mkdir flask-wykop  
\$ cd flask-wykop  
\$ virtualenv --no-site-packages venv/wykop  
New python executable in venv/wykop\\Scripts\\python.exe  
Installing setuptools................done.  
Installing pip...................done.  
\$ mkdir src  
\$ cd src  
\$ git init  
\[/code\]

W zależności od wykorzystywanego systemu:  
Windows

\[code language="bash"\]  
\$ ..\\venv\\wykop\\Scripts\\activate  
\[/code\]

Linux

\[code language="bash"\]  
\$ source ../venv/wykop/bin/activate  
\[/code\]

W chwili obecnej powinniśmy mieć w linii poleceń uaktywnione środowisko wirtualne odseparowane od systemowej instalacji; dzięki parametrowi --no-site-packages ignorujemy katalog site-packages z systemowej instalacji Pythona.  
W ramach virtualenva dobrym pomysłem jest także wykonanie aktualizacji pip:

\[code language="bash"\]  
\$ pip install --upgrade pip  
\[/code\]

lub

\[code language="bash"\]  
\$ python -m pip install --upgrade pip  
\[/code\]

W Windows mogą być niewielkie problemy związane z uprawnieniami wymaganymi do aktualizacji, ale można to szybko ominąć uruchamiając cmd.exe na prawach Administratora: prawym przyciskiem myszy na programie "Wiersz polecenia" i "Uruchom jako Administrator" - oczywiście przed aktualizacją trzeba jeszcze uaktywnić środowisko wirtualne.

Następnym krokiem jest instalacja bazy naszej aplikacji - frameworka Flask.

\[code language="bash"\]  
\$ pip install flask  
\[/code\]

Pierwsza aplikacja wykorzystująca framework Flask
-------------------------------------------------

Cały kod naszej aplikacji (oczywiście kod pisany przez nas) umieścimy w katalogu **src.** Jest to kwestia upodobań, a nie standardów. Katalog ten może mieć dowolną nazwę, ale przyjmijmy, że będzie to **src**.  
W tej chwili stajemy przed istotną decyzją, ponieważ w ramach prostych aplikacji wykorzystać 3 sposoby budowy aplikacji:  
Pierwszy sposób - gdy nasza aplikacja będzie tak prosta, że jej kompletny kod można umieścić w jednym pliku.  
Drugi sposób - gdy nasza aplikacja będzie mogła być wykorzystana jako moduł w innej, większej aplikacji.  
Trzeci sposób - wykorzystujemy Flask Blueprints w celu budowy aplikacji składającej się z wielu niezależnych modułów - to spróbuję omówić w innym wpisie.

Najprostszą z możliwych struktur plików i katalogów aplikacji Flask prezentuje się jak poniżej:

[![project\_structure](https://filipgorczynski.files.wordpress.com/2015/07/project_structure1.png){.alignleft .size-full .wp-image-1111 width="276" height="84"}](https://filipgorczynski.files.wordpress.com/2015/07/project_structure1.png)

 

 

 

Zawartość strony pobierzemy wykorzystując bibliotekę Pythona - [requests](http://docs.python-requests.org/en/latest/), natomiast treść tej strony będziemy parsować dokument HTML przyda nam się [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/). To wszystko co będzie nam potrzebne.

\[code language="bash"\]  
\$ pip install beautifulsoup  
\$ pip install requests  
\[/code\]

W ulubionym edytorze otwieramy plik run.py. Rozpoczynamy od najprostszej wersji:

\[code language="python"\]  
from flask import Flask  
app = Flask(\_\_name\_\_)

\@app.route('/')  
def hello\_world():  
return 'Witaj swiecie!'

if \_\_name\_\_ == '\_\_main\_\_':  
app.run(debug=True)  
\[/code\]

Już tłumaczę. Na początku - importujemy klasę aplikacji frameworka Flask; następnie wykorzystujemy tą klasę do utworzenia obiektu aplikacji.

Ale po co w ogóle przekazujemy \_\_name\_\_? Otóż jest to sposób na rozróżnienie aplikacji w zależności od sposobu uruchomienia \[WHAAT?!!\]. Jeśli będzie to prosta aplikacja to w \_\_name\_\_ będziemy mieć nazwę aktualnie uruchomionego pliku. Jeśli natomiast nasza aplikacja będzie budowana jak pakiet - wówczas \_\_name\_\_ przyjmie nazwę tego pakietu.

Następnie określamy widok definiując funkcję - w naszym przypadku hello\_world(). Dostęp do tego widoku będzie realizowany dzięki dekoratorowi \@app.route('/'). W dekoratorze widzimy, że wchodząc na adres http://127.0.0.1:5000/ uruchomi się funkcja hello\_world(). Jako jedyne działanie tej funkcji to zwrócenie łańcucha znaków. Oczywiście nie jest to nic ambitnego, ale na początek wystarczy. W bardziej rozbudowanych aplikacjach znajdą się tam różniste rzeczy: walidacje formularzy, pobieranie i zapisywanie danych, współpraca z bazą danych i ostatecznie np.: renderowanie dowolnej odpowiedzi - HTML, JSON, XML - cokolwiek tylko przyjdzie nam do głowy.

Instrukcja warunkowa uruchamia wcześniej utworzoną aplikację jeśli skrypt zostanie uruchomiony w linii poleceń. W trakcie budowy naszej aplikacji przydatna może okazać się opcja debug ustawiona na True - w razie wystąpienia błędu pojawi nam się bardzo ładny backtrace, a zmiany w plikach często nie wymagają ponownego uruchomienia serwera. Najczęściej restart wymagany będzie w momencie dodawania plików do projektu.

Sprawdźmy jak to działa. W konsoli - tam gdzie instalowaliśmy biblioteki Pythona wpisujemy:

\[code language="bash"\]  
\$ python run.py\</pre\>  
\<pre\> \* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)  
\[/code\]

W przeglądarce wchodzimy na adres http://127.0.0.1:5000/ i powinniśmy zobaczyć komunikat zwrócony przez nasz widok - Witaj swiecie.

Aby nie pisać wszystkiego od zera, wykorzystamy szablon dostępny pod adresem [http://www.initializr.com/](http://www.initializr.com/builder?izr-responsive&jquerymin&h5bp-iecond&h5bp-chromeframe&h5bp-analytics&h5bp-favicon&h5bp-appletouchicons&modernizrrespond&h5bp-css&h5bp-csshelpers&h5bp-mediaqueryprint&izr-emptyscript). Z pobranego archiwum wybieramy katalogi css, img, fonts oraz js oraz wszystkie pliki z pominięciem plików \*.html i kopiujemy je do katalogu *static* w naszej strukturze katalogów. Pliki index.html i 404.html kopiujemy do katalogu *templates*.  
W pliku run.py musimy jeszcze dodać informację o szablonie, który chcemy wyrenderować - w naszej sytuacji będzie to templates/index.html.

Zatrzymujemy serwer (CTRL+C) oraz ponownie go uruchamiamy.

 
