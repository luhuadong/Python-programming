'''
 格式化输出
'''
# -- coding: utf-8 --

my_name = 'Rudy Lo'
my_age = 26 # not a lie
my_height = 70 # inches
my_weight = 65 # kilogram
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print("Let's talk about %s." %(my_name))
print("He's %d inches tall." %(my_height))
print("He's %d kg heavy." %(my_weight))
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." %(my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." %(my_teeth))

# this line is tricky, try to get it exactly right
print("If I add %d, %d and %d, I get %d." %(my_age, my_height, my_weight, my_age + my_height + my_weight))

description = '''

    Hello, everyone. I am a programmer, I am writing Python code.
    It's so excited to become a software designer. Now, I'm working
    for China Zero Waste Alliance, the NGO that focus on the topic
    of environmental protection. I hope the time will soon come
    when therewill be no pollution and waste in the world.

'''

print("")
print("DECLARATION : %s" %(description))

# %r 非常有用，它的含义是不管什么都打印出来
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print(x)
print(y)
print("I said: %r" %x)
print("I also said: '%s'" %y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."
print(w+e)

print("-"*32)
print("")

print("Mary had a little lamb.")
print("Its fleece was white as %s." % 'snow')
print("And everywhere that Mary went.")
print("."*10) # what'd that do?

print("")
formatter = "%r %r %r %r"

print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
            "I had this thing.",
            "That you could type up right.",
            "But it did't sing.",
            "So I said goodnight."
))
