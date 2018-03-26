#Last Modified 23rd March
#ADETUNJI KAYODE
#Resources are referenced and linked here

from import_export import resources
from .models import Industry

class IndustryResource(resources.ModelResource):
    class Meta:
        model = Industry


