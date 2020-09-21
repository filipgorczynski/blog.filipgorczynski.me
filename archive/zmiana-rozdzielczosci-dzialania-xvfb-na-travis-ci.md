Title: Zmiana rozdzielczości działania Xvfb na Travis CI
Date: 2019-07-27 11:12
Author: filipgorczynski
Category: Dobre praktyki, Programowanie
Tags: automation tests, ci, e2e, resolution, robot framework, rozdzielczość, selenium, testowanie automatyczne, travis, xvfb
Slug: zmiana-rozdzielczosci-dzialania-xvfb-na-travis-ci
Status: archive

![Travis CI Logo](https://filipgorczynski.files.wordpress.com/2018/03/travisci-logo.png){.alignleft .wp-image-1752 .size-full width="128" height="128"}

O ile uruchamianie "zwykłych" testów w ramach ciągłej integracji (Jenkins, Travis CI, Circle CI) raczej nie jest problematyczne - bo przecież uruchamiamy je tylko przeciwko konkretnym fragmentom kodu - to testy wymagające Xvfb (X virtual framebuffer) już takie oczywiste nie są.

Po zainstalowaniu Xvfb na Travisie powinien być dostępny plik konfiguracyjny tej usługi - `/etc/systemd/system/xvfb.service`. Jego zmiana  wymagać będzie `sudo`.  
Warto sprawdzić, jaka rozdzielczość ustawiona jest domyślnie - u mnie było to 1024x768px - co w sumie w czasach obecnych bardziej pokrywa się z urządzeniami mobilnymi i **błędnie** założyłem, że Travis będzie operował na wyższej rozdzielczości - no bo przecież mamy XXI wiek.  
W samych testach, mimo wymuszania maksymalizacji okna otwartej przeglądarki - niektóre testy kończyły się niepowodzeniem. Okazało się, że problemem jest właśnie rozdzielczość ekranu, a nawet zmaksymalizowane okno było na tyle małe, że strona wyświetlana była jak na urządzeniach mobilnych, przez co pewne elementy strony nie były widoczne w ogóle albo wymagały wykonania dodatkowych akcji. Wyjaśnia to też, dlaczego lokalnie testy przechodziły bez zająknięcia.

Niemało stresu kosztowało mnie znalezienie sposobu na wymuszenie, aby xvfb uruchamiał okienka w większej rozdzielczości - gdy już udało się to rozgryźć - okazuje się to wyjątkowo banalne.

Jedyne co trzeba było wykonać, to zatrzymać usługę xvfb, poleceniem - na przykład `sed` - zmienić poprzednio ustawioną rozdzielczość na nową w pliku konfiguracyjnym usługi i ponownie uruchomić usługę, czyli:

<script src="https://gist.github.com/filipgorczynski/07840941c0e613b32d6be56fe4fe373d.js"></script>

Dodatkowo, Travis CI pozwala na zbieranie artefaktów ale  ograniczeni jesteśmy tylko do wysyłania tego do AWS, a dokładniej do S3 (przynajmniej w chwili obecnej) - debugowanie było z tego powodu mniej przyjemne. Robot Framework, w przypadku niepowodzenia robi zrzuty ekranu - rozdzielczość tych zrzutów ekranu możemy uzyskać poleceniem `file selenium-screenshot-1.png` - oczywiście, wymagać to będzie uruchomienia buildu w trybie debugowania i/lub dostępu do utworzonych wcześniej artefaktów.

Przy okazji kilka kolejnych wskazówek, które mogą się przydać w pracy z Travisem.

1. Podczas uruchamiania buildu w trybie debugowania otrzymujemy polecenie, którego potrzebujemy, aby zalogować się do Travisa. Warto dodać parametr `-o ConnectTimeout=0` do tego polecenia SSH, jak w poniższym przypadku:  
   `ssh -o ConnectTimeout=0 unique-id-xyz@to2.tmate.io`  
   Oczywiście, potrzebne to jest tylko wtedy, gdy nie mamy tego ustawionego na stałe w konfiguracji SSH.  
   Po zalogowaniu będziemy mieć możliwość wykonywać polecenia ręcznie - analogicznie do automatycznego wykonywania kolejnych poleceń z pliku `.travis.yml`.
2. Gdy już będziemy zalogowani - aby przyspieszyć pracę i wykonanie poszczegółnych grup poleceń które wiemy, że nie stanowią problemu, możemy korzystać z poleceń basha: `travis_run_*`{style="font-size:18px;"} - czyli travis\_run\_before\_install, travis\_run\_install, travis\_run\_before\_script, itd - do każdej sekcji z naszego pliku `.travis.yml` dodajemy po prostu prefix `travis_run_` i powinny wykonać się wszystkie polecenia z tej sekcji.
3. Ponieważ Travis w momencie napotkania błędu, przy włączonej - chyba nawet domyślnie - opcji `fast_finish: true` oraz błędów w linii poleceń - zamyka połączenie SSH - sugeruję, by w trakcie debugowania ustawić w Bashu `set +e`, zabezpieczy nas to przed przedwczesnym zakończeniem builda z wynikiem błędu (jeśli wpiszemy coś nieprawidłowo w linii poleceń) i będziemy mogli na spokojnie przyjrzeć się komunikatom zwróconym przez wywoływane programy.
4. Próby ustawiania różnych (wyższych) rozdzielczości dawały dziwne rezultaty:  
   **1280x1024 px -\> 1050x888 px**  
   1920x1080 px -\> 945x944 px  
   1680x1050 px -\> 825x914 px  
   czyli jak widać, największą szerokość zrzutu ekranu dała pierwsza rozdzielczość.
5. Nie ma możliwości komunikacji z Travisem poprzez `scp` - więc próba przesłania artefaktów w ten sposób także się nie powiedzie (uwzględniając kwestie przekazywania agenta SSH).

Cały przykład można znaleźć na [GitHub](https://github.com/filipgorczynski/robo-travis) i bezpośrednio na [Travisie](https://travis-ci.com/filipgorczynski/robo-travis), a przykładowy plik `.travis.yml` poniżej:

<script src="https://gist.github.com/filipgorczynski/860feb42e43915c22ddc4861b896421c.js"></script>
