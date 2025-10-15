from dbmanager import dbmanager
class external():
    def __init__(self):
        self.db = dbmanager()
        print("connected to database with success ")
    def data_insert(self,e):
        query = "insert into etudiant (id,name,age) VALUES (%s ,%s ,%s)"
        self.db.curr.execute(query,(e.id,e.name,e.age))
        self.db.conn.commit()
        print("linserion de l'instance est faite avec succès")
    def data_recover(self):
        query = "select * from etudiant"
        self.db.curr.execute(query)
        rows = self.db.curr.fetchall()
        print("la recuperation des donnéés est faite avec succes ")
        return rows