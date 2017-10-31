from django import forms 

class FormName(forms.Form):
			name = form.CharField()
			email = forms.EmailField()
			text = forms.CharField(widget=forms.Textarea)