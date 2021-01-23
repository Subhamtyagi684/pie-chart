from django.shortcuts import render
from .forms import PiedataForm

# Create your views here.

def home(request):
    if request.method=='POST':
        form = PiedataForm(request.POST)
        sum = [i for i in range(1,6)]
        if form.is_valid():
            title = request.POST.get('title')
            context = {'title':title,'form':form,'sum':sum}
            for i in range(1,6):
                context['column1'+str(i)] = request.POST.get(f'column1{str(i)}','')
                context['column2'+str(i)] = request.POST.get(f'column2{str(i)}','')
            return render(request,'piechart.html',context)
        return render(request,'home.html',{'form':form,'sum':sum})
    form = PiedataForm
    sum = [i for i in range(1,6)]
    return render(request,'home.html',{'form':form,'sum':sum})