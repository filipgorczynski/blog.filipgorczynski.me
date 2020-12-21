Title: Pierwsze kroki z Robot Framework
Date: 2019-11-18 18:05
Author: filipgorczynski
Category: Tech
Tags: ATDD, robot framework, robotframework, selenium, TDD, Testowanie, XPath
Slug: pierwsze-kroki-z-robot-framework
Status: draft

![Robot Framework Logo](https://filipgorczynski.files.wordpress.com/2019/05/robot-framework-logo.png?w=128){.alignleft .wp-image-2234 .size-thumbnail width="128" height="128"}Nadarzyła się okazja w projekcie do spróbowania swoich sił w roli testera automatyzującego. Po kilku pogawędkach z ludźmi z zespołu na temat różnych narzędzi wybór padł na [Robot Framework](https://robotframework.org/) - z przyczyn marketingowych niezbyt znany, ale ze względu na swoje możliwości - projekt prezentujący się naprawdę ciekawie.<!--more-->

Sam framework to tylko prosty "silnik" i dopiero zainstalowanie rozszerzeń dodaje mu super mocy; projekt ma otwarte źródła i jest napisany w Pythonie.  
Podstawową składnię pisanych w nim testów określić można jako Keyword-Driven, natomiast nic nie stoi na przeszkodzie, aby do pisania przypadków testowych stosować składnię Gherkina, czyli Behavior Driven.  
Służyć może jako baza do testów akceptacyjnych, programowania sterowanego testami akceptacyjnymi (ATDD - Acceptance Test Driven Development) i tzw Robotic Process Automation (RPA).  
Jego główna zaleta (dla programistów to w sumie może być wada) - to składania oparta na białych znakach - co najmniej 2 spacjach.

Jak już wspomniałem, możliwości Robot Framework znacznie wzrastają dzięki rozszerzaniu go różnymi bibliotekami, które mogą być implementowane w językach Python i/lub Java - co pozwala na utworzenie własnej listy rozbudowanych **"Keywordsów"**.

Spróbujmy może napisać jakieś proste testy, żeby pokazać jak łatwe jest automatyzowanie zadań testowania w przeglądarce z użyciem tego narzędzia.

How it works?

Instalacja

`pip install robotframework robotframework-seleniumlibrary`

Built-in tools

Zmienne (+przekazywanie wartości do zmiennych podczas uruchomienia skryptu)

Zmienne globalne i lokalne

Typy zmiennych: zmienne skalarne, zmienne listy

Lokalizowanie elementów na stronie:

\- XPath - szybkie wprowadzenie

\- CSS

https://gist.github.com/filipgorczynski/068b6f8cdcfa54d3404d0cbf7aeb94e2

Writing First test + viewing reports (with tests running) - Use Case SeleniumLibrary

Organizing Test Cases

Page Objects

Directory and Tests structure

tests/

resources/

page-objects/

results/

tests/

Struktura pakietu testów:

Plik pakietu testów (Test Suite) składa się

`https://github.com/rhesusminus/robot-framework/blob/master/Resources/PageObjects/GooglePOM.robot`

```

\*\*\* Settings \*\*\*

\*\*\* Variables \*\*\*

\*\*\* Keywords \*\*\*

\*\*\* Testcases \*\*\*

```

 

 

\[1\] https://robotframework.org/

It has easy-to-use tabular test data syntax and it utilizes the keyword-driven testing approach. Its testing capabilities can be extended by test libraries implemented either with Python or Java, and users can create new higher-level keywords from existing ones using the same syntax that is used for creating test cases.

Spróbujmy może napisać jakieś proste testy, żeby pokazać jak łatwe jest automatyzowanie zadań z użyciem tego narzędzia.

XPath - szybkie wprowadzenie

Struktura pakietu testów:

Plik pakietu testów (Test Suite) składa się

`https://github.com/rhesusminus/robot-framework/blob/master/Resources/PageObjects/GooglePOM.robot`

```

\*\*\* Settings \*\*\*

\*\*\* Variables \*\*\*

\*\*\* Keywords \*\*\*

\*\*\* Testcases \*\*\*

```

\[1\] https://robotframework.org/

Page Object:

`https://martinfowler.com/bliki/PageObject.html`

The rule of thumb is to model the structure in the page that makes sense to the user of the application.

Struktura katalogów

`https://www.code-learner.com/how-to-use-selenium-webdriver-in-python-to-make-web-automation-testing-example/`

 
