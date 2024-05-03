
nrs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quad_zahl = []

for zahl in nrs:
    if zahl%2 == 0:
        quad_zahl.append(zahl)
    else:
        quad_zahl.append(zahl**2)
    
print(quad_zahl)

quad_zahl = [zahl**2 if zahl%2 != 0 else zahl for zahl in range(1,11)]

print(quad_zahl)
    
# =============================================================================
# a = 1
# r = 0.5
# n = 10
# s_n = []
# summe = 0
# 
# for k in range(0, n):
#     summe += a * r**k
#     s_n.append(summe)
#     
# print(s_n)
# 
# import matplotlib.pyplot as plt
# plt.plot(s_n)
# 
# =============================================================================
