# ssssssssh. these aren't "real" tests

from character import Character
from character import Hero
from character import Monster

# Characters can be instanciated with name and avatar

Arya = Character('Arya Stark', 'Arya.png')
Jon = Character('Jon Snow', 'Jon.png')

print(Arya.name, Arya.avatar)
print(Jon.name, Jon.avatar)

# after adding two items to inventory 
# length of inventory should == 2
Arya.inventory.append('Sword')
Arya.inventory.append('Mask')

print(len(Arya.inventory))

# Arya should have a `greet` method
# when i call it with `Arya.greet()`, it should return
# "Hello, I am Arya Stark. I am awesome."
print(Arya.greet())


# Arya should have a `greet` method
# when i call it with `Arya.greet(Jon)`, it should return
# "Hello, Jon Snow, I am Arya Stark. I am awesome."
print(Arya.greet(Jon))

# I should be able to create a hero instance
Bronn = Hero("Bronn of the Blackwater", "bron.png")

# Hero should be able to greet Character
print(Bronn.greet(Arya))
print(Jon.greet(Bronn))
print(Arya.greet(Bronn))

#I should be able to create a Monster instance
White_walker = Monster()

#When I print white_walker.name and white_walker.avatar the name and avatar will be returned
# print(White_walker.name, White_walker.avatar)

# When I call White_walker.greet() it will return 
# "Grr, Im a monster"
print(White_walker.greet())