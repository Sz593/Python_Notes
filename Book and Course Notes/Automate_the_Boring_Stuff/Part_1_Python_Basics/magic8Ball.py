import random

def getAnswer(ans):
    if ans == 1:
        return 'It is certain'
    elif ans == 2:
        return 'It is decidely so'
    elif ans == 3:
        return 'Yes'
    elif ans == 4:
        return 'Reply is hazy, try again'
    elif ans == 5:
        return 'Ask again later'
    elif ans == 6:
        return 'Concentrate and ask again'
    elif ans == 7:
        return 'My reply is no'
    elif ans == 8:
        return 'The outlook is not good...'
    elif ans == 9:
        return 'Very doubtful'


## Three lines of program code
## r = random.randint(1,9)
## fortune = getAnswer(r)
## print(fortune)

## The above three lines can be shortened to a single line of code
print(getAnswer(random.randint(1,9)))
