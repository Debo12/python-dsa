class TreeNode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children
    
    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
    def add_child(self, TreeNode):
        self.children.append(TreeNode)

drinks = TreeNode("Drinks", [])
cold = TreeNode("Cold", [])
hot = TreeNode("Hot", [])
drinks.add_child(cold)
drinks.add_child(hot)

tea = TreeNode("Tea", [])
coffee = TreeNode("Coffee", [])
hot.add_child(tea)
hot.add_child(coffee)

juice = TreeNode("Juice", [])
fanta = TreeNode("Fanta", [])
cold.add_child(juice)
cold.add_child(fanta)

print(drinks)