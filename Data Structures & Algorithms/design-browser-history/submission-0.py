class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = ListNode(homepage)
        self.cur = self.homepage

    def visit(self, url: str) -> None:
        newPage = ListNode(url)
        newPage.prev = self.cur
        self.cur.next = newPage
        self.cur = newPage

        return None

    def back(self, steps: int) -> str:
        while self.cur.prev and steps > 0:
            steps -= 1
            self.cur = self.cur.prev

        return self.cur.val

    def forward(self, steps: int) -> str:
        while self.cur.next and steps > 0:
            steps -= 1
            self.cur = self.cur.next

        return self.cur.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)