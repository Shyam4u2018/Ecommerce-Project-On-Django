from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, EmailInput
# Create your models here.


class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    fax = models.CharField(blank=True, max_length=50)
    email = models.EmailField(blank=True, null=True, max_length=50)
    smptserver = models.CharField(max_length=100)
    smtpemail = models.EmailField(blank=True, null=True, max_length=50)
    smptpassword = models.CharField(blank=True, max_length=50)
    smptport = models.CharField(blank=True, max_length=100)
    icon = models.ImageField(blank=True, null=True, upload_to='icon/')
    facebook = models.CharField(blank=True, max_length=100)
    instagram = models.CharField(blank=True, max_length=100)
    address = models.TextField()
    contact = models.TextField()
    reference = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),

    )
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=40)
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField(max_length=1000, blank=True)
    status = models.CharField(max_length=40, choices=STATUS, default='New')
    ip = models.CharField(max_length=100, blank=True)
    Note = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'Name & Sure name'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'Write your email'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Wrte your Subjects'}),
            'message': TextInput(attrs={'class': 'input', 'placeholder': 'Write your messages'}),
        }


class FAQ(models.Model):
    STATUS = (
        ("True", "True"),
        ("False", "False")
    )
    ordernumber = models.IntegerField()
    question = models.CharField(max_length=200)
    answer = models.TextField()
    status = models.CharField(choices=STATUS, max_length=200, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class UserProfile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	phone=models.CharField(blank=True,max_length=20)
	address = models.CharField(blank=True,max_length=200)
	city = models.CharField(blank=True,max_length=200)
	country = models.CharField(blank=True,max_length=200)
	image=models.ImageField(blank=True,upload_to='user_img')

	def __str__(self):
		return self.user.username


	def user_name(self):
		return self.user.first_name+' '+ self.user.last_name+'['+self.user.username+']'

	def  image_tag(self):
		return mark_safe('<img src="{}" heights="50" width="50" />'.format(self.image.url))
	image_tag.short_description='Image'
	def imageUrl(self):
		if self.image:
			return self.image.url
		else:
			return ""