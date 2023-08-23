from enum import Enum


class Good(Enum):
    """
    - Price is based in IRR
    - Weight is based on gr
    - For size there are 4 category 1 : very small, 2 : small, 3 : medium, big : 4, very big : 5
    """
    title = "title"
    price = "price"
    weight = "weight"
    size = "size"


    @property
    def field_type(self):
        if self.name == self.title.name:
            return "VARCHAR(50)"
        elif self.name in (
                self.price.name,
                self.weight.name,
                self.size.name
        ):
            return "INT"


class GoodWarehouse(Enum):
    """
    - warehouse_id foreignkey of Warehouse
    - good_id foreignkey of Good
    - good_count number of existing goods based of goods
    """
    warehouse_id = "warehouse_id"
    good_id = "good_id"
    good_count = "good_count"

    @property
    def field_type(self):
        if self.name in (
                self.warehouse_id.name,
                self.good_id.name,
                self.good_count.name
        ):
            return "INT"


# #TODO later to create ORM
# from django.db import connections
# cursor = connections['specific_db'].cursor()
# cursor.execute("select * from item")


# class Good:
#     title: str
#     price: float
#     weight: int
#     size: int


# class good_warehouse:
#     warehouse_id: foreign_key
#     good_id: foreign_key
#     count: int