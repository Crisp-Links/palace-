

from tkinter.tix import Tree
from django import forms
from crispy_forms.helper import FormHelper

from core.models import * 

class PropertyForm(forms.ModelForm):
    """Form definition for Property."""


    amenities = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset = Amenity.objects.all(),
    )
    class Meta:
        """Meta definition for CreatePropertyform."""

        model = Property
        fields = '__all__'
        exclude = ['user', 'ref']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['district'].queryset = District.objects.none()
    
        if 'region' in self.data:
            try:
                region_id = int(self.data.get('region'))
                self.fields['district'].queryset = District.objects.filter(region_id=region_id).order_by('name')
            except:
                pass
        elif self.instance.pk:
            self.fields['district'].queryset = self.instance.region.district_set.order_by('name')