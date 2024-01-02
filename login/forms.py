from django import forms
from django.contrib.auth.models import User


class CreateUserForm(forms.ModelForm):
    confirm = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def clean_confirm(self):
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')

        if password and confirm and password != confirm:
            raise forms.ValidationError("As senhas não coincidem.")

        return confirm
    
    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user