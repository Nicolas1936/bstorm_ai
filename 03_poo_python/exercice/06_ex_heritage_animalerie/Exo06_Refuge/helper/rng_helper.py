import random

class RngHelper():

    @staticmethod
    def proba(chance):

        if chance >= 100:
            return True

        return (random.random() * 100) < chance
        # return random.randrange(1,101) <= chance



if __name__ == '__main__':
    # print("0%")
    # for i in range(10):
    #     print(RngHelper.proba(0))
    # print()

    # print("100%")
    # for i in range(10):
    #     print(RngHelper.proba(100))
    # print()

    value = 0.1

    print(value,"%")
    count = 0
    nb_try = 100000
    for i in range(nb_try):
        if(RngHelper.proba(value)):
            count+=1
    print("resultat = ", count, "/", nb_try)