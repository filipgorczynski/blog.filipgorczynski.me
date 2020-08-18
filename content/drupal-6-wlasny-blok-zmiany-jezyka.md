Title: Drupal 6 - Własny blok zmiany języka
Date: 2012-10-12 18:56
Author: filipgorczynski
Category: Programowanie, Rozwiązania
Tags: blok, Drupal 6, hook_block, Language switcher, zmiana języka
Slug: drupal-6-wlasny-blok-zmiany-jezyka
Status: published

[![](http://filipgorczynski.files.wordpress.com/2011/11/drupal-logo-application_logo.png?w=131 "Drupal-Logo.application_logo"){.wp-image-473 .alignleft width="47" height="54"}](http://filipgorczynski.files.wordpress.com/2011/11/drupal-logo-application_logo.png)Domyślny blok *"Przełączanie języków"* nie posiada zbyt ciekawych możliwości formatowania. Często tego typu elementy opisuje się w HTML na liście, co później znacznie ułatwia dla tej struktury określanie kaskadowych arkuszy stylów. Poniżej  sposób na zastosowanie swojego bloku bazujący na module *locale* domyślnie dostarczanym z Drupalem:

\[code language="php"\]  
\<?php  
/\*\*  
\* Implements hook\_block();  
\*/  
function hook\_block(\$op = 'list', \$delta = 0, \$edit = array()) {  
if (\$op == 'list') {  
\$blocks\['custom\_language\_switcher'\] = array(  
'info' =\> t('Custom Language Switcher'),  
);  
return \$blocks;  
} else if (\$op == 'view') {  
switch (\$delta) {  
case 'custom\_language\_switcher':  
if (variable\_get('language\_count', 1) \> 1  
&& variable\_get('language\_negotiation', LANGUAGE\_NEGOTIATION\_NONE) != LANGUAGE\_NEGOTIATION\_NONE) {  
\$path = drupal\_is\_front\_page() ? '\<front\>' : \$\_GET\['q'\];  
\$languages = language\_list('enabled');  
\$links = array();  
foreach (\$languages\[1\] as \$language)  
\$links\[\$language-\>language\] = array(  
'href' =\> \$path,  
'title' =\> \$language-\>native,  
'language' =\> \$language,  
'attributes' =\> array('class' =\> 'language-link'),  
);  
drupal\_alter('translation\_link', \$links, \$path);

\$block = array(  
'subject' =\> t('Custom Language Switcher'),  
'content' =\> \_custom\_get\_language\_switcher(\$links)  
);  
}  
break;  
}  
return \$block;  
}  
}

function \_custom\_get\_language\_switcher(\$links = array()) {  
global \$language;  
\$html = '';  
if (count(\$links)) {  
\$html = '\<ul class="language-switcher"\>';  
foreach (\$links as \$key =\> \$value) {  
\$active = '';  
if (\$key == \$language-\>language)  
\$active = ' class="active"';  
\$html .= "\\t\\t" . '\<li' . \$active . '\>\<a href="' . url(\$value\['href'\], array('language' =\> \$value\['language'\])) . '"' . \$active . '\>' . \$value\['title'\] . '\</a\>\</li\>' . "\\n";  
}  
\$html .= "\\t" . '\</ul\>' . "\\n";  
}  
return \$html;  
}  
\[/code\]
