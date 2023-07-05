from django import forms
from bloge.models import YazilarModel

class YaziGuncelleFormModel(forms.ModelForm):
    class Meta:
        model = YazilarModel
        exclude = ('yazar', 'slug')