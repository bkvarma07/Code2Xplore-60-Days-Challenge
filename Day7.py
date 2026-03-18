#Smart Campus Energy Analyzer

n=int(input("Enter Number of buildings: "))
energies=[0]*n
for i in range(n):
    energies[i]=int(input("Enter energy reading: "))

dictionary={
    "efficient": [],
    "moderate": [],
    "high": [],
    "invalid": []
}

for i in energies:
    if i<0:
        dictionary["invalid"].append(i)
    elif i<=50:
        dictionary["efficient"].append(i)
    elif i<=150:
        dictionary["moderate"].append(i)
    else:
        dictionary["high"].append(i)

valid = [i for i in energies if i >= 0]
total_consumption = sum(valid)

num_energies=len(energies)
summary_tuple=(total_consumption,num_energies)

if len(dictionary["high"])>3:
    ans="Overconsumption"
elif abs(len(dictionary["efficient"])-len(dictionary["moderate"]))<=1:
    ans="Balanced Usage"
elif total_consumption>600:
    ans="Energy Waste"
else:
    ans="good campus"

print("categorized reading: ",dictionary)
print("total consumption: ",summary_tuple[0])
print("Number of Buildings: ",summary_tuple[1])
print("efficiency results: ",ans)
