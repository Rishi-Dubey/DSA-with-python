"""Here I will create tree data structure and implement its methods"""

class Tree:
    def __init__(self, data, children = None) -> None:
        self.data = data
        if children is None:
            self.children = []
        else:
            self.children = children
    
    def __str__(self, level = 0) -> str:
        # using recursion to call classes stored inside the main class [class1, class1]
        layer = "  " * level + str(self.data) + "\n"
        for child in self.children:
            layer += child.__str__(level + 1)
            
        return layer

    def addChild(self, TreeNode):
        self.children.append(TreeNode)
        
# Root of Tree    
drink = Tree("Drink")

# Child of Tree
cold = Tree("Cold")
hot = Tree("Hot")

# adding it to root(passing the class(cold, hot) as tree)
drink.addChild(cold)
drink.addChild(hot)

print(drink)

# now creating add adding children of cold and hot subclass
fruti = Tree("Fruti")
Coca_Cola = Tree("Coca_Cola")
cold.addChild(fruti)
cold.addChild(Coca_Cola)

Coffee = Tree("Coffee")
Chai = Tree("Chai")
hot.addChild(Coffee)
hot.addChild(Chai)

print(drink)
