Title: Eksport wszystkich baz z MySQL do plików SQL
Date: 2012-10-12 19:09
Author: filipgorczynski
Category: Bazy danych, Programowanie, Rozwiązania
Tags: export, MySQL, mysqldump, SQL
Slug: eksport-wszystkich-baz-z-mysql-do-plikow-sql
Status: published

Eksport wszystkich baz danych z MySQL.

\[code language="php"\]  
\<?php  
header('Content-type: text/html; charset=utf-8');  
class Config {  
public static \$host = '127.0.0.1';  
public static \$username = 'root';  
public static \$password = '';  
public static \$port = 3306;  
}

if (!file\_exists('dbdumps') \|\| !is\_dir('dbdumps'))  
mkdir('dbdumps', 0700);

\$dsn = 'mysql:host=' . Config::\$host . ';port=' . Config::\$port;  
\$options = array(PDO::MYSQL\_ATTR\_INIT\_COMMAND =\> 'SET NAMES utf8');  
\$dbh = new PDO(\$dsn, Config::\$username, Config::\$password, \$options);

\$result = \$dbh-\>query('SHOW DATABASES;');  
if (\$result !== false)  
foreach (\$result-\>fetchAll() as \$row) {  
\$cmd = 'mysqldump -u ' . Config::\$username . ' -p' . Config::\$password  
. ' ' . \$row\['Database'\] . ' \> dbdumps/' . \$row\['Database'\] . '.sql';  
system(\$cmd);  
\$fileSize = filesize('dbdumps/' . \$row\['Database'\] . '.sql');  
echo 'File ' . \$row\['Database'\] . '.sql saved \[' . \$fileSize . ' bytes\] .\<br /\>';  
}  
\[/code\]
