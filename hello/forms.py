from django import forms
from .models import Friend

# 2章の内容=====================================================
# class HelloForm(forms.Form):
#     name = forms.CharField(label='name', max_length=20,
#         widget=forms.TextInput(
#         attrs = {'placeholder':'ユーザ名'}))
#     mail = forms.CharField(label='mail')
#     age = forms.IntegerField(label='age')
#     birthday = forms.DateField(label='birthday(yyyy-mm-dd)')
#     check = forms.BooleanField(label='CheckBox', required=False)
#     data_choice = [
#         ('one', 'item 1'),
#         ('two', 'item 2'),
#         ('three', 'item 3'),
#         ('cat', '猫')
#     ]
#     choice = forms.ChoiceField(label='choice', choices=data_choice)
#     data_radio = [
#         ('one', 'item 1'),
#         ('two', 'item 2'),
#         ('three', 'item 3'),
#         ('cat', '猫')
#     ]
#     radio = forms.ChoiceField(label='radio', choices=data_radio, widget=forms.RadioSelect())
#     data_select = [
#         ('one', 'item 1'),
#         ('two', 'item 2'),
#         ('three', 'item 3'),
#         ('cat', '猫')
#     ]
#     select = forms.ChoiceField(label='select', choices=data_select, widget=forms.Select(attrs={'size':4}))
#     data_multiple_select = [
#         ('one', 'item 1'),
#         ('two', 'item 2'),
#         ('three', 'item 3'),
#         ('cat', '猫')
#     ]
#     multiple_select = forms.MultipleChoiceField(label='multiple_select', choices=data_multiple_select, widget=forms.SelectMultiple(attrs={'size':4}))
# 2章の内容=====================================================


# 3章の内容=====================================================
# class HelloForm(forms.Form):
#     id = forms.IntegerField(label='ID')
# 3章の内容=====================================================


# 3-24=====================================================
class HelloForm(forms.Form):
    name = forms.CharField(label='Name')
    mail = forms.EmailField(label='Email')
    gender = forms.BooleanField(label='Gender', required=False)
    age = forms.IntegerField(label='Age')
    birthday = forms.DateField(label='Birth')
# 3-24=====================================================


# 3-29=====================================================
class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'mail', 'gender', 'age', 'birthday']
# 3-29=====================================================