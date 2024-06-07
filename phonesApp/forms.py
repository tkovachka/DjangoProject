from django import forms
from phonesApp.models import Phone


class PhoneForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PhoneForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = "form-control"
        self.fields['isNew'].widget.attrs['class'] = "form-check-input"

    class Meta:
        model = Phone
        fields = "__all__"
        exclude = ["user"]
