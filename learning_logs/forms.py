from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.TextInput(attrs={'placeholder':'Add New Topic', 'cols':80})}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False, widget=forms.TextInput(attrs={
        'class': 'border-2 border-gray-300 p-2 w-full',
        'placeholder': 'Search topics'
    }))