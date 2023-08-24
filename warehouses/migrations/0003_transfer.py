from django.db import migrations
from ..models import Good, Warehouse, Transfer


def create_transfer(apps, schema_editor):
    cursor = schema_editor.connection.cursor()
    cursor.execute(f"CREATE TABLE {Transfer.__name__.lower()} ("
                   f"id INT NOT NULL PRIMARY KEY, "
                   f"{Transfer().field_field_dict()['warehouse_id']} {Transfer.warehouse_id} NOT NULL, "
                   f"{Transfer().field_field_dict()['good_id']} {Transfer.good_id} NOT NULL,"
                   f"{Transfer().field_field_dict()['count']} {Transfer.count} NOT NULL,"
                   f"{Transfer().field_field_dict()['datetime']} {Transfer.datetime} NOT NULL,"
                   f"{Transfer().field_field_dict()['status']} {Transfer.status} NOT NULL,"
                   f"FOREIGN KEY ({Transfer().field_field_dict()['good_id']}) REFERENCES {Good.__name__.lower()}(id),"
                   f"FOREIGN KEY ({Transfer().field_field_dict()['warehouse_id']}) REFERENCES {Warehouse.__name__.lower()}(id)"
                   f")"
                   )


class Migration(migrations.Migration):
    dependencies = [
        ('warehouses', '0002_goods'),
    ]
    operations = [
        migrations.RunPython(
            create_transfer,
            reverse_code=migrations.RunPython.noop,
        )
    ]
