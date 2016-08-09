fi = open('p067_triangle.txt', 'r')
Tri=[]
for line in fi:
    Tri.append( map( int, line.split() ) )

print Tri


def best_path():
    for a in xrange(len(Tri) - 2, -1, -1):
        for b in xrange(0, a + 1):
            Tri[a][b] += max(int(Tri[a + 1][b]), int(Tri[a + 1][b + 1]))
    print Tri[0][0]

best_path()
print 99**98
print 98**99
print 99**99