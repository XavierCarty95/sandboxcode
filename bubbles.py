# Get the highest scores in the table
# Get the length of the table
# Solutions to get the most cost effective price from the array table
scores = [ 60 , 50 , 60 , 58 , 54 ,54 , 50 , 52, 54 ,48,
            69,34,55,51,52,44,51,69,64,66,55,52,61,46,31,
            57,52,44,18,41,53,55,61,51,44]
            
costs = [.25,.27,.25,.25,.25,.25,.33,.31,.25,.29,.27,.22,
.31,.25,.25,.33,.21,.25,.25,.28,.25,.24,.22,.20,.25,.30,.25,
.25,.25,.27,.25,.26,.29]

high_scores = 0
length = len(scores)



for i in range(length):
    if scores[i] > high_scores:
        high_scores = scores[i]
print("Test eqaul", length)
print("Highest" , high_scores)

best_solutions = []
for i in range(length):
    if high_scores == scores[i]:
        best_solutions.append(i)
    
print("Best solutions" , best_solutions)

cost = 100.0 
most_effective = 0

for i in range(length):
    if scores[i] == high_scores and costs[i] < cost:
        most_effective = i 
        cost = costs[i]
print("Solutions", most_effective, 'is the most effectibe with a cost of', costs[most_effective])