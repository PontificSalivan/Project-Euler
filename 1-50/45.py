n_t=286
n_p=166
n_h=144
t = n_t*(n_t+1)/2
p = n_p*(3*n_p-1)/2
h = n_h*(2*n_h-1)*1.0
while t != p or t != h:
    if t < p or t < h:
        n_t += 1
        t = n_t*(n_t+1)/2
        continue
    if p < t or p < h:
        n_p += 1
        p = n_p*(3*n_p-1)/2
        continue
    if h < t or h < p:
        n_h += 1
        h = n_h*(2*n_h-1)*1.0
        continue
    
print(int(n_t*(n_t+1)/2))





