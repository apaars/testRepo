# -*- coding: utf-8 -*-
"""
Created on Tue Aug 05 09:04:18 2014

@author: tonu
"""
names = {}

f = open('dist.female.first')
for line in f:
    fields = line.split()
    names[fields[0]] = [1.,float(fields[1])]
f.close()

f = open('dist.male.first')
for line in f:
    fields = line.split()
    name = fields[0]
    if name in names:
        names[name][0] = names[name][1]/(names[name][1] + float(fields[1]))
    else:
        names[name] = [0.]
f.close()

checkNames = ["PETER", "LOIS", "STEWIE", "BRIAN", "JASON"]
for name in checkNames:
    if name in names:
        ret = names[name][0]
    else:
        ret = "0.5"
    print "(%s, %s)" % (name, ret)
        