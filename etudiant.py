
class etudiant :
    def __init__(self,id,name,age):
        self.id =id
        self.name = name
        self.age = age
    def __str__(self):
        return f"voici id {self.id},le nom est {self.name}lage est {self.age}"
 

