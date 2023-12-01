from django.contrib import admin
from .models import technology , topics,subtopics,reusablecode
# Register your models here.
admin.site.register(technology)
admin.site.register(topics)
admin.site.register(subtopics)
admin.site.register(reusablecode)