Title: Narzędzia do statycznej analizy kodu źródłowego w PyCharm
Date: 2018-03-07 18:06
Author: filipgorczynski
Category: Dobre praktyki, Programowanie, Rozwiązania
Tags: Narzędzia, PyCharm, Python, tools
Slug: narzedzia-do-statycznej-analizy-kodu-zrodlowego-w-pycharm
Status: hidden

![PyCharm](https://filipgorczynski.files.wordpress.com/2018/03/pycharm_logo.png){.alignleft .wp-image-1675 .size-full width="128" height="128"}

Kilkukrotnie wspominałem już o IDE PyCharm i jego możliwościach. Oprócz kolorowania składni i obsługi kilku innych głupotek pozwala na przykład definiować narzędzia, które później możemy uruchamiać w trakcie pisania kodu.

Jako programiści Pythona możemy do tych narzędzi zaliczyć te dbające o jakość pisanego przez nas kodu. Oprócz standardowego PEP8 - który jest tylko czubkiem góry lodowej - osobiście chciałbym polecić także: [flake8](http://flake8.pycqa.org/en/latest/), [pylint](https://www.pylint.org/) oraz [radon](http://radon.readthedocs.io/en/latest/).

`flake8` jako linter sprawdza kod pod kątem zgodności ze standardami - dodatkowo rozszerza wspomniany przed chwilą PEP8 o kilka innych wartościowych usprawnień, np. takie związane z komentarzami, nazewnictwem zmiennych, itp.

Podobnie ma się sytuacja z `pylint`-em, jednak jego zaletą jest ocena naszego kodu z użyciem skali - każda zmiana może wpływać pozytywnie lub negatywnie zgodnie z następującym [wzorem](https://docs.pylint.org/en/1.8/faq.html#pylint-gave-my-code-a-negative-rating-out-of-ten-that-can-t-be-right). Satysfakcją jest uzyskać ocenę 10.00/10.00 :). Oprócz oceny liczbowej otrzymujemy także zestawienie i najróżniejsze statystyki.

`radon` natomiast w całkiem przyjemny sposób prezentuje nam informacje na temat złożoności fragmentów naszego kodu - może nam się wtedy zapalić czerwona lampka, że pewne elementy powstałego kodu mogą potencjalnie stanowić wąskie gardło w aplikacji i są dobrym miejscem zaczepienia jeśli chodzi o refaktoryzację.

Zainstalujmy więc sobie narzędzia w czystym środowisku wirtualnym:

https://gist.github.com/filipgorczynski/0794a41c5ba09061c24fcf67eb6911c4

flake8 zostanie zainstalowany jako zależność podczas instalacji radon-a.

[![PyCharm Settings External Tools](https://filipgorczynski.files.wordpress.com/2018/03/pycharm-settings-external-tools.png?w=76){.aligncenter .size-thumbnail .wp-image-1722 width="76" height="128"}](https://filipgorczynski.files.wordpress.com/2018/03/pycharm-settings-external-tools.png)

Klikamy "+" aby dodać nowe narzędzie. W otwartym okienku uzupełniamy jak poniżej:

[![PyCharm external tool window](https://filipgorczynski.files.wordpress.com/2018/03/pycharm-external-tool-radon.png?w=128){.aligncenter .wp-image-1723 .size-thumbnail width="128" height="96"}](https://filipgorczynski.files.wordpress.com/2018/03/pycharm-external-tool-radon.png) [![PyCharm external tool pylint](https://filipgorczynski.files.wordpress.com/2018/03/pycharm-external-tool-pylint.png?w=128){.aligncenter .wp-image-1724 .size-thumbnail width="128" height="96"}](https://filipgorczynski.files.wordpress.com/2018/03/pycharm-external-tool-pylint.png) [![PyCharm external tool flake8](https://filipgorczynski.files.wordpress.com/2018/03/pycharm-external-tool-flake8.png?w=128){.aligncenter .wp-image-1725 .size-thumbnail width="128" height="96"}](https://filipgorczynski.files.wordpress.com/2018/03/pycharm-external-tool-flake8.png)

Oczywiście dobrym pomysłem jest także grupowanie naszych narzędzi, np. ze względu na technologię oraz konfiguracja skrótów klawiaturowych:

[![PyCharm settings python tools keymap](https://filipgorczynski.files.wordpress.com/2018/03/pycharm-settins-python-tools-keymap.png?w=128){.aligncenter .size-thumbnail .wp-image-1727 width="128" height="93"}](https://filipgorczynski.files.wordpress.com/2018/03/pycharm-settins-python-tools-keymap.png)

Poniżej kilka zrzutów po uruchomieniu:

-   flake8:

https://gist.github.com/filipgorczynski/f470f8dd309321c8bad9beb3849facc4

-   pylint

https://gist.github.com/filipgorczynski/4acad39c9bb49557f67f989143e387ff

-   radon

https://gist.github.com/filipgorczynski/4b8c160690c54db11c4a814c186ac090

Więcej doczytać można w następujących źródłach:

1. [About style guide of python and linter tool. pep8, pyflakes, flake8, haking, Pylint.](https://blog.sideci.com/about-style-guide-of-python-and-linter-tool-pep8-pyflakes-flake8-haking-pyling-7fdbe163079d)
2. [What is Flake8 and why we should use it?](https://medium.com/python-pandemonium/what-is-flake8-and-why-we-should-use-it-b89bd78073f2)
