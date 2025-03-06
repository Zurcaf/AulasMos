import time
from gurobipy import Model, GRB

# Solve with Gurobi
model1 = Model("simplex-problem")

# Define the binary decision variables
x1 = model1.addVar(vtype=GRB.INTEGER, name="x1")
x2 = model1.addVar(vtype=GRB.INTEGER, name="x2")

# Set objective function (maximize value)
model1.setObjective(2*x1 + x2, GRB.MAXIMIZE)

# Add constraint (total weight should not exceed 20)
model1.addConstr(3*x1 - 5*x2 <= 0, "1 Constraint")
model1.addConstr(3*x1 + 5*x2 <= 15, "2 Constraint")

model1.addConstr(x1 >= 0, "3 Constraint")
model1.addConstr(x2 >= 0, "4 Constraint")

# Measure time and optimize the model
start_time = time.time()
model1.optimize()
gurobi_time = time.time() - start_time

# Print results for Gurobi
if model1.status == GRB.OPTIMAL:
    print("Optimal Solution (Gurobi):")
    for var in model1.getVars():
        print(f"{var.varName}: {var.x}")
    print(f"Maximum Value: {model1.objVal}")
    print(f"Gurobi Solver Time: {gurobi_time:.6f} seconds")
else:
    print("No optimal solution found.")





# Solve with Gurobi
model2 = Model("simplex-problem")

# Define the binary decision variables
x1 = model2.addVar(vtype=GRB.CONTINUOUS, name="x1")
x2 = model2.addVar(vtype=GRB.CONTINUOUS, name="x2")

# Set objective function (maximize value)
model2.setObjective(2*x1 + x2, GRB.MAXIMIZE)

# Add constraint (total weight should not exceed 20)
model2.addConstr(3*x1 - 5*x2 <= 0, "1 Constraint")
model2.addConstr(3*x1 + 5*x2 <= 15, "2 Constraint")

model2.addConstr(x1 >= 0, "3 Constraint")
model2.addConstr(x2 >= 0, "4 Constraint")

# Measure time and optimize the model
start_time = time.time()
model2.optimize()
gurobi_time = time.time() - start_time

# Print results for Gurobi
if model2.status == GRB.OPTIMAL:
    print("Optimal Solution (Gurobi):")
    for var in model2.getVars():
        print(f"{var.varName}: {var.x}")
    print(f"Maximum Value: {model2.objVal}")
    print(f"Gurobi Solver Time: {gurobi_time:.6f} seconds")
else:
    print("No optimal solution found.")