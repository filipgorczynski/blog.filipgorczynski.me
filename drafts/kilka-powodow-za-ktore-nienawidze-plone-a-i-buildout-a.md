Title: Kilka powodów za które nienawidzę Plone'a i Buildout'a
Date: 2018-05-11 14:07
Author: filipgorczynski
Category: Tech
Slug: kilka-powodow-za-ktore-nienawidze-plone-a-i-buildout-a
Status: draft

Wymaga instalacji paczek systemowych:

    sudo apt-get install build-essential python-dev libjpeg-dev libxslt-dev supervisor nginx


    https://docs.plone.org/manage/deploying/production/ubuntu_production.html#step-1-platform-preparation

 

Magiczne pożenienie Plone z zc.buildout i Zope.

Niekompatybilność pomiędzy wersjami: zc.buildout, bootstrap.py, setuptools, zope2, ZODB3, zope.\*, Products.\*, plone.app.\*. mr.developer, - często nowsze wersje psują się w innym miejscu lub wymagają wyższych wersji paczek z projektu.

Coraz większe problemy ze znalezieniem paczek Pythona w odpowiednich wersjach

To, że buildout przejdzie bez zająknięcia nie oznacza, że będzie można uruchomić instancję Plone'a

Niewiele mówiące komunikaty błędów lub ich brak - po prostu zapętlenie i próbowanie chyba wszystkich możliwych kombinacji paczek, albo rzucanie

```

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* PICKED VERSIONS \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
\[versions\]

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* /PICKED VERSIONS \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

```

Społeczność - potencjalne propozycje rozwiązań w sieci datuje się często na lata 2008-2010 - bo akurat takie wersje paczek

ZODB -

Brak porządnej dokumentacji.

Wuchtyliard opcji do ustawienia zanim cokolwiek odpalisz

Nieintuicyjny interfejs do zarządzania zainstalowanym Plonem

 
