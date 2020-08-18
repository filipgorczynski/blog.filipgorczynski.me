Title: Komunikaty (flash messages) w Symfony2
Date: 2014-09-17 20:45
Author: filipgorczynski
Category: Programowanie, Rozwiązania
Tags: error, flash-messages, messages, Notice, symfony, Symfony2, warning
Slug: komunikaty-flash-messages-w-symfony2
Status: published

    Przykładowy sposób wykorzystania komunikatów w Symfony.
    W kontrolerze:

\[code language="php"\]  
\$success = 'Komunikat informujący o powodzeniu wykonanej operacji.';  
\$this-\>get('session')-\>getFlashBag()-\>add('success', \$success);  
\$error = 'Komunikat informujący o niepowodzeniu wykonanej operacji.';  
\$this-\>get('session')-\>getFlashBag()-\>add('error', \$error);  
\$warning = 'Komunikat informujący o ostrzeżeniu podczas wykonywanej operacji.';  
\$this-\>get('session')-\>getFlashBag()-\>add('warning', \$warning);  
\$notice = 'Komunikat informujący o wykonanej operacji.';  
\$this-\>get('session')-\>getFlashBag()-\>add('notice', \$notice);  
\[/code\]

W szablonie (Twig)

\[code language="php"\]  
{\# twig template \#}  
{% for type, flashMessages in app.session.flashbag.all() %}  
{% for flashMessage in flashMessages %}  
\<div class="{{ type }}"\>{{ flashMessage }}\</div\>  
{% endfor %}  
{% endfor %}  
\[/code\]
