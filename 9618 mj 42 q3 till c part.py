class Employee:
    #self.__hourlypay integer
    #self.__empnumber string
    #self.__jtitle string
    def __init__(self,hpay,empnum,jobtitle):
        self.__hourlpay=hpay
        self.__empnumber=empnum
        self.__jtitle=jobtitle
        self.__pyear2022=[]
        for y in range(52):
            self.__pyear2022.append(0.00)
    def GetEmployeeNumber(self):
        return self.__empnumber
    def setpay(self,wnum,hnum):
        self.__pyear2022[wnum-1]=hnum*self.__hourlpay
    def GetTotalPay(self):       
        tpay=o
        for y in range(52):
            tpay=tpay+self.__pyear2022[y]
        return tpay
class Manager(Employee):
    #BonusValue single
    def __init__(self, hpay,empnum,jobtitle, BonusP):
        super().__init__(hpay,empnum,jobtitle)
        self.__BonusValue = BonusP
    def setpay(self,wnum,hnum):
        hours=hours*(1+self.__BonusValue/100)
        super().setpay(wnum.hnum)
# Declare the array to store data about 8 employees
EmployeeArray = [] * 8

# Read in the data from the file
with open('Employees.txt', 'r') as file:
    for i in range(8):
        hourly_pay = file.readline().strip()
        print(hourly_pay)
        employee_number = file.readline().strip()
        print(employee_number)
        bonus_value = (file.readline().strip()) 
        
        if bonus_value.isnumeric():
            job_title = file.readline().strip()
        else:
            job_title=bonus_value
            bonus_value=None
        print(bonus_value)
        print(job_title)  
        

        # Instantiate each employee based on the bonus value
        if bonus_value.isnumeric():
            EmployeeArray.append(Manager(hourly_pay, employee_number, job_title, bonus_value))
        else:
          EmployeeArray.append(Employee(hourly_pay, employee_number, job_title))

# Access and print information about each employee
# employee in EmployeeArray:
 #   if isinstance(employee, Manager):
  #      print(f"Manager - Employee Number: {employee.employee_number}, Job Title: {employee.job_title}, Bonus Value: {employee.bonus_value}%")
   # else:
    #    print(f"Employee - Employee Number: {employee.employee_number}, Job Title: {employee.job_title}")
#print(EmployeeArray)   
