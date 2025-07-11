from django import forms

from application.models import Cake


class CakeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CakeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Cake
        exclude = ('baker',)
