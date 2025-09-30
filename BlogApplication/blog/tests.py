from django.test import TestCase
# Replicate into a new database
from .models import Post


class ModelTesting(TestCase):

    # It will be run first
    def setUp(self):
        # It will create some new data using default model manager(objects)
        self.blog = Post.objects.create(title = 'django', author = 'django', slug = 'django')

    def test_post_model(self):
        d = self.blog
        # data is d and database is Post If blog worked and data stored in database(Post) it will return True (Means OK)
        self.assertTrue(isinstance(d, Post)) 
        # We will check if two things are equal
        self.assertEqual(str(d), 'django') # d will return django and in second parameter we giving 'django' to check if str(d) value is equal to django

