from Core.local_database.sqlite_base import SqliteBase

class LocalDatabaseDemo(SqliteBase):


    def __init__(self):
        super().__init__("UI/local_database/demo.db")
        self.table_name = "demo"


    def create_table(self):
        super()._create_table("CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY, text_value TEXT, decimal_value REAL)".format(self.table_name))
        return True

    def add(self,text_value,decimal_value):
        super()._add("INSERT INTO {} (text_value, decimal_value) VALUES (?,?)".format(self.table_name),text_value,decimal_value)
        return True
    
    def get(self):
        result = super()._get("SELECT * FROM {}".format(self.table_name))
        return result

    def update(self,id):
        super()._update("""UPDATE {} SET text_value = 'new text' WHERE id={}""".format(self.table_name,id))
        return True
    
    def delete(self,id):
        super()._delete("DELETE FROM {} WHERE id={}".format(self.table_name,id))
        return True
