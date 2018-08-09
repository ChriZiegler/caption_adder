from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from captionadder.views import index

# Create your tests here.

class HomePageTest(TestCase):

    def test_index_view(self):
        found_page = resolve('/')
        self.assertEqual(found_page.func, index)

    def test_index_html(self):
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf8')

        self.assertIn('Snapchat Caption Adder', html)
