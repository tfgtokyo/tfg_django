from django.test import TestCase
# from django.core.urlresolvers import reverse old
from django.urls import reverse, resolve
# Create your tests here.


class IndexTests(TestCase):
    def test_index_view_status_code(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
