Title: CORS Headers - komunikacja VueJS i Django
Date: 2018-02-09 13:42
Author: filipgorczynski
Category: Programowanie, Rozwiązania
Tags: Access-Control-Allow-Origin, cors, django, django rest framework, drf, Same Origin Policy, SOP, vuejs
Slug: cors-headers-komunikacja-vuejs-i-django
Status: published

[![vuejs logo](https://filipgorczynski.files.wordpress.com/2017/11/vuejs_logo.png?w=150){.alignleft .wp-image-1359 .size-thumbnail width="150" height="150"}Cross-Origin Resource Sharing ([CORS](https://developer.mozilla.org/en-US/docs/Glossary/CORS "CORS: CORS (Cross-Origin Resource Sharing) is a system, consisting of transmitting HTTP headers, that determines whether to block or fulfill requests for restricted resources on a web page from another domain outside the domain from which the resource originated."){.glossaryLink}) to mechanizm wykorzystujący dodatkowe nagłówki HTTP pozwalające różnym agentom (np. przeglądarkom) na dostęp do zasobów znajdujących się na innej domenie, porcie czy protokole niż aktualna. ]{.seoSummary}

Na potrzeby wpisu zakładam, że framework ([Django](https://www.djangoproject.com/)) i biblioteki ([Vue.js](https://vuejs.org/) i [axios](https://github.com/axios/axios)) z których będziemy korzystać - mamy już zainstalowane w projekcie.

W projekcie Vue wprowadźmy następujące zmiany:

W pliku `App.vue`:

https://gist.github.com/filipgorczynski/b0f3cb73529abfec37a906430e33d16b

W pliku `config/dev.env.js`:

https://gist.github.com/filipgorczynski/0923d45ea68f9b3d3f7ce1114777759d

[gist:id=0923d45ea68f9b3d3f7ce1114777759d]

Pliki `src/assets/logo.png` i `src/components/HelloWorld.vue` możemy wyrzucić, jako w tej chwili nie używane.

W backendzie natomiast, w pliku `views.py` naszej aplikacji (`movies`):

https://gist.github.com/filipgorczynski/2d88596364a238ee385ac3f95f5bf0c7

i dodajemy routing dla naszej aplikacji w pliku `urls.py` (plik ten domyślnie nie istnieje i należy go utworzyć):

https://gist.github.com/filipgorczynski/3acaede9f616abeaed3e52e0532aea3f

Następnie dokunujemy zmian w plikach `urls.py` - głównym pliku routingu całego projektu Django:

https://gist.github.com/filipgorczynski/ebf421288d8cef05d8b122634c5dd5af

oraz `settings.py`:

https://gist.github.com/filipgorczynski/f62a3e0c77d9b8fe13555ac926547f45

Startujemy serwery poniższymi poleceniami w odpowiednich katalogach:

https://gist.github.com/filipgorczynski/066239d6e31b21d16fbacc4e1d83a0de

Uruchamiamy przeglądarkę i otwieramy 2 zakładki. W pierwszej zweryfikujemy tylko, czy serwer Django zwraca prawidłową odpowiedź - JSON (`http://127.0.0.1:8000`) i jeśli tak, to od razu można ją zamknąć. W drugiej zakładce otwieramy narzędzia programisty i przechodzimy pod adres aplikacji Vue (`http://127.0.0.1:8080`).  
[Dziwne - w zakładce `Network` zobaczyć możemy, że żądanie GET do serwera się udało i nawet możemy podejrzeć zwrócone wyniki:]{.seoSummary}

https://gist.github.com/filipgorczynski/30c0320691c7fe7f9ecb5bc09c8e8a2c

[Czyli wszystko jest prawidłowo? No nie do końca niestety. ]{.seoSummary}O ile domena (host) - w tej sytuacji `127.0.0.1` nie są problemem - to sprawa komplikuje się właśnie w przypadku niezgodności portów i przeglądarka może nam w konsoli sypnąć następującym błędem:

https://gist.github.com/filipgorczynski/37fb22093aa4549107f115045de65ef0

Problem nasz rozwiązać możemy paczką `django-cors-headers`, jej instalacja nie odbiega za bardzo od instalacji innych paczek Pythona:

`pip install django-cors-headers==2.1.0`

Zmieniamy trochę w pliku `settings.py` (ale naprawdę ciut-ciut):

https://gist.github.com/filipgorczynski/b21e07e1e1b010bc380e0d2bb7d6f8ea

... restartujemy serwer Django i już, wchodząc na adres naszej aplikacji powinniśmy cieszyć się pobranymi z serwera danymi.

Wymagane paczki do postawienia projektu Django znajdują się  w katalogu `backend/requirements/base.txt`, natomiast całość kodu źródłowego bezpośrednio w repozytorium [VueJS-Django-CORS](https://github.com/filipgorczynski/vuejs-django-cors).

Dla zainteresowanych można jeszcze poszukać informacji na temat [Same Origin Policy](https://en.wikipedia.org/wiki/Same-origin_policy).

Dodatkowe źródła (często z fajnymi obrazkami):

1.  [MDN CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
2.  [Understanding CORS](https://medium.com/@baphemot/understanding-cors-18ad6b478e2b)
3.  [Understanding CORS: Cross-Origin Resource Sharing](https://blog.jscrambler.com/understanding-cors-cross-origin-resource-sharing/)
4.  [Understanding and using CORS](https://templth.wordpress.com/2014/11/12/understanding-and-using-cors/)

 
