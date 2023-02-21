"""
create generator class to
produce random numbers

"""
import random
import requests


class ProduceChars:
    """Generate class to produce random numbers in given range"""

    def __init__(self, start, end, limit):
        self.start = start
        self.end = end
        self.limit = limit

    def __iter__(self):
        current = self.start
        while current <= self.limit:
            yield random.randint(self.start, self.end)
            current += 1


class ProduceUrls:
    """Generate class to produce random url from list"""
    def __init__(self, inf):
        self.inf = inf

    def function(self):
        bar = []
        i = 1
        while i <= 3:
            bar.append(random.choice(self.inf))
            i += 1
        data = []
        for url in bar:
            data_ = requests.get(url)
            info = data_.json()
            data.append(info)
        return data
