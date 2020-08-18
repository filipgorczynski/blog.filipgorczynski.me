Title: Publikowanie kodu źródłowego z kolorowaniem składni w postach na Wordpress.com
Date: 2018-02-05 11:06
Author: filipgorczynski
Category: Dobre praktyki, Programowanie, Rozwiązania
Tags: formatowanie kodu, gist, GitHub, kod źródłowy, kolorowanie składni, wordpress
Slug: publikowanie-kodu-zrodlowego-z-kolorowaniem-skladni-w-postach-na-wordpress-com
Status: published

![](https://filipgorczynski.files.wordpress.com/2015/04/python1.png){.alignleft .wp-image-1002 .size-full width="128" height="128"}

Post ten skierowany jest do ludzi trzymających swoje blogi bezpośrednio na Wordpress.com i/lub którzy od czasu do czasu zmuszeni są opublikować kawałek kodu źródłowego.

Do wstawienia kolorowanego i sformatowanego kodu [oficjalna dokumentacja](https://en.support.wordpress.com/code/posting-source-code/) wspomina o wykorzystaniu znacznika \`code\` (w nawiasach kwadratowych) bezpośrednio we wpisie. Dodatkowo dysponujemy kilkoma parametrami konfiguracyjnymi co daje całkiem ciekawe możliwości:

\[code language="python" autolinks="true" title="Public source code for guess the number game" highlight="11,21"\]  
"""  
Code for program 33 from https://wiki.python.org/moin/SimplePrograms  
"""  
import random

guesses\_made = 0  
name = raw\_input('Hello! What is your name: ')  
number = random.randint(1, 20)  
print 'Well, {0}, I am thinking of a number between 1 and 20.'.format(name)

while guesses\_made \< 6:  
guess = int(raw\_input('Take a guess: '))  
guesses\_made += 1  
if guess \< number: print 'Your guess is too low.' if guess \> number:  
print 'Your guess is too high.'  
if guess == number:  
break

if guess == number:  
print 'Good job, {0}! You guessed my number in {1} guesses!'.format(name, guesses\_made)  
else:  
print 'Nope. The number I was thinking of was {0}'.format(number)\</pre\>

\[/code\]

Minusem tego rozwiązania jest jednak ograniczona liczba wspieranych języków (do przejrzenia na stronie oficjalnej dokumentacji). Jednak jeśli nie używamy niczego egzotycznego to do naszych potrzeb powinno to w zupełności wystarczyć.

Kolejnym sposobem w dokumentacji nie wspomnianym (ale wspomnianym na innej stronie dotyczącej samego Wordpressa) jest użycie narzędzia od GitHuba - [Gist](https://gist.github.com/). I jedyne co należy zrobić to po prostu wkleić URL gista, np. wklejenie adresu \`https://gist.github.com/filipgorczynski/04f4b97613da6970c44f5c4c8c115d72\` bezpośrednio do posta będzie skutkowało "załadowaniem" okienka jak poniżej:

https://gist.github.com/filipgorczynski/04f4b97613da6970c44f5c4c8c115d72

Zaletą tego rozwiązania jest obsługa całkiem sporej ilości kolorowania składni dla najróżniejszych języków - w sumie tego należałoby się spodziewać po narzędziu, którego głównym celem jest hosting kodu źródłowego. Wystarczy nadać odpowiednie rozszerzenie dla nazwy pliku podczas tworzenia gista. Minus to np.: brak możliwości podświetlania konkretnych linii.

Źródła:  
\[1\] <https://en.support.wordpress.com/code/posting-source-code/>  
\[2\] <https://codex.wordpress.org/Writing_Code_in_Your_Posts>
