from django.db import models

# Create your models here.

class LogEntry(models.Model):
    MEDIA_TYPES = [
        ('BOOK', 'Livro'),
        ('MOVIE', 'Filme'),
        ('Game', 'jogo'),
    ]

    media_type = models.CharField(max_length=5, choices=MEDIA_TYPES)
    title = models.CharField(max_length=200)
    rating = models.IntegerField()
    comment = models.TextField()
    logged_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_media_type_display()}: {self.title} {self.rating}/5"