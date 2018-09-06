import os

from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from selenium import webdriver



class NormalUserExperience_Chrome(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_canVisitSiteAndUploadImage(self):
        self.browser.get('http://localhost:8000')
        # User enters site and see that it is for adding captions to images
        self.assertIn('Caption', self.browser.title)

        # A placeholder image exists on the side
        img_holder = self.browser.find_element_by_id('user_image_holder')
        placeholder_img = img_holder.find_element_by_tag_name('img')
        self.assertIsNotNone(placeholder_img)

        # User sees button for uploading images
        button = self.browser.find_element_by_name('file_upload_button')
        self.assertEqual(button.get_attribute('type'), 'file')

        # User clicks the button and is prompted to upload an image
        form = self.browser.find_element_by_id('file_upload_form')
        path_to_img = os.path.abspath('assets\\test_image.jpg')
        button.send_keys(path_to_img)


        # User uploads image

        # User is prompted to enter a caption

        # User enters caption

        # Image with caption appears on web page in place of previous placeholder
        user_img = img_holder.find_element_by_tag_name('img')
        self.assertNotEqual(user_img, placeholder_img)
        self.fail('Finish the test!')
