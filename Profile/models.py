from django.db import models

# Importaciones de modelos
from django.contrib.auth.models import User

# Create your models here
class Profile(models.Model):
    id_user = models.OneToOneField(User, on_delete = models.CASCADE, null=False, blank=False)
    # name=models.CharField(User)
    url_img = models.ImageField(null=True,blank=True, default='/assets/img-profile/Jirafita.png', upload_to='img-profile/')
    # created = models.DateTimeField(default = timezone.now)
    # edited =  models.DateTimeField(blank=True, null=True, default=None) 
    
    class Meta:
        db_table: 'Profile'
        