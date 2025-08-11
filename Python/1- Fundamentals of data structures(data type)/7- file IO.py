'''create file in CMD:
    in directory:
copy con myfile.txt
This is my new file
and this is 2nd line
have fun
and live free

^z

copy myfile.txt con         -----> con = console
'''

f = open("myfile.txt")
print(type(f))
print(f.read())     # return text in file[and seeker position is in the end of file]
print(f.read())     # return nothing
#for read again text of file:
f.seek(0)   # too change position of seeker from end of text to first
print(f.read())

new = open("new_file.txt")
line = new.readline()    # hiii, this is new
#line = new.readline(1)  ----->   h
#line = new.readline()   ----->   hiii,
#line = new.readlines()   ----->  read all lines
print(line)
new.close()         # for close file


with open("myfile.txt") as f:   # this closed automatically file
    lines = f.readlines()
    print(lines)
    print(lines[-1])        # print last line


'''
with open("myfile", 'r') as reader:
'r'             reading(default)
'w'             write(overwriting) 
'rb' or 'wb'    read/write binary mode
'r+'            read and write
'a'             add (append)
'''


output = open("new_file.txt", 'a')
output.write("oh, this is new line add")
output.close()
# now check file in CMD with: copy filename.txt con  in that directory