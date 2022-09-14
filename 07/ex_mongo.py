import pymongo

connection_string = \
    "mongodb+srv://educando:python2022@cluster0.ppjibfy.mongodb.net/\
?retryWrites=true&w=majority"


class MongoManager():
    client = None
    collection = None

    def __init__(self, connection_string, collection_name):
        self.client = pymongo.MongoClient(connection_string)
        self.collection = self.client[db_name][collection_name]

    def __to_list(self, records):
        result = [x for x in records]
        return result

    def getAll(self, limit=0):
        registros = self.collection.find().limit(limit)
        return self.__to_list(registros)

    def getOne(self, params={}):
        if params == {}:
            return self.collection.find_one()

        registros = self.collection.find(params)
        return self.__to_list(registros)

    def update(self, id_update, new_values):
        myquery = {'_id': id_update}
        self.collection.update_one(myquery, new_values)

    def deleteOne(self, id_delete):
        myquery = {'_id': id_delete}
        self.collection.delete_one(myquery)

    def reset(self):
        result = mycol.delete_many({})
        return result.deleted_count

    def insert(self, new_values):
        self.collection.insert_one(new_values)


class Producto(MongoManager):

    def __init__(self, connection_string):
        super(Producto, self).__init__(connection_string, "producto")


class Cliente(MongoManager):

    def __init__(self, connection_string):
        super(Cliente, self).__init__(connection_string, "cliente")


cli = Cliente(connection_string)
prod = Producto(connection_string)

cli.getAll()
cli.getAll(5)

import ipdb

ipdb.set_trace()

# class Product(object):
#     manager = MongoManager(connection_string, "producto")

# class Cliente(object):
#     manager = MongoManager(connection_string, "cliente")

# Product().manager.insert({"nombre": "Agua Mineral", "precio": 2})
# Product().manager.insert({"nombre": "Coca-cola", "precio": 3})
# Product().manager.insert({"nombre": "Te Verde x Kilo", "precio": 10})

# Cliente().manager.insert({"nombre": "Jose", "edad": 20})
# Cliente().manager.insert({"nombre": "Juan", "edad": 15})
# Cliente().manager.insert({"nombre": "Roberto", "edad": 28})
# Cliente().manager.insert({"nombre": "Mauro", "edad": 40})