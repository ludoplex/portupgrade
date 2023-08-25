class PkgVersion:
    def __init__(self, pkgversion):
        if '-' in pkgversion or ' ' in pkgversion:
            raise ValueError(f"{pkgversion}: Must not contain a '-' or whitespace.")
        
        parts = pkgversion.split('_')
        if len(parts) != 2:
            raise ValueError(f"{pkgversion}: Not in due form: '<version>_<revision>'.")

        self.version = parts[0]
        self.revision = int(parts[1])

    def __str__(self):
        return f"{self.version}_{self.revision}"

    def __eq__(self, other):
        if isinstance(other, PkgVersion):
            return self.version == other.version and self.revision == other.revision
        return False

    def __lt__(self, other):
        if isinstance(other, PkgVersion):
            return self.version < other.version or (self.version == other.version and self.revision < other.revision)
        return False

    def __le__(self, other):
        return self == other or self < other

    @classmethod
    def compare_numbers(cls, n1, n2):
        return (n1 > n2) - (n1 < n2)
