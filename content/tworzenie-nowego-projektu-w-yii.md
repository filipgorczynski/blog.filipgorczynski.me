Title: Tworzenie nowego projektu w Yii
Date: 2011-04-17 20:37
Author: filipgorczynski
Category: Programowanie, Rozwiązania
Slug: tworzenie-nowego-projektu-w-yii
Status: published

Ostatnio coraz więcej frameworków zostaje wyposażonych w skrypty pozwalające jeszcze bardziej przyspieszyć tworzenie aplikacji poprzez generowanie jak największej ilości kodu. W przypadku frameworka Yii możliwości jest sporo, od generowania struktury katalogów i plików samej aplikacji, po generowanie modułów, modeli, całej struktury CRUD w kontrolerach a w nowszych wersjach także kodu pozwalającego synchronizowanie struktury baz danych.  
Nazewnictwo dla katalogów jest następujące:  
WebRoot - katalog główny serwera HTTP - jego zawartość prezentuje się po wpisaniu http://localhost/ w pasku adresu przeglądarki. Dla mnie będzie to x:\\htdocs\\.  
YiiDir - katalog w którym został zainstalowany framework Yii. W moim przypadku jest to x:\\htdocs\\yii.  
AppDir - katalog aplikacji - tworzonego projektu. Na tutejsze potrzeby nazwijmy go **demo**. W tym przypadku, będzie to x:\\htdocs\\demo.  
Oto co musimy zrobić, aby stworzyć nowy projekt z wykorzystaniem frameworka Yii.  
Na początku oczywiście musimy posiadać zainstalowany framework - pobieramy go najlepiej na stronie projektu [Yii framework](http://www.yiiframework.com/download/). Wszystkie pliki wypakowujemy w katalogu YiiDir.  
Następnym krokiem jest uruchomienie okna poleceń - cmd.exe i wpisanie następujących poleceń oraz słówka **Yes** w odpowiednim momencie.  
\[code language="powershell"\]  
\> cd x:\\htdocs  
\> yii\\framework\\yiic webapp demo  
Create a Web application under 'x:\\htdocs\\demo'? \[Yes\|No\] Yes  
unchanged css/bg.gif  
unchanged css/form.css  
unchanged css/ie.css  
unchanged css/main.css  
unchanged css/print.css  
unchanged css/screen.css  
generate index-test.php  
generate index.php  
unchanged protected/.htaccess  
unchanged protected/components/Controller.php  
unchanged protected/components/UserIdentity.php  
unchanged protected/config/console.php  
unchanged protected/config/main.php  
unchanged protected/config/test.php  
unchanged protected/controllers/SiteController.php  
unchanged protected/data/schema.mysql.sql  
unchanged protected/data/schema.sqlite.sql  
unchanged protected/data/testdrive.db  
unchanged protected/models/ContactForm.php  
unchanged protected/models/LoginForm.php  
unchanged protected/tests/bootstrap.php  
unchanged protected/tests/functional/SiteTest.php  
unchanged protected/tests/phpunit.xml  
unchanged protected/tests/WebTestCase.php  
unchanged protected/views/layouts/column1.php  
unchanged protected/views/layouts/column2.php  
unchanged protected/views/layouts/main.php  
unchanged protected/views/site/contact.php  
unchanged protected/views/site/error.php  
unchanged protected/views/site/index.php  
unchanged protected/views/site/login.php  
unchanged protected/views/site/pages/about.php  
unchanged protected/yiic  
unchanged protected/yiic.bat  
unchanged protected/yiic.php  
unchanged themes/classic/views/.htaccess

Your application has been created successfully under x:\\htdocs\\demo.  
\>  
\[/code\]  
Tak, to już. Posiadamy działającą aplikację. Wystarczy wejść na stronę http://localhost/demo by zobaczyć działającą stronę kontakt z formularzem, logowanie oraz wyświetlanie stron, proste menu, breadcrumb.
