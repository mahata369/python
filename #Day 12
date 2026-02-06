# Check whether given word is palindrome or not

# def check_palindrome():
#     str = input("Enter a word to check").lower()
#     if str == str[::-1]:
#         print("Palindrome")
#     else:
#         print("Not palindrome")

# check_palindrome()


# def check_palindrome(word):
#     word = word.lower()
    
#     if str == str[::-1]:
#         return print("Palindrome")
#     else:
#         return print("Not palindrome")

# str = input("Enter a word to check").lower()   
# check_palindrome(str)


# Armstrong number
# def check_armstrong(num):
#     temp = num
#     num_length = len(str(num))
#     total = 0

#     while temp > 0:
#         digits = temp % 10
#         total += digits**num_length
#         temp //= 10

#     if total == num:
#         return print("Armstrong")
#     else:
#         return print("Not armstrong")
    
# check_armstrong(153)


# Sum of digits
# def sum_of_digits(num):
#     total = 0
#     while num > 0:
#         digit = num % 10
#         total += digit
#         num //= 10
#     return total

# n =int(input("Enter a number"))
# print(sum_of_digits(n))

# Count number of vowels in a word
# def count_vowels(text):
#     v_count = 0
#     c_count = 0
#     for char in text.lower():
#         if  char in "aeiou":
#             v_count +=1
#         if not char in " aeiou":
#             c_count +=1
#     #return count
#     print(f"Number of vowels: {v_count}")
#     print(f"Number of consonant:{c_count}")
# count_vowels("hello world")

# find longest word
def longest_word(sentence):
    words = sentence.split()#split() converts to a list
    longest = words[0]

    for word in words:
        if len(word)>len(longest):
            longest = word
    return longest

print(longest_word("Hello this is python programming"))

"""
['Hello','this','is','python','programming']
longest = hello
1st itetration:
word = Hello/5
longest = Hello/5

2nd itetration:
word=this/4
longest=hello/5

3rd itetration:
word=is/2
longest=hello/5

4th itetration:
word=python/6
longest=hello/5(update longest)

5th itetration:
word = programming/11
longest=python/6 (update longest)
longest=programming

"""