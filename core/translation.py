from modeltranslation import translator
from . import models


@translator.register(models.category)

class categoryTranslation(translator.TranslationOptions):
  fields = ('category',)


@translator.register(models.SubCategory)

class SubCategoryTranslation(translator.TranslationOptions):
  fields = ('SubCategory',)


@translator.register(models.Item)

class ItemTranslation(translator.TranslationOptions):
  fields = ('title', 'label', 'slug', 'description',)


@translator.register(models.title_contact)

class title_contactTranslation(translator.TranslationOptions):
  fields = ('title', 'subtitle',)
