from django.db import models

class WallProfile(models.Model):
    name = models.CharField(max_length=100)

class Section(models.Model):
    profile = models.ForeignKey(WallProfile, related_name='sections', on_delete=models.CASCADE)
    initial_height = models.IntegerField()
    current_height = models.IntegerField(default=0)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    completed_day = models.IntegerField(null=True, blank=True)
    assigned_team = models.IntegerField(null=True, blank=True)  # Track which team is assigned
