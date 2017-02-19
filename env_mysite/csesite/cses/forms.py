from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField(widget = forms.Textarea(attrs={'class':"materialize-textarea"}))
class ChatForm(forms.Form):
	Name = forms.CharField()
	Email = forms.EmailField()
	Subject = forms.CharField()
	