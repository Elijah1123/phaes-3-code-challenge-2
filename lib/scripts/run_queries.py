from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def print_menu():
    print("\n--- CLI Menu ---")
    print("1. List all authors")
    print("2. List all magazines")
    print("3. List all articles")
    print("4. Find articles by author")
    print("5. Find magazines by author")
    print("6. Find articles by magazine")
    print("0. Exit")

def run():
    while True:
        print_menu()
        choice = input("Select an option: ")

        if choice == "1":
            for author in Author.get_all():
                print(f"{author.id}: {author.name}")

        elif choice == "2":
            for mag in Magazine.get_all():
                print(f"{mag.id}: {mag.name} ({mag.category})")

        elif choice == "3":
            for article in Article.get_all():
                print(f"{article.id}: {article.title} (Author: {article.author_id}, Magazine: {article.magazine_id})")

        elif choice == "4":
            aid = int(input("Enter author ID: "))
            author = Author(aid, "")
            for art in author.articles():
                print(f"{art.id}: {art.title}")

        elif choice == "5":
            aid = int(input("Enter author ID: "))
            author = Author(aid, "")
            for mag in author.magazines():
                print(f"{mag.id}: {mag.name} ({mag.category})")

        elif choice == "6":
            mid = int(input("Enter magazine ID: "))
            for art in Article.find_by_magazine(mid):
                print(f"{art.id}: {art.title}")

        elif choice == "0":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    run()
