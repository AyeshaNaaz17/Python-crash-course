# parameters
def say_hello (name, emoji):
    print(f'Helllloooooo {name}{emoji}')

# default parameters
def say_hello(name="Mike", emoji=";)"):
    print(f'Helllloooooo {name}{emoji}')

# arguments
say_hello("Ayesha", " ;)") # call / invoke
say_hello("Taehyung", " :)")

# keyword arguments - bad practice
say_hello(emoji=' :)', name="Jungkook")

say_hello()
say_hello(emoji=':)')
say_hello(name='Steve')
say_hello(name='El', emoji=':>')