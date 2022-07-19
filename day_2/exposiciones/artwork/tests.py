from django.test import TestCase

from artwork.models import Type, Author, Artwork

# Create your tests here.

class TypeModelTest(TestCase):
  def setUp(self):
    Type.objects.create(name='test', status=True)
    
  def test_type_not_blank(self):
    type_artwork = Type.objects.get(id=1)
    self.assertEqual(type_artwork.name, 'test')
