#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "bo")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name("yahdiel", "bitcoin")
except Exception as e:
    print(e)