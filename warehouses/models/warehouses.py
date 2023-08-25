import inspect

from utilities.db import Manager


class Warehouse(Manager):
    title = "VARCHAR(50)"
    is_full = "BIT"



w = Warehouse(Warehouse.__name__)
w.insert(title="hhhghghghghghgh", is_full=1)
w.filter(is_full__gt=0)
