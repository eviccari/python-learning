from abc import ABC, abstractmethod # abc -> module of abstract base class

class InvalidOperationError(Exception):
    pass

class Stream(ABC): # inheritance of ABC, this class cannot be instantiate anymore 
    def __init__(self) -> None:
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream already open.")
        self.opened = True
        print("Stream opened.")

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream already closed.")
        self.opened = False
        print("Stream closed.")

    @abstractmethod # notify subclasses that method must be implemented
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")        

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")
    

try:
    fs = FileStream()
    fs.open()
    fs.read()

    ns = NetworkStream()   
    ns.open()
    ns.read()
except InvalidOperationError as error:
    print(error)
finally:
    fs.close()
    ns.close()

