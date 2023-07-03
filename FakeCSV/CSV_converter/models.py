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
    actions = models.CharField(max_length=255, default="Edit scheme")

    def __str__(self):
        return self.name
    

class Column(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(
        max_length=255,
        choices=TYPE_CHOICES
    )
    if type == "Integer":
        from_field = models.IntegerField()
        to_field = models.IntegerField()

    order = models.CharField(max_length=255)
    delete = models.CharField(max_length=255, default="delete")

    schema = models.ForeignKey(
        Schema,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self) -> str:
        return self.name
