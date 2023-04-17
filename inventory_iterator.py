from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.index = -1
        self.data = data

    def __next__(self):
        self.index += 1
        if self.index >= len(self.data):
            raise StopIteration
        return self.data[self.index]

