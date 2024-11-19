from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

UserModel = get_user_model()


class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'account-input',
            })

            field.help_text = ''


class AppUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'account-input',
            })

            field.help_text = ''
