from enum import Enum


class Warehouse(Enum):
    title = "name"
    is_full = "is_full"

    @property
    def field_type(self):
        if self.name == self.title.name:
            return "VARCHAR(50)"
        elif self.name == self.is_full.name:
            return "BIT"


# #TODO later to create ORM
# from django.db import connections
# cursor = connections['specific_db'].cursor()
# cursor.execute("select * from item")