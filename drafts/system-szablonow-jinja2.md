Title: System szablonów - Jinja2
Date: 2015-04-24 21:14
Author: filipgorczynski
Category: Tech
Slug: system-szablonow-jinja2
Status: draft

[![Flask - logo](https://filipgorczynski.files.wordpress.com/2015/04/flask.png?w=150){.alignleft .wp-image-969 .size-thumbnail width="150" height="134"}](https://filipgorczynski.files.wordpress.com/2015/04/flask.png)

 

The variables and/or logic are placed between tags or delimiters. For example, Jinja templates use `{% ... %}` for expressions or logic (like for loops), while `{{ ... }}` are used for outputting the results of an expression or a variable to the end user. The latter tag, when rendered, is replaced with a value or values, and are seen by the end user.

Make sure you have Jinja installed before running these examples – `pip install jinja2`

System szablonów [Jinja2](http://jinja.pocoo.org/docs/dev/) został wybrany jako jeden z 2 głównych komponentów mikroframeworka Flask (obok routingu Werkzeug).

 

Źródło: https://realpython.com/blog/python/primer-on-jinja-templating/

Spis treści:

0\. Co będzie nam potrzebne?

\[code language="bash"\]

\$ virtualenv jinja2-sandbox

\$ Scripts\\activate  
\$ source bin\\activate

\$ setprojectdir .

\$ pip install flask

\$ pip install Flask

1\. Skok na głęboką wodę - szybki przykład w trybie interaktywnym.\</pre\>  
\<pre\>\[code language="python"\]

\>\>\> from jinja2 import Template  
\>\>\> tpl = Template("Witaj, {{ name }}!")  
\>\>\> tpl.render(name="Filip")  
u'Witaj, Filip!'  
\>\>\> tpl2 = Template("Liczby parzyste w przedziale 1-10:{% for i in range(1, 11) %} {{ i }}{% endfor %}")  
\>\>\> tpl2.render()  
u'Liczby w przedziale 1-10: 1 2 3 4 5 6 7 8 9 10'  
\>\>\>

\[/code\]

Pierwsze co musimy zrobić, to zaimportować klasę Template z paczki jinja2.

2\. Podstawowa składnia - {{ }}, {% %}, {\# \#}

Składnia Jinja2 nie należy do skomplikowanych. Elementy kodu, które mogą się nam wydać nowe i niejasne to:

{{ obiekt }}  - wykorzystujemy, gdy chcemy wydrukować na ekranie wartość obiekt.

Przykład:

{{ imie }}

{% instrukcja %}

{\# komentarz \#}

3\. Jinja2 i framework Flask

Jak pisałem już wcześniej system szablonów Jinja2 otrzymujemy w momencie instalacji Flask, dlatego zakładam, że zainstalowaliśmy już Flask a nie sam system szablonów.

 

4\. Bloki

5\. Dziedziczenie

6\. Makra

7\. Filtry (w tym własne filtry)

8\. Szybkie szablony - korzystamy z

8\. Podsumowanie

10\. Źródła:

http://jinja.pocoo.org/docs/dev/templates/

http://jinja.pocoo.org/docs/dev/tricks/

http://jinja.pocoo.org/docs/dev/api/
