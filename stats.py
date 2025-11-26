def count_words(book):
    count = len(book.split())
    return count

def count_char(book):
    dict = {}
    for i in range(0,len(book)-1):
        char = book[i].lower()
        if char in dict:
            dict[char] +=1
        else:
            dict[char] = 1
    return dict

def sort_on(items):
    return items["count"]

def sort_char(dict):
    output_list = [{"char": key, "count": value} for key, value in dict.items()]
    output_list.sort(reverse=True,key=sort_on)
    return output_list