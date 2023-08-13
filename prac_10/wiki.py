import wikipedia


def main():
    user_search = input("Enter a page title or search phrase: ")
    while user_search != "":
        try:
            search_page = wikipedia.page(title=user_search, auto_suggest=False)
            wikipedia.summary(search_page)
        except wikipedia.exceptions.DisambiguationError:
            user_search = input("Please enter a more specific search term: ")
        print(f"{search_page.title}{search_page.summary()}\n{search_page.url}")


main()
