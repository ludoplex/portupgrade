class PkgInfo:
    def __init__(self, pkgname):
        if not isinstance(pkgname, str):
            raise TypeError("pkgname must be a string")
        if " " in pkgname:
            raise ValueError("pkgname must not contain whitespace")
        if "-" not in pkgname:
            raise ValueError("pkgname must be in the form: <name>-<version>")
        self.name, self.version = pkgname.rsplit("-", 1)

    def __str__(self):
        return f"{self.name}-{self.version}"

    def __eq__(self, other):
        if not isinstance(other, PkgInfo):
            return NotImplemented
        return (self.name, self.version) == (other.name, other.version)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if not isinstance(other, PkgInfo):
            return NotImplemented
        return (self.name, self.version) < (other.name, other.version)

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not (self == other or self < other)

    def __ge__(self, other):
        return self == other or self > other
