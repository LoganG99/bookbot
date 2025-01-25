def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    print(how_many_words(file_contents))

def how_many_words(file_contents):
    words = file_contents.split()
    count = len(words)
    return count
    
    
    





























main()