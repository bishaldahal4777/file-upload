from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

def user_upload_path(instance, filename):
    # media/user_<id>/<filename>
    return f"user_{instance.user.id}/{filename}"

class Upload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to=user_upload_path, null=True, blank=True)
    file = models.FileField(upload_to=user_upload_path, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.title or self.file.name or self.image.name}"
