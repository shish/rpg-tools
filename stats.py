#!/usr/bin/python

"""
A quick script to print out the odds of rolling a certain number,
a demonstration that if you need a 6 to pass a test, then rolling
a d4 gives you higher odds of succeeding than rolling a d6 (assuming
that your game system makes a 4 on a d4 explode)
"""

die_types = [4, 6, 8, 10, 12]

results = [[0 for n in range(0, 100)] for n in range(0, max(die_types)+1)]

def stat(d, recurses, limit):
    for n in range(1, d+1):
        if n == d:
            if recurses < limit:
                stat(d, recurses+1, limit)
        else:
            #results[recurses*d+n] = 1.0/d * pow(1.0/d, 1+recurses)
            results[d][recurses*d+n] = pow(1.0/d, 1+recurses)

for d in die_types:
    stat(d, 0, 5)


print "chance of rolling n"
for n in range(1, 21):
    print "%2d" % n,
    for d in die_types:
        print "%8.5f" % results[d][n],
    print

print
print "average roll"
print "  ",
for d in die_types:
    print "%8.5f" % sum([
        # sum of (n * chance of rolling n)
        n*results[d][n] for n in range(1, len(results[d]))
    ]),
print

print
print "chance of rolling at least n"
for n in range(1, 21):
    print "%2d" % n,
    chances = []
    for d in die_types:
        # chance of rolling at least n
        chance = 1-sum(results[d][0:n])
        print "%8.5f" % chance,
        chances.append(chance)
    for d in range(0, len(chances)-1):
        if chances[d] > chances[d+1]:
            print die_types[d], ">", die_types[d+1],
    print


#print "  ",
#for d in die_types:
#    print "%8.5f" % sum(results[d]),
#print


#6 = 1/6 * 1    1/4 * 2/4
#7 = 1/6 * 1    1/4 *
#8 = 1/6 * 5/6
