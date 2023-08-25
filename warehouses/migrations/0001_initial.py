from django.db import migrations
from ..models import Warehouse


def create_warehouse(apps, schema_editor):
    cursor = schema_editor.connection.cursor()
    cursor.execute(f"CREATE TABLE {Warehouse.__name__.lower()} ("
                   f"id INT NOT NULL PRIMARY KEY IDENTITY(1,1),"
                   f"{Warehouse().field_field_dict()['title']} {Warehouse.title} NOT NULL, "
                   f"{Warehouse().field_field_dict()['is_full']} {Warehouse.is_full} DEFAULT 0)"
                   )


class Migration(migrations.Migration):
    dependencies = []
    operations = [
        migrations.RunPython(
            create_warehouse,
            reverse_code=migrations.RunPython.noop,
        )
    ]
