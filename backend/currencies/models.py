from django.db import models


class CurrencyName(models.Model):
    name = models.CharField(max_length=35)
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Currency name"
        verbose_name_plural = "Currency names"


class CurrencyDate(models.Model):
    date = models.DateField(db_index=True)

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name = "Currency date"
        verbose_name_plural = "Currency dates"


class CurrencyValue(models.Model):
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=8)
    currency_name = models.ForeignKey("CurrencyName", related_name="currency_values", on_delete=models.CASCADE)
    currency_date = models.ForeignKey("CurrencyDate", related_name="currency_values", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.exchange_rate)

    class Meta:
        verbose_name = "Currency value"
        verbose_name_plural = "Currency Values"
        unique_together = ["currency_name", "currency_date"]
