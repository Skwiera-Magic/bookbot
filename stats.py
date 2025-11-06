def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def counted(text):
    counted = text.split()
    return (len(counted))

def specific_number(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char] = 1
    return char_count

def sorter(char_count):
    char_list = []
    for char, count in char_count.items():
        char_list.append({"char": char, "num": count})
    def sort_by_amount(dict_item):
        return dict_item["num"]
    char_list.sort(key=sort_by_amount, reverse=True)
    return char_list

def report_printer(path, number, char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path} ...")
    print("----------- Word Count ----------")
    print(f"Found {number} total words")
    print("--------- Character Count -------")
    for char_dict in char_list:
        char = char_dict["char"]
        if char.isalpha():
            print(f"{char}: {char_dict['num']}")
    print("============= END ===============")