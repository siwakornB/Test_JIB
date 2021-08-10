# 1. Implement function input integer and print as result
# ex: printTriAngle(5)

# result:
# 0
# 11
# 222
# 3333
# 44444

#nested loop
def printTriAngle(iter):
    print('result:')
    for i in range(0,iter):
        result = ''
        for j in range(0,i+1):
            result += str(i)
        print(result)
        
#nested loop
printTriAngle(5)
