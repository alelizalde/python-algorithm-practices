hello='Hello'
print(f'{hello[::-1]}')

for letter in 'Hello':
    if letter == 'e':
        continue
    print(letter)

word = 'hello'

for index, letter in enumerate(word):
    print(f'index {index} for letter {letter}')

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

for item in zip(list1, list2):
    print(item)

print(list(zip(list1, list2)))

dic = {'k1', 123}
print('k1' in dic)

# name = input("What's your name?")
# print(name)

mylist = [num**2 for num in range(0,11) if num%2 == 0]
print(mylist)

celcius = [0, 10, 20, 30.5]

fahrenheith = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheith)

results = [ x if x % 2 == 0 else 'ODD' for x in range(0, 10)]
print(results)

mylist = [x * y for x in [1, 2, 3] for y in [1, 10, 100]]
print(mylist)

##################
# Practice

str = 'Print only the words that start with an s in this sentence'

for word in str.split():
    if word[0] == 's':
        print(word)

print([num for num in range(1, 51) if num % 3 == 0])

for word in str.split():
    if len(word) % 2 == 0:
        print(f'{word} is even')

print(list(range(0, 11, 2)))

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(f'{num} FizzBuzz')
    elif num % 3 == 0:
            print(f'{num} Fizz')
    elif num % 5 == 0:
        print(f'{num} Buzz')
    else:
        print(num)

str = 'Create a list of the first letters of every word in the list below'
print([letter[0] for letter in str.split()])
##################

'''
Description of a function
'''


def say_hello(name='NAME'):
    return 'Hello ' + name


print(say_hello('Al'))


def check_dog(mystring):
    return 'dog' in mystring.lower()


print(check_dog('my dog is here'))



