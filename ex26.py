from sys import argv
script, filename = argv

age = input()
height = input()
weight = input()

print("How old are you?", end=' ')
print("How tall are you?", end=' ')
print("How much do you weigh?", end=' ')
print(f"So, you're {age} old, {height} tall and {weight} heavy.")


txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt.read())


print("Let's practice everything.")
print("You\'d need to know \'bout escapes with \ that do \n newlines and \t tabs.")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 -6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


started = 10000
jelly_beans, jars, crates = secret_formula(started)

# remember that this is another way to format a string
def start_point(started):
    start_point = start_point / 10
    print(f"With a starting point of: {started}".format(start_point))

# it's just like with an f"" string.
print(f"We'd have: {jelly_beans} beans, {jars} jars, and {crates} crates.")


print("We can also do that this way:")
formula = secret_formula(start_point)

# this is an easy way to apply a list to a format string
print(f"We'd have {jelly_beans} beans, {jars} jars, and {crates} crates.".format(*formula))



people = input()
cates = input()
dogs = input()


if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")
