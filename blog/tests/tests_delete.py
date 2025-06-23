from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from blog.factories import PostFactory, UserFactory


# delete test
class PostAPITestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory(username="owner")
        self.other_user = UserFactory(username="intruder")
        self.post = PostFactory(author=self.user)

    def test_only_owner_can_delete_post(self):
        url = f"/api/posts/{self.post.id}/"

        # Try deleting as someone else
        self.client.login(username="intruder", password="pass123")
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.logout()

        # Try deleting as the owner
        self.client.login(username="owner", password="pass123")
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
