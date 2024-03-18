from django import forms
from .models import NATO_Member, News, InfoNATO, Story

class CountryForm(forms.ModelForm):
    class Meta:
        model = NATO_Member
        fields = ['name', 'description', 'photo']  


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'image']

class NATOInfoForm(forms.ModelForm):
    class Meta:
        model = InfoNATO
        fields = ['name', 'description', 'photo']

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'content']

class DeleteStoryForm(forms.Form):
    story_id = forms.IntegerField(widget=forms.HiddenInput())

class EditStoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'content']