#ADETUNJI KAYODE
#Last Modified 23rd March
#Used to test
from django.test import TestCase

# Create your tests here.

from Test.models import Industry

class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Industry.objects.create( Vector="100",COMMOD='Rice' )

    def test_first_name_label(self):
        industry=Industry.objects.get(id=1)
        field_label = industry._meta.get_field('Vector').verbose_name
        self.assertEquals(field_label,'Vector')


    def test_first_name_max_length(self):
        industry=Industry.objects.get(id=1)
        max_length = industry._meta.get_field('COMMOD').max_length
        self.assertEquals(max_length,100)

