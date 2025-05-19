import sys
from stats import word_count, char_count, sort_on

# This function takes a file path as input and returns the text in the file
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        text = f.read()
        return text
    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}..." )
    book = get_book_text(path_to_file)
    count = word_count(book)
    char_counts = char_count(book)
    report = sort_on(char_counts)
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for repo in report:
            if repo["char"].isalpha():
            
                print(f'{repo["char"]}: {repo["num"]}')
    print("============= END ===============")
        
main()


