def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        string_from_file = f.read()
        words = string_from_file.split()

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found in the document\n\n")

        letters_count = sort_letters_count(count_letters(string_from_file))

        for entry in letters_count:
            print(f"The '{entry["letter"]}' character was found {entry["count"]} times")
        

def count_letters(str):
    letters_count = {}
    for letter in str.lower():
        if letter == " ":
            continue

        if letter in letters_count:
            letters_count[letter] += 1
        else:
            letters_count[letter] = 1

    return letters_count

def sort_letters_count(letters_count):
    list_of_letters_count = []

    for letter in letters_count:
        if letter.isalpha():
            list_of_letters_count.append({"letter": letter, "count": letters_count[letter]})

    list_of_letters_count.sort(reverse=True, key=sort_by("count"))

    return list_of_letters_count

def sort_by(param_name):
    def sort_fn(dictionary):
        return dictionary[param_name]
    
    return sort_fn

main()