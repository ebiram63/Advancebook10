import sys

text = []
try:
    fileName = input ("Enter a file name: ")
    fh = open(fileName, 'r')
    text = fh.readlines()
    fh.close()

except:
    print('cannot open', fileName)

if text:
    print(text)