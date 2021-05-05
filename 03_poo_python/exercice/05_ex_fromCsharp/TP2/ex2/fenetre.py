class Fenetre:

    def __init__(self, quit_x=0, quit_y=0):
        self.quit_x = quit_x
        self.quit_y = quit_y
    
    # def click_action(self, x, y):
        
    #     if x == self.quit_x and y == self.quit_y:
    #         print("la fenetre se ferme...")
    #     else:
    #         print("la fenetre ne se ferme pas...")

    def click_action(self, souris):
    
        if souris.x == self.quit_x and souris.y == self.quit_y:
            print("la fenetre se ferme...")
        else:
            print("la fenetre ne se ferme pas...")
