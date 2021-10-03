class UnionFind:
    def __init__(self):
        self.father = {}
        self.accounts = {}

    def find(self, x):
        if not self.father[x]:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        if len(self.accounts[root_x]) > len(self.accounts[root_y]):
            self.father[root_y] = root_x
            self.accounts[root_x] += self.accounts[root_y]
            del self.accounts[root_y]
        else:
            self.father[root_x] = root_y
            self.accounts[root_y] += self.accounts[root_x]
            del self.accounts[root_x]

    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.accounts[x] = [x]

class Solution:
    def accountsMerge(self, accounts: list):
        uf = UnionFind()
        for account in accounts:
            name, master = account[0], account[1]
            uf.add((name, master))
            account = list(set(account[2:]))
            for i in range(len(account)):
                uf.add((name, account[i]))
                uf.merge((name, master), (name, account[i]))
        res = []
        for key, value in uf.father.items():
            if not value:
                usr_account = [uf.accounts[key][0][0]]
                for account in uf.accounts[key]:
                    usr_account.append(account[1])
                res.append(sorted(usr_account))
        return res

