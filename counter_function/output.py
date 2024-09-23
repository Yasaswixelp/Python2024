from Function_creation.loop import create_counter


counter = create_counter(10)
values = counter()
for value in values:
    print(value)
