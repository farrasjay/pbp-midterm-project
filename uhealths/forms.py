from django import forms

class HealthStatsForm(forms.Form):
    age = forms.IntegerField(label="age", required=True)
    gender = forms.CharField(label="gender", max_length=6)
    height = forms.IntegerField(label="height", required=True)
    weight = forms.IntegerField(label="weight", required=True)
    calories_intake = forms.IntegerField(label="calories_intake", required=True)