Title: Grupowanie podprojektów w PyCharm
Date: 2018-03-05 07:34
Author: filipgorczynski
Category: Dobre praktyki, Programowanie, Rozwiązania
Tags: grupowanie, Projekty, PyCharm
Slug: grupowanie-podprojektow-w-pycharm
Status: published

![](https://filipgorczynski.files.wordpress.com/2018/03/pycharm_logo.png){.alignleft .wp-image-1675 .size-full width="128" height="128"}

Niezbyt często używaną funkcją PyCharma jest jego wsparcie dla dużych projektów w postaci możliwości dodawania nowych projektów w ramach bieżącego okna. Jeszcze mniej znaną (według mnie) funkcją pozwalającą zapanować nad wieloma projektami jest możliwość grupowania projektów w strukturze drzewa.

Co warto zrobić na początku - głównie z czysto estetycznych powodów - to ustalić jakiś całkowicie oddzielny katalog, który może pozostać pusty. Ewentualnie możemy trzymać jakieś "śmieci" związane z projektem, które nie muszą być, np. pod kontrolą wersji.

Zazwyczaj podczas tworzenia nowego projektu otwieramy go w nowym oknie PyCharm - i tak też zalecałbym zrobić dla dopiero co utworzonego katalogu "głównego". To będzie nasz punkt startowy - a PyCharm będzie nam ładnie w tytule wyświetlał nowo powstały projekt główny.

[![](https://filipgorczynski.files.wordpress.com/2018/03/pycharm-open-project.png?w=150){.aligncenter .wp-image-1687 .size-thumbnail width="150" height="122"}](https://filipgorczynski.files.wordpress.com/2018/03/pycharm-open-project.png)

Pozostałe projekty, które chcemy mieć widoczne w PyCharmie w odpowiedniej strukturze dodawać będziemy już w taki sposób:

[![](https://filipgorczynski.files.wordpress.com/2018/03/pycharm-open-project-in-current.png?w=150){.aligncenter .wp-image-1686 .size-thumbnail width="150" height="122"}](https://filipgorczynski.files.wordpress.com/2018/03/pycharm-open-project-in-current.png)

Przechodząc do sedna sprawy **wszystko rozbija się o nazewnictwo katalogów**. Jeśli uporządkujemy projekty na dysku nadając im odpowiednie człony (prefixy) rozdzielane kropką, PyCharm zatroszczy się o resztę.

Po dodaniu kolejnych projektów będą w elegancki sposób pogrupowane w paczki, jak poniżej:

[![](https://filipgorczynski.files.wordpress.com/2018/03/pycharm-grouped-projects.png?w=150){.aligncenter .wp-image-1685 .size-thumbnail width="150" height="125"}](https://filipgorczynski.files.wordpress.com/2018/03/pycharm-grouped-projects.png)

Nic więcej się nie zmienia i np. nadal posiadamy udogodnienie w postaci konfigurowania środowisk Pythona dla każdego projektu indywidualnie.

Oczywiście powyższe nie dotyczy osób, które są zwolennikami trzymania w PyCharm każdego projektu oddzielnie - jak zawsze ma to swoje plusy i minusy.
