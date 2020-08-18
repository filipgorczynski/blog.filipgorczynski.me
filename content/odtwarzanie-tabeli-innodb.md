Title: Odtwarzanie tabeli InnoDB
Date: 2014-01-11 06:04
Author: filipgorczynski
Category: Bazy danych, Programowanie, Rozwiązania
Slug: odtwarzanie-tabeli-innodb
Status: published

[![MySQL logo](http://filipgorczynski.files.wordpress.com/2014/01/mysql_logo_250x129.png?w=150){.alignleft .wp-image-846 width="90" height="46"}](http://filipgorczynski.files.wordpress.com/2014/01/mysql_logo_250x129.png)W kilku projektach zdarzyło mi się z bliżej nieokreślonych powodów podczas próby czyszczenia cache w Drupalu wystąpienie błędu MySQL w postaci:

\[code language="sql"\]  
mysql\> show tables;  
+--------------------------------------+  
\| Tables\_in\_drupal7demo                \|  
+--------------------------------------+  
\| ...            \|  
\| cache\_apachesolr    \|  
\| ...            \|  
+--------------------------------------+  
108 rows in set (0.00 sec)  
mysql\> TRUNCATE \`cache\_apachesolr\`;  
ERROR 1146 (42S02): Table 'drupal7demo.cache\_solr' doesn't exist  
\[/code\]

Mogło to być spowodowane wykonaniem polecenia TRUNCATE \`cache\_apachesolr\` i sposobem w jaki w rzeczywistości wykonywane jest polecenie [TRUNCATE](http://en.wikipedia.org/wiki/Truncate_%28SQL%29).

Jednym z najprostszych rozwiązań jakie udało mi się znaleźć jest odtworzenie struktury tabeli, a ponieważ praktycznie każda próba odczytu/zapisu z/do tabeli zwróci komunikat błędu (np.: ERROR 1030 (HY000): Got error -1 from storage engine) musimy dodać jeszcze jedno polecenie w ostateczności wykonując poniższe polecenia:

\[code language="sql"\]  
ALTER TABLE \`cache\_apachesolr\` DISCARD TABLESPACE;  
DROP TABLE IF EXISTS \`cache\_apachesolr\`;  
CREATE TABLE \`cache\_apachesolr\` (  
\`cid\` varchar(255) NOT NULL DEFAULT '' COMMENT 'Primary Key: Unique cache ID.',  
\`data\` longblob COMMENT 'A collection of data to cache.',  
\`expire\` int(11) NOT NULL DEFAULT '0' COMMENT 'A Unix timestamp indicating when the cache entry should expire, or 0 for never.',  
\`created\` int(11) NOT NULL DEFAULT '0' COMMENT 'A Unix timestamp indicating when the cache entry was created.',  
\`serialized\` smallint(6) NOT NULL DEFAULT '0' COMMENT 'A flag to indicate whether content is serialized (1) or not (0).',  
PRIMARY KEY (\`cid\`),  
KEY \`expire\` (\`expire\`)  
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Cache table for apachesolr to store Luke data and...';  
\[/code\]

Potencjalne przyczyny problemu: <http://dba.stackexchange.com/a/6269>

Źródło rozwiązania: <http://www.palominodb.com/blog/2011/11/02/how-recreate-innodb-table-after-tablespace-has-been-removed>

Kilka innych pomysłów, które można wypróbować by odzyskać tabele: <http://www.chriscalender.com/?tag=innodb-error-tablespace-id-in-file>
