from django.db import migrations
from ..models import Good, Warehouse, Transfer


def create_transfer(apps, schema_editor):
    cursor = schema_editor.connection.cursor()
    cursor.execute(f"CREATE TABLE {Transfer.__name__.lower()} ("
                   f"id INT NOT NULL PRIMARY KEY, "
                   f"{Transfer.warehouse_id.name} {Transfer.warehouse_id.field_type} NOT NULL, "
                   f"{Transfer.good_id.name} {Transfer.good_id.field_type} NOT NULL,"
                   f"{Transfer.count.name} {Transfer.count.field_type} NOT NULL,"
                   f"{Transfer.datetime.name} {Transfer.datetime.field_type} NOT NULL,"
                   f"{Transfer.status.name} {Transfer.status.field_type} NOT NULL,"
                   f"FOREIGN KEY ({Transfer.good_id.name}) REFERENCES {Good.__name__.lower()}(id),"
                   f"FOREIGN KEY ({Transfer.warehouse_id.name}) REFERENCES {Warehouse.__name__.lower()}(id)"
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
