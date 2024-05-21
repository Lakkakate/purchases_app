from django.shortcuts import render
from .models import Purchases

# Create your views here.
def table_home(request):
    goods = Purchases.objects.all()
    return render(request, 'table/table_home.html', goods)
