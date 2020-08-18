Title: SimpleXMLElement i count - zliczanie elementów obiektu w różnych wersjach PHP
Date: 2011-05-11 21:19
Author: filipgorczynski
Category: Programowanie, Rozwiązania
Slug: simplexmlelement-i-count-zliczanie-elementow-obiektu-w-roznych-wersjach-php
Status: published

Zliczanie elementów w obiekcie SimpleXMLElement. Jak się okazuje, możemy się zdziwić, jeśli na którymś z serwerów posiadamy wcześniejsze niż 5.3 wersje PHP.

\[code language="php"\]  
\$xml = new SimpleXMLElement("plik.xml", null, true);  
\$allNodes = 0;  
if (version\_compare(PHP\_VERSION, '5.3.0', '\>=')) {  
\$allNodes = \$xml-\>Project-\>count(); // PHP \>= 5.3  
} else {  
\$allNodes = count(\$xml-\>children()); // PHP \< 5.3  
}  
\[/code\]
