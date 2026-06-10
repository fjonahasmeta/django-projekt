from django import forms
from .models import Post, Review, Booking, HelpMessage


# 🏠 POST FORM
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'image']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Titulli i postit'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Përshkrimi...'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Autori'
            }),
        }


# ⭐ REVIEW FORM
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'comment', 'rating']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Emri yt'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Shkruaj koment...'
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 5
            }),
        }


# 📅 BOOKING FORM
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'date']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Emri'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }


# 💬 HELP / SUPPORT FORM (FINAL + DB READY)
class HelpMessageForm(forms.ModelForm):
    class Meta:
        model = HelpMessage
        fields = ['name', 'email', 'message']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Emri yt'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email yt'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Shkruaj mesazhin këtu...'
            }),
        }