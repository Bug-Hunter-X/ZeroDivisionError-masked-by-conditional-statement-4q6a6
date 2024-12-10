def function_with_uncommon_error(x):
    if x == 0:
        return float('inf') # Or raise a more descriptive exception
    else:
        return x + 5

result = function_with_uncommon_error(0) 
print(result) # Output: inf