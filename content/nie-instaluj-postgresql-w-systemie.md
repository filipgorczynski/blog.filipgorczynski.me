Title: Nie instaluj PostgreSQL w systemie
Date: 2020-06-02 06:34
Author: filipgorczynski
Category: Tech
Slug: nie-instaluj-postgresql-w-systemie
Lang: pl
Status: draft


Od zawsze jednym z podstawowych programów, które instalowałem w systemie był PostgreSQL. Baza danych używana praktycznie w każdym moim projekcie. Jednak dużo zaczęło się komplikować, gdy pracowałem z innymi programistami albo z pewnymi wymaganiami stawianymi przez projekt.

<!-- /wp:paragraph -->

<!-- wp:syntaxhighlighter/code -->

```
docker run -p 5432:5432
  -e POSTGRES_PASSWORD=postgres
  -e POSTGRES_USER=postgres
  -e POSTGRES_DB=djobeet_dev
  -v pgdata:/var/lib/postgresql/data
  --name djobeet_db_dev
  -d postgres;
2a2692d0a2531dd3289c0fd25f9c05e0ee7febec2ef13f8ee40e38df8657f9fd

psql djobeet_dev -h localhost -U postgres
> PASSWORD

docker exec -it ID psql -U postgres djobeet_dev


src/SynApps/djobeet-project 
➜ psql djobeet_dev -U postgres -h localhost
Hasło użytkownika postgres: 
psql (11.8, serwer 12.2 (Debian 12.2-2.pgdg100+1))
OSTRZEŻENIE: psql wersja główna 11, wersja główna serwera 12.
             Niektóre cechy psql mogą nie działać.
Wpisz "help" by uzyskać pomoc.

djobeet_dev=# exit


docker run --name djobeet_db_dev -v "$PWD"/:/opt/demo/ -e POSTGRES_PASSWORD=postgres -d postgres;
docker exec -it djobeet_db_dev psql -U postgres -c "CREATE DATABASE djobeet_db"
```

<!-- /wp:syntaxhighlighter/code -->

<!-- wp:paragraph -->

Document  
Block

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

No block selected.  
Open publish panel  
Document

<!-- /wp:paragraph -->
