from django import forms

class FeedBack(forms.Form):

    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    phone = forms.CharField(max_length=15)
    car = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)
