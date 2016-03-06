
# link on image which demonstrates this program
# https://lh5.googleusercontent.com/-ce_9fhWBLpE/VH788Al7DYI/AAAAAAAALE8/aolL8UljHi4/w649-h377-no/2014-12-03_133141.jpg
#python
import sys, string
#TsotneP

def FindStart (numb,theline): #returns the startpoint of number
    for i in range(numb, -1, -1):
        if(theline[int(i)]=='+' or theline[int(i)]=='-'):
            return i+1
    return 0


def FindQ (theline): #collects every coefficients in A or B or C
    A=B=C=0
    for i in range(0,len(theline)-1,1):
        if(theline[i] == 'x'):
            if (theline[i+1] == '2'):
                st = FindStart(i,theline)
                if (theline[st-1] == '-'):
                    A = (A - float(theline[st:i]))
                else:
                    A = (A + float(theline[st:i]))
            else:
                st = FindStart(i,theline)
                if (theline[st-1] == '-'):
                    B = (B - float(theline[st:i]))
                else:
                    B = (B + float(theline[st:i]))
        else:
            if(((theline[i] == '+') or (theline[i] == '-') or (theline[i] == '=')) and theline[i-1] != 'x' and theline[i-2]!='x'):
                st = FindStart(i-1,theline)
                if (theline[st-1] == '-'):
                    C = C - float(theline[st:i])
                else:
                    C = C + float(theline[st:i])
            else:
                pass
    print("sum of x2   Coeffs : "+str(A))
    print("sum of x    Coeffs : "+str(B))
    print("sum of free Coeffs : "+str(C))
    return (A,B,C)


def Solve(arr = []): #takes three coefficients and calculates solutions 
    a=arr[0]
    b=arr[1]
    c=arr[2]
    
    D = float(b**2 - 4*a*c)
    if (D >=0):
        X1 = float(((-b + D**0.5)/(2*a)))
        X2 = float(((-b - D**0.5)/(2*a)))
        return (X1,X2)
    else:
        print ("getout its complex")
        
    print (a,b,c)
    return "AND I CANT CALCULATE COMPLEX NUMBERS"

def Arrange (theline): #puts right side of equation to left side
    stayed = theline
    moved = moved4 = ""
    end = ""
    for i in range(0,len(theline)-1,1):
        if(theline[i]== '=' and theline[i+1] != '0'):
            moved=theline[i+1:len(theline)]
            stayed=theline[0:i]
            end = "=0"
            break
        else:
            pass
    #print(moved)
    
    if(len(moved)>0):
        if(moved[0]!='+' and moved[0]!='-'):
            moved = '+'+moved
            end = "=0"
        else:
            pass
        moved2=moved.replace('+', '#')
        moved3=moved2.replace('-', '+')
        moved4=moved3.replace('#', '-')
        '''
        print(moved)
        print(moved4)
        print(stayed)
        '''
    else:
        pass
    print("ORDERED FUNCTION LOOKS LIKE THIS: "+ stayed+moved4+end)
    return Solve(FindQ((stayed+moved4+end)))
    
# MAIN FUNCTION STARTS here
#line = sys.argv[1] #delete first '#' from this line and put same symbol in next line, to use CMD as input
line = input()
theline=line.replace(' ',"")
print (Arrange(theline))

input()
