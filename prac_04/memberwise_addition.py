"""
CP1404 - memberwise addition
Gets Two Lists and adds the lists together
"""

LIST_1 = [1,2,3]
LIST_2 = [4,5,6,4]

def main():
    print(memberwise_addition(LIST_1,LIST_2))

def memberwise_addition(a,b):
    output = []
    if len(a) == len(b):
        for i in range(0,len(a)):
            output.append(a[i]+b[i])
        return output
    else:
        return "Error: Length of both list are different"




main()