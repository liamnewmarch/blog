from django.test import TestCase

from .models import Post


class PostTestCase(TestCase):
    fixtures = ('fixtures/placeholder.yaml',)

    def test_post_fixture(self):
        self.assertEqual(Post.objects.count(), 1)

    def test_post_has_slug(self):
        foo = Post.objects.first()
        foo.title = 'Foo bar'
        foo.slug = None
        foo.save()
        self.assertEqual(foo.slug, 'foo-bar')

    def test_post_has_body(self):
        foo = Post.objects.first()
        foo.body_markdown = 'Hello, world'
        self.assertEqual(foo.body, '<p>Hello, world</p>')
