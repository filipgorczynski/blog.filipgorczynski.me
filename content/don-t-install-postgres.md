Title: Don't install Postgres
Date: 2020-06-01 08:45
Author: filipgorczynski
Category: Programowanie
Slug: don-t-install-postgres
Status: draft

<!-- wp:paragraph -->```  
docker run -p 5432:5432 \\  
-e POSTGRES\_PASSWORD=postgres \\  
-e POSTGRES\_USER=postgres \\  
-e POSTGRES\_DB=djobeet\_dev \\  
-v pgdata:/var/lib/postgresql/data \\  
--name djobeet\_db\_dev \\  
-d postgres;  
2a2692d0a2531dd3289c0fd25f9c05e0ee7febec2ef13f8ee40e38df8657f9fd

psql djobeet\_dev -h localhost -U postgres  
\> PASSWORD

docker exec -it ID psql -U postgres djobeet\_dev

src/SynApps/djobeet-project  
➜ psql djobeet\_dev -U postgres -h localhost  
Hasło użytkownika postgres:  
psql (11.8, serwer 12.2 (Debian 12.2-2.pgdg100+1))  
OSTRZEŻENIE: psql wersja główna 11, wersja główna serwera 12.  
Niektóre cechy psql mogą nie działać.  
Wpisz "help" by uzyskać pomoc.

djobeet\_dev=\# exit

docker run --name djobeet\_db\_dev -v "\$PWD"/:/opt/demo/ -e POSTGRES\_PASSWORD=postgres -d postgres;  
docker exec -it djobeet\_db\_dev psql -U postgres -c "CREATE DATABASE djobeet\_db"  
```<!-- /wp:paragraph -->
