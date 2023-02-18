from .models import uid
from django.forms import ModelForm

class uidform(ModelForm):
    class Meta:
        model = uid
        fields = ['uid_arr']
