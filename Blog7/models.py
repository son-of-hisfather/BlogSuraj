from django.db import models


# Create your models here.
SERVICE_CHOICES = [
        ('Service 1', 'Consulting'),
        ('Service 2', 'Development'),
        ('Service 3', 'Marketing'),
        ('Service 4', 'Support'),
    ]

class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    
class Expertise(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


class Posts(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/') 
    # I erased blog_images in tht bracket
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add =True)



    def __str__(self):
        return self.title


class Comment(models.Model):
    posts = models.ForeignKey(Posts,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self',null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return f'{self.name} on {self.posts}'
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50, null=True)
    bio = models.TextField()
    content = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/')
    social_x = models.URLField(blank=True)
    social_facebook = models.URLField(blank=True)
    social_instagram = models.URLField(blank=True)
    social_linkedin = models.URLField(blank=True)
    articles_count = models.IntegerField(default=0)
    awards_count = models.IntegerField(default=0)
    followers_count = models.IntegerField(default=0)
    expertise = models.ManyToManyField(Expertise, blank=True)
     
    def __str__(self):
        return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profiles/')
    bio = models.TextField()
    social_facebook = models.URLField(blank=True)
    social_x = models.URLField(blank=True)
    social_linkedin = models.URLField(blank=True)
    social_youtube = models.URLField(blank=True)


    
