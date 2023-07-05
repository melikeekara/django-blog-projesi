from django import forms
from bloge.models import YazilarModel

class YaziEkleModelForm(forms.ModelForm):
    class Meta:
        model = YazilarModel
        exclude = ('yazar', 'slug')