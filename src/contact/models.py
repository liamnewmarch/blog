from django.db import models


class Response(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=500)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        ordering = ('-datetime',)

    def __str__(self):
        return self.name
