class Dog:
 
    def __init__(self, breed):
        self.breed = breed
 
    def bark(self):
        #print( f'{self.breed} is barking.')
        print( '{} is barking'.format(self.breed))
 
d = Dog('Labrador')
e = Dog('Dabarman')
d.bark()
e.bark()

x = int(input("Please enter an integer:\n"))
 
int_type = ('even', 'odd')[x % 2]
 
print('You entered {} which is an {} integer.'.format(x , int_type))