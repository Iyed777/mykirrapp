from django.shortcuts import render
from django.views import View
# Create your views here.

from .forms import SubmitURLForm

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitURLForm()
        context = {
            "title": "Submit form",
            "form": the_form
        }
        return render(request, "home.html", context)


    def post(self, request, *args, **kwargs):
        form = SubmitURLForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        context = {
            "title": "Submit form",
            "form": form
        }
        return render(request, "home.html", context)
