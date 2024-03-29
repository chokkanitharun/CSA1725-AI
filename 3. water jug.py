from collections import defaultdict
visited = defaultdict(lambda: False) 
J1, J2, L = 0, 0, 0
def Water(X, Y):  
    global J1, J2, L
    if (X == L and Y == 0) or (Y == L and X == 0): 
        print("(",X, ", ",Y,")", sep ="") 
        return True
    if visited[(X, Y)] == False: 
        print("(",X, ", ",Y,")", sep ="") 
        visited[(X, Y)] = True
        return (Water(0, Y) or
                Water(X, 0) or
                Water(J1, Y) or
                Water(X, J2) or
                Water(X + min(Y, (J1-X)), 
                Y - min(Y, (J1-X))) or
                Water(X - min(X, (J2-Y)),
                Y + min(X, (J2-Y)))) 
    else:
        return False
J1 = int(input("Enter jug 1 volume : "))
J2 = int(input("Enter jug 2 volume : "))
L = int(input("Enter volume to measure : "))
print("Path is as Follow:")  
Water(0,0)
