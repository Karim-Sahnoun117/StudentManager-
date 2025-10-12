from database import database
class etudiant :
    def __init__(self,id,name,age):
        self.db = database()
        print("connected to database with success ")
        self.id =id
        self.name = name
        self.age = age
    def __str__(self):
        return f"voici id {self.id},le nom est {self.name}lage est {self.age}"
    def insert_to_data(self,e):
        query = "insert into etudiant (id,name,age) VALUES (%s ,%s ,%s)"
        self.db.curr.execute(query,(e.id,e.name,e.age))
        self.db.conn.commit()
        print("linserion de l'instance {e}est faite avec succès")

