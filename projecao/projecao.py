
A = []
b = []

j = 0
s = ""
caso = input()
#caso 1
#caso 2
if (caso != "caso1" and caso != "caso2"):
    print("Escreva uma opção entre caso1 e caso2")
    exit(1)

if (caso == "caso1"):
    c=[]
    d = input().split()
    for i in range (len(d)):
        c.append(float(d[i]))
else:
    pass
    #não precisa ler vetor de direção se não for o caso1.
#Processando entrada:
while s != "fim":
    try:
        s = input().split("+")
        if (s[0] == "fim"):
            raise 
        A.append([])
        i = 0
        while (i < len(s)-1):
            q = s[i].split("x"+str(i+1))
            A[j].append(float(q[0]))
            i+=1
        p = s[len(s)-1].split("x"+str((i+1)))
        A[j].append(float(p[0]))
        q = p[1].split("<=")
        b.append(float(q[1]))
        j+=1
    except:
        if (s[0] != "fim"):
            exit(1)
        break           

#Entrada processada
m=0 #Variável utilizada para resolver o problema de detectar se um poliedro é vazio ou não
rodou=0 #Variável utilizada para saber se a projeção já foi feita (é usada para o Problema 1)
while ((caso == "caso1" and not rodou) or (caso == "caso2" and len(A) != 0 and m < len(A[0]))):
    
    N = []
    Z = []
    P = []
    for i in range (len(A)):
        d = 0
        if (caso == "caso1"):
            for j in range(len(c)):
                d+= A[i][j]*c[j]
        else:
            d = A[i][m]
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
            for j in range(len(A[p[i]])):
                D[i].append(A[p[i]][j])
            d.append(b[p[i]])
        else:
            s,t = p[i]
            h = 0
            k=0
            if (caso == "caso1"):
                for j in range (len(c)):
                    h+=A[t][j]*c[j]
                    k+=A[s][j]*c[j]
            else:
                h=A[t][m]
                k=A[s][m]
            for j in range(len(A[0])):
                D[i].append(h*A[s][j] - k*A[t][j])
            d.append(h*b[s]-k*b[t])
            #D[j].append(A[])
    A=[]
    for i in range(len(D)):
        A.append([])
        for j in range (len(D[0])):
            A[i].append(D[i][j])
    #print(D)
    #print(d)
    m+=1
    rodou = 1

#Projeções Realizadas. Hora de mostrar os resultados.
if (caso == "caso1"):
    print("Poliedro P(D,d):")
    print("D=")
    print(D)
    print()
    print("d=")
    print(d)
else:
    f = 0
    for i in range(len(d)):
        if (d[i] < 0):
            f = 1
            break
    if (f):
        print("P(A,b) é vazio")
    else:
        print("P(A,b) não é vazio")



