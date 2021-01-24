import math

def calculatePoints(a,b,p):
    
    for x in range(0,p):
        print (">>>>>Calculate the points for X=",x)
        print("y^2 = ",x,"^3 +",(a*x),"+",b,"mod",p)
        ySquare = (pow(x,3) + (a*x) + b) % p
        print("y^2=",ySquare,"mod",p)
        expectedSquareRootValue = math.sqrt(ySquare)
        if( expectedSquareRootValue == math.floor(expectedSquareRootValue)):
            print ("When x = ",x,"The point is (",x,",",expectedSquareRootValue,")")
            
        else:
            currentSQR = squareRoot(ySquare,p)
            if(currentSQR == -1):
                print ("When x = ",x,"There is no point")
            else:
                print ("When x = ",x,"The point is (",x,",",currentSQR,")")





def squareRoot(n,p):
    n = n%p
    print("Calculating the Square Root using x^2 mod p == n")
    for x in range(2,p):
        print (x,"^2 mod", p, " = ", (x*x)%p)
        if ((x*x)%p == n):
            return x

    return -1

    

def modInverse(a, m): 
    a = a % m 
    for x in range(1, m): 
        if ((a * x) % m == 1): 
            return x 
    return 1
    

def addTwoPoints(x1,y1,x2,y2,p):
    print("X1=",x1,",Y1=",y1)
    print("X2=",x2,",Y2=",y2)
    print("λ=(Y2-Y1)(X2-X1)^-1 mod p")
    print("λ=(",y2,"-",y1,")(",x2,"-",x1,")^-1 mod",p)
    lamda = ((y2-y1) * (modInverse((x2-x1),p)))%p
    print("λ=(",(y2-y1),")(",modInverse((x2-x1),p),")mod",p)
    print ("λ=",lamda)
    
    #Calculate X3 
    print("X3=(λ^2 - X1 - X2) mod",p)
    print("X3=(",pow(lamda,2),"-",x1,"-",x2,") mod",p)
    x3 = (pow(lamda,2) - x1 - x2)%p
    print("X3=",x3)
    
    #Calculate Y3
    print("Y3=(λ(X1 - X3) - Y1 )mod ",p)
    print("Y3=(",lamda,"(",x1,"-",x3,")-",y1,") mod",p)
    
    y3 = (lamda*(x1-x3) - y1)%p
    print("Y3=",y3)
    print("(X3,Y3)=(",x3,",",y3,")")
    

def doublePoint(x1,y1,a,p):
    print("2P=P+P")
    print("λ=((3X1^2 + a)(2Y1)^-1) mod",p)
    print("λ=((",3*pow(x1,2),"+",a,")(",(2*y1),")^-1 ) mod",p)
    lamda = (3*pow(x1,2) + a) *(modInverse((2*y1),p))%p
    print("λ=",lamda)
    
    #Calculate X3
    print("X3=(λ^2 - 2X1) mod",p)
    print("X3=(",pow(lamda,2),"-",2*x1,") mod",p)
    x3=(pow(lamda,2) - (2*x1))%p
    print("X3=",x3)
    #Calculate Y3
    print("Y3=(λ(X1-X3) -Y1) mod",p)
    print("Y3=(",lamda,"(",x1,"-",x3,")-",y1,") mod",p)
    y3 = (lamda*(x1-x3) - y1)%p
    print("Y3=",y3)
    print("(X3,Y3)=(",x3,",",y3,")")
 

########################CALL FUNCTIONS
    

#calculatePoints(a,b,p) NOTICE THIS
#calculatePoints(1,1,13)

#addTwoPoints(x1,y1,x2,y2,p) NTICE THIS
#addTwoPoints(4,2,10,6,13)

#doublePoint(x1,y1,a,p) NOTICE THIS
# doublePoint(1,4,1,13)