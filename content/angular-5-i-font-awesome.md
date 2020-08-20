Title: Angular 5 i Font-Awesome
Date: 2018-02-07 10:49
Author: filipgorczynski
Category: Programowanie, Rozwiązania
Tags: angular, angular-font-awesome, bulma, font-awesome, npm
Slug: angular-5-i-font-awesome
Status: published

![](https://filipgorczynski.files.wordpress.com/2018/02/angular1-e1517653581617.png){.alignleft .wp-image-1487 .size-full width="120" height="128"}

Jedną z możliwości integracji [font-awesome](https://fontawesome.com/) z [Angular](https://angular.io/) jest użycie gotowych paczek z repozytoriów npm. Przegląd kilku - oraz szybki rzut oka na datę publikacji ostatnich zmian w tych paczkach wyłonił `angular-font-awesome'. I o ile instrukcja instalacji dostępna jest na stronie repozytorium tej paczki - nie jestem zwolennikiem ponownego szukania samej nazwy paczki ani jak jej użyć.

Dla porządku tworzymy sobie czysty projekt w Angularze:

https://gist.github.com/filipgorczynski/1fdc941dae677ed85396c9337f4d7f3d

Instalujemy wybrane przez nas paczki (jako, że jestem zwolennikiem [yarn](https://yarnpkg.com/lang/en/)a to tego będę używał):

https://gist.github.com/filipgorczynski/87b9cbce88c0e9498dc550667b7cac3b

`yarn add` od razu załatwi nam sprawę dodania tych paczek z odpowiednimi wersjami do pliku `package.json`.

Dodajemy odpowiednie importy w pliku `app.module.js`:

https://gist.github.com/filipgorczynski/6c1416548a951214d0d775d6ea9889fa

oraz ładujemy style globalnie dla całej aplikacji w pliku `.angular-cli.json` w sekcji `styles`:

https://gist.github.com/filipgorczynski/4ded01b01ddd87ca67c53202271acc1e

I to już wszystko - powinniśmy mieć możliwość korzystania z ikonek font-awesome w naszej aplikacji wrzucając do szablonu, przykładowo:

https://gist.github.com/filipgorczynski/cdee8259a0b441fa0be0434b24061789

**Bonus:** Bulma CSS Framework

Wartym uwagi jest niewielki framework CSS - Bulma. Instalujemy odpowiednią paczkę (oczywiście nie jest to jedyny sposób instalacji):

https://gist.github.com/filipgorczynski/51747a4e88b932917541908014833fb0

W pliku `.angular-cli.json` dodajemy odpowiednią referencję do pliku CSS naszego frameworka, aby był dostępny globalnie w całej aplikacji:

https://gist.github.com/filipgorczynski/ef98fcbb0d56dbf4d9b79e702e6a5801

I oczywiście aby zobaczyć, czy wszystko działa, uzupełniamy np.: `app.component.html` przykładowym szablonem:

https://gist.github.com/filipgorczynski/ca7b01726268f0ae268bf1bbb5685879

Uruchamiamy serwer i weryfikujemy w przeglądarce, czy wszystko śmiga.

Całość kodu źródłowego dostępna jest też w repozytorium [NG5-FontAwesome-Bulma-Boilerplate](https://github.com/filipgorczynski/NG5-FontAwesome-Bulma-Boilerplate). Klonujemy (`git clone git@github.com:filipgorczynski/NG5-FontAwesome-Bulma-Boilerplate.git`), przechodzimy do katalogu projektu (`cd NG5-FontAwesome-Bulma-Boilerplate`), odpalamy `yarn` aby zainstalować zależności z `package.json` i startujemy serwer (`ng serve`).
