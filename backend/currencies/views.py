from django.shortcuts import render
from django.views.generic import FormView

from . import forms


class CurrencyFormView(FormView):
    form_class = forms.CurrencyForm
    template_name = "currencies/currency_form.html"
    success_url = "/"
