from django.contrib import admin
from vaccineapp.models import Vaccine, Disease, User, Collection, Person, PersonVaccine

# Register your models here.
@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'comments')


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email',)

# class DiseaseInline(admin.TabularInline):
#     model = Disease

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    # inlines = [
    #     DiseaseInline
    # ]
    pass

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','dateofbirth', 'sex')

@admin.register(PersonVaccine)
class PersonVaccineAdmin(admin.ModelAdmin):
    list_display = ('disease','vaccine',)