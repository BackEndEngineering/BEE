from django.test import TestCase
from Beehive.models import Article
# Create your tests here.
class ArticlesTestCase(TestCase):
    def setUp(self):
        Article.objects.create(title="Test #1")
        Article.objects.create(title="Test #2")
        Article.objects.create(title="Test #3")

    def testArticleFields(self):
        """Test basic article fields"""
        first = Article.objects.get(title="Test #1")
        self.assertEquals("Test #1", first.title)
