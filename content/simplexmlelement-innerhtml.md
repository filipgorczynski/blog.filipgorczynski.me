Title: SimpleXMLElement innerHTML
Date: 2011-06-08 09:20
Author: filipgorczynski
Category: Programowanie, Rozwiązania
Slug: simplexmlelement-innerhtml
Status: published

W przypadku otrzymania niezbyt przyjaznego pliku XML, w którym to w tagu znajduje się wrzucony kod HTML (elementy p, span, strong, itp) nie otoczony \<!\[CDATA\[ i \]\]\>, zawartość tego tagu można by pobrać w następujący sposób:

\[code language="php"\]

echo preg\_replace('\#\</?tag\[\^\>\]\*\>\#is', '', (string)\$xml-\>tag-\>asXML());

\[/code\]
