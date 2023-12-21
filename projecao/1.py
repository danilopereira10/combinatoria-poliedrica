//#include <stdio>
#include <iostream>
#include <cmath>
#include <vector>
#include <stack>
#include <tuple>
#include <cstring>
#include <cstdlib>


A = []
b = []
j = 0
while True:
    try:
        A.append([])
        s = input.split("+")
        i = 0
        while (i < len(s)-1):
            q = s[i].split("x"+i+1)
            A[j].append(float(q[0]))
            i+=1
        p = s[len(s)-1].split("x"+(i+1))
        A[j].append(float(p[0]))
        b.append(float(p[1].split("<=")))
        j+=1            
    except EOFError:
        break
c = [1, 2]
N = []
Z = []
P = []
for i in range (len(A)):
    d = 0
    for j in range(len(A[i])):
        d += A[i][j] * c[j]
    if (d == 0):
        Z.append(i)
    elif (d < 0):
        N.append(i)
    else:
        P.append(i)
p = []
for i in range(len(Z)):
    p.append(Z[i])
for i in range(len(N)):
    for j in range(len(P)):
        p.append((N[i],P[j]))

r = len(p)
D = []
j=0
d = []
for i in range (r):
    D.append([])
    if (p[i] in Z):
        for j in range(A[p[i]]):
            D[j].append(A[p[i]][j])
        d[j].append(b[p[i]])
    else:
        s,t = p[i]
        h = 0
        k=0
        for j in range(len(A[0])):
            h+=A[t][j]*c[j]
            k+=A[s][j]*c[j]
        for j in range(len(A[0])):
            D[j].append(h*A[s][j] - k*A[t][j])
        d.append(h*b[s]-k*b[t])
        #D[j].append(A[])
        

    j+=1
print(D)
print(d)




    break
    while (true) {
        string s;
        if (cin.eof()) {
            break;
        } else 
            cin >> s;
        
        for ()
        long long int a, b;
        cin >> a;
        if (cin.eof())
        break;
        cin >> b;
        // YOUR SOLUTION HERE
    }
  return 0;
    string s;
    cin >> s;
    vi a;
    vi b;
    double n;
    for (int i = 0; i < s.size(); i++) {

    }
    while (s != "0") {
        cin >> s;
    }
    for (int i = 0; i < s; i++) {
        string b;
        cin >> b;
        int sum = 0;
        if (b[0] == '0') {
            sum+= 10;
        } else {
            sum += b[0] - '1' + 1;
        }
        for (int j = 1; j < 4; j++) {
            if (b[j] == b[j-1] && b[j] == '0') {
                sum += 1;
            } else if (b[j] == '0') {
                sum += '9'+1 - b[j-1] + 1;
            } else if (b[j-1] == '0') {
                sum += abs(b[j] - ('9' + 1)) + 1;

            } else {
                sum += abs(b[j] - b[j-1]) + 1;
            }
        }
        cout << sum << endl;
    }

}