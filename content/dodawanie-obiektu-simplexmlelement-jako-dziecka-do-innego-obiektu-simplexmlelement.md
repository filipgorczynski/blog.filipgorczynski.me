Title: Dodawanie obiektu SimpleXmlElement jako dziecka do innego obiektu SimpleXmlElement
Date: 2011-06-15 11:06
Author: filipgorczynski
Category: Programowanie, Rozwiązania
Tags: addChild, DOM, dziecko, rodzic, simplexmlelement
Slug: dodawanie-obiektu-simplexmlelement-jako-dziecka-do-innego-obiektu-simplexmlelement
Status: published

[![Application - XML](http://filipgorczynski.files.wordpress.com/2011/06/application-xml.png "application-xml"){.alignleft .size-full .wp-image-357 width="128" height="128"}](http://filipgorczynski.files.wordpress.com/2011/06/application-xml.png) Podczas budowania struktury XML z wykorzystaniem SimpleXmlElement dla [jachcenawakacje.pl](http://jachcenawakacje.pl "JaChcęNaWakcje") natknąłem się na problem dodawania do obiektu typu SimpleXmlElement jako dziecka innego obiektu SimpleXmlElement - wyciętego z innej struktury XML. Problem jest o tyle dziwny, że metoda SimpleXmlElement::addChild() przyjmuje jako wartość tylko i wyłącznie łańcuch znaków. W związku z dość sporą ilością kodu, jaki trzeba by napisać, aby przenieść jedną strukturę XML do innej takie rozwiązanie nie wchodziło w grę. Z pomocą przyszedł kod udostępniony przez członka społeczności Stackoverflow.

[code language="php"]
<?php  
$xml = new SimpleXMLElement('<?xml version="1.0" encoding="UTF-8"?><element></element>');  
$request = $xml->addChild('request');  
$request->addChild('type', 'test');  
$sxe = simplexml_load_string('<sxe></sxe>');  
$inner1 = $sxe->addChild("inner1");  
$inner2 = $inner1->addChild("inner2");  
$inner3 = $inner2->addChild("inner3");  
$toDom = dom_import_simplexml($xml);  
$fromDom = dom_import_simplexml($sxe);  
$toDom->appendChild($toDom->ownerDocument->importNode($fromDom, true));  
header('Content-type: application/xml; charset=utf-8');  
echo $xml->asXML();  
[/code]

Oczywiście najważniejsze są tutaj linie 9-11, które to realizują całe zadanie kopiowania struktury pomiędzy XML.  
Efekt poniżej:

\[code language="xml"\]  
\<?xml version="1.0" encoding="UTF-8"?\>  
\<element\>  
\<request\>  
\<type\>test\</type\>  
\</request\>  
\<sxe\>  
\<inner1\>  
\<inner2\>  
\<inner3/\>  
\</inner2\>  
\</inner1\>  
\</sxe\>  
\</element\>  
\[/code\]

Link do oryginału: <http://stackoverflow.com/questions/4778865/php-simplexml-addchild-with-another-simplexmlelement/4778964#4778964>
