from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee
import csv
from django.views.generic import  TemplateView


# Create your views here.
def CSVPage(request, *args, **kwargs):
    person = Employee.objects.all()
    return render(request, "csv_page.html", {"person":person})

class ReportDownload(TemplateView):

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'
        ] = 'attachment; filename="sample.csv"'
        writer = csv.writer(response)
        writer.writerow(
            [
                'First Name', 'Last Name', 'Location'   
            ]
        )
        results = Employee.objects.all()
        for data in results:
            try:
                writer.writerow(
                    [
                        data.first_name,
                        data.last_name,
                        data.location,
                    ]
                )
            except Exception as e:
                print(e)
        return response

