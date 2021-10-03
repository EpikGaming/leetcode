import collections
class ThroneInheritance:
    def __init__(self, kingName:str):
        self.king = kingName
        self.edges = collections.defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str):
        self.edges[parentName].append(childName)

    def death(self, name: str):
        self.dead.add(name)

    def getInheritanceOrder(self):
        ans = []

        def preorder(name: str):
            if name not in self.dead:
                ans.append(name)
            if name in self.edges:
                for child in self.edges[name]:
                    preorder(child)
        preorder(self.king)
        return ans