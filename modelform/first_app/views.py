from django.shortcuts import render
from .forms import ContactForm, StudentForm


# Create your views here.
def form(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    else:
        form = ContactForm()
    return render(request, 'form.html',{'form':form})


def model_form(request):
    form = StudentForm(request.POST)
    if form.is_valid():
        form.save()
        print(form.cleaned_data)
    else:
        form = StudentForm()
    return render(request, 'modelform.html',{'form':form})

