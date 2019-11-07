from io import BytesIO

from PIL import Image
from django.core.files.base import ContentFile
from django.db import models

from users.models import User


class UploadedImage(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    imagefile = models.ImageField("Uploaded image", max_length=255, null=True, blank=True)  # stores the filename of an uploaded image
    path_to_image = models.CharField(null=True, max_length=100)

    def save(self, *args, **kwargs):
        if not self.id and not self.imagefile:
            return

        original_image = Image.open(self.imagefile)
        (width, height) = original_image.size

        ratio = min(1080/width, 1920/height)
        (width, height) = (width * ratio, height * ratio)
        new_image = original_image.resize((int(width), int(height)), Image.ANTIALIAS)

        new_image_io = BytesIO()
        new_image.save(new_image_io, format='JPEG', dpi=[401, 401])

        temp_name = self.imagefile.name
        self.imagefile.delete(save=False)

        self.imagefile.save(
            temp_name,
            content=ContentFile(new_image_io.getvalue()),
            save=False
        )

        super(UploadedImage, self).save(*args, **kwargs)