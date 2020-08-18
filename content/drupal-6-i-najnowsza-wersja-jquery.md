Title: Drupal 6 i najnowsza wersja jQuery
Date: 2012-02-20 20:47
Author: filipgorczynski
Category: Dobre praktyki, Programowanie, Rozwiązania
Tags: Drupal 6, JavaScript, jQuery, najnowsze jQuery
Slug: drupal-6-i-najnowsza-wersja-jquery
Status: published

[![](http://filipgorczynski.files.wordpress.com/2011/11/drupal-logo-application_logo.png?w=131 "Drupal-Logo.application_logo"){.wp-image-473 .alignleft width="56" height="65"}](http://filipgorczynski.files.wordpress.com/2011/11/drupal-logo-application_logo.png)Od kilku już projektów w Drupalu spotykałem się z problemem przy wykorzystaniu najaktualniejszej wersji jQuery. Drupal w wersji 6 wykorzystuje jQuery w wersji 1.2.6. Instalacja modułu jquery\_update trochę poprawia tą sytuację jednak nadal pozostajemy z wersją 1.3.2. W chwili pisania tego tekstu najnowszą wersją jQuery jest 1.7.1, więc jak widać sporo rzeczy mogło ulec zmianie. Korzystając z najnowszej wersji jQuery mamy w dodatku pewność, że znalezione błędy zostały poprawione (i ewentualnie, powstały nowe), kod został przepisany by działać szybciej, zwiększył się asortyment funkcji.

\[code language="javascript"\]  
/\*! jQuery v1.7.1 jquery.com \| jquery.org/license \*/  
// źródło najaktualniejszej wersji jQuery

\$\$ = jQuery.noConflict();

console.log('o1. ', \$.fn.jquery);  
// o1. 1.2.6  
// LUB  
// o1. 1.3.2

(function(\$) {  
// W tej przestrzeni znajdzie się nasz kod  
console.log('o2. ', \$.fn.jquery);  
// o2. 1.7.1  
})(\$\$);  
\[/code\]

Co się tutaj dzieje?

Poprzez funkcję [jQuery.noConflict()](http://api.jquery.com/jQuery.noConflict/ "jQuery.noConflict()") obiektu jQuery utworzymy referencję \$\$, która będzie przechowywała nowy obiekt biblioteki jQuery (1.7.1 w tym wypadku). Zmienna \$\$ będzie dostępna w zasięgu globalnym (window), a my będziemy posiadać zmienne \$\$ (wersja  1.7.1) oraz \$ (wersja 1.2.6/1.3.2).

Tworzymy następnie kolejny zasięg poprzez wywołanie kolejnej funkcji anonimowej, do której przekazujemy wcześniej utworzony obiekt jQuery 1.7.1. Drugie wywołanie funkcji anonimowej moglibyśmy pominąć i odwoływać się w naszym kodzie do jQuery wykorzystując zmienną \$\$, ale osobiście uważam to za mało wygodne.
