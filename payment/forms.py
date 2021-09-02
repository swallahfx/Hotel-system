from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('amount', 'email')
        
        # def __unicode__(self):
        #     return self.model
        
        def __str__(self):
            return self.model