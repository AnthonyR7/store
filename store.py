class store(object):
    def __init__(self, location, owner):
        self.location = location
        self.owner = owner
        self.products = []

    def add(self,product_name):
        self.product_name = product_name
        self.products.append(product_name)

    def remove(self):
        self.products.pop()

    def inventory(self):
        if self.products < 0:
            print "You have no inventory for"
            print self.owner, "in", self.location
        else:
            for stuff in self.products:
                print "Your product name", stuff
                print "From ", self.owner, "in", self.location
walmart = store("Anaheim","Tony")
walmart.add("chicken")
walmart.remove()
walmart.inventory()
