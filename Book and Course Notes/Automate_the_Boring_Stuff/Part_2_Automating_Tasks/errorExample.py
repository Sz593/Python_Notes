#! python3

def spam():
    bacon()

def bacon():
    raise Exception('This is an error message.')

spam()
