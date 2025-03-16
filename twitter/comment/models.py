from django.db import models

# Create your models here.

class Comment(models.Model):
    itself = models.TextField()
    writer = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-sent_date']

    def __str__(self):
        return f"{self.writer}, {self.sent_date}"

