"""Python functions for JavaScript Trials 1."""

def outputAllItems(items): 
    for item in items: 
        print(item)

def getAllEvens(nums):
    evenNums = []

    for num in nums:
        if num % 2 == 0:
            evenNums.append(num)
    return evenNums

def getOddIndices(items):
    results = []
    for idx in items: 
        if idx % 2 != 0:
            results.append(idx)
    return results;

def printAsNumberedList(items):
    i = 1 

    for item in items:
        print(f"{i}. {item}")
        i += 1;


def getRange(start, stop):
    nums = []
    i = int(start)

    while int(i) != int(stop) + 1:
        nums.append(i)
        i += 1

    return nums  

def censorVowels(word):
    chars = []
    for letter in word:
        if letter in "aeiou":
            chars.append('*')
        else:
            chars.append(letter)
    censored_word = ""
    for letter in chars:
        censored_word += letter
        # .join() does the same thing as above
    return censored_word

def snakeToCamel(string):
    camelCase = []

    string = string.split('_')

    for index, word in enumerate(string):
        if index == 0:
            word[0].lowercase()
        elif index > 0:
            word[0].uppercase()

    return string


def longestWordLength(words):
    longest = len(words[0])

    for word in word: 
        if len(word) > longest:
            longest = len(word)
    return longest

def truncate(string):
    result = []

    for index, char in enumerate(string): 
        if index != 0:
            if char[index] != char[index-1]:
                result.append(char)


    return result.join()

print(truncate('mississippi'))
# def has_balanced_parens(string):
#     pass  # TODO: 
#      let parens = 0;

#   for (const char of string) {
#     if (char === '(') {
#       parens += 1;
#     } else if (char === ')') {
#       parens -= 1;

#       if (parens < 0) {
#         return false;
#       }
#     }
#   }

#   return parens === 0;
# }


# def compress(string):
#     pass  # TODO: 
#     const compressed = [];

#   let currChar = '';
#   let charCount = 0;
#   for (const char of string) {
#     if (char !== currChar) {
#       compressed.push(currChar);

#       if (charCount > 1) {
#         compressed.push(charCount.toString());
#       }

#       currChar = char;
#       charCount = 0;
#     }

#     charCount += 1;
#   }

#   compressed.push(currChar);
#   if (charCount > 1) {
#     compressed.push(charCount.toString());
#   }

#   return compressed.join('');
# }

