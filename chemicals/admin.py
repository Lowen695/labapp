from django.contrib import admin
from .models import User, chemicals, Agent


admin.site.register(User)
admin.site.register(chemicals)
admin.site.register(Agent)



