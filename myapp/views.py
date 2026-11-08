from django.shortcuts import render


def home(request):
    return render(request, 'myapp/spark_admin/index.html')
