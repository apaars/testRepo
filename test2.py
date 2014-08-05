# -*- coding: utf-8 -*-
"""
Created on Mon Aug 04 15:27:20 2014

@author: tonu
"""

female  = set()
f = open('dist.female.first')
for line in f:
    female.add(line.split()[0])
f.close()

male  = set()
f = open('dist.male.first')
for line in f:
    male.add(line.split()[0])
f.close()

count = (len(female), len(male))
print "Females: %s, Males: %s" % count
print "names in both sets are %s" % len(male & female)

names = ["PETER", "LOIS", "STEWIE", "BRIAN"]
for name in names:
    if name in male:
        ret = "M"
    elif name in female:
        ret = "M"
    else:
        ret = "NA"
    print "(%s, %s)" % (name, ret)

#this biases towards males and also the case of the input 
#use probability
names = {}
f = open('dist.female.first')
for line in f:
    names[line.split()[0]] = 1.
f.close()

f = open('dist.male.first')
for line in f:
    name = line.split()[0]
    if name in names:
        names[name] = 0.5
    else:
        names[name] = 1.
f.close()

checkNames = ["PETER", "LOIS", "STEWIE", "BRIAN"]
for name in checkNames:
    if name in names:
        ret = names[name]
    else:
        ret = "0.5"
    print "(%s, %s)" % (name, ret)


#a stack is a list in python



