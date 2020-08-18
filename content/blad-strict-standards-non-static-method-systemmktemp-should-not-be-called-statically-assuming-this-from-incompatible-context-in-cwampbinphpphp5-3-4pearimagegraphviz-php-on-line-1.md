Title: Błąd Strict standards: Non-static method System::mktemp() should not be called statically, assuming $this from incompatible context in C:\wamp\bin\php\php5.3.4\PEAR\Image\GraphViz.php on line 1005
Date: 2012-02-29 21:25
Author: filipgorczynski
Category: Programowanie, Rozwiązania
Tags: graphviz, GraphViz.php, pear, System::mktemp
Slug: blad-strict-standards-non-static-method-systemmktemp-should-not-be-called-statically-assuming-this-from-incompatible-context-in-cwampbinphpphp5-3-4pearimagegraphviz-php-on-line-1
Status: published

[![](http://filipgorczynski.files.wordpress.com/2012/02/phppear.png?w=150 "PHPpear"){.wp-image-552 .alignright width="72" height="72"}](http://filipgorczynski.files.wordpress.com/2012/02/phppear.png)Trafiłem ostatnio na artykuł opisujący wykorzystanie paczki Image\_Graphviz z repozytorium PEAR do obsługi i generowania grafów w języku PHP. Instalacja przebiegła bez najmniejszych problemów:

\[code language="text"\]  
pear install --alldeps Image\_GraphViz  
\[/code\]

jednak już próba uruchomienia przykładu <http://pear.php.net/manual/en/package.images.image-graphviz.example.php> sprzyjała pojawianiu się błędu:

\[code language="text"\]  
Strict standards: Non-static method System::mktemp() should not be called statically,  
assuming \$this from incompatible context in C:\\wamp\\bin\\php\\php5.3.4\\PEAR\\Image\\GraphViz.php on line 1005  
\[/code\]

Niestety, mimo zgłoszenia błędu, autorzy uznali, że błędu nie poprawią, a sam błąd wynika z PHP w wersji 4.x, pod kątem której paczka Image\_Graphviz była pisana. Rozwiązaniem idealnym byłoby przystosowanie kodu Image\_Graphviz do pracy z PHP 5.X - mniej idealnym zastosowanie niewielkiego obejścia:  
wyłączenia wyświetlania błędów w kodzie na samym początku kodu generującego obrazek z grafem - przykład więc powinien wyglądać jak poniżej:

\[code language="php"\]  
\<?php  
error\_reporting(E\_ALL & \~E\_STRICT); // EDIT: zmiany zalecone przez D3Xa :)  
ini\_set('display\_errors', 0);  
require\_once 'Image/GraphViz.php';  
\$gv = new Image\_GraphViz();  
\$gv-\>addEdge(array('wake up' =\> 'visit bathroom'));  
\$gv-\>addEdge(array('visit bathroom' =\> 'make coffee'));  
\$gv-\>image();  
// EDIT: poniżej zmiany zalecane przez D3Xa  
error\_reporting(-1);  
ini\_set('display\_errors', 1);  
\[/code\]

czego efektem będzie pożądany obrazek:

[![](http://filipgorczynski.files.wordpress.com/2012/02/graphviz.png "graphviz"){.aligncenter .size-full .wp-image-551 width="179" height="251"}](http://filipgorczynski.files.wordpress.com/2012/02/graphviz.png)  
Warto także przyjrzeć się [dokumentacji Image\_Graphviz](pear.php.net/package/Image_GraphViz/docs/latest/Image_GraphViz/Image_GraphViz.html) oraz sam projekt [GraphViz](http://www.graphviz.org/).
