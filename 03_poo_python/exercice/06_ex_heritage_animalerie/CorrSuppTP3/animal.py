class Animal:
    def __init__(self, nom):
        self.nom = nom
        self.age = 0
        self.en_vie = False

    def Naissance(self):
        self.en_vie = True
        print(f"Naissance de : {self.nom}")

    def Respirer(self):
        print("Inspire - expire")

    def Parler(self):
        print(f"{self.nom} pousse un cri")
       

    def Viellir(self, ans = 1):
        if ans > 0 :
            self.age += ans
        

    def Deces(self):
        self.en_vie = False
        print(f"{self.nom} est mort")

    def __str__(self):
        return f"nom : {self.nom} \nAge : {self.age} \nVivant : {self.en_vie}"