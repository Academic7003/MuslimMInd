from django.contrib import admin
from posts.models import *
from creators.models import *

admin.site.register(PostModel)
admin.site.register(Creator)

