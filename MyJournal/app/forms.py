from django import forms

class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'autocomplete': 'off'
        })

    username = forms.CharField(label='Username', max_length=20, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)

class SignupForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'autocomplete': 'off'
        })

    username = forms.CharField(label='Username', max_length=20, required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Password (again)', widget=forms.PasswordInput, required=True)

class PostForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({
            'autocomplete': 'off'
        })

    content = forms.CharField(widget=forms.Textarea(attrs={"rows": "5"}), label='', max_length=2048, required=True)

class UpdateForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({
            'autocomplete': 'off'
        })

    content = forms.CharField(label='', max_length=2048, required=True)