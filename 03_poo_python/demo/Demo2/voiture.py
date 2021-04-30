class Voiture:

    def __init__(self, model):
        self.__model = model
        self._nb_roue = 4

    #model
    def _get_model(self):
        return self.__model.upper()
    
    def _set_model(self, value):
        if len(value) > 1:
            self.__model = value
        else :
            self.__model = "DEFAULT"

    model = property(_get_model, _set_model)