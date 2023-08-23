# class Transfer:
#     good_id: foreign_key
#     warehouse_id: foreign_key
#     user: user_id
#     status: 1: sender, 2: keeper
#     datetime:
#     count:
#
#     @signal post_save:
#     # to good_warehouse


# #TODO later to create ORM
# from django.db import connections
# cursor = connections['specific_db'].cursor()
# cursor.execute("select * from item")