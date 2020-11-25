from django import forms
from vaccineapp.models import Person

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, label='Имя вакцины', required=False)


class BootstapForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class' : 'form-control'})
        # self.fields['myfield'].widget.attrs.update({'class' : 'myfieldclass'})


class PersonForm(BootstapForm):
    class Meta:
        model = Person
        # fields= "__all__"
        fields= ('name', 'dateofbirth', 'sex')