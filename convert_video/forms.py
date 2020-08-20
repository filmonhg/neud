from django import forms
class YouTubeLink(forms.ModelForm):
    youtube_link = forms.CharField(label='YouTube Link', max_length=200)
