from django import forms

class SendQuestionForm(forms.Form) :
    question_in_form = forms.CharField(max_length=500)