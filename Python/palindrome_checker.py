"""
Palindrome Checker
A simple program to check if a word or phrase is a palindrome.
A palindrome reads the same forwards and backwards.
"""

def is_palindrome(text):
    """
    Check if the given text is a palindrome.
    
    Args:
        text (str): The text to check
        
    Returns:
        bool: True if palindrome, False otherwise
    """
    # Remove spaces and convert to lowercase for comparison
    cleaned_text = text.replace(" ", "").lower()
    
    # Check if the text is the same forwards and backwards
    return cleaned_text == cleaned_text[::-1]


def main():
    """Main function to run the palindrome checker."""
    print("=" * 50)
    print("PALINDROME CHECKER".center(50))
    print("=" * 50)
    
    while True:
        # Get user input
        user_input = input("\nEnter a word or phrase (or 'quit' to exit): ").strip()
        
        # Check for exit condition
        if user_input.lower() == 'quit':
            print("\nThank you for using Palindrome Checker!")
            break
        
        # Check if input is empty
        if not user_input:
            print("Please enter a valid word or phrase.")
            continue
        
        # Check if it's a palindrome
        if is_palindrome(user_input):
            print(f"✓ '{user_input}' is a PALINDROME!")
        else:
            print(f"✗ '{user_input}' is NOT a palindrome.")
        
        # Show some examples
        print("\nExamples of palindromes: racecar, madam, A man a plan a canal Panama")


if __name__ == "__main__":
    main()

