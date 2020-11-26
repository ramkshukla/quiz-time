from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import NameForm
# Create your views here.


def fun(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index2.html')
    else:
        form = NameForm()
        return render(request, 'index.html', {'form': form})
