import string
from bin.Dog import Dog, Cat
from bin import package_script


def myfunc(a):
    if a:
        print('Hello')
    else:
        print('Goodbye')


myfunc(False)


def myfunc_dicc(**kwargs):
    if 'fruit' in kwargs:
        print(kwargs['fruit'])
    else:
        print('not a fruit')


myfunc_dicc(fruit='apple', veggie='lettuce')


def myfunc2(*args, **kwargs):
    print(args)
    print(kwargs)
    print(f'{args[0]} {kwargs["food"]}')


myfunc2(10, 20, 30, fruit='apple', veggie='lettuce', food='jam')


def compare_two_words(str):
    return str.lower().split()[0][0] == str.lower().split()[1][0]


print(compare_two_words('Crazy cat'))


def makes_twenty(num1, num2):
    return (num1+num2) == 20 or num1 == 20 or num2 == 20


makes_twenty(10, 10)

my_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda num: num*2, my_nums)))
print(list(filter(lambda num: num % 2 == 0, my_nums)))

x = range(1, 10, 2)

for i in x:
    print(i)


def range_check(low, high, num):
    if num in range(low, high):
        print(f"{num} is in range")
    else:
        print(f"{num} is not in range")


range_check(1, 10, 5)
range_check(1, 10, 15)


def range_check_bool(low, high, num):
    return num in range(low, high)


print(range_check_bool(1, 10, 5))
print(range_check_bool(1, 10, 15))


def up_low(s):
    d = {"upper": 0, "lower": 0}
    for letter in s:
        if letter.islower():
            d["lower"] += 1
        elif letter.isupper():
            d["upper"] += 1
        else:
            pass
    print("Original string : ", s)
    print("Upper characters: ", d["upper"])
    print("Upper characters: ", d["lower"])


s = "Hello Mr. Al, How Are you this Thursday"
up_low(s)

mylist = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7]


def de_dup(l):
    list2 = []
    for e in l:
        if e not in list2:
            list2.append(e)
    return list2


print(de_dup(mylist))


def palindrom(s):
    return s == s[::-1]


print(palindrom("sugus"))


def ispangram(str1, alphabet=string.ascii_lowercase):
    alphabet = set(alphabet)
    return alphabet <= set(str1.lower())


print(ispangram("The quick brown fox jumps over the lazy dog"))

my_dog = Dog(breed="Lab", name="Dopy", spots=False)
print(type(my_dog))
print(my_dog)
my_dog.speak()
my_cat = Cat(breed="street", name="felix", spots=True)
my_cat.speak()
print(my_cat)

package_script.print_pk_script()
