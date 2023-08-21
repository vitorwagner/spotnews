from django import forms
from .models import Categories, News, Users


class CategoryForm(forms.ModelForm):
    name = forms.CharField(label="Nome", max_length=200)

    class Meta:
        model = Categories
        fields = ["name"]


class NewsForm(forms.ModelForm):
    title = forms.CharField(label="Título", max_length=200)
    content = forms.CharField(label="Conteúdo", widget=forms.Textarea)
    author = forms.ModelChoiceField(
        label="Autoria", queryset=Users.objects.all()
    )
    created_at = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), label="Criado em"
    )
    image = forms.ImageField(label="URL da Imagem")

    class Meta:
        model = News
        fields = [
            "title",
            "content",
            "author",
            "created_at",
            "image",
        ]
