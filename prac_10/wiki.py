"""
Wikipedia Library API
"""
import wikipedia

def run_test():
    search = input("What would you like to search up? ")
    while search != "":
        print(wikipedia.summary(search,sentences=3))
        search = input("What would you like to search up? ")
    print("Thanking for using the search function")
run_test()