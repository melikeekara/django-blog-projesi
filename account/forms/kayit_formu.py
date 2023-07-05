from django.contrib.auth.forms import UserCreationForm
from account.models import CustomUserModel
class KayitFormu(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

