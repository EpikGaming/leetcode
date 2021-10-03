import collections
class Solution:
    def build_graph(self, accounts: list):
        graph = collections.defaultdict(list)
        for account in accounts:
            master = account[1]
            for email in list(set(account[2:])):
                graph[master].append(email)
                graph[email].append(master)
        return graph

    def dfs(self, email, graph, visited, emails):
        if email in visited:
            return

        visited.add(email)
        emails.append(email)

        for neighbor in graph[email]:
            self.dfs(neighbor, graph, visited, emails)

    def accountsMerge(self, accounts: list):
        graph = self.build_graph(accounts)
        res = []
        visited = set()
        for account in accounts:
            emails = []
            self.dfs(account[1], graph, visited, emails)
            if emails:
                res.append([account[0]] + sorted(emails))

        return res