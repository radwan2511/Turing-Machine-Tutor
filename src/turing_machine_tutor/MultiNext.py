class MultiNext:
    def __init__(self, *info):
        self.info = []
        for x in info:
            self.info.append(x)
    def __getitem__(self, index):
        return self.info[index]
    
    def __str__(self):
        res = ""
        for x in self.info:
            res += ",'" + str(x) + "'"
        res = res[1:]
        return f"MultiNext({res})"