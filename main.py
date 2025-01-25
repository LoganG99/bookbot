def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    print(how_many_words(file_contents))
    print(count_characters(file_contents))

def how_many_words(file_contents):
    words = file_contents.split()
    count = len(words)
    return count

def count_characters(file_contents):
    lowered_string = file_contents.lower()
    characters = list(lowered_string)
    dic = {}
    count = 1
    for l in characters:
        if l not in dic:
            dic[l] = count
    
        else:
            dic[l] += 1
    return dic
    
    
    





























main()