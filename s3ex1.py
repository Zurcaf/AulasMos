import time
from gurobipy import Model, GRB
from docplex.mp.model import Model as CplexModel

# # Solve with Gurobi
# model = Model("simplex-problem")

# # Define the binary decision variables
# y1 = model.addVar(vtype=GRB.INTEGER, name="y1")
# y2 = model.addVar(vtype=GRB.INTEGER, name="y2")
# y3 = model.addVar(vtype=GRB.INTEGER, name="y3")
# y4 = model.addVar(vtype=GRB.INTEGER, name="y4")
# y5 = model.addVar(vtype=GRB.INTEGER, name="y5")
# y6 = model.addVar(vtype=GRB.INTEGER, name="y6")

# # Set objective function (maximize value)
# model.setObjective(18*y1 + 15*y2 + 8*y3 + 6*y4, GRB.MINIMIZE)

# # Add constraint (total weight should not exceed 20)
# model.addConstr(2*y1 + y2 + y3 - y5 == 3, "1 Constraint")
# model.addConstr(y1 + 2*y2 + y4 - y6 == 4, "2 Constraint")

# model.addConstr(y1 >= 0, "3 Constraint")
# model.addConstr(y2 >= 0, "4 Constraint")
# model.addConstr(y3 >= 0, "5 Constraint")
# model.addConstr(y4 >= 0, "6 Constraint")
# model.addConstr(y5 >= 0, "7 Constraint")
# model.addConstr(y6 >= 0, "8 Constraint")

# # Measure time and optimize the model
# start_time = time.time()
# model.optimize()
# gurobi_time = time.time() - start_time

# # Print results for Gurobi
# if model.status == GRB.OPTIMAL:
#     print("Optimal Solution (Gurobi):")
#     for var in model.getVars():
#         print(f"{var.varName}: {var.x}")
#     print(f"Maximum Value: {model.objVal}")
#     print(f"Gurobi Solver Time: {gurobi_time:.6f} seconds")
# else:
#     print("No optimal solution found.")

# Solve with CPLEX
docplex_model = CplexModel(name="knapsack-problem-cplex")

# Define the binary decision variables
y1_c = docplex_model.continuous_var(name="y1")
y2_c = docplex_model.continuous_var(name="y2")
y3_c = docplex_model.continuous_var(name="y3")
y4_c = docplex_model.continuous_var(name="y4")
y5_c = docplex_model.continuous_var(name="y5")
y6_c = docplex_model.continuous_var(name="y6")

# Objective function (maximize value)
docplex_model.minimize (18*y1_c + 15*y2_c + 8*y3_c + 6*y4_c)

# Constraint (total weight should not exceed 20)
docplex_model.add_constraint(2*y1_c + y2_c + y3_c - y5_c == 3)
docplex_model.add_constraint(y1_c + 2*y2_c + y4_c - y6_c == 4)


# Measure time and solve the problem using CPLEX
start_time = time.time()
solution = docplex_model.solve(log_output=True)
cplex_time = time.time() - start_time

# Print results for CPLEX
if solution:
    print("Optimal Solution (CPLEX):")
    for var in [y1_c, y2_c, y3_c, y4_c, y5_c, y6_c]:
        print(f"{var.name}: {var.solution_value}")
    print(f"Maximum Value: {solution.objective_value}")
    print(f"CPLEX Solver Time: {cplex_time:.6f} seconds")
else:
    print("No optimal solution found with CPLEX.")