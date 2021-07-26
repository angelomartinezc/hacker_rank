# Alphabet filter
# Given a string consisting of only lowercase characters, create two methods that remove all the consonants or lowels from the given word. 
# They must retain the original order of the characters in the returned strings.
# Example:
# s = 'onomatopeia'
# The filter_vowel method removes all vowels from s and returns the string 'nmtp'.
# The filter_consonants method removes all consonants from s and returns the string 'ooaoeia'.

# Function Description
# For a given definition of a class LetterFilter, complete its methods filter_vowels and filter_consonants. 
# The class takes a string in the constructor and stores it to its s attribute. 
# The method filter_vowels must return a new string with all vowels removed from it. 
# Similarly, the method filter_consonants must return a new string with all consonants removed from it.



class LetterFilter:
    def __init__(self, s):
        self.s = s
	
    def filter_vowels(self):
        # Enter your code here
        vowels = ('a', 'e', 'i', 'o', 'u')
        r = ''
        for char in self.s:
            if char not in vowels:
               r +=''+char
        return r
        # Return a string

    def filter_consonants(self):
        # Enter your code here
        vowels = ('a', 'e', 'i', 'o', 'u')
        c = ''
        for char in self.s:
            if char in vowels:
                c +=''+char
        return c
        # Return a string



s = input()
f = LetterFilter(s)
print(f.filter_vowels())
print(f.filter_consonants())
