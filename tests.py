# ssssssssh. these aren't "real" tests

from character import Character

# Characters can be instanciated with name and avatar

Arya = Character('Arya Stark', 'Arya.png')
Jon = Character('Jon Snow', 'Jon.png')
no_one = Character('', '')

print(Arya.name, Arya.avatar)
print(Jon.name, Jon.avatar)

# after adding two items to inventory 
# length of inventory should == 2
Arya.inventory.append('Sword')
Arya.inventory.append('Mask')

print(len(Arya.inventory))

# Arya should have a `greet` method
# when i call it with `Arya.greet(Jon)`, it should return
# "Hello Jon Snow, I am Arya Stark. I am awesome."
print(Arya.greet(Jon))
print(Arya.greet(no_one))
