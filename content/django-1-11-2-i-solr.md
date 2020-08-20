Title: Django 1.11.2 i Solr
Date: 2017-07-22 17:27
Author: filipgorczynski
Category: Bazy danych, Programowanie, Rozwiązania
Slug: django-1-11-2-i-solr
Status: draft

 

./bin/solr create -c blog

zostanie utworzona lista plików (nowy core).

    polecenie build_solr_schema w haystack rzuca błędem:
    [code language="text"]
    TypeError: context must be a dict rather than Context.
    [/code]
    Usunąć Context w metodzie build_context.
