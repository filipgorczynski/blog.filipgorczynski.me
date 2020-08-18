Title: Ubuntu + Apache2 + symfony framework + wirtualne hosty
Date: 2010-07-29 09:36
Author: filipgorczynski
Category: Programowanie, Rozwiązania
Slug: ubuntu-apache2-symfony-framework-wirtualne-hosty
Status: published

Postanowiłem spróbować swoich sił z frameworkiem symfony i jadąc po kolei wg zaleceń z kursu [Jobeet](http://www.symfony-project.org/jobeet/1_4/Doctrine/en/) natrafiłem na problem w konfiguracji serwera Apache2. Wymiataczem Ubuntu też nie jestem, a Jobeet zapomniał chyba wspomnieć o modyfikacji /etc/hosts - w moim przypadku tylko dzięki temu zadziałało. Zawartości moich plików:

**Zawartość pliku /etc/hosts**  
\[code language="text"\]  
127.0.0.1 localhost  
127.0.0.1 www.jobeet.local  
127.0.1.1 laptop

\# The following lines are desirable for IPv6 capable hosts  
::1 localhost ip6-localhost ip6-loopback  
fe00::0 ip6-localnet  
ff00::0 ip6-mcastprefix  
ff02::1 ip6-allnodes  
ff02::2 ip6-allrouters  
ff02::3 ip6-allhosts  
\[/code\]

**Zawartość pliku httpd.conf**  
\[code language="text"\]  
ServerName www.jobeet.local  
\[/code\]

**Zawartość pliku /etc/apache2/sites-available/default**  
\[code language="text"\]  
\<VirtualHost www.jobeet.local:80\>  
ServerAdmin filip.gorczynski\@gmail.com  
DocumentRoot /var/www/sfproject/web  
DirectoryIndex index.php  
\<Directory "/var/www/sfproject/web"\>  
AllowOverride All  
Allow from All  
\</Directory\>  
Alias /sf /var/www/sfproject/data/web/sf  
\<Directory "/var/www/sfproject/data/web/sf"\>  
AllowOverride All  
Allow from All  
\</Directory\>  
\</VirtualHost\>

\<VirtualHost \*:80\>  
ServerAdmin filip.gorczynski\@gmail.com

DocumentRoot /var/www  
\<Directory /\>  
Options FollowSymLinks  
AllowOverride All  
\</Directory\>  
\<Directory /var/www/\>  
Options Indexes FollowSymLinks MultiViews  
AllowOverride All  
Order allow,deny  
allow from all  
Allow from 127.0.0.0/255.0.0.0 ::1/128  
\</Directory\>

ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/  
\<Directory "/usr/lib/cgi-bin"\>  
AllowOverride None  
Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch  
Order allow,deny  
Allow from all  
\</Directory\>

ErrorLog /var/log/apache2/error.log

\# Possible values include: debug, info, notice, warn, error, crit,  
\# alert, emerg.  
LogLevel warn

CustomLog /var/log/apache2/access.log combined

Alias /doc/ "/usr/share/doc/"  
\<Directory "/usr/share/doc/"\>  
Options Indexes MultiViews FollowSymLinks  
AllowOverride None  
Order deny,allow  
Deny from all  
Allow from 127.0.0.0/255.0.0.0 ::1/128  
\</Directory\>

\</VirtualHost\>  
\[/code\]

Po tych zmianach i  
\[code language="text"\]  
sudo /etc/init.d/apache2 restart  
\[/code\]  
wszystko śmiga jak należy. Wpisując w przeglądarkę www.jobeet.local odwołuje mi się bez problemu do projektu symfony. Wpisanie localhost działa jak poprzednio - czyli póki co wyświetla słodko brzmiące "It works!".  
Jeśli chodzi o strukturę moich katalogów, to ściągniętą paczkę symfony rozpakowałem do /var/www/sfproject/.
