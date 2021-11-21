from django.shortcuts import render
from django.http import HttpResponse
from .feature_extraction import feature_extraction
from .topsis import topsis
from .forms import rangeform
# Create your views here.

def home(request):
    
    if request.method=='POST':
        form=rangeform(data=request.POST)
        if form.is_valid():
            rnge=form.cleaned_data['price_range_']
            print(rnge)
            names,inputlst=feature_extraction(rnge)
            ranks=topsis(inputlst)
            objects=zip(names,ranks)
            return render(request,'home.html',{'form':form,"objects":objects})

    else:
        names=['a','b','c']
        ranks=[1,2,3]
        objects=zip(names,ranks)
        form=rangeform(data=request.POST)
        return render(request,"home.html",{"form":form,"objects":objects})