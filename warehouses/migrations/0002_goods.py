from django.db import migrations
from ..models import Good, Warehouse, GoodWarehouse


def create_good(apps, schema_editor):
    cursor = schema_editor.connection.cursor()
    cursor.execute(f"CREATE TABLE {Good.__name__.lower()} ("
                   f"id INT NOT NULL PRIMARY KEY, "
                   f"{Good.title.name} {Good.title.field_type} NOT NULL, "
                   f"{Good.weight.name} {Good.weight.field_type} NOT NULL,"
                   f"{Good.size.name} {Good.size.field_type} NOT NULL,"
                   f"{Good.price.name} {Good.price.field_type})"
                   )


def create_good_warehouse(apps, schema_editor):
    cursor = schema_editor.connection.cursor()
    cursor.execute(f"CREATE TABLE {Good.__name__.lower()}_{Warehouse.__name__.lower()} ("
                   f"id INT NOT NULL PRIMARY KEY, "
                   f"{GoodWarehouse.warehouse_id.name} {GoodWarehouse.warehouse_id.field_type} NOT NULL, "
                   f"{GoodWarehouse.good_id.name} {GoodWarehouse.good_id.field_type} NOT NULL,"
                   f"{GoodWarehouse.good_count.name} {GoodWarehouse.good_count.field_type} NOT NULL,"
                   f"FOREIGN KEY ({GoodWarehouse.good_id.name}) REFERENCES {Good.__name__.lower()}(id),"
                   f"FOREIGN KEY ({GoodWarehouse.warehouse_id.name}) REFERENCES {Warehouse.__name__.lower()}(id)"
                   f")"
                   )


class Migration(migrations.Migration):
    dependencies = [
        ('warehouses', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(
            create_good,
            reverse_code=migrations.RunPython.noop,
        ),
        migrations.RunPython(
            create_good_warehouse,
            reverse_code=migrations.RunPython.noop,
        )
    ]
