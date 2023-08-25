# TODO later to create ORM
from django.db import connection
from typing import Optional
from django.core.exceptions import ValidationError
# cursor = connections['specific_db'].cursor()
# cursor.execute("select * from item")


# TODO: show data in dictionary type
# sql_query = "SELECT * FROM your_table_name"
# cursor.execute(sql_query)
# columns = [col[0] for col in cursor.description]
# data = cursor.fetchall()
# data_as_dicts = [dict(zip(columns, row)) for row in data]

from enum import Enum


class Manager:
    def __init__(self, model_name: Optional[str] = None, data: Optional[dict] = None):
        self.model_name = model_name.lower() if model_name else None
        # self.data = data

    def field_type_dict(self):
        return {attr: value for attr, value in vars(type(self)).items() if
                not attr.startswith('__') and isinstance(value, str)}

    def field_field_dict(self):
        return {attr: attr for attr, value in vars(type(self)).items() if
                not attr.startswith('__') and isinstance(value, str)}

    def insert(self, **kwargs):
        # TODO: The problem was that cursor.execute(query, values) does not work
        if not kwargs:
            raise ValidationError(r"data to be insert is required")
        try:
            with connection.cursor() as cursor:
                columns = list(kwargs.keys())
                values = list(kwargs.values())
                if len(values) > 1:
                    cursor.execute(f"insert into {self.model_name}({', '.join(columns)}) VALUES {tuple(values)}")
                else:
                    v = values[0]
                    value = f"('{v}')" if isinstance(v, str) else f"({v})"
                    cursor.execute(f"insert into {self.model_name}({', '.join(columns)}) VALUES {value}")
                connection.commit()
        except Exception as e:
            raise ValidationError(e)

    def insert_many(self):
        # TODO: should be developed if it needs
        pass

    def filter(self, **kwargs):
        try:
            with connection.cursor() as cursor:
                cursor.execute()
                # columns = list(kwargs.keys())
                # values = list(kwargs.values())
                # if len(values) > 1:
                #     cursor.execute(f"insert into {self.model_name}({', '.join(columns)}) VALUES {tuple(values)}")
                # else:
                #     v = values[0]
                #     value = f"('{v}')" if isinstance(v, str) else f"({v})"
                #     cursor.execute(f"insert into {self.model_name}({', '.join(columns)}) VALUES {value}")
                connection.commit()
        except Exception as e:
            raise ValidationError(e)

    def _filter_operators(self):
        return {
            "gt": ">",
            "gte": ">=",
            "lt": "<",
            "ltq": "<=",
            "in": "in",
        }

    def exclude(self):
        # TODO: implement is if you need
        pass
