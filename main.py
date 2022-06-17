fileName = input("What is your filename? ")

f = open(fileName,'x')

f = open(fileName,'w')
f.write('hello world')
f.close()

f = open(fileName,'r')
message = f.read()
print(message)
f.close()

f = open(fileName,'w')
f.write('\n' + 'hello world')
f.close()

f = open(fileName,'r')
message = f.read()
print(message)
f.close()