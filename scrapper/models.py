from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class ScrapperConfig(models.Model):

    name = models.CharField(max_length=100)
    url = models.URLField()
    css_selector = models.CharField(max_length=255)
    frequency = models.IntegerField(default=60)

    class Meta:
        verbose_name = _("ScrapperConfig")
        verbose_name_plural = _("ScrapperConfigs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ScrapperConfig_detail", kwargs={"pk": self.pk})
