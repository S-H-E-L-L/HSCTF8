adj = [-72, 7, -58, 2, -33, 1, -102, 65, 13, -64, 21, 14, -45, -11, -48, -
       7, -1, 3, 47, -65, 3, -18, -73, 40, -27, -73, -13, 0, 0, -68, 10, 45, 13]

st = "4n_3nd0th3rm1c_rxn_4b50rb5_3n3rgy"
aux = [0]*33
for i in range(len(adj)):
    aux[i] = ord(st[i]) - adj[i]

print(aux)
a = [51, 110, 119, 104, 58, 108]
cb = [124, 103, 153, 49, 143, 99, 150, 51, 91, 115, 93, 95, 94, 110,
      143, 121, 121, 107, 48, 117, 95, 71, 121, 74, 125, 126, 108]
cb2 = []
for i in range(len(cb)):
    cb2.append([cb[:i], cb[i:]])

for i in cb2:
    t = a + i[1] + i[0]
    s = ""
    for j in range(len(t)):
        if (j % 2 == 0):
            s += chr(int(t[j] - 3 * (j / 2)))
        else:
            s += chr(t[j])
    print(s[16:] + s[:16])
