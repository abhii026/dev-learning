s1={1,2,3,4,5}
s2={4,5,6,7,8}

union_set=s1.union(s2)
a=s1|s2
print("Union or s1|s2: ",a)
print("Union or s1|s2: ",union_set)

diff_set=s1.difference(s2)
d=s1-s2
print("Difference or s1-s2: ",d)
print("Difference: ",diff_set)

intersection_set=s1.intersection(s2)
a1=s1&s2
print("Intersection or s1&s2: ",a1)
print("Intersection: ",intersection_set)

symmetric_diff=s1.symmetric_difference(s2)
sd=s1^s2
print("Symmetric or s1^s2: ",sd)
print("Symmetric or s1^s2: ",symmetric_diff)

# OUTPUT:
# Union or s1|s2:  {1, 2, 3, 4, 5, 6, 7, 8}     
# Difference or s1-s2:  {1, 2, 3}
# Intersection or s1&s2:  {4, 5}      
# Symmetric or s1^s2:  {1, 2, 3, 6, 7, 8} 