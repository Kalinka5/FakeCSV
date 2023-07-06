from django.db import models


TYPE_CHOICES = (
    ("1", "Full name"),
    ("2", "Job"),
    ("3", "Email"),
    ("4", "Integer"),
    ("5", "Date"),
)


class Schema(models.Model):
    name = models.CharField(max_length=255)
    column_separator = models.CharField(max_length=255)
    string_character = models.CharField(max_length=255)
    modified = models.DateField()

    def __str__(self):
        return self.name
    

class Column(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(
        max_length=255,
        choices=TYPE_CHOICES
    )
    order = models.CharField(max_length=255)
    schema = models.ForeignKey(
        Schema,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name
    
class IntegerColumn(Column):
    range_low = models.IntegerField(blank=True, null=True, default=0)
    range_high = models.IntegerField(blank=True, null=True, default=100)

class File(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    schema = models.ForeignKey(
        Schema,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name
