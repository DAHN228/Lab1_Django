from django import forms


class UserForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, help_text="Введите текст")

