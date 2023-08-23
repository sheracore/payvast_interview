from enum import Enum


class Transfer(Enum):
    """
    - warehouse_id: foreignkey of Warehouse
    - good_id: foreignkey of Good
    - status: 1: sender, 2: receiver
    - datetime: datetime of put/get goods into/from warehouses
    - count: number of goods
    """
    warehouse_id = "warehouse_id"
    good_id = "good_id"
    count = "count"
    status = "status"
    datetime = "datetime"

    @property
    def field_type(self):
        if self.name in (
                self.warehouse_id.name,
                self.good_id.name,
                self.count.name
        ):
            return "INT"
        elif self.name == self.status.name:
            return "BIT"
        elif self.name == self.datetime.name:
            return "DATETIME"
