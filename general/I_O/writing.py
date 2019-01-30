def write_file(file_name, content):
    import os
    if os.path.isdir('madetxt'):
        file = open('./madetxt/'+file_name+'.txt', 'w')
        file.write(content)
        file.close()
    else:
        os.mkdir('madetxt')
        file = open('./madetxt/'+file_name+'.txt', 'w')
        file.write(content)
        file.close()

def main():
    file_name = input("Enter name: ")
    contents = input("Enter lines: ")
    write_file(file_name, contents)
    print("File Written")

main()
