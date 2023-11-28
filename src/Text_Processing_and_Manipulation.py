# Counting Words in a Text File
def count_words(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
        word_count = len(text.split())
        return word_count


# Finding and Replacing Text in a File
def find_replace(file_path, search_text, replace_text):
    with open(file_path, 'r') as f:
        text = f.read()
        modified_text = text.replace(search_text, replace_text)
    with open(file_path, 'w') as f:
        f.write(modified_text)


# Generating Random Text
def generate_random_text(length):
    import random
    import string

    letters = string.ascii_letters + string.digits + string.punctuation
    random_text = ''.join(random.choice(letters) for i in range(length))
    return random_text
