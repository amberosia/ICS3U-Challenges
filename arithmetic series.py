#title: arithmetic series
#developer: jenna wan
#purpose: outputs the sum of the first "num" positive integers

def gauss(num):
    if num <= 0:
        return 0
        
    else:
        return num + gauss(num - 1)
