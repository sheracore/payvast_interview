from django.db import connection
from typing import Optional, List
from django.core.exceptions import ValidationError


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

    def original_columns(self):
        result = ['id']
        result.extend(list(self.field_field_dict().keys()))
        return result

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
                    value = self._query_value_cotation(v)
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
                query = "select * from {model_name}"
                if kwargs:
                    conditions = ""
                    for f, v in kwargs.items():
                        condition_operator = '='
                        s_f = f.split('__')
                        field = s_f[0]
                        if len(s_f) > 1:
                            condition_operator = self._filter_operators()[s_f[1]]
                        value = self._query_value_cotation(v)
                        conditions += f" {field} {condition_operator} {value} and"
                    if conditions.endswith("and"):
                        conditions = conditions[:-len("and")]
                    query += f" where{conditions}"
                query = query.format(model_name=self.model_name)

                cursor.execute(query)
                original_columns = self.original_columns()
                data = cursor.fetchall()
                return self._make_dict(original_columns, data)
        except Exception as e:
            raise ValidationError(e)

    def _filter_operators(self):
        return {
            "gt": ">",
            "gte": ">=",
            "lt": "<",
            "lte": "<=",
            # "in": "in",
        }

    def _make_dict(self, original_columns: list, data: List[tuple]):
        return [dict(zip(original_columns, row)) for row in data]

    def _query_value_cotation(self, value):
        return f"'{value}'" if isinstance(value, str) else f"{value}"

    def exclude(self):
        # TODO: implement is if you need
        pass

