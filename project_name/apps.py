from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class FilerConfig(AppConfig):
    name = 'filer'
    verbose_name = _("Uploads")


from suit.apps import DjangoSuitConfig

class SuitConfig(DjangoSuitConfig):
    layout = 'vertical'
