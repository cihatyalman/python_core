from UI.decorators.decorator_demo import DecoratorDemo
from UI.results.result_demo import ResultDemo
from UI.local_database.local_database_demo import LocalDatabaseDemo
from Core.datetime_operations.datetime_core import DateTimeCore
from UI.json_file.json_file_demo import JsonFileDemo


def decorator_test():
    print("--------------------")
    DecoratorDemo().on_before_demo(1,"value2")
    print("--------------------")
    DecoratorDemo().on_after_demo(1,"value2")
    print("--------------------")
    DecoratorDemo().on_exception_demo(1,"value2")
    print("--------------------")
    DecoratorDemo().double_demo(1,"value2")

def result_test():
    print( ResultDemo().fonk1("value1") )
    print( ResultDemo().fonk2("value1") )
    print( ResultDemo().fonk3("value1") )
    print( ResultDemo().fonk4("value1") )

def local_database_test():
    local_db = LocalDatabaseDemo()
    local_db.create_table()
    #local_db.add("text1",1.0)
    #local_db.add("text2",2.0)
    #local_db.add("text3",3.0)
    #local_db.update(1)
    #local_db.delete(3)
    result = local_db.get()
    print(result)

def json_file_test():
    json_file_demo = JsonFileDemo()
    data = [{"key1":"value1"},{"key2":"value2"}]
    json_file_demo.write(data)
    result = json_file_demo.read()
    print(result)
    #json_file_demo.delete()

def datetime_test():
    timestamp = DateTimeCore.get_timestamp(3)
    print(timestamp)

    date = DateTimeCore.to_datetime(timestamp)
    print(date)

    convert_timestamp = DateTimeCore.to_timestamp(date)
    print(convert_timestamp)

def main():
    #decorator_test()
    #result_test()
    #local_database_test()
    #json_file_test()
    datetime_test()

main()
