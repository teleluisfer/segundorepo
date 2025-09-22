from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Post
from .models import Person
from .models import consulta1
from .models import DetalleVulnerabilidad

admin.site.register(Post)
admin.site.register(Person)
admin.site.register(consulta1)
admin.site.register(DetalleVulnerabilidad)
