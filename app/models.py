from django.db import models
from ckeditor.fields import RichTextField
from parler.models import TranslatableModel,TranslatedFields
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Advantages(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_("Title"), max_length=200),
        description = RichTextField(_("Description"))
    )


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Advantage")
        verbose_name_plural = _("Advantages")

class Category(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_("Title"), max_length=200),
        description = RichTextField(_("Description"))
    )
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")


class Team(TranslatableModel):
    translations = TranslatedFields(
        description = RichTextField(_("About"))
    )
    

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Team")

class TeamMember(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=35,verbose_name=_("name")),
        rank = models.CharField(max_length=55,verbose_name=_("rank")),
        description = RichTextField(_("About"))
    )
    team = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='team')
    photo = models.ImageField(upload_to='Members')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Member")
        verbose_name_plural = _("Team")

class Questions(TranslatableModel):
    translations = TranslatedFields(
        question = models.CharField(max_length=155,verbose_name=_("question")),
        answer = RichTextField(_("answer"))
    )
  
    def __str__(self):
        return self.question

    class Meta:
        verbose_name = _("question")
        verbose_name_plural = _("Questions")

class Banner(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=155,verbose_name=_("title")),
        text = RichTextField(_("text"))
    )
  
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Banner")
        verbose_name_plural = _("Banner")

class About(TranslatableModel):
    translations = TranslatedFields(
        text = RichTextField(_("text")),
        footer = models.TextField(_("footer text"))
    )
    adress = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    email = models.EmailField()
    facebook = models.CharField(max_length=150)
    telegram = models.CharField(max_length=150)
    instagram = models.CharField(max_length=150)
    twitter = models.CharField(max_length=150)
    bot_token = models.CharField(max_length=200)
    admin_id = models.CharField(max_length=200)
  
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _("About")
        verbose_name_plural = _("About Us")


class Partner(models.Model):
    logo =  models.ImageField(upload_to='partners')
    about = models.ForeignKey(About,on_delete=models.CASCADE,related_name='about')

class Contact(models.Model):
    service =  models.CharField(max_length=100)
    source =  models.CharField(max_length=100)
    target =  models.CharField(max_length=100)
    name =  models.CharField(max_length=100)
    email =  models.CharField(max_length=100)
    phone =  models.CharField(max_length=100)
    message =  models.TextField()
