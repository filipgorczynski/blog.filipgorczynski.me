Title: Język Python jest lepszy od C++ a 42 jest lepsze od czerwonego
Date: 2018-03-06 10:02
Author: filipgorczynski
Category: Life, Programowanie
Slug: jezyk-python-jest-lepszy-od-c-a-42-jest-lepsze-od-czerwonego
Status: draft

Od kiedy tylko bywam w Internecie - a będzie co najmniej dekada - we wszystkich miejscach w jakikolwiek sposób związanych z programowaniem natrafić można na pytania:

-   Jaki jest najlepszy język programowania?
-   Jakie jest najlepsze środowisko do programowania w języku X?
-   Jaki jest najlepszy framework?
-   Jak mam uczyć się programowania?
-   Chcę napisać Facebooka. Jak zacząć?

... i wiele przeróżnych odmian powyższych pytań.<!--more-->

Takie pytania z reguły zadają osoby bardzo początkujące, które jeszcze nie napisały linijki kodu albo napisały tego kodu na tyle mało, aby nie mieć jeszcze wyrobionej opinii. Jeśli ktoś zadaje w sieci po raz 100 to samo ogólne pytanie bez najmniejszej chociażby chęci wyszukania tego na własną - nie jest chyba jeszcze gotowy na to, aby zająć się programowaniem na poważnie.

O ile "Jaki język programowania jest najlepszy?" jest słabym pytaniem, to "Jaki język programowania będzie najlepszy do pisania gier w przeglądarce" będzie już dawało jakiś konkretny obraz odpowiadającym. Chociaż na takie pytanie też już odpowiedzi da się względnie łatwo znaleźć.

Spróbuję jednak odpowiedzieć na te pytania w sposób, który **według mnie** jest tym prawidłowym. ???

W telegraficznym skrócie, w naszej branży odpowiedź zawsze brzmi: **to zależy**.

Jaki jest najlepszy język programowania?
----------------------------------------

Najlepszy do czego? Co chcesz osiągnąć dzięki swojemu rozwiązaniu? Czy do rozwiązania masz  aplikację webową? A może musisz zaprogramować Raspberry PI? A może chcesz przetwarzać tekst? A może...

Nie ma jednej i poprawnej odpowiedzi na to pytanie. Praktycznie każdy problem można rozwiązać w każdym języku programowania - ale, język to tylko narzędzie i nie oznacza to, że jest ono najlepsze przy rozwiązywaniu problemów konkretnego typu.

Jeśli zaczynasz swoją przygodę z programowaniem, osobiście poleciłbym każdemu język Python. I nie dlatego, że piszę w nim codziennie, ale dlatego, że jest to język bardzo zwięzły, czytelny i oszczędza początkującym wielu stresów z "nieintuicyjnym zachowaniem".  
Pisałem w Perlu, C, PHP, JavaScript i Pythonie - i będę twardo trzymał stanowisko, że Python jest najlepszym językiem dla początkujących.

Jakie jest najlepsze środowisko do programowania w języku X?
------------------------------------------------------------

Najlepsze środowisko to takie, z którego Tobie dobrze się korzysta, które spełnia wszystkie Twoje potrzeby i przyspiesza Twoją pracę.

Wbrew temu, co publikuje się w sieci, jedynym właściwym rozwiązaniem nie jest ani PyCharm, ani Vim,  ani VS Code, ani Atom czy Sublime Text.

Jedynym właściwym **dla Ciebie** środowiskiem jest to, które Tobie najbardziej odpowiada. W miarę Twojej ewolucji jako programisty zmienisz zdanie jeszcze wiele razy.

Propozycja z mojej strony jest taka, żebyś w trakcie swojej codziennej pracy, spróbował przez ok. 2 tygodnie używać jednego z narzędzi (dłużej w przypadku Vima, ze względu na czas potrzebny do nauki wychodzenia z niego) i sam sprawdził, które narzędzie daje Ci pełną swobodę i nie rzuca Ci kłód pod nogi.

Od razu mogę powiedzieć, że o ile większość narzędzi będzie w miarę spójna do edycji tekstu (kodu źródłowego), tak Vim będzie wymagał pewnego rodzaju "przestawienia się" na inny sposób myślenia. Niemniej, znam sytuacje, że możliwości narzędzi są w pewien sposób łączone poprzez wykorzystanie pluginów.

Jaki jest najlepszy framework w języku X?
-----------------------------------------

A który już znasz? I co musisz osiągnąć? W sieci istnieje wiele porównań oraz dobrze rozpisanych zalet i wad każdego frameworka, czy nadają się do dużych projektów, są szybkie/łatwe do nauki, są łatwe do rozszerzania, itd.

Drobna uwaga: w sytuacji, gdy zaczynasz przygodę z programowaniem może to nie być dobry moment na wybór frameworka. Narzędzie to zostało napisane w jakimś języku programowania, jeśli nie znasz chociaż podstaw tego języka - szybko wpadniesz w kłopoty.

Jak wszędzie, możliwości wyboru są przeogromne. Dla Pythona można się miotać między Django, Flask, Pyramid oraz kilkoma innymi, mniej rozpoznawalnymi. W JavaScript sprawa wygląda trochę ciężej. Jest tam AngularJS, Angular (tak, wbrew nazwie są to praktycznie 2 różne frameworki)... i w sumie na tym należałoby zakończyć dostępność frameworków. Aktualnie w ekosystemie JavaScript królują jeszcze ReactJS i VueJS. O ile pierwszy jest biblioteką do tworzenia interfejsów, ten drugi z czasem ewoluował i stał się frameworkiem.

Ponownie, jeśli miałbym wybierać co polecałbym początkującym programistom webowym to Django i VueJS.

I już wyjaśniam dlaczego.

W przypadku Django - uważam - że jest to kompletny framework działający od momentu jego zainstalowania. Flask czy Pyramid są dla mnie bardziej narzędziami do budowy frameworka, gdzie na starcie dostajemy niezbędne minimum i dopiero my dobieramy sobie komponenty, które chcemy mieć w naszym frameworku. Dlatego - Django jako framework spisze się doskonale i nie przytłoczy nas potrzeba instalowania dodatkowych komponentów.

W przypadku VueJS - uważam, że pozwala na proste wejście w świat frameworków - tak jak kiedyś było z jQuery - dołącz plik i korzystaj - tak teraz można zacząć przygodę z VueJS. W miarę potrzeb oczywiście możemy go rozbudowywać o kolejne elementy, komplikować cały proces budowania aplikacji, ale jednak wydaje się świetnym punktem startowym.  
Brak spójności w AngularJS wywoływał u mnie frustrację - możliwości jakie oferował były bardzo często rozbieżne w sposobach pracy różnych programistów, przez co każdy projekt AngularJS był inny, czego konsekwencją były problemy w odnalezieniu się w kodzie. Angular - o ile wiele rzeczy teraz jest bardziej spójne, o tyle natłok wszystkich importów komponentów, modułów czy elementów potrzebnych do zbudowania aplikacji - jest po prostu zniechęcający.  
ReactJS to odrębna kategoria - jest biblioteką, a nie kompletnym frameworkiem. Niemniej, o ile pamiętam, także wymagał dodatkowej wiedzy zanim zaczęło się z tej biblioteki korzystać (tam pierwszy raz spotkałem się z JSX... i jakoś mi to do gustu nie przypadło).

Jak mam uczyć się programowania?
--------------------------------

To pytanie dość popularne, a wbrew pozorom nie jest tak prosto na nie odpowiedzieć - a przynajmniej tak wnioskuję z widzianych odpowiedzi. Programowanie to nie język programowania. Jeśli poznam języki Python, JavaScript czy Java, nadal nie będzie to oznaczało, że wiem jak programować.

Chociaż wcześniej myślałem podobnie, że nauka programowania to po prostu nauka jakiegoś wcześniej wybranego języka, to aktualnie uważam, że najlepszy sposób na naukę programowania to po prostu: właściwa książka, ołówek (dla lubiących ryzyko - długopis) i czysta kartka, możliwość skupienia się przez pewien czas. Mile widziany także jakiś mentor. Tylko tyle i aż tyle.

Programowanie to zrozumienie i umiejętność podzielenia nierozwiązywalnego (na pierwszy rzut oka) problemu na mniejsze i względnie łatwe do rozwiązania problemy.

To, czy wykorzystamy do tego technologię X to inna sprawa.

 
