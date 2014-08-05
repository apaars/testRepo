# -*- coding: utf-8 -*-
"""
Created on Mon Aug 04 14:58:05 2014

@author: tonu
"""

#dictionaries -- mutable except keys cant be mutable
paras = {}
paras['niter'] = 500
paras['tol'] = 1.e-06
print paras
print paras['niter']
paras.pop('niter')
print paras
del paras['tol']
print paras


paras = {}
paras['niter'] = 500
paras['tol'] = 1.e-06
for key in paras:
    print "a[%s] = %s" % (key,paras[key])


#tuples -- immutable
lis = (19, 73, -42)
for n in range(len(lis)):
    print "lis[%s] = %s" % (n,lis[n])

#sets -- mutable, no order for elements
myset = set()
myset.add("math")
myset.add("chem")

yourset = set()
yourset.add("physics")
yourset.add("math")

print myset & yourset
print myset | yourset

myset.remove("math")
print myset & yourset
#in set you cant have duplicate elems, unlike for lists, and we can also take 
#intersection and unionsfs









