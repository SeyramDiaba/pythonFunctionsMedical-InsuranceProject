# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(name,age,sex,bmi,num_of_children,smoker):
  estimated_cost=250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  output="The estimated insurance cost for "+name+" is "+str(estimated_cost)+" dollars."
  print(output)
  return output,estimated_cost

def different_cost(omar_insurance_cost,stephen_insurance_cost):
  diff=omar_insurance_cost-stephen_insurance_cost
  printer="The difference in insurance cost is "+str(diff)+" dollars."
  print(printer)
  return printer

# Initial variables for Maria 

# Estimate Maria's insurance cost
maria_insurance_cost=calculate_insurance_cost("Maria",28,0,26.2,3,0)
# Initial variables for Omar

# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost("Omar",35,1,22.2,0,1)

#Estimate Stephen's insurance cost
stephen_insurance_cost=calculate_insurance_cost("Stephen",25,1,26,0,1)

total_diff=different_cost(28336.0,27242.0)

