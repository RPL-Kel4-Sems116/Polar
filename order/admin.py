from django.contrib import admin

# Register your models here.
from .models import Customer,Gambar, Gambar2, Gambar3

class gambarAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Customer)
admin.site.register(Gambar,gambarAdmin)
admin.site.register(Gambar2,gambarAdmin)
admin.site.register(Gambar3,gambarAdmin)