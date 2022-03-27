"""
月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员1800底薪加销售额5%提成
"""

from abc import ABCMeta,abstractmethod

class Employee(metaclass=ABCMeta):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def getSalary(self):
        pass

class Manager(Employee):
    def __init__(self,name):
        # super(Employee, self).__init__(name)
        super().__init__(name)

    def getSalary(self):
        return 15000

class Program(Employee):
    def __init__(self,name,workTime):
        super(Program, self).__init__(name)
        self.workTime=workTime

    def getSalary(self):
        return self.workTime*200

class Saler(Employee):
    def __init__(self,name,saleMoney):
        super().__init__(name)
        self.saleMoney=saleMoney

    def getSalary(self):
        return 1800+self.saleMoney*5/100

class EmployeeFactory():
    @staticmethod
    def create(emp_type,*args,**kwargs):
        all_emp= { "M":Manager,
                   "P":Program,
                   "S":Saler
        }
        cls=all_emp[emp_type]
        return cls(*args,**kwargs) if cls else None
def main():
    emps=[EmployeeFactory.create('M','zhangsan'),EmployeeFactory.create('P','lisi',240),EmployeeFactory.create('S','wangwu',100000)]
    for emp in emps:
        print(emp.name,emp.getSalary())

if __name__ == '__main__':
    main()