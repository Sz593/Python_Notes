#! python3

def listToStr(l):
    output = str(l[0])
    for i in range(1,len(l)-1):
        output += ', ' + str(l[i])
    output += ' and ' + str(l[len(l)-1])
    print(output)

spam = ['apples','bananas','tofu','cats']
#spam = [1,2,3,4,5,6,7,8]
listToStr(spam)
