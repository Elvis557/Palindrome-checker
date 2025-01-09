def is_palindrome(text):
    cleaned_text = ''.join(e for e in text if e.isalnum()).lower()
    return cleaned_text == cleaned_text[::-1]

def main():
    text = input("Enter a word or phrase: ")
    if is_palindrome(text):
        print("Yes, it's a palindrome!")
    else:
        print("No, it's not a palindrome.")

if __name__ == "__main__":
    main()
