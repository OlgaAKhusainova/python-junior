class FileClass():
    def __init__(self, filepath):
        self.filepath = filepath
        print('Init')

    def __enter__(self):
        self.file = open(self.filepath)
        print(len(self.file.readlines()))
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Close')
        self.file.close()


with FileClass('log.txt') as file:
    file.close()