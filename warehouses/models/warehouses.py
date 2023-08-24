import inspect

from utilities.db import Manager


class Warehouse(Manager):
    title = "VARCHAR(50)"
    is_full = "BIT"

