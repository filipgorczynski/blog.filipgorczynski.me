Title: Usuwanie znaków interpunkcyjnych z łańcucha znaków
Date: 2017-12-07 13:29
Author: filipgorczynski
Category: Tech
Slug: usuwanie-znakow-interpunkcyjnych-z-lancucha-znakow
Status: draft

Usuwanie znaków interpunkcyjnych z łańcucha znaków:

\[code language="python"\]  
import re  
import string  
pattern = re.compile(r'\[{}\]+'.format(string.punctuation))  
pattern.sub('', word).strip()  
\[/code\]

\[code language="python"\]\</pre\>  
\<pre\>"""Tests for ingredients name fuzzy search."""  
from parameterized import param, parameterized  
from rest\_framework.reverse import reverse  
from rest\_framework.test import APITestCase

from gcplus\_ews.test\_utils import AuthTestMixin

class FuzzySearchTestCase(AuthTestMixin, APITestCase):  
"""APITestCase class for ingredients name fuzzy search."""

fixtures = \[  
'modules\_test\_data',  
'search\_data',  
\]  
multi\_db = True

def setUp(self):  
"""Hook method for setting up the test fixture before exercising it."""  
super().setUp()  
self.URL = reverse('search-list')  
self.data = {  
'module\_id': 1,  
'identifier\_type': 'Name',  
}

\@parameterized.expand(\[  
param('', 7),  
param('acid', 6),  
param('sulphur', 0),  
param('@@@', 0),  
param('@@@ @@@', 0),  
param('acid drink', 5),  
param('@@@ drink', 5),  
param('acid @@@@@', 6),  
param('@@\@acid@@@ @@\@drink@@@', 5),  
param('drink acid', 5),  
param('AcId', 6),  
param('\_\_\_', 0),  
param('????', 0),  
param('\*', 0),  
param('żółw', 1),  
param('\@żółw@', 1),  
\])  
def test\_ingredient\_search(self, query, rows\_quantity):  
"""Search ingredient by query string

:param query: Query with ingredient search  
:param rows\_quantity: Quantity of returned elements  
"""  
self.data.update({'q': query})  
response = self.authorized\_get(self.URL, data=self.data,)  
self.assertEqual(  
response.data\['count'\],  
rows\_quantity,  
msg="Query: '{}', expeted {} results".format(query, rows\_quantity),  
)  
\[/code\]
