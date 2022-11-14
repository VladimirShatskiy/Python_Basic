class MyDict(dict):
    def get(self, key, default=0):
        return super().get(key, default)


test_dict = MyDict({'вася': 34, 'петя': 3, 'вова': 356, 'гуся': 134})

print(test_dict.get('фвася'))
