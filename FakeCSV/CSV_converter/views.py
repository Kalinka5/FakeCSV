from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.conf import settings
from django.views import View
from django.shortcuts import get_object_or_404

from faker import Faker

import os
import random
import csv

from .forms import SchemaForm
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


def delete_files(prefix):
    folder_path = "media"
    files = os.listdir(folder_path)

    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path) and file.startswith(prefix) and len(file) > len(prefix) and file[len(prefix)].isdigit():
            try:
                os.remove(file_path)
            except OSError as e:
                print(f"Error deleting {file_path}: {e}")


def home(request):
    return render(request, "home.html", {})


class DataSchemasView(View):
    template_name = "data_schemas.html"

    def get(self, *args, **kwargs):
        data_schemas = Schema.objects.filter(user=self.request.user)
        data_schemas_dict = {'schemas': data_schemas}
        return render(self.request, self.template_name, data_schemas_dict)

    def post(self, *args, **kwargs):
        if self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            schema_id = self.request.POST.get('schema_id')
            try:
                schema = Schema.objects.get(pk=schema_id)
                schema_name = schema.schema_name
                delete_files(schema_name)
                schema.delete()
                return JsonResponse({'success': True})
            except Schema.DoesNotExist:
                return JsonResponse({'success': False, 'error': 'Schema not found.'})


class NewSchemaView(View):
    template_name = "new_schema.html"

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, {})

    def post(self, *args, **kwargs):
        schema_form = SchemaForm(self.request.POST)
        if schema_form.is_valid():
            schema = schema_form.save()

            column_name_list = self.request.POST.getlist("column_name")
            column_type_list = self.request.POST.getlist("type")
            column_order_list = self.request.POST.getlist("order")
            integer_from_list = self.request.POST.getlist("from[]")
            integer_to_list = self.request.POST.getlist("to[]")
            zip_lists = zip(column_name_list, column_type_list, column_order_list, integer_from_list, integer_to_list)
            
            for column_name, column_type, column_order, integer_from, integer_to, in zip_lists:
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
            
            messages.success(self.request, "The schema was created successfully.")
            return redirect(f"/data-sets/{schema.schema_name}/")


class DataSetsView(View):
    template_name = "data_sets.html"
    fake = Faker()

    def get(self, *args, **kwargs):
        name = kwargs.get('name')
        if name:
            schema = get_object_or_404(Schema, schema_name=name)
            columns = schema.column_set.all()
            files = schema.file_set.all()
        else:
            columns = ''
            files = ''
        schema_dict = {"schema_name": schema.schema_name, "columns": columns, "files": files}

        return render(self.request, self.template_name, schema_dict)

    def post(self, *args, **kwargs):
        name = kwargs.get('name')
        if self.request.method == "POST":
            schema = get_object_or_404(Schema, schema_name=name)
            schema_name = schema.schema_name
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

            columns = schema.column_set.all().order_by('order')

            # Set "flat=True" to flatten the resulting list of values into a one-dimensional list.
            column_names = columns.values_list('name', flat=True)

            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=schema_delimeter, quotechar=schema_character)
                writer.writerow(column_names)
                for _ in range(1, rows):
                    writer.writerow(generate_fake_data(columns, self.fake))

            new_file_data = {
                'date': file.date,
                'name': file.name,
            }

            return JsonResponse(new_file_data)

        return JsonResponse({"error": ""}, status=400)


class EditSchemaView(View):
    template_name = "edit_schema.html"

    def get(self, *args, **kwargs):
        name = kwargs.get('name')
        schema = get_object_or_404(Schema, schema_name=name)
        columns = schema.column_set.all().order_by('order')
        options = ['Full name', 'Job', 'Email', 'Integer', 'Date']
        schema_dict = {"schema": schema, "columns": columns, 'options': options}

        return render(self.request, self.template_name, schema_dict)


    def post(self, *args, **kwargs):
        if self.request.POST["submit"] == "Submit":

            name = kwargs.get('name')
            schema_name = self.request.POST.get("schema_name")
            separator = self.request.POST.get("separator")
            character = self.request.POST.get("character")

            schema = get_object_or_404(Schema, schema_name=name)
            schema.name = schema_name
            schema.column_separator = separator
            schema.string_character = character
            schema.save()

            columns_to_delete = schema.column_set.all()
            for column in columns_to_delete:
                column.delete()

            column_name_list = self.request.POST.getlist("column_name")
            column_type_list = self.request.POST.getlist("type")
            column_order_list = self.request.POST.getlist("order")
            integer_from_list = self.request.POST.getlist("from[]")
            integer_to_list = self.request.POST.getlist("to[]")
            zip_lists = zip(column_name_list, column_type_list, column_order_list, integer_from_list, integer_to_list)
            for column_name, column_type, column_order, integer_from, integer_to, in zip_lists:
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
                
            return redirect(f"/data-sets/{schema.schema_name}/")
