from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('short_description', 'description')

@register(SkillCategory)
class SkillCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Skill)
class SkillTranslationOptions(TranslationOptions):
    fields = ('detail',)
