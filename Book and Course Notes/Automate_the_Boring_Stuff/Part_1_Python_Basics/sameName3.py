def spam():
    global eggs
    eggs = 'spam' #global variable

def bacon():
    eggs = 'bacon' #local variable

def ham():
    print(eggs) #this uses the global eggs, since no local eggs is defined

eggs = 42 #global
spam()
print(eggs)
