from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class ServicePost(models.Model):
    name = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    category_name = models.CharField(max_length=200)
    contact_no = models.IntegerField()
    email = models.IntegerField()
    gender = models.CharField(max_length=50)
    per_hour_charge = models.IntegerField()
    aval_date = models.DateTimeField('aval_date')
    Image = models.CharField(max_length=200)
    certificate = models.BooleanField()
    oter_skills_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name + " - " + self.category_name + "-"+ self.experience
    

class EventPost(models.Model):
        event_name = models.CharField(max_length=200)
        no_of_tickets = models.CharField(max_length=200)
        event_image = models.CharField(max_length=200)
        contact_no = models.IntegerField()
        email = models.CharField(max_length=200)
        user_name = models.CharField(max_length=200)
        event_date = models.DateTimeField('aval_date')
        approved = models.BooleanField()
        def __str__(self):
            return self.name + " - " + self.category_name + "-"+ self.experience



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')


        return self.create_user(email, username, password, **extra_fields)

class User(AbstractBaseUser):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name', 'contact_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class ServicePostByUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category_name = models.CharField(max_length=100)
    description = models.TextField()
    experience = models.IntegerField()
    available_date = models.DateTimeField()
    open_to_work = models.BooleanField()
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    service_img = models.ImageField(upload_to='img/', blank=True)
    per_hour_rate = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.category_name}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_post = models.ForeignKey(ServicePostByUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    other_description = models.TextField(blank=True)
    # Add any other fields related to booking

    def __str__(self):
        return f"{self.user.full_name}'s Booking for {self.service_post.name}"
    