from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

    
    
# class UserProfile(AbstractUser):
#     username = models.CharField(max_length=100, unique=True)
#     market_name = models.CharField(max_length=100, blank=True) 
#     role = models.CharField(max_length=50, default="Market Manager") 
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=15, blank=True, null=True)
#     profile_picture = models.ImageField(upload_to='profile_picture/', blank=True, null=True) 
    
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     groups = models.ManyToManyField(Group, related_name='market_manager_set', blank=True)
#     user_permissions = models.ManyToManyField(Permission, related_name='market_manager_set', blank=True)

#     def __str__(self):
#         return f"{self.username} - {self.role} - {self.market_name}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    username = models.CharField(max_length=100, blank=True) 
    market_id = models.CharField(max_length=100, blank=True) 
    role = models.CharField(max_length=50, default="Market Manager") 
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_picture/', blank=True, null=True) 
    

    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} - {self.role}"


