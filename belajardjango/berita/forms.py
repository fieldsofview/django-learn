from django import forms

class ChoiceCheckForm(forms.Form):
    choice = forms.ChoiceField(label='Choice',
                                choices=[('rock','rock'),('paper','paper'),('scissors','scissors')],
                                )
