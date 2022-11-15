from django.urls import path
from .views import CSVPage,ReportDownload

urlpatterns = [
    path("", CSVPage, name="csv_page"),
    path("download-report/", ReportDownload.as_view(), name="download-report"),
]
