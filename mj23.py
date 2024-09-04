class vechile:
    def __init__(self,i,ms,ia):
        self.__id=i
        self.__maxspeed=ms
        self.__Increaseamount=ia
        self.__currentspeed=0
        self.__horizontalpostion=0
    def setcurrentspeed(self,c):
        self.__currentspeed=c
    def sethorizontalpostion(self,h):
        self.__horizontalpostion=h
    def getcurrentspeed(self):
        return(self.__currentspeed)
    def getmaxspeed(self):
        return(self.__maxspeed)
    def getincreaseamount(self):
        return(self.__Increaseamount)
    def gethorizontalpostion(self):
        return(self.__horizontalpostion)

    def increasespeed(self):
        if self.__maxspeed<(self.__Increaseamount+self.__currentspeed):
            self.__horizontalpostion=self.__horizontalpostion+(self.__Increaseamount+self.__currentspeed)       
        

    

    
