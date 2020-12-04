from django.contrib import admin
from vaccineapp.models import Vaccine, Desease, User, Collection, Person

# Register your models here.
@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'comments')

class VaccineInline(admin.TabularInline):
    model = Vaccine

@admin.register(Desease)
class DeseaseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [
        VaccineInline
    ]

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email',)

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    pass

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','dateofbirth', 'sex')