class PkgTSort:
    def __init__(self):
        self.hints = {}

    def empty(self):
        return len(self.hints) == 0

    def clear(self):
        self.hints.clear()

    def dump(self):
        return self.hints.copy()

    def add(self, a, *b):
        if a is None:
            return self
        b = [x for x in b if x is not None]
        self.hints[a] = self.hints.get(a, []) + b
        for x in b:
            if x not in self.hints:
                self.hints[x] = []
        return self

    def delete(self, a, *b):
        if a not in self.hints:
            return self
        if len(b) == 0:
            del self.hints[a]
            for x in self.hints:
                if a in self.hints[x]:
                    self.hints[x].remove(a)
        else:
            for x in b:
                if x in self.hints[a]:
                    self.hints[a].remove(x)
        return self

    def tsort(self):
        result = []
        visited = {}

        def visit(n):
            if n in visited:
                if visited[n] == 0:
                    raise ValueError("Found a cycle")
            else:
                visited[n] = 0
                for m in self.hints.get(n, []):
                    visit(m)
                visited[n] = 1
                result.append(n)

        for n in self.hints:
            visit(n)

        return result
