Title: CRON - regularny backup baz danych
Date: 2019-04-25 13:48
Author: filipgorczynski
Category: Tech
Slug: cron-regularny-backup-baz-danych
Status: draft

\$\> mysqldump --defaults-file=\~/mysql.cnf -u root zarembastore\_dev \> \~/zarembastore\_backup.sql

\~/mysql.cnf  
\[mysqldump\]  
user=root  
password=xtest

\[client\]  
user=root  
password=xtest
