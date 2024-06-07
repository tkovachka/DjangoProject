from django.http import HttpResponse
from django.shortcuts import render, redirect

from phonesApp.forms import PhoneForm
from phonesApp.models import Phone


# Create your views here.

def phones(request):
    context = {"phones": Phone.objects.all()}
    return render(request, 'phones.html', context)


def details(request, phone_id):
    phone = Phone.objects.get(id=phone_id)
    context = {"phone": phone}
    return render(request, "details.html", context)


def add_phone(request):
    if request.method == "POST":
        form = PhoneForm(request.POST, files=request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.image = form.cleaned_data['image']
            item.user = request.user
            item.save()
            return redirect('phones')
    else:
        phone = PhoneForm()

    return render(request, "add_form.html", {"form": phone})


def edit(request, phone_id):

    phone = Phone.objects.filter(id=phone_id).get()
    if request.method == "POST":
        form = PhoneForm(request.POST, instance=phone, files=request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.image = form.cleaned_data["image"]
            item.user = request.user
            item.save()
            return redirect("phones")
    else:
        form = PhoneForm(instance=phone)

    return render(request, "edit_phone.html", {"form": form})


def delete(request, phone_id):
    phone = Phone.objects.get(id=phone_id)
    context = {"phone": phone}
    if request.method == "POST":
        phone.delete()
        return redirect("phones")

    return render(request, "delete_phone.html", context)
