class car:
    def __init__(self,n,e):
    
        self.__vechilid=n
        self.__registration=""
        self.__dateofregsitration=None
        self.__enginesize=e
        self.__purchaseprice=0.00
        self.__tax=0.00
    def settax(self):
        t=self.__purchaseprice*0.25
        self.__tax=t
    def setprice(self,p):
        
        self.__purchaseprice=p
    def setdor(self,d):
        self.__dateofregsitration=d
    def getvechileid(self):
        return(self.__vechilid)
    def getenginesize(self):
        return(self__enginesize)
    def getprice(self):
        return(self.__purchaseprice)
    def gettax(self):
        return(self.__tax)
#civic=car("abcd",1800)
#civic.setprice(800000)
#print("The price of cvic is",(civic.getprice()))
      
#city=car("wery",2000)
#civic.settax()
#print(civic.gettax())
vigo=car("a21",30000)
x=int(input("Enter Vigo Price"))
vigo.setprice(x)
vigo.settax()
print("The price of vigo is",vigo.getprice(),"and the tax is",vigo.gettax())












        
