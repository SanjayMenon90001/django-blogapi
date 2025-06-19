from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from blog.factories import PostFactory

#posts test
class PostAPITestCase(APITestCase):
    def setUp(self):
        self.post = PostFactory()

    def test_get_post_list_returns_200(self):
        url = reverse('post-list')  # Or use "/api/posts/" if this fails
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

#pagination test 
def test_post_list_has_pagination_metadata(self):
    # Create 12 posts — this should be more than 1 page
    PostFactory.create_batch(12, author=self.user)

    url = reverse('post-list')  # or use "/api/posts/"
    response = self.client.get(url)

    self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Check for pagination keys in response
    self.assertIn('count', response.data)
    self.assertIn('next', response.data)
    self.assertIn('results', response.data)
