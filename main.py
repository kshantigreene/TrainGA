import random

allowedLetters="123DBE"


def generateInitialPopulation():
    currentPopulation=[]
    w=[1,1,1,1,1,1] #weights for each code.
    for i in range(populationSize):
        train= ''.join(random.choices(allowedLetters,weights=w, k=trainSize))
        #print(train)
        currentPopulation.append(train)
    return currentPopulation

def printTrain(train):
    names={'1':'First','2':'Second','3':'Third','E':'Engine','D':'Dining','B':'Bathroom'}
    #join the name for each character, separated by a -
    string='-'.join(names[c] for c in train)
    print(string)

###############Functions you will write ###########

# 1. compute fitness of solution. 
def computeFitness(train):
    pass

# 2. selection: Select two individuals from current generation
def select():
    pass

# 3. crossover (takes two individuals and returns one or more 
# individuals created from crossover). You may choose your crossover
# approach
def crossover(train1, train2):
    pass

# 4. mutation (takes one individual and returns a possible mutation)
def mutate(train):
    pass

# 5. create new generation: this function will call the previous
# functions. It should repeatedly select
# a number of pairs and do crossover and mutation on those pairs.
# and it should create a new generation which will be an
# an array of new train strings
def newGeneration(currentPopulation):
    pass


###########################
# parameters that can be adjusted 
trainSize=20
populationSize=1000 #number of trains in population
numGenerations=1 #number of generations to run
firstPassengers=10 #number of passengers a first class car carries
secondPassengers=24 #number of passengers a second class car carries
thirdPassengers=50 #number of passengers a third class car carries

# for now make these a multiple of the number of passengers a car will hold 
numFirst=firstPassengers*10
numSecond=secondPassengers*12
numThird=thirdPassengers*20

currentPopulation=generateInitialPopulation()
printTrain(currentPopulation[0])
for i in range(numGenerations):
    currentPopulation=newGeneration(currentPopulation)
