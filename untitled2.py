

"""arr1 = np.array([2,4,5,6])
arr2 = np.array([5,6,8,9])
res = []
for i in range(4):
    res.append(arr1[i]*arr2[i])       
print(res)
"""
arr12 = [[2,4,5],
         [1,2,3],
         [5,6,7]]
arr22 = [[5,6,8],
         [1,3,4],
         [5,3,9]]
res2 = [[0,0,0],
        [0,0,0],
        [0,0,0]]

r1 = 3
c1 = 3
r2 = 3
c2 = 3
for i in range (r1):
    for j in range (c2):
        for k in range(r2):
            res2[i][j]+= (arr12[i][k]*arr22[k][j])
        
print(res2,end='')