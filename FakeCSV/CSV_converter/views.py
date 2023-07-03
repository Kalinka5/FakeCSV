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

            column_name = request.POST.get("column_name")
            column_type = request.POST.get("type")
            column_order = request.POST.get("order")
            column = Column(
                name=column_name,
                type=column_type,
                order=column_order,
                schema=schema
            )
            column.save()
            return redirect("/data-sets")
        
        else:
            pass

    return render(request, "new_schema.html")


@login_required
def data_sets(request):
    schema = Schema.objects.last()
    columns = schema.column_set.all()
    columns_dict = {'columns': columns}
    return render(request, "data_sets.html", columns_dict)
