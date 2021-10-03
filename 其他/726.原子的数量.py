import collections
class Solution:
    def countOfAtoms(self, formula: str):
        dic = collections.defaultdict(lambda: 1)
        i = idx = 0
        n = len(formula)
        q = collections.deque([])
        while i < n:
            c = formula[i]
            if c == '(' or c == ')':
                q.append(c)
                i += 1
            else:
                if str.isdigit(c):
                    #获取完整int元素
                    j = i
                    while j < n and str.isdigit(formula[j]):
                        j += 1
                    cnt = int(formula[i: j])
                    i = j
                    #如果栈顶是")"，说明数字能用于一个完整的原子符号
                    if q and q[-1] == ')':
                        tmp = []
                        q.pop()
                        while q and q[-1] != '(':
                            cur = q.pop()
                            dic[cur] *= cnt
                            tmp.append(cur)
                        q.pop()

                        for k in range(len(tmp) - 1, -1, -1):
                            q.append(tmp[k])
                    else:
                        cur = q.pop()
                        dic[cur] *= cnt
                        q.append(cur)

                else:
                    j = i + 1
                    while j < n and str.islower(formula[j]):
                        j += 1
                    cur = formula[i:j] + "_" + str(idx)
                    idx += 1
                    dic[cur] = 1
                    i = j
                    q.append(cur)

        mm = collections.defaultdict(int)
        for key, value in dic.items():
            atom = str(key).split('_')[0]
            mm[atom] += value

        res = []
        for key in sorted(mm.keys()):
            if mm[key] > 1:
                res.append(key + str(mm[key]))
            else:
                res.append(key)

        return "".join(res)


s = Solution()
test = "K4(ON(SO3)2)2"
print(s.countOfAtoms(test))