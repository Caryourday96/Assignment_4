from django.shortcuts import render
#ADETUNJI KAYODE
#Last Modified 23rd March
# Create your views here.
from tablib import Dataset
from .resources import IndustryResource

def simple_upload(request):
    if request.method == 'POST':

       industry_resource = IndustryResource()
        dataset = Dataset()
        new_industry = request.FILES['myfile']

        imported_data = dataset.load(new_industry.read())
        result = industry_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            industry_resource.import_data(dataset, dry_run=False)  # Actually import now


        return render(request, 'core/simple_upload.html')

