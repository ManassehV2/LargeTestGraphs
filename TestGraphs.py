
def generateXi(x0,m,a,c):
    Xi = []
    Xi.append(x0)
    nextnum = (a*x0+c) % m
    i = 1
    while nextnum not in Xi:
        Xi.append(nextnum)
        nextnum = (a*Xi[i]+c) % m
        i += 1
    return Xi

def generateYi(Xi,n):
    Yi = []
    i = 0
    while i < len(Xi):
        Yi.append(Xi[i] % n)
        i += 1
        
    return Yi    
    
def gcd(a,b):
    if b > a:
        if b % a == 0:
            return a
        else:
            return gcd(b % a,a)
    else:
        if a % b == 0:
            return b
        else:
            return gcd(b,a % b)

def generateEdges(Yi,vb,n,m):
    #Chromatic number of the graph
    k = gcd(n,m)
    i = 0
    
    openfile = open("g1.txt","w")
    while i < len(vb):
        tempYi = Yi[:]
        if vb[i] >= 1:
            j = vb[i]
            while j >= 1:
                openfile.write(str(tempYi[0:k-i]))
                openfile.write("\n")
                del tempYi[:k-i]
                j -= 1
        i += 1
    openfile.close()
        
        
    
    
    
def main():
    n = int(raw_input("Enter Number of nodes: "))
    a = int(raw_input("Enter the value of the multiplier: "))
    c= int(raw_input("Enter the value of the increment: "))
    m = int(raw_input("Enter the value of the modulo: "))
    x0 = int(raw_input("Enter the initial value of the sequence Xi: "))
    rawb  = raw_input("Enter the (k-1) vector b: ")
    b = map(int,rawb.split(","))
    
    
    
    xi = generateXi(x0, m, a, c)
    yi = generateYi(xi,n)
    #print(xi)
    #print(yi)
    #print(len(xi))
    #print("\n")
    #print(len(yi))

    generateEdges(yi, b, n, m)
    
    
main()
    