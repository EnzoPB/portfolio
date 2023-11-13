from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('short_description', 'description')
