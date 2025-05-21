from django.contrib import admin
from . models import Posts, Tag, Category,Comment, Contact

# Register your models here.

admin.site.register(Posts)
list_display = ['author', 'title', 'content', 'image', 'tags' 'category' 'date_posted']
search_fields =['title', 'category']

admin.site.register(Tag)
list_display = ['name']
search_fields = ['name']


admin.site.register(Category)
list_display = ['name']
search_fields =['name']

admin.site.register(Comment)
list_display = ['posts', 'name', 'email', 'website', 'content', 'cretaed_at', 'parents']
search_fields = ['posts', 'name', 'email', 'website', 'content',]

admin.site.register(Contact)
list_display = ['name', 'email', 'phone', 'service', 'message']
search_fields = ['name', 'email', 'phone', 'service', 'message']





