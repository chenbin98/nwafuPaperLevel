from django.db import models


class JournalLevel(models.Model):
    name = models.CharField("期刊名称", max_length=255, unique=True)
    level = models.CharField("等级", max_length=50)

    def __str__(self):
        return f"{self.name} ({self.level})"