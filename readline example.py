file_handle=open ("data123/test.txt")
lines=file_handle.readlines()
print(lines)
file_handle.close

file_handle= open("data123/test.txt")
file_data=file_handle.read()
file_lines=file_data.split("\n")
print(file_lines)
file_handle.close

file_handle=open("data123/test.txt")
file_lines=[]
while True:
    line=file_handle.readline()
    if line=="":
        break
    file_lines.append(line.strip())
print(file_lines)
file_handle.close()

