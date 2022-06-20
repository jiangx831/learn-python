# import pygame
# Day1
# standard = 'EA3333'
# price = 20000
# name = '方向盘'
# supplier = '供应商XX'
# print('名称：%s, 型号：%s, 价格：%d, 供应商: %s' % (name, standard, price , supplier))


# Day2
# names = ['姜雪', '刘畊宏', 'Vivi', '周杰伦']
# names.append('昆凌')
# print('增加数据后的列表内容：')
# print(names)
# names[4]='李涛'
# print('修改数据后的列表内容：')
# print(names)
# del  names[4]
# print('删除数据后的列表内容：')
# print(names)


# Day3
# import turtle
# turtle.screensize(600, 400, 'black')
# t = turtle.Pen()
# t.hideturtle()
# t.pensize(10)
# t.speed(1)
# t.pencolor('white')
# t.penup()
# t.forward(-100)
# t.pendown()
# t.circle(50)
# t.penup()
#
# t.forward(70)
# t.pendown()
# t.circle(50)
# t.penup()
#
# t.forward(70)
# t.pendown()
# t.circle(50)
# t.penup()
#
# t.forward(70)
# t.pendown()
# t.circle(50)
# t.penup()
#
# turtle.done()

# Day3
# Day3-python字典应用思考题
# dic = {
#     '阳光': 3000,
#     '僵尸': '铁桶僵尸',
#     '战车': '池塘清洁车'
# }
# print('字典中的原有内容是：')
# print(dic)
# print('增加炸弹角色后的字典内容：')
# dic['炸弹'] = '巴豆炸弹'
# print(dic)
# print('查看植物大战僵尸中的所有角色：')
# print(dic.keys())
#
# print('删除战车角色后的字典内容：')
# del dic['战车']
# print(dic)

# Day4
# import turtle
# turtle.setup(400, 400)
# turtle.screensize(300, 300, 'red')
# t = turtle.Pen()
# t.hideturtle()
# t.speed(1)
# t.pencolor("yellow")
# t.penup()
#
# t.goto(-100, 50)
# t.fillcolor("yellow")
# t.begin_fill()
# for i in range(1, 6):
#     t.pendown()
#     t.forward(200)
#     t.left(216)
# t.end_fill()
# turtle.done()

# Day4
# 《Day4-python条件应用思考题》
# mount = int(input('输入您的银行存款（万元）：'))
# if mount > 300:
#     print('我买玛莎拉蒂')
# elif mount > 200:
#     print('我买保时捷')
# elif mount > 100:
#     print('我买奥迪A6L')
# elif mount > 50:
#     print('我买大众迈腾')
# elif mount > 30:
#     print('我买大众速腾')
# else:
#     print('看来我只能买捷安特自行车了')

# Day5
# import turtle
# turtle.setup(800, 600)
# t = turtle.Pen()
# t.hideturtle()
# t.speed(1)
# t.pensize(1)
# t.penup()
# t.pencolor("red")
#
# t.fillcolor('red')
# t.begin_fill()
# t.goto(-300, -200)
# t.pendown()
# t.goto(300, -200)
# t.pendown()
# t.goto(300, 200)
# t.pendown()
# t.goto(-300, 200)
# t.pendown()
# t.goto(-300, -200)
# t.end_fill()
# t.penup()
#
# t.pencolor('yellow')
# t.fillcolor('yellow')
# t.goto(-260, 130)
# t.pendown()
# t.begin_fill()
# for i in range(0, 5):
#     t.forward(40)
#     t.left(72)
#     t.forward(40)
#     t.right(144)
# t.end_fill()
# t.penup()
#
# t.goto(-120, 170)
# t.pendown()
# t.begin_fill()
# t.right(20)
# for i in range(0, 5):
#     t.forward(10)
#     t.left(72)
#     t.forward(10)
#     t.right(144)
# t.end_fill()
# t.penup()
#
# t.goto(-90, 130)
# t.pendown()
# t.begin_fill()
# t.right(30)
# for i in range(0, 5):
#     t.forward(10)
#     t.left(72)
#     t.forward(10)
#     t.right(144)
# t.end_fill()
# t.penup()
#
# t.goto(-94, 90)
# t.pendown()
# t.begin_fill()
# t.right(10)
# for i in range(0, 5):
#     t.forward(10)
#     t.left(72)
#     t.forward(10)
#     t.right(144)
# t.end_fill()
# t.penup()
#
# t.goto(-120, 60)
# t.pendown()
# t.begin_fill()
# t.right(15)
# for i in range(0, 5):
#     t.forward(10)
#     t.left(72)
#     t.forward(10)
#     t.right(144)
# t.end_fill()
# t.penup()
#
#
# turtle.done()

# Day5
# Day5-python循环应用思考题
# sum = 0
# for i in range(1, 11):
#     age = int(input('请输入第%d位顾客的年领：' % i))
#     if age > 30:
#         sum = sum + 1
# else:
#     p = (10 - sum) / 10 * 100
#     d = 100 - p
#     print('30岁以下的比例是：%0.1f %%' % p)
#     print('30岁以上的比例是：%0.1f %%' % d)

# Day6
# import random
# i = 1
# count = 0
# countPerson = 0
# countComputer = 0
# while i <= 10:
#     person = input('请您出拳(石头、剪刀、布)：')
#     while person != '石头' and person != '剪刀' and person != '布':
#         person = input('输入有误，请您出拳(石头、剪刀、布)：')
#     computer = random.randint(1, 3)
#     if computer == 1:
#         computer = '石头'
#     elif computer == 2:
#         computer = '剪刀'
#     elif computer == 3:
#         computer = '布'
#     print('机器出拳：%s' % computer)
#     if person == computer:
#         print('第%d轮平局' % i)
#         count += 1
#     elif person == '石头' and computer == '剪刀' or person == '剪刀' and computer == '布' or person == '布' and computer == '石头':
#         print('第%d轮您获胜' % i)
#         countPerson += 1
#     else:
#         print('第%d轮机器获胜' % i)
#         countComputer += 1
#     choose = int(input('按0退出，按1继续:'))
#     if choose == 0:
#         break
#     i += 1
# if countPerson > countComputer:
#     print('您获得最终胜利')
# elif countComputer > countPerson:
#     print('机器获得最终胜利')
# else:
#     print('平局')
# print('游戏结束')

# Day6
# rows = int(input('输入菱形变长:'))
# i = 1
# while i <= rows:
#     j = 1
#     while j <= (rows-i):
#         print(' ', end='')
#         j += 1
#     k = 1
#     while k <= i:
#         print('*', end=' ')
#         k += 1
#     print()
#     i += 1
#
# m = rows - 1
# while m > 0:
#     n = 1
#     while n <= rows - m:
#         print(' ', end='')
#         n += 1
#     q = 1
#     while q <= m:
#         print('*', end=' ')
#         q += 1
#     print()
#     m -= 1

# Day7
# emps = ['姜雪', '周杰伦']
# def menu():
#     print('**********企业员工管理************')
#     print('********   1.员工列表************')
#     print('********   2.添加员工************')
#     print('********   3.删除员工************')
#     print('********   4.退出程序************')
#     choose = int(input('请选择:'))
#     while choose != 1 and choose != 2 and choose != 3 and choose != 4:
#         choose = int(input('输入错误，请选择：'))
#     if choose == 1:
#         display()
#     elif choose == 2:
#         addEmp()
#     elif choose == 3:
#         delEmp()
#     elif choose == 4:
#         print('程序退出')
#         return
#     returnMenu()
#
# def display():
#     print('员工姓名列表：')
#     for name in emps:
#         print(name, end=' ')
#
# def addEmp():
#     name = input('输入添加员工的姓名：')
#     count = emps.count(name)
#     if count == 0:
#         emps.append(name)
#         print('添加成功')
#     else:
#         print('员工已存在，不能重复添加')
#
# def delEmp():
#     name = input('输入删除员工的姓名：')
#     count = emps.count(name)
#     if count == 0:
#         print('员工不存在，不能删除')
#     else:
#         idx = emps.index(name)
#         emps.pop(idx)
#         print('删除成功')
#
# def returnMenu():
#     print('')
#     inpNum = int(input('按0返回：'))
#     if inpNum == 0:
#         menu()
#
# menu()

# Day8
# import time
# class Corpse:
#     def __init__(self, name, blood, harm):
#         self.name = name
#         self.blood = blood
#         self.harm = harm
#     def bite(self):
#         print('%s咬了一口，伤害值：%d'% (self.name, self.harm))
#
# class Shooter:
#     def __init__(self, name, blood, harm):
#         self.name = name
#         self.blood = blood
#         self.harm = harm
#     def bite(self):
#         print('%s咬了一口，伤害值：%d'% (self.name, self.harm))
#
# s1 = Shooter('豌豆射手', 50, 10)
# c1 = Corpse('普通僵尸', 100, 15)
#
# while s1.blood > 0 and c1.blood:
#     s1.bite()
#     c1.blood -= s1.harm
#     time.sleep(1)
#
#     s1.bite()
#     c1.blood -= s1.harm
#     time.sleep(1)
#
#     c1.bite()
#     s1.blood -= c1.harm
# else:
#     if s1.blood > 0:
#         print('%s获胜，剩余血量%d'%(s1.name, s1.blood))
#     else :
#         print('%s获胜，剩余血量%d' % (c1.name, c1.blood))

# Day8
# class Emp:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def work(self):
#         print('%s努力工作，每月能赚%d元' % (self.name, self.salary))
#
# e1 = Emp('周杰伦', 10000)
# e2 = Emp('王心凌', 12000)
# e1.work()
# e2.work()

# Day9
# class Vehicle:
#     def __init__(self, licenseNo, name):
#         self.name = name
#         self.licenseNo = licenseNo
#     def calculate(self, days):
#         return 0
# class Car(Vehicle):
#     def __init__(self, licenseNo, name, seat):
#         super().__init__(licenseNo, name)
#         self.seat = seat
#     def calculate(self, days):
#         if self.seat <= 5:
#             return 300 * days
#         elif self.seat <= 7:
#             return 400 * days
#         else:
#             return 500 * days
# class Trunk(Vehicle):
#     def __init__(self, licenseNo, name, load):
#         super().__init__(licenseNo, name)
#         self.load = load
#     def calculate(self, days):
#         if self.load <= 10:
#             return 500 * days
#         elif self.load <= 15:
#             return 800 * days
#         else:
#             return 1000 * days
# list1 = []
# car1 = Car('京A12312', '奥迪A6', 5)
# car2 = Car('京P45645', '大众商务', 7)
# truck = Trunk('吉A66666', '一汽大众', 30)
# list1.append(car1)
# list1.append(car2)
# list1.append(truck)
# sum2 = 0
# for v in list1:
#     sum2 += v.calculate(2)
# print('共需支付%d元' % sum2)


#  Day9
# class Emp(object):
#     def __init__(self):
#         self.__name = ''
#         self.__no = ''
#         self.__salary = 0
#
#     def getName(self):
#         return self.__name
#
#     def setName(self, name):
#         self.__name = name
#
#     def getNo(self):
#         return self.__no
#
#     def setNo(self, no):
#         self.__no = no
#
#     def getSalary(self):
#         return self.__salary
#
#     def setSalary(self, salary):
#         self.__salary = salary
#
#
# emp1 = Emp()
# emp1.setName('马云')
# emp1.setNo('1001')
# emp1.setSalary(11000)
# print('工号：%s, 姓名：%s, 工费：%d' % (emp1.getNo(), emp1.getName(), emp1.getSalary()))

# Day10
# def inputs():
#     try:
#         num1 = int(input('输入第一个数:'))
#         num2 = int(input('输入第二个数:'))
#         result = num1 / num2
#     except ValueError:
#         print('输入非法字符')
#     except ZeroDivisionError:
#         print('以0作除数')
#     except Exception as result:
#         print('未知错误:%s' % result)
#     else:
#         print('%d/%d=%0.1f' % (num1, num2, result))
#     finally:
#         print('程序结束')
#
# inputs()

# Day10
# list = ['python课程', 'Diango课程', 'Flash课程']
# def inputs():
#     try:
#         num = int(input('请输入一个0-3之间的数字：'))
#     except ValueError:
#         print('输入格式不正确')
#     else:
#         if num < 0 or num > 3:
#             print('范围必须在1-3之间')
#             return
#         print(list[num - 1])
#     finally:
#         print('欢迎提出建议')
# inputs()

# Day15
import tkinter
import tkinter.messagebox
import tkinter.filedialog

root = tkinter.Tk()
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
ww = 500
wh = 400

root.title('我的弹窗')
root.geometry('500x300+%d+%d' % ((sw - ww) // 2, (sh - wh) // 2))
root.config(bg='pink')
lbltitle = tkinter.Label(root, text="选择EXCEL文件：", font=('楷体', 12), width=10, height=2, pady=3, padx=20, bg='pink')
lbltitle.grid(row=0, column=0)

euname = tkinter.Entry(root, font=('楷体', 12), width=20)
euname.grid(row=0, column=1)


def choose1():
    file_name = tkinter.filedialog.askopenfilename(title='选择excel文件')
    euname.insert('end', file_name)


def save():
    file_name = str(euname.get())
    if file_name == '':
        tkinter.messagebox.showinfo(title='错误提示', message='文件不能为空')
    elif file_name.find('.xls', 0, len(file_name)) == -1 and file_name.find('.xlsx', 0, len(file_name)) == -1:
        tkinter.messagebox.showinfo(title='错误提示', message='请选择excel文件')
    else:
        tkinter.messagebox.showinfo(title='选择提示', message='文件选择正确')


btn = tkinter.Button(root, text="选择", font=('楷体', 12), width=8, padx=5, command=choose1)
save_btn = tkinter.Button(root, text="保存", font=('楷体', 12), width=8, padx=5, command=save)
btn.grid(row=0, column=2)

root.mainloop()
