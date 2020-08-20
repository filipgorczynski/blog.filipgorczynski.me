Title: Django problem with Geos 3.8 and GEOSException
Date: 2020-01-20 11:07
Author: filipgorczynski
Category: Programowanie
Slug: django-problem-with-geos-3-8-and-geosexception
Status: draft

`GEOSException('Could not parse version info string "%s"' % ver)`.  
The problem is that geos version is `u'3.8.0-CAPI-1.13.1 '` with whitespace which does not met regular expression pattern in file: `u'3.8.0-CAPI-1.13.1 '`. Just strip version.
