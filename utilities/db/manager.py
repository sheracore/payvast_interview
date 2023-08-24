# TODO later to create ORM
from django.db import connections
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
    # def __init__(self, model_name: str, data: dict):
    #     self.model_name = model_name
    #     self.data = data
    #     self.cursor = connections[model_name].cursor()

    def field_type_dict(self):
        return {attr: value for attr, value in vars(type(self)).items() if
                not attr.startswith('__') and isinstance(value, str)}

    def field_field_dict(self):
        return {attr: attr for attr, value in vars(type(self)).items() if
                not attr.startswith('__') and isinstance(value, str)}

    # def create(self, data_dict):
    #     try:
    #         print(self.model_name)
    #     except:
    #         raise Exception
