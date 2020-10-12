class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        mymap = {}
        self.n = len(tickets) + 1
        for i in range(len(tickets)):
            tf = tickets[i][0]
            tt = tickets[i][1]
            if tf not in mymap:
                mymap[tf] = [tt]
            else:
                mymap[tf].append(tt)
        for key in mymap:
            mymap[key].sort(reverse=True)
        stack = []
        self.dfs(mymap, stack, "JFK")
        res = []
        while stack:
            res.append(stack.pop())
        return res
        
    def dfs(self,mymap,stack,fromt):
        if fromt in mymap:
            arrivals = mymap[fromt]
            while arrivals:
                to = arrivals.pop()
                self.dfs(mymap,stack,to)
        stack.append(fromt)
