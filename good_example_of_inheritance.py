class InvalidOperationError(Exception):
    pass

class Stream:
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
    fs.close()     

    ns = NetworkStream()   
    ns.open()
    ns.read()
    ns.close()     
except InvalidOperationError as error:
    print(error)

