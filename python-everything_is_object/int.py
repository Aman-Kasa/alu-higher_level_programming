import sys

# Function to count integer objects
def count_int_objects(code):
    # Split code into lines
    lines = code.splitlines()
    
    # Counter for int objects
    int_objects_count = []
    
    # Execute each line and count int objects
    for line in lines:
        exec(line)
        int_objects_count.append(sys.getrefcount(1024) - 1)  # Subtract 1 to exclude current reference
    
    return int_objects_count

# Function to determine if object is deleted
def is_deleted(code):
    exec(code)
    try:
        del a
    except NameError:
        a_deleted = "Yes"
    else:
        a_deleted = "No"

    try:
        del b
    except NameError:
        b_deleted = "Yes"
    else:
        b_deleted = "No"
    
    return a_deleted, b_deleted

# Read int.py content
with open('int.py', 'r') as file:
    script_content = file.read()

# Count int objects created by each line
counts = count_int_objects(script_content)

# Update 104-line1.txt and 104-line2.txt
with open('104-line1.txt', 'w') as file:
    file.write(str(counts[0]))

with open('104-line2.txt', 'w') as file:
    file.write(s
