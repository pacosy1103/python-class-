class PrintClass:
    def __init__(self, desc="default value"):
        #__var = private valuable
        self.__desc = desc
    
    def getDesc(self):
        return self.__desc
    
    def setDesc(self, desc):
        self.__desc = desc

