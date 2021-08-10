# 2. Find index in string by for loop character (start index with 1)
# !Don't use .indexOf() function

# ex: findChar("I am engineer", "g")

# result: 8

#Assume that find and print the first character from left to right, like .indexOf()
def findChar(string,c):
    for i in range(0,len(string)):
        if string[i] == c:
            print('result:',i+1)
            return 0
    print('Not found')

findChar("I am engineer", "eng")