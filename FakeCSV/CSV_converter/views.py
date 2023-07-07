from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings
from django.views import View

from faker import Faker

import os
from datetime import date
import random
import csv

from .models import Schema, Column, IntegerColumn, File


def get_email(faker):
    first_name = faker.first_name()
    last_name = faker.last_name()
    domain = faker.domain_name()
    return f"{first_name}.{last_name}@{domain}"


def generate_fake_data(all_columns, faker):

    fake_data = list()

    for column in all_columns:
        if column.type == "1":
            fake_data.append(faker.name())
        elif column.type == "2":
            fake_data.append(faker.job())
        elif column.type == "3":
            fake_data.append(get_email(faker))
        elif column.type == "4":
            integer = IntegerColumn.objects.filter(id=column.id).first()
            fake_data.append(random.randrange(integer.range_low, integer.range_high))
        else:
            fake_data.append(faker.date())
    
    return fake_data


@login_required
def data_schemas(request):
    data_schemas = Schema.objects.all()
    data_schemas_dict = {'schemas': data_schemas}
    return render(request, "data_schemas.html", data_schemas_dict)


@login_required
def new_schema(request):

    if request.method == "POST":

        if request.POST["submit"] == "Submit":
            schema_name = request.POST.get("schema_name")
            separator = request.POST.get("separator")
            character = request.POST.get("character")
            modified_date = date.today().strftime("%Y-%m-%d")
            schema = Schema(
                name=schema_name,
                column_separator=separator,
                string_character=character,
                modified=modified_date
            )
            schema.save()

            column_name_list = request.POST.getlist("column_name")
            column_type_list = request.POST.getlist("type")
            column_order_list = request.POST.getlist("order")
            integer_from_list = request.POST.getlist("from[]")
            integer_to_list = request.POST.getlist("to[]")
            for column_name, column_type, column_order, integer_from, integer_to, in zip(column_name_list, column_type_list, column_order_list, integer_from_list, integer_to_list):
                if column_type == "4":
                    IntegerColumn.objects.create(
                        name=column_name,
                        type=column_type,
                        order=column_order,
                        schema=schema,
                        range_low=integer_from,
                        range_high=integer_to
                    )
                else:
                    Column.objects.create(
                        name=column_name,
                        type=column_type,
                        order=column_order,
                        schema=schema
                    )
                
            return redirect("/data-sets")

    return render(request, "new_schema.html")


class DataSetsView(View):
    template_name = "data_sets.html"
    fake = Faker()

    def get(self, *args, **kwargs):
        schema = Schema.objects.last()
        columns = schema.column_set.all()
        files = schema.file_set.all()

        return render(self.request, self.template_name, {"columns": columns, "files": files})

    def post(self, *args, **kwargs):
        if self.request.method == "POST":
            schema = Schema.objects.last()
            schema_name = schema.name
            schema_delimeter = schema.column_separator
            schema_character = schema.string_character

            n = 1
            while True:
                filename = f'{schema_name}{n}.csv'
                if not File.objects.filter(name=filename).exists():
                    file = File.objects.create(name=filename, schema=schema)
                    break

                n += 1
                
            file_path = os.path.join(settings.MEDIA_ROOT, filename)
            rows = int(self.request.POST.get("rows"))

            columns = schema.column_set.all()
            # Set "flat=True" to flatten the resulting list of values into a one-dimensional list.
            column_names = columns.values_list('name', flat=True)

            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=schema_delimeter, quotechar=schema_character)
                writer.writerow(column_names)
                for _ in range(1, rows):
                    writer.writerow(generate_fake_data(columns, self.fake))

            # Prepare the data for the new file
            new_file_data = {
                'date': file.date,
                'name': file.name,
            }

            return JsonResponse(new_file_data)

        return JsonResponse({"error": ""}, status=400)
