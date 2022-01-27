from django.contrib import admin
from parler.admin import TranslatableAdmin,TranslatableTabularInline,TranslatableStackedInline
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
  list_display = ['title' ]
  fieldsets = (
    ('Main informations about Areas', {'fields': ['title','description',]}),
  )
  max_num = 4

@admin.register(Advantages)
class AdvantagesAdmin(TranslatableAdmin):
	list_display = ['title' ]
	fieldsets = (
    ('Main informations about Advantages', {'fields': ['title','description',]}),
  )

class Member(TranslatableStackedInline):
  model = TeamMember
  extra = 0


@admin.register(Team)
class TeamAdmin(TranslatableAdmin):
  list_display = ['description' ]
  inlines = [Member]

@admin.register(Questions)
class QuestionsAdmin(TranslatableAdmin):
  pass


@admin.register(Banner)
class BannerAdmin(TranslatableAdmin):
  pass


class Partners(admin.TabularInline):
  model = Partner
  extra = 0

@admin.register(About)
class AboutAdmin(TranslatableAdmin):
  inlines = [Partners]


admin.site.register(Contact)



