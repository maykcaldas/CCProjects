from random import randint
import math 

length=21
min=0
max=10
count=5000
target=0
aleat=50
itermax=200
err=0.01
cut=0.1
nmut=10

def individual(length, min, max):
    ind=[]
    for k in range(length):
        ind.append(randint(min, max))
    return ind


def population(count, length, min, max):
    pop=[]
    for k in range(count):
        pop.append(individual(length, min, max))
    return pop


def fitness(ind,target):
    emt=0
    try:
        if length%3 == 0:
            atoms=length/3
        else:
            raise Exception
        for i in range(0, length-3, 3):
            n=i+3
            while n<length:
                r=math.sqrt( (ind[i]-ind[n])**2+(ind[i+1]-ind[n+1])**2+(ind[i+2]-ind[n+2])**2 )
                if r < err:
                    r+=5
                else:
                    emt+=(1/r**12)-(1/r**6)
                n+=3

    except ZeroDivisionError:
        print("alauoooooo")
#    except Exception:
#        print("ulauoooooo")


    return(emt-target)

#def fitness(ind, target):
#    sum=0
#    for i in ind:
#        sum+=i
#    return (sum-target)


def bestOne(pop, target):
    fit=[]
    for i in pop:
        fit.append(abs(fitness(i,target)))

    best=sorted(fit)[0]
    
    for i in pop:
        if abs(fitness(i,target)) == best:
            return i
            break


def selcut(pop, aleat, count, cut):
    dad=[]
    dad_fit=[]
    dadchamp=[]
    mom=[]
    mom_fit=[]
    momchamp=[]
    child=[]
    
    for i in range(aleat):
        dadrand=randint(0,(len(pop)-1))
        dad.append(pop[dadrand])
        dad_fit.append(abs(fitness(pop[dadrand], target)))
        
        momrand=randint(0,(len(pop)-1))
        mom.append(pop[momrand])
        mom_fit.append(abs(fitness(pop[momrand], target)))
    
    dadbest=sorted(dad_fit)[0]
    mombest=sorted(mom_fit)[0]
    
    for i in dad:
        if abs(fitness(i,target))==dadbest:
            dadchamp=i

    for i in mom:
        if abs(fitness(i,target))==mombest:
            momchamp=i
    champ=dadchamp+momchamp
    for i in range(length):
        child.append(champ[randint(0,len(champ)-1)])
        #print(child)
    
    return(child)
    
            
def selroullete(pop, aleat):
    champ=[]
    champ_fit=[]
    rol=0
    guess=0
    
    for i in range (aleat):
        rand=randint(0,(len(pop)-1))
        champ.append(pop[rand])
        champ_fit.append(abs(fitness(pop[rand], target)))
        rol+=abs(fitness(pop[rand], target))

    shoot=randint(0, int(rol))
    for i in champ:
        guess+=abs(fitness(i, target))
        if guess>=shoot:
            return i
            break
            
            
def mutation(pop, length, min, max, nmut):
    for i in range(nmut):
        mut=randint(0,len(pop)-1)
        pop[mut][randint(0,length-1)]=randint(min,max)


##########################################################################

def main():
    ind=individual(length, min, max)
    pop=population(count, length, min, max)
    
    n=0
    while n<itermax:
        n+=1
        newpop=[]
        #print(pop)
        
        if n%10 ==0:
            for i in range((len(pop)/10)):
                pop[randint(0, len(pop)-1)] = individual(length, min, max)

        if n%50 == 0:
            mutation(pop, length, min, max, nmut)
        
        for i in range(count/2):
            newpop.append(selcut(pop, aleat, count, cut))
            newpop.append(selroullete(pop, aleat))
        pop=newpop
        
        theguy = bestOne(pop,target)
        print(n, fitness(theguy,target))
        print(theguy)
        if abs(fitness(theguy, target)) <= (err*target):
            break
                
    print(theguy)
    print(fitness(theguy,target))


#########################################################################

main()


