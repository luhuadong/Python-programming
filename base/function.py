# 基本函数格式
def show_hello():
    print("Hello World")

# 带有参数的函数格式
def myadd(x, y):
    '''
        两个数相加
    '''
    return (x+y)

# 带有默认值的参数
def stu(name='Rudy', age=20, gender='male'):
    print("Name:{};Age:{};Gender:{}".format(name,age,gender))

# 关键字参数（可以有效地防止参数传错）
stu("Flower", gender='female', age=2.5)


# 收集参数（带*）
def demo_tuple(*arg):
    print(arg)
    sum=0
    for i in arg:
        sum+=i
    print("Sum: ", sum)

def demo_dict(**arg):
    print(arg)

# 多种参数混合


# 匿名函数
sum = lambda v1,v2: v1+v2


show_hello()
print(myadd(12,13))
stu()
stu("Tina",18,"female")
demo_tuple(10,20,30,40)
demo_dict(length=1,width=2,height=3)

print(sum(10,20))
print(sum(100,200))

