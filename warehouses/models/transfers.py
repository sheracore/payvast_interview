from enum import Enum
from utilities.db import Manager


class Transfer(Manager):
    """
    - warehouse_id: foreignkey of Warehouse
    - good_id: foreignkey of Good
    - status: 1: sender, 2: receiver
    - datetime: datetime of put/get goods into/from warehouses
    - count: number of goods
    """
    warehouse_id = "INT"
    good_id = "INT"
    count = "INT"
    status = "BIT"
    datetime = "DATETIME"
