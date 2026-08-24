'''Create a class with a class attribute a; create an object from
it and set ‘aʼ directly using ‘object.a = 0ʼ. Does this change the 
class attribute?'''

class Demo:
    a = 4          # class attribute

object = Demo()   
print(object.a)    # prints class attribute (4)

object.a = 0       # object attribute set to 0 (a=0)
print(object.a)    # prints object attribute (0)

print(Demo.a)      # prints the class attribute

# ANSWER: changing the object attribute does not change the class attribute!