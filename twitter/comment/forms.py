from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['itself']
        widgets = {
            'itself': forms.Textarea(attrs={
                'placeholder': 'Bu yerga yozishingiz mumkin... ',
                'rows': 1,  # Single line by default
                'style': 'overflow: hidden;'  # Prevents scrollbar until needed
            }),
        }