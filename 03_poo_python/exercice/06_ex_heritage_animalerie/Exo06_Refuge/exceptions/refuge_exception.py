class RefugeError(Exception):

    def __init__(self, msg):
        self.__msg = msg


    @property
    def msg(self):
        return self.__msg
