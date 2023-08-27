from utilities.db import Manager


class Good(Manager):
    """
    - Price is based in IRR
    - Weight is based on gr
    - For size there are 4 category : 1 -> very small, 2 -> small, 3 -> medium: 4 -> big, 5 -> very big
    """
    title = "VARCHAR(50)"
    price = "INT"
    weight = "INT"
    size = "INT"


class GoodWarehouse(Manager):
    """
    - warehouse_id foreignkey of Warehouse
    - good_id foreignkey of Good
    - good_count number of existing goods based of goods
    """
    warehouse_id = "INT"
    good_id = "INT"
    good_count = "INT"
