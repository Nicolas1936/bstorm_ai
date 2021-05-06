from personne import Personne

class Hero(Personne):
    
    def __init__(self):
        super().__init__()
        self.stock = []



    def __str__(self):
        return str(self.force)

if __name__ == "__main__":

    h = Hero()
    print(h)