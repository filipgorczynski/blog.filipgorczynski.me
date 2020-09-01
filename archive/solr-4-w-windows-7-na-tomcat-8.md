Title: Solr 4 w Windows 7 na Tomcat 8
Date: 2014-10-18 18:28
Author: filipgorczynski
Category: Programowanie, Rozwiązania, Systemy Operacyjne
Tags: Apache Tomcat, SolR
Slug: solr-4-w-windows-7-na-tomcat-8
Status: hidden

[![Apache Solr](https://filipgorczynski.files.wordpress.com/2014/10/solr.png?w=150){.alignleft .wp-image-910 .size-thumbnail width="150" height="82"}](http://filipgorczynski.wordpress.com/2014/10/18/solr-4-w-windows-7-na-tomcat-8/ "Solr 4 w Windows 7 na Tomcat 8")Poniżej przedstawiam czynności jakie musiałem wykonać w celu zainstalowania Solr4 w Windows 7 na serwerze Apache Tomcat 8.

1\. Pobieramy wersję instalacyjną [JDK8](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) odpowiednią dla naszego systemu operacyjnego (oczywiście o ile już jej wcześniej nie instalowaliśmy); dla mnie było to [jdk-8u25-windows-x64.exe](http://download.oracle.com/otn-pub/java/jdk/8u25-b18/jdk-8u25-windows-x64.exe). Instalujemy jak każdą inną aplikację w Windows.

2\. Pobieramy i instalujemy [Apache Tomcat 8](http://tomcat.apache.org/download-80.cgi). Dla wygody można pobrać plik instalacyjny [32-bit/64-bit Windows Service Installer](http://ftp.piotrkosoft.net/pub/mirrors/ftp.apache.org/tomcat/tomcat-8/v8.0.14/bin/apache-tomcat-8.0.14.exe). Jako katalog instalacyjny dla Tomcat 8 wybrałem *C:\\dev\\tomcat8*.

3\. Po zainstalowaniu możemy wejść w przeglądarce na adres *http://localhost:8080/* w celu zweryfikowania poprawności instalacji (oczywiście określając odpowiedni port, którypodaliśmy w trakcie instalacji Tomcata). Powinniśmy zobaczyć ekran podobny do poniższego:

[![tomcat8](https://filipgorczynski.files.wordpress.com/2014/10/tomcat8.png?w=300){.size-medium .wp-image-911 .aligncenter width="300" height="218"}](https://filipgorczynski.files.wordpress.com/2014/10/tomcat8.png)

4\. Zatrzymujemy usługę Tomcat: wybieramy *Monitor Tomcat* w menu programów Windows, w oknie klikamy przycisk *Stop*.

5\. Ze [strony domowej Solr](http://lucene.apache.org/solr/) pobieramy ostatnią wersję, ja wybrałem [solr-4.10.1.zip](http://ftp.ps.pl/pub/apache/lucene/solr/4.10.1/solr-4.10.1.zip).

6\. Pobrany plik możemy rozpakować do C:\\solr-4.10.1\\; z tego katalogu będziemy potrzebowali tylko niewielką część.

7. Z lokalizacji *C:\\solr-4.10.1\\dist\\* kopiujemy plik *solr-4.10.1.war* do katalogu *C:\\dev\\tomcat8\\webapps\\* oraz zmieniamy nazwę tego pliku - usuwamy numer wersji pozostawiając tylko *solr.war*.

8\. Tworzymy nowy pusty katalog i uznajemy go za katalog domowy Solra - przykładowo *C:\\dev\\solr*.

9\. Z katalogu *C:\\solr-4.10.1\\example\\solr\\* kopiujemy wszystko do utworzonego przed chwilą katalogu *C:\\dev\\solr* - będziemy mieć tu m.in. katalogi *bin* oraz *collection1*.

10\. Z katalogu *C:\\solr-4.10.1\\example\\lib\\ext\\* kopiujemy wszystkie pliki *\*.jar* (ok 5 plików) do katalogu C:\\dev\\tomcat8\\lib.

11\. Ustawiamy wartość dla solr.solr.home. W okienku Monitor Tomcat; w zakładce Java w polu  Java Options dodajemy na końcu katalog domowy naszego Solra:

\* *

\[code language="text"\]  
-Dsolr.solr.home=C:\\dev\\solr  
\[/code\]

*  
*

12\. W tym samym oknie przechodzimy do pierwszej zakładki, gdzie uruchamiamy usługę Tomcat 8 przyciskiem *Start*.

13\. Tomcat dostępny jest pod adresem *http://localhost:8080/*. Solr natomiast jest dostępny pod adresem *http://localhost:8080/solr/*.

[![Solr4 Dashboard](https://filipgorczynski.files.wordpress.com/2014/10/solr4dashboard.png?w=300){.size-medium .wp-image-917 .aligncenter width="300" height="99"}](https://filipgorczynski.files.wordpress.com/2014/10/solr4dashboard.png)
