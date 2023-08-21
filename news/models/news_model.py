from django.db import models
from news.validators import validate_title_word_count


class News(models.Model):
    title = models.CharField(
        max_length=200, validators=[validate_title_word_count]
    )
    content = models.TextField()
    author = models.ForeignKey("Users", on_delete=models.CASCADE)
    created_at = models.DateField()
    image = models.ImageField(upload_to="img/", null=True, blank=True)
    categories = models.ManyToManyField("Categories")

    def __str__(self) -> str:
        return self.title
