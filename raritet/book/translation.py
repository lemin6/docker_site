from .models import Author
from modeltranslation.translator import TranslationOptions,register

@register(Author)
class AuthorTranslationOptions(TranslationOptions):
    fields = ('last_name', 'first_name')