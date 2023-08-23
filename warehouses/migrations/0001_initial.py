from django.db import migrations
from django.db import connection
from ..models import Warehouse


def create_warehouse(apps, schema_editor):
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE TABLE {Warehouse.__name__.lower()} ("
                       f"id INT NOT NULL PRIMARY KEY, "
                       f"{Warehouse.title.name} {Warehouse.title.field_type} NOT NULL, "
                       f"{Warehouse.is_full.name} {Warehouse.is_full.field_type} DEFAULT 1)"
                       )

def create_goods(apps, schema_editor):
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE TABLE {Warehouse.__name__.lower()} ("
                       f"id INT NOT NULL PRIMARY KEY, "
                       f"{Warehouse.title.name} {Warehouse.title.field_type} NOT NULL, "
                       f"{Warehouse.is_full.name} {Warehouse.is_full.field_type} DEFAULT 1)"
                       )


class Migration(migrations.Migration):
    dependencies = []
    operations = [
        migrations.RunPython(
            create_index,
            reverse_code=migrations.RunPython.noop,
        )
    ]