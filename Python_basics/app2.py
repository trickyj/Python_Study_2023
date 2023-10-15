import sys

original_stdout = sys.stdout

# check the value of the oringal sys.stdout

print("Orignal sys.stdout:", original_stdout)

with open("output.txt", "w") as file:
    sys.stdout = file
    print("This is written to output.txt", flush=False)

# reset sys.stdout to its orignal value.
sys.stdout = original_stdout
