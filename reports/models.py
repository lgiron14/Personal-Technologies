from django.db import models

class Report(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    generated_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='reports/', null=True, blank=True)

    def __str__(self):
        return self.title
