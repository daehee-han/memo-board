from django.db import models

# Create your models here.
class Memo(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('auth.User')
    upload_time = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return str(self.text)