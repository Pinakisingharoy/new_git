from django.shortcuts import render
from .models import Invoice
# Create your views here.

def index(request):
    item=Invoice.objects.all()
    return render (request,"myapp/item.html",{'item':item})

def accept(request):
    if request.method=='POST':
        name=request.POST.get('name','')
        phone=request.POST.get('phone','')
        address=request.POST.get('address','')
        item=request.POST.get('item','')
        summary=request.POST.get('summary','')
        database=Invoice(name=name,phone=phone,address=address,item=item,summary=summary)
        database.save()

    return render (request,"myapp/show.html")