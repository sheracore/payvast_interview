from django.db import migrations
from ..models import Good, Warehouse, GoodWarehouse


def create_good(apps, schema_editor):
    cursor = schema_editor.connection.cursor()
    cursor.execute(f"CREATE TABLE {Good.__name__.lower()} ("
                   f"id INT NOT NULL PRIMARY KEY IDENTITY(1,1),"
                   f"{Good().field_field_dict()['title']} {Good.title} NOT NULL, "
                   f"{Good().field_field_dict()['weight']} {Good.weight} NOT NULL,"
                   f"{Good().field_field_dict()['size']} {Good.size} NOT NULL,"
                   f"{Good().field_field_dict()['price']} {Good.price})"
                   )


def create_good_warehouse(apps, schema_editor):
    cursor = schema_editor.connection.cursor()
    cursor.execute(f"CREATE TABLE {Good.__name__.lower()}_{Warehouse.__name__.lower()} ("
                   f"id INT NOT NULL PRIMARY KEY IDENTITY(1,1),"
                   f"{GoodWarehouse().field_field_dict()['warehouse_id']} {GoodWarehouse.warehouse_id} NOT NULL, "
                   f"{GoodWarehouse().field_field_dict()['good_id']} {GoodWarehouse.good_id} NOT NULL,"
                   f"{GoodWarehouse().field_field_dict()['good_count']} {GoodWarehouse.good_count} NOT NULL,"
                   f"FOREIGN KEY ({GoodWarehouse().field_field_dict()['good_id']}) REFERENCES {Good.__name__.lower()}(id),"
                   f"FOREIGN KEY ({GoodWarehouse().field_field_dict()['warehouse_id']}) REFERENCES {Warehouse.__name__.lower()}(id)"
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
