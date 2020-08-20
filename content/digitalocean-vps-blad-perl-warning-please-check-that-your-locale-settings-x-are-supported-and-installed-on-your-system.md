Title: DigitalOcean VPS - błąd: perl warning - please check that your locale settings X are supported and installed on your system
Date: 2019-04-25 13:38
Author: filipgorczynski
Category: Programowanie
Slug: digitalocean-vps-blad-perl-warning-please-check-that-your-locale-settings-x-are-supported-and-installed-on-your-system
Status: draft

````
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
    LANGUAGE = (unset),
    LC_ALL = (unset),
    LANG = "en_US.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
locale: Cannot set LC_CTYPE to default locale: No such file or directory
locale: Cannot set LC_MESSAGES to default locale: No such file or directory
locale: Cannot set LC_ALL to default locale: No such file or directory
```
````

locale-gen en_US en_US.UTF-8 pl_PL pl_PL.UTF-8

```
dpkg-reconfigure locales
```
