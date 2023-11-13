def reverse_words(string):
    # Split the string into words using the dot as a separator
    words = string.split('.')
    
    # Reverse the order of the words
    reversed_words = words[::-1]
    
    # Join the reversed words back together with dots
    reversed_string = '.'.join(reversed_words)
    
    return reversed_string

# Example usage:
input_string = "Hello.World"
result = reverse_words(input_string)
print(result)  # Output: "World.Hello"



# def reverse_words_alternative(string):
#     reversed_string = []
#     word = []
    
#     for char in string:
#         if char != '.':
#             word.append(char)
#         else:
#             if word:
#                 reversed_string.extend(reversed(word))
#                 reversed_string.append('.')
#             word = []
    
#     if word:
#         reversed_string.extend(reversed(word))
    
#     return ''.join(reversed_string)

# # Example usage:
# input_string = "Hello.World"
# result = reverse_words_alternative(input_string)
# print(result)  # Output: "World.Hello"

