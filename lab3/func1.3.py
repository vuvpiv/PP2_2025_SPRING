numheads=int(input())
numlegs=int(input())
def solve(numheads,numlegs):
    y=(numlegs-2*numheads)/2
    x=numheads-y
    return int(x), int(y)
chickens, rabbits=solve(numheads, numlegs)
print(f"куры:{chickens}, кролики:{rabbits}")