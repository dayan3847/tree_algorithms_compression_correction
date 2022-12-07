class TreeObject:
    name = str
    value = float

    def __init__(self, name: str = '', value: float = 0):
        self.name = name
        self.value = value

    def __gt__(self, other: 'TreeObject'):
        return self.value > other.value

    def __lt__(self, other: 'TreeObject'):
        return self.value < other.value

    def __eq__(self, other: 'TreeObject'):
        return self.value == other.value

    def __ge__(self, other: 'TreeObject'):
        return self.value >= other.value

    def __le__(self, other: 'TreeObject'):
        return self.value <= other.value

    def __ne__(self, other: 'TreeObject'):
        return self.value != other.value
