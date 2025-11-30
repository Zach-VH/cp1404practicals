"""
Wikipedia Library API
"""
import wikipedia
from wikipedia import DisambiguationError, PageError


def run_test():
    search = input("Enter page title: ")
    while search != "":
        try:
            page = wikipedia.page(search)
            print(page.title)
            print(page.summary)
            print(page.url)
            print()
        except DisambiguationError:
            print('We need a more specific title. Try one of the following, or a new search:')
            print(wikipedia.search(search,5))
        except PageError:
            print(f'Page id "{search}" does not match any pages. Try another id!')
        search = input("Enter page title: ")
    print("Thank you for using the search function")
run_test()