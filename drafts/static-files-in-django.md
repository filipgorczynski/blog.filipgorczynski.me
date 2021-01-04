Title: Static files in Django
Date: 2021-01-01 09:41
Modified: 2021-01-01 09:41
Category: Tech
Tags: #django, #css, #javascript
Slug: static-files-in-django
Author: filipgorczynski
Status: draft
Summary: I'm still trying to rearrange in my head thing related with static files and their support in Django...

* [ ] create project top-level `static` folder (point it with `STATIFFILES_DIRS`)
* [ ] Set the `STATIC_ROOT` configuration (`settings.py`), which is the absolute location of these collected files, to a folder called `staticfiles` (or any better suited directory).
* [ ] Set - [optional](https://docs.djangoproject.com/en/3.1/ref/settings/#staticfiles-storage) - `STATICFILES_STORAGE`, which is the file storage engine used by `collectstatic` (can be used with some gzipping)
* [ ] Use Django's `collectstatic` command which compiles all static files throughout the project into a single directory suitable for deployment.

STATIC_URL ?
STATIFILES_DIR = [

]
STATIC_ROOT
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

Before each new deployment, the collectstatic command **must be run** to compile them into this `staticfiles` folder used in production.

Because it is easy-to-overlooked, most of the time it's automated.

The most common approach to serve staticfiles in production is to use WhiteNoise package.

And since STATICFILES_STORAGE method changed run `collecstatic` to use the one provided by whitenoise.
