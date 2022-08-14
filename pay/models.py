
from django.db import models
import secrets
# Create your models here.
from .paystack import Paystack
from authentication.models import *

class Payment(models.Model):
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length=200)
    email = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self) -> str:
        return f"Payment: (self.amount)"

    def save(self, *args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(10)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs) 


    def amount_value(self) -> int:
        return self.amount * 100

    def verify_payment(self):
        paystack = Paystack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 100 == self.amount:
                self.verified = True
                self.save()
        if self.verified:
            return True
        return False