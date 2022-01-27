class TagCloud:
    def __init__(self) -> None:
        self.__tags = {} # add two _ to set attribute or function to private

    def add(self, tag) -> None:
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)

cloud = TagCloud()
cloud.add("python")
cloud.add("Python")
cloud["python"] = 10
print(cloud.__dict__)        
