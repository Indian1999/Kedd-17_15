"""
print("Hello World!") # f5 comment
név = "Adam" # string típusú változó
print("Hello " + név + "!")

myName = input("Add meg a neved: ")
print("Hello " + myName + "!")
print(type(myName)) #<class 'str'>
print(id(myName)) #1788252108784
print(id(név)) #1788252099312
"""

name = "Logi Róbert" #string
age = 11 #int
weight = 46.7 #float
smart = True #bool

print(type(name))   # <class 'str'>
print(type(age))    # <class 'int'>
print(type(weight)) # <class 'float'>
print(type(smart))  # <class 'bool'>

print("Szia! " + name + " vagyok.")
print("Idén vagyok " + str(age) + " éves.")
print(str(weight) + " kg a súlyom.")
if smart:
    print("Okos vagyok.")
else:
    print("Nem vagyok valami okos.")

print("commit test")

