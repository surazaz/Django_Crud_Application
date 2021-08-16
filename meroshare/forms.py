from django import forms  
from meroshare.models import MeroShare  
class ShareForm(forms.ModelForm):  
    class Meta:  
        model = MeroShare  
        fields = "__all__"  