import os

from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from captionadder.views import index

# Create your tests here.

class HomePageTest(TestCase):

    def test_index_template(self):
        request = HttpRequest()
        response = self.client.get('/')
        html = response.content.decode('utf8')

        self.assertTemplateUsed(response, 'captionadder/index.html')

    def test_get_image_from_post(self):
        path_to_img = os.path.abspath('assets\\test_image.jpg')
        response = self.client.post('/', data={'file_upload_button':path_to_img})
        self.assertIn('id="user_image"', response.content.decode())
