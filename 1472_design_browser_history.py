"""
    Class designed to hold browser history.
"""

class BrowserHistory:
    """
        Class designed to hold browser history.
    """
    def __init__(self, homepage: str):
        self.arr = [homepage]
        self.cur = 0
        self.end = 0

    def visit(self, url: str) -> None:
        """
            Visits a url. Deletes any future urls
        """
        if self.cur == self.end and self.end == len(self.arr) - 1:
            self.cur += 1
            self.end += 1
            self.arr.append(url)
        else:
            self.cur += 1
            self.end = self.cur
            self.arr[self.cur] = url

    def back(self, steps: int) -> str:
        """
            Goes back number of steps. Does not go back farther than the first page. 
        """
        self.cur = max(0, self.cur - steps)

        return self.arr[self.cur]

    def forward(self, steps: int) -> str:
        """
            Goes forward number of steps. Does not go back farther than the last page. 
        """
        self.cur = min(self.end, self.cur + steps)

        return self.arr[self.cur]
