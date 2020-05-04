from django import forms

class HelloForm(forms.Form):
    name = forms.CharField(label='name', max_length=20,
        widget=forms.TextInput(
        attrs = {'placeholder':'ユーザ名'}))
    mail = forms.CharField(label='mail')
    age = forms.IntegerField(label='age')
    birthday = forms.DateField(label='birthday(yyyy-mm-dd)')
    check = forms.BooleanField(label='CheckBox', required=False)
    data = [
        ('one', 'item 1'),
        ('two', 'item 2'),
        ('three', 'item 3')
    ]
    choice = forms.ChoiceField(label='choice', choices=data)