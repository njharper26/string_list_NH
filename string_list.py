words = "It's thanksgiving day. It's my birthday,too!"

x = 'day'
positionDay = words.find(x)
print positionDay

y = 'month'
newWords = words.replace(x, y)
print newWords

x = [2,54,-2,7,12,98]
min = min(x)
max = max(x)
print "min =", min, "max =", max

x = ["hello",2,54,-2,7,12,98,"world"]
first = x[0]
last = x[len(x) -1]
newX = [first, last]
print 'first =', first,';  last =', last,';  new list =', newX

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x = sorted(x)
length = (len(x) -1) / 2
x1 = [x[0:length]]
x2 = x[length:]
x3 = x1 + x2
print x3
