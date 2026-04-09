import pulp

# Use the Homebrew-installed CBC
solver = pulp.PULP_CBC_CMD(path="/opt/homebrew/bin/cbc", msg=0)

print("Available solvers:", pulp.listSolvers(onlyAvailable=True))
print("Using CBC from:", solver.path)
