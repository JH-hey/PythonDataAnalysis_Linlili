# import math
# print("hello")
# print("he said:\"Let\'s go!\"")
# print("""hello,my love
# before the sun rising
# after it goes down""")
# greet="您吃了没"
# print(greet + "大爷")
#
# print(math.sin(1))
#
# a=1
# b=9
# c=20
#
# print((-b+math.sqrt(b**2-4*a*c))/2*a)
# print((-b+math.sqrt(b**2-4*a*c))/2*a)

# user_weight=float(input("请输入您的体重：（Kg）"))
# user_height=float(input("请输入您的身高：（m）"))
# bmi=user_weight/(user_height**2)
# print("您的bmi为"+str(bmi))

# a=float(input("请输入一个数字："))
# if a >10:
#     print("a大于10")
# elif a>5:
#     print("a大于5小于10")
# else:
#     print("a小于5")

# shopping_list=[]
# shopping_list.append("运动鞋")
# shopping_list.append("运动裤")
# shopping_list.append("运动套装")
# print(shopping_list)
# shopping_list.remove("运动套装")
# print(shopping_list)
# price=[]
# price.append(100)
# price.append(300)
# price.append(200)
# price.sort()
# print(price)

# dic={"yyds":"就是yyds",
#      "牛逼":"就是牛逼"}
# dic["dd"]="大大的"
# print(dic)
# query = input("请输入查询的词条：")
# if query in dic:
#     print(dic[query])
# else:
#     print("没有这个词条")
#     print("词条数目是"+str(len(dic)))

# tempreture_dic = {"111":"38.9",
#                   "112":"39.9",
#                   "155":"37.7",
#                   "116":"35"}
# for staffid, tempreture in tempreture_dic.items():
#     if float(tempreture) < 38:
#         print(staffid+"的体温是"+tempreture)

#
# user_input = input("请输入你的数字:")
# count=0
# sum=0
# while user_input != "q":
#     count+=1
#     sum+=int(user_input)
#     user_input=input("请输入你的数字:")
# print(count,sum)
# if count==0:
#     print("没有输入数字")
# else:
#     print(sum/count)


#
# gpa_dict={"小明":3.521,
#           "小花":3.869,
#           "小李":2.683}
# for name, gpa in gpa_dict.items():
#     print(f"{name},你好。你当前绩点是{gpa:.2f}")

# class Student:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#         self.grades={"数学":"0",
#                     "语文":"0"}
#     def set_grade(self,course,grades):
#         if course in self.grades:
#             self.grades[course]=grades
#         else:
#             print("没有这个课程")
#     def print_grades(self):
#         print(f"{self.name}，学号是{self.id}:")
#         for course in self.grades:
#             print(f"{course}:{self.grades[course]}")
#
# chen=Student("chen","111")
# zeng=Student("zeng","112")
# chen.set_grade("数学",100)
# chen.print_grades()

# class employee:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def print_info(self):
#         print(f"{self.name},{self.id}")
#
# class FullTimeEmployee(employee):
#     def __init__ (self,name,id,monthly_salary):
#         super().__init__(name,id)
#         self.monthly_salary=monthly_salary
#     def calculate_monthly_pay(self):
#         return self.monthly_salary
#
# class PartTimeEmployee(employee):
#     def __init__ (self,name,id,daily_salary,workdays):
#         super().__init__(name,id)
#         self.daily_salary=daily_salary
#         self.workdays=workdays
#     def calculate_monthly_pay(self):
#         return self.daily_salary*self.workdays
#
# zhang=FullTimeEmployee("zhang","111",10000)
# print(zhang.calculate_monthly_pay())
#
# li=PartTimeEmployee("li","112",100,20)
# print(li.calculate_monthly_pay())
#



#
# with open("./file.txt","r",encoding="utf-8") as f:
#     print(f.read())
#     print(f.readline())
#     print(f.readlines())
#     lines = f.readlines()
#     for line in lines:
#         print(line)
#
# with open("./file2.txt","w",encoding="utf-8") as f:
#     f.write("hello\n")
#     f.write("my love\n")
#     f.write("before the sun rising\n")


# with open("./file2.txt","r+",encoding="utf-8") as f:
#     f.seek(0,2)
#     f.write("after it goes down\n")
#     f.write("I love you, hey hey hey\n")







