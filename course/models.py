from django.db import models

class TimeStampeModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
class Barchasi(TimeStampeModel):
    ism = models.CharField(null=True, blank=True)
    gapir = models.TextField(null=True, blank=True)
    gap = models.EmailField(null=True, blank=True)
    q = models.URLField(null=True, blank=True)
    w = models.IntegerField(null=True, blank=True)
    e = models.SmallIntegerField(null=True, blank=True)
    r = models.BigIntegerField(null=True, blank=True)
    t = models.PositiveIntegerField(null=True, blank=True)
    y = models.PositiveSmallIntegerField(null=True, blank=True)
    u = models.FloatField(null=True, blank=True)
    i = models.DecimalField(null=True, blank=True)
    o = models.DateField(null=True, blank=True)
    p = models.TimeField(null=True, blank=True)
    a = models.DateTimeField(null=True, blank=True)
    s = models.DurationField(null=True, blank=True)
    d = models.BooleanField(null=True, blank=True)
    f = models.FileField(null=True, blank=True)


