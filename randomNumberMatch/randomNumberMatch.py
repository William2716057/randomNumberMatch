import random

def generateNumber():
    return random.sample(range(1, 41), 6)

if __name__ == "__main__":
    GeneratedRandom = generateNumber()
    TargetNumber = ''.join(map(str, GeneratedRandom)) 
    
    print("Target Number: ", TargetNumber)
    
    found = False
    
    while not found:
        generated = generateNumber()
        generatedString = ''.join(map(str, generated))
        
        print("Generated Numbers:", generated)
        
        if generatedString == TargetNumber:
            found = True
            print("Match found: ", generatedString)
