import time
from gurobipy import Model, GRB
from docplex.mp.model import Model as CplexModel

# Solve with Gurobi
model = Model("knapsack-problem")

# Define the binary decision variables
x1 = model.addVar(vtype=GRB.BINARY, name="x1")
x2 = model.addVar(vtype=GRB.BINARY, name="x2")
x3 = model.addVar(vtype=GRB.BINARY, name="x3")
x4 = model.addVar(vtype=GRB.BINARY, name="x4")
x5 = model.addVar(vtype=GRB.BINARY, name="x5")

# Set objective function (maximize value)
model.setObjective(x1 + 1.8*x2 + 1.6*x3 + 0.8*x4 + 1.4*x5, GRB.MAXIMIZE)

# Add constraint (total weight should not exceed 20)
model.addConstr(6*x1 + 12*x2 + 10*x3 + 4*x4 + 8*x5 <= 20, "Weight Constraint")

# Measure time and optimize the model
start_time = time.time()
model.optimize()
gurobi_time = time.time() - start_time

# Print results for Gurobi
if model.status == GRB.OPTIMAL:
    print("Optimal Solution (Gurobi):")
    for var in model.getVars():
        print(f"{var.varName}: {var.x}")
    print(f"Maximum Value: {model.objVal}")
    print(f"Gurobi Solver Time: {gurobi_time:.6f} seconds")
else:
    print("No optimal solution found.")

# Solve with CPLEX
docplex_model = CplexModel(name="knapsack-problem-cplex")

# Define the binary decision variables
x1_c = docplex_model.binary_var(name="x1")
x2_c = docplex_model.binary_var(name="x2")
x3_c = docplex_model.binary_var(name="x3")
x4_c = docplex_model.binary_var(name="x4")
x5_c = docplex_model.binary_var(name="x5")

# Objective function (maximize value)
docplex_model.maximize(x1_c + 1.8*x2_c + 1.6*x3_c + 0.8*x4_c + 1.4*x5_c)

# Constraint (total weight should not exceed 20)
docplex_model.add_constraint(6*x1_c + 12*x2_c + 10*x3_c + 4*x4_c + 8*x5_c <= 20)

# Measure time and solve the problem using CPLEX
start_time = time.time()
solution = docplex_model.solve(log_output=True)
cplex_time = time.time() - start_time

# Print results for CPLEX
if solution:
    print("Optimal Solution (CPLEX):")
    for var in [x1_c, x2_c, x3_c, x4_c, x5_c]:
        print(f"{var.name}: {var.solution_value}")
    print(f"Maximum Value: {solution.objective_value}")
    print(f"CPLEX Solver Time: {cplex_time:.6f} seconds")
else:
    print("No optimal solution found with CPLEX.")