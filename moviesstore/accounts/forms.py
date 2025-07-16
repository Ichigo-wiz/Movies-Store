from django.contrib.auth.forms import UserCreationForm

class CustomSignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in ['username', 'password1', 'password2']:
            self.fields[field].help_text = None 
            self.fields[field].widget.attrs.update({'class':'form-control'})