import cplex

# Create a CPLEX problem object
problem = cplex.Cplex()

# Set the problem type (Maximize)
problem.set_problem_type(cplex.Cplex.problem_type.LP)

# Set the objective sense (maximize)
problem.objective.set_sense(problem.objective.sense.maximize)

# Define the variables
variables = ['x1', 'x2']
objective_coeffs = [1, 1]
lower_bounds = [0, 0]  # x1, x2 >= 0
upper_bounds = [cplex.infinity, cplex.infinity]  # No upper bounds

# Add variables to the problem
problem.variables.add(names=variables, 
                       types=['C', 'C'],  # Continuous variables
                       obj=objective_coeffs, 
                       lb=lower_bounds, 
                       ub=upper_bounds)

# Define a simple constraint
# Constraints are added as pairs of (index, coefficient)
constraint_names = ['c1']
constraint_coeffs = [[[0, 1], [1, 1]]]  # [index, coefficient] format
constraint_rhs = [10]
constraint_senses = ['L']  # L means less than or equal to

# Add the constraint to the problem
problem.linear_constraints.add(names=constraint_names, 
                               lin_expr=constraint_coeffs, 
                               senses=constraint_senses, 
                               rhs=constraint_rhs)

# Solve the problem
problem.solve()

# If integration is successful, this should output the result
print("Solution Status: ", problem.solution.status[problem.solution.get_status()])
print("Objective Value: ", problem.solution.get_objective_value())
print("Variable Values: ", problem.solution.get_values())
