"""
CP1404 - memberwise addition
Gets Two Lists and adds the lists together
"""

LIST_1 = [1.0,2,3,0]
LIST_2 = [4.5,5.5,3,0]

def main():
    print(memberwise_addition(LIST_1,LIST_2))

def memberwise_addition(a,b):
    output = []
    if len(a) == len(b):
        try:
            for i in range(0,len(a)):
                output.append(a[i]+b[i])
            return output
        except TypeError:
            return "Error: List contains value other than int or float"
    else:
        return "Error: Length of both list are different"




main()