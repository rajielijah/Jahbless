from django import forms
from .models import Author

top_choices = (
	('general', "General Enquiry"),
	('bug', 'Bug Report'),
	('suggestion', 'Suggestion')
	)

class ContactForm(forms.Form):
	choices = forms.ChoiceField(choices = top_choices)
	message = forms.CharField()
	sender = forms.EmailField(required =False)

