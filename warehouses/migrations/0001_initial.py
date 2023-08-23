from django.db import migrations
from ..models import Warehouse


def create_warehouse(apps, schema_editor):
    cursor = schema_editor.connection.cursor()
    cursor.execute(f"CREATE TABLE {Warehouse.__name__.lower()} ("
                   f"id INT NOT NULL PRIMARY KEY, "
                   f"{Warehouse.title.name} {Warehouse.title.field_type} NOT NULL, "
                   f"{Warehouse.is_full.name} {Warehouse.is_full.field_type} DEFAULT 1)"
                   )


class Migration(migrations.Migration):
    dependencies = []
    operations = [
        migrations.RunPython(
            create_warehouse,
            reverse_code=migrations.RunPython.noop,
        )
    ]
