def find_element(arr, divisor):
    xor_value = 0

    for num in arr: # For loop
        if num % divisor == 0: # To check is remainder is zero
            xor_value ^= num # XORing operation with num to get result
    
    return xor_value

# Example array
array = [20, 25, 30, 35, 40, 50] # input array
divisor = 10 # Set divisor value
result = find_element(array, divisor) # Store the final value in the result variable
print("XOR of divisible elements:", result) # Print out result