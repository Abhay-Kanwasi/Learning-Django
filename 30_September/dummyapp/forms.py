from django import forms
from .models import Article

class ContactForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'content']

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError('Title must be at least 5 characters')
        return title
