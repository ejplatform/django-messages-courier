from django import forms


class NotificationSendInBulkForm(forms.Form):
    sender = forms.CharField(max_length=50)
    title = forms.CharField(max_length=200)
    short_description = forms.CharField(widget=forms.Textarea)
