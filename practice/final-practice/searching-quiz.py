def linear_search_multiple(input_nums,search_term):
    ls = []
    for i in range(len(input_nums)):
        if input_nums[i] == search_term:
            ls.append(i)

    return ls

def is_palindrome(word):
    ls = []
    for i in range(len(word) - 1, -1, -1):
        ls.append(word[i])

    s = ''.join(ls)

    if word == s:
        print('True')
    else:
        print('False')

is_palindrome('racecar')
is_palindrome('raceca')
