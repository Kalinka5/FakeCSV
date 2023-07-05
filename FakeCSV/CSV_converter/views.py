from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Schema, Column

from datetime import date



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
            for column_name, column_type, column_order in zip(column_name_list, column_type_list, column_order_list):
                column = Column(
                    name=column_name,
                    type=column_type,
                    order=column_order,
                    schema=schema
                )
                column.save()
                
            return redirect("/data-sets")

    return render(request, "new_schema.html")


@login_required
def data_sets(request):
    schema = Schema.objects.last()
    columns = schema.column_set.all()
    columns_dict = {'columns': columns}
    return render(request, "data_sets.html", columns_dict)
