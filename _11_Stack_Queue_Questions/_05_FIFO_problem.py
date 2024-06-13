"""We have to create FIFO Queue
In which we have cat - dogs 
user can only get the oldest dog-cat
or only oldest animal"""


class animals:
    def __init__(self) -> None:
        self.animals = []
    
    def enqueue(self, value):
        self.animals.append(value)
        
    def dequeue(self):
        if self.animals:
            return self.animals.pop(0)
        else:
            print("No pets !!!")
            return None
    
    def dequeueDog(self):
        for i in self.animals:
            if "dog" in i.lower():
                self.animals.pop(self.animals.index(i))
                return i
        else:
            print("Dogs not available")
            
    def dequeueCat(self):
        for i in self.animals:
            if "cat" in i.lower():
                self.animals.pop(self.animals.index(i))
                return i
        else:
            print("Cats not available")

    def __str__(self) -> str:
        if not self.animals:
            return "No animals Available"

        else:
            return str(self.animals)
        
sol = animals()

sol.enqueue("Dog1")
sol.enqueue("Dog2")
sol.enqueue("Cat1")
sol.enqueue("Cat2")
sol.enqueue("Cat3")
sol.enqueue("Dog3")
print(sol)

print(sol.dequeueCat())
print(sol.dequeue())
print(sol.dequeueDog())
print(sol)