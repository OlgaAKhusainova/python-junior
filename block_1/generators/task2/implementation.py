def read_txt(file_name):
    file_text = open(file_name)
    for line in file_text.readlines():
        if (line.lower()).find("error") >= 0:
            yield line
    file_text.close()


result = read_txt("log.txt")
print(result.__next__())