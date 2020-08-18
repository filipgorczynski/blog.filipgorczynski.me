Title: Generowanie unikalnego identyfikatora
Date: 2010-11-10 21:29
Author: filipgorczynski
Category: Programowanie, Rozwiązania
Slug: generowanie-unikalnego-identyfikatora
Status: published

Szukając prostego generatora unikatowych łańcuchów znaków natrafiłem na poniższe rozwiązanie:  
[Stackoverflow](http://stackoverflow.com/questions/1846202/php-how-to-generate-a-random-unique-alphanumeric-string/1846229#1846229)  
Podsumowując:  
Jeśli nie potrzebujemy zawsze unikalnego identyfikatora  
\[code language="php"\]  
\<?php  
md5(uniqid(rand(), true));  
\[/code\]  
w przeciwnym razie, możemy wykorzystać unikalny identyfikator użytkownika, np.: adres email:  
\[code language="php"\]  
\<?php  
md5(uniqid('filip\[dot\]gorczynski\[at\]gmail\[dot\]com', true));  
\[/code\]
