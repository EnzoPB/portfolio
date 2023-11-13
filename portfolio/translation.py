from modeltranslation.translator import register, TranslationOptions
from .models import *

print('COUCOU CA VAèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèèè')
@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('short_description', 'description')
