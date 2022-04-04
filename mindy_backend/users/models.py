from django.db import models


# Create your models here.
class User(models.Model):

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    created_time = models.DateField(auto_now=True)
    has_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_time']
        verbose_name = "User"
        verbose_name_plural = verbose_name


class Confirm_Message(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.name + ": " + self.code

    class Meta:
        ordering = ["-created_time"]
        verbose_name = "Verification code"
        verbose_name_plural = verbose_name
