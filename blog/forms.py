from django import forms
from .models import Post
from .models import Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "featured_image", "status"]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if not title or title.strip() == "":
            raise forms.ValidationError("Title cannot be empty.")
        return title

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if not content or content.strip() == "":
            raise forms.ValidationError("Content cannot be empty.")
        return content

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"placeholder": "Enter a title..."})
        self.fields["content"].widget.attrs.update(
            {"placeholder": "Write your post content here..."}
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']    


class NewsletterSignupForm(forms.Form):
    email = forms.EmailField(label="Your email") 
