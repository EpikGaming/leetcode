class Solution:
    def canEat(self, candiesCount: list, queries: list):
        answer = [False] * len(queries)
        if not queries:
            return answer

        for i in range(1, len(candiesCount)):
            candiesCount[i] += candiesCount[i - 1]

        for i in range(len(queries)):
            print(i)
            favoriteType = queries[i][0]
            favoriteDay = queries[i][1] + 1
            daily = queries[i][2]
            if favoriteType == 0:
                if favoriteDay > candiesCount[favoriteType]:
                    continue
                else:
                    answer[i] = True
            else:
                if favoriteDay > candiesCount[favoriteType]:
                    continue
                if favoriteDay >= candiesCount[favoriteType - 1]:
                    answer[i] = True
                    continue
                elif daily * favoriteDay > candiesCount[favoriteType - 1]:
                    answer[i] = True
        return answer


s = Solution()
candy = [46,5,47,48,43,34,15,26,11,25,41,47,15,25,16,50,32,42,32,21,36,34,50,45,46,15,46,38,50,12,3,26,26,16,23,1,4,48,47,32,47,16,33,23,38,2,19,50,6,19,29,3,27,12,6,22,33,28,7,10,12,8,13,24,21,38,43,26,35,18,34,3,14,48,50,34,38,4,50,26,5,35,11,2,35,9,11,31,36,20,21,37,18,34,34,10,21,8,5]
question = [[85,54,42]]
x = 0
for i in range(85):
    x += candy[i]
print(x)
print(54 * 42)
print(s.canEat(candy, question))


test1 = "false,false,false,false,true,false,false,false,false,false,false,true,true,false,true,true,true,true,false,false,false,false,true,false,false,true,false,false,false,true,false,true,false,false,true,false,false,false,false,true,true,false,true,true,false,false,true,true,true,true,true,true,true,false,true,false,true,true,true,true,true,false,false,true,true,false,true,false,false,false,true,true,false,true,false,true,true,false,false,true,false,true,false,true,true,true,true,false,true,false,false,true,true,true"
test2 = "false,false,false,false,true,false,false,false,false,false,false,true,true,false,true,true,true,true,false,false,false,false,true,false,true,true,false,false,false,true,false,true,false,false,true,false,false,false,false,true,true,false,true,true,false,false,true,true,true,true,true,true,true,false,true,false,true,true,true,true,true,false,false,true,true,false,true,false,false,false,true,true,false,true,false,true,true,false,false,true,false,true,false,true,true,true,true,false,true,false,false,true,true,true"