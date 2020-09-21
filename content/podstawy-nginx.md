Title: Podstawy nginx
Date: 2018-02-17 19:11
Author: filipgorczynski
Category: Tech
Slug: podstawy-nginx
Status: draft

Dyrektywy = Option name + Option value

[code language="text"]
<span class="k">worker_processes</span> <span class="mi">5</span><span class="p">;</span>
<span class="k">error_log</span> <span class="s">logs/error.log</span><span class="p">;</span>
<span class="k">pid</span> <span class="s">logs/nginx.pid</span><span class="p">;</span>
<span class="k">worker_rlimit_nofile</span> <span class="mi">8192</span><span class="p">;</span>
[/code]

Contexts: main - najwyższy poziom w pliku, events, http \> server \> location

 

server context \~ Apache vhost configuration

 

\[code language="text"\]  
\<pre\>\<span class="k"\>user\</span\> \<span class="s"\>www\</span\> \<span class="s"\>www\</span\>\<span class="p"\>;\</span\> \<span class="c1"\>\#\# Default: nobody\</span\>  
\<span class="k"\>worker\_processes\</span\> \<span class="mi"\>5\</span\>\<span class="p"\>;\</span\> \<span class="c1"\>\#\# Default: 1\</span\>  
\<span class="k"\>error\_log\</span\> \<span class="s"\>logs/error.log\</span\>\<span class="p"\>;\</span\>  
\<span class="k"\>pid\</span\> \<span class="s"\>logs/nginx.pid\</span\>\<span class="p"\>;\</span\>  
\<span class="k"\>worker\_rlimit\_nofile\</span\> \<span class="mi"\>8192\</span\>\<span class="p"\>;\</span\>

\<span class="k"\>events\</span\> \<span class="p"\>{\</span\>  
\<span class="kn"\>worker\_connections\</span\> \<span class="mi"\>4096\</span\>\<span class="p"\>;\</span\> \<span class="c1"\>\#\# Default: 1024\</span\>  
\<span class="p"\>}\</span\>

\<span class="k"\>http\</span\> \<span class="p"\>{\</span\>  
\<span class="kn"\>include\</span\> \<span class="s"\>conf/mime.types\</span\>\<span class="p"\>;\</span\>  
\<span class="kn"\>include\</span\> \<span class="s"\>/etc/nginx/proxy.conf\</span\>\<span class="p"\>;\</span\>  
\<span class="kn"\>include\</span\> \<span class="s"\>/etc/nginx/fastcgi.conf\</span\>\<span class="p"\>;\</span\>  
\<span class="kn"\>index\</span\> \<span class="s"\>index.html\</span\> \<span class="s"\>index.htm\</span\> \<span class="s"\>index.php\</span\>\<span class="p"\>;\</span\>

\<span class="kn"\>default\_type\</span\> \<span class="s"\>application/octet-stream\</span\>\<span class="p"\>;\</span\>  
\<span class="kn"\>log\_format\</span\> \<span class="s"\>main\</span\> \<span class="s"\>'\</span\>\<span class="nv"\>\$remote\_addr\</span\> \<span class="s"\>-\</span\> \<span class="nv"\>\$remote\_user\</span\> \<span class="s"\>\[\</span\>\<span class="nv"\>\$time\_local\]\</span\> \<span class="nv"\>\$status\</span\> \<span class="s"\>'\</span\>  
\<span class="s"\>'"\</span\>\<span class="nv"\>\$request"\</span\> \<span class="nv"\>\$body\_bytes\_sent\</span\> \<span class="s"\>"\</span\>\<span class="nv"\>\$http\_referer"\</span\> \<span class="s"\>'\</span\>  
\<span class="s"\>'"\</span\>\<span class="nv"\>\$http\_user\_agent"\</span\> \<span class="s"\>"\</span\>\<span class="nv"\>\$http\_x\_forwarded\_for"'\</span\>\<span class="p"\>;\</span\>  
\<span class="kn"\>access\_log\</span\> \<span class="s"\>logs/access.log\</span\> \<span class="s"\>main\</span\>\<span class="p"\>;\</span\>  
\<span class="kn"\>sendfile\</span\> \<span class="no"\>on\</span\>\<span class="p"\>;\</span\>  
\<span class="kn"\>tcp\_nopush\</span\> \<span class="no"\>on\</span\>\<span class="p"\>;\</span\>  
\<span class="kn"\>server\_names\_hash\_bucket\_size\</span\> \<span class="mi"\>128\</span\>\<span class="p"\>;\</span\> \<span class="c1"\>\# this seems to be required for some vhosts\</span\>

\<span class="kn"\>server\</span\> \<span class="p"\>{\</span\> \<span class="c1"\>\# php/fastcgi\</span\>  
\<span class="kn"\>listen\</span\> \<span class="mi"\>80\</span\>\<span class="p"\>;\</span\>  
\<span class="kn"\>server\_name\</span\> \<span class="s"\>domain1.com\</span\> \<span class="s"\>www.domain1.com\</span\>\<span class="p"\>;\</span\>  
\<span class="kn"\>access\_log\</span\> \<span class="s"\>logs/domain\</span\>\<span class="mi"\>1\</span\>\<span class="s"\>.access.log\</span\> \<span class="s"\>main\</span\>\<span class="p"\>;\</span\>  
\<span class="kn"\>root\</span\> \<span class="s"\>html\</span\>\<span class="p"\>;\</span\>

\<span class="kn"\>location\</span\> \<span class="p"\>\~\</span\> \<span class="sr"\>\\.php\$\</span\> \<span class="p"\>{\</span\>  
\<span class="kn"\>fastcgi\_pass\</span\> \<span class="n"\>127.0.0.1\</span\>\<span class="p"\>:\</span\>\<span class="mi"\>1025\</span\>\<span class="p"\>;\</span\>  
\<span class="p"\>}\</span\>  
\<span class="p"\>}\</span\>

\<span class="kn"\>server\</span\> \<span class="p"\>{\</span\> \<span class="c1"\>\# simple reverse-proxy\</span\>  
\<span class="kn"\>listen\</span\> \<span class="mi"\>80\</span\>\<span class="p"\>;\</span\>  
\<span class="kn"\>server\_name\</span\> \<span class="s"\>domain2.com\</span\> \<span class="s"\>www.domain2.com\</span\>\<span class="p"\>;\</span\>  
\<span class="kn"\>access\_log\</span\> \<span class="s"\>logs/domain\</span\>\<span class="mi"\>2\</span\>\<span class="s"\>.access.log\</span\> \<span class="s"\>main\</span\>\<span class="p"\>;\</span\>

\<span class="c1"\>\# serve static files\</span\>  
\<span class="kn"\>location\</span\> \<span class="p"\>\~\</span\> \<span class="sr"\>\^/(images\|javascript\|js\|css\|flash\|media\|static)/\</span\> \<span class="p"\>{\</span\>  
\<span class="kn"\>root\</span\> \<span class="s"\>/var/www/virtual/big.server.com/htdocs\</span\>\<span class="p"\>;\</span\>  
\<span class="kn"\>expires\</span\> \<span class="s"\>30d\</span\>\<span class="p"\>;\</span\>  
\<span class="p"\>}\</span\>

\<span class="c1"\>\# pass requests for dynamic content to rails/turbogears/zope, et al\</span\>  
\<span class="kn"\>location\</span\> \<span class="s"\>/\</span\> \<span class="p"\>{\</span\>  
\<span class="kn"\>proxy\_pass\</span\> \<span class="s"\>http://127.0.0.1:8080\</span\>\<span class="p"\>;\</span\>  
\<span class="p"\>}\</span\>  
\<span class="p"\>}\</span\>

\<span class="kn"\>upstream\</span\> \<span class="s"\>big\_server\_com\</span\> \<span class="p"\>{\</span\>  
\<span class="kn"\>server\</span\> \<span class="n"\>127.0.0.3\</span\>\<span class="p"\>:\</span\>\<span class="mi"\>8000\</span\> \<span class="s"\>weight=5\</span\>\<span class="p"\>;\</span\>  
\<span class="kn"\>server\</span\> \<span class="n"\>127.0.0.3\</span\>\<span class="p"\>:\</span\>\<span class="mi"\>8001\</span\> \<span class="s"\>weight=5\</span\>\<span class="p"\>;\</span\>  
\<span class="kn"\>server\</span\> \<span class="n"\>192.168.0.1\</span\>\<span class="p"\>:\</span\>\<span class="mi"\>8000\</span\>\<span class="p"\>;\</span\>  
\<span class="kn"\>server\</span\> \<span class="n"\>192.168.0.1\</span\>\<span class="p"\>:\</span\>\<span class="mi"\>8001\</span\>\<span class="p"\>;\</span\>  
\<span class="p"\>}\</span\>

\<span class="kn"\>server\</span\> \<span class="p"\>{\</span\> \<span class="c1"\>\# simple load balancing\</span\>  
\<span class="kn"\>listen\</span\> \<span class="mi"\>80\</span\>\<span class="p"\>;\</span\>  
\<span class="kn"\>server\_name\</span\> \<span class="s"\>big.server.com\</span\>\<span class="p"\>;\</span\>  
\<span class="kn"\>access\_log\</span\> \<span class="s"\>logs/big.server.access.log\</span\> \<span class="s"\>main\</span\>\<span class="p"\>;\</span\>

\<span class="kn"\>location\</span\> \<span class="s"\>/\</span\> \<span class="p"\>{\</span\>  
\<span class="kn"\>proxy\_pass\</span\> \<span class="s"\>http://big\_server\_com\</span\>\<span class="p"\>;\</span\>  
\<span class="p"\>}\</span\>  
\<span class="p"\>}\</span\>  
\<span class="p"\>}\</span\>\</pre\>  
\[/code\]

`

events {

}

http {  
\# Should be replaced with include instead adding content types manually  
\#types {  
\# Files with html extension send with text/html Content-Type  
\# text/html html;  
\# similar for other file types  
\# text/css css;  
\#}  
include mime.types;

server {  
listen 80;  
server\_name vhost-bootstrap.local;  
root /opt/www/sites/bootstrap;

\# Matching Order:  
\# 1. = Exact Match  
\# 2. \^\~ Preferencial Prefix (same as standard match, but more important than RegEx)  
\# 3. \~ & \~\* RegEx Match  
\# 4. no modifier Prefix Match (no modifier)

\# Matches any prefix  
\# - /greet\*  
\# - /greeting  
\# - /greet/something  
\# Commented out to prevent: 'nginx: \[emerg\] duplicate location "/greet" in /etc/nginx/nginx.conf' error  
\#location /greet {  
\# return 200 'Hello from Nginx location block';  
\#}

\# Exact match  
location = /hello-world {  
return 200 'Hello from exact match Nginx location block';  
}

\# Regex match - case sensitive  
location \~ /greet\[0-9\] {  
return 200 'Hello from case sensitive RegEx match Nginx location block';  
}

\# Prefix preferential match  
location \^\~ /greet {  
return 200 'Hello from Nginx with preference over RegEx match... location block';  
}

\# Regex match - case insensitive  
location \~\* /NginX-2018 {  
return 200 'Hello from case insensitive RegEx match Nginx location block';  
}

\# This location is outside root location  
location /downloads {  
root /opt/www/sites;  
try\_files \$uri =404; \# First try to match \$uri, throw 404 if no match found

}

}  
}

    `
    http -h http://vhost-bootstrap.local/title.png 
    curl -I http://vhost-bootstrap.local/css/bootstrap.css
