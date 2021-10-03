import collections
class Solution:
    def displayTable(self, orders: list):
        dic = collections.defaultdict(list)
        foods = set()
        for i in range(len(orders)):
            dic[orders[i][1]].append(orders[i][2])
            if orders[i][2] not in foods:
                foods.add(orders[i][2])
        res = [['Table'] + sorted(foods)]
        for i in sorted(dic, key=lambda x: int(x)):
            temp = [i]
            for j in sorted(foods):
                temp.append(str(dic[i].count(j)))
            res.append(temp)
        return res

