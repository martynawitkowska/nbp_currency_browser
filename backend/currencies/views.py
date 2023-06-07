from django.views.generic import FormView

from . import forms, models


class CurrencyFormView(FormView):
    form_class = forms.CurrencyForm
    template_name = "currencies/currency_form.html"
    success_url = "/"

    def form_valid(self, form):
        start_date = form.cleaned_data.get("start_date")
        end_date = form.cleaned_data.get("end_date")
        currencies = models.CurrencyName.objects.all()

        currency_data = models.CurrencyValue.objects.filter(currency_date__date__range=(start_date, end_date))

        context = self.get_context_data()
        context.update({"currency_data": currency_data})

        return self.render_to_response(context)

    def get_form(self, form_class=None):
        currencies = models.CurrencyName.objects.all()
        form = super().get_form(form_class)

        form.fields["currency"].choices = [(currency.code, currency.name.title()) for currency in currencies]

        return form
