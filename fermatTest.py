import random

# Iterative Function to calculate (a^n)%p in O(logn)
def power(a, n, p):
	
	# Initialize result
	result = 1
	
	# Update 'a' if 'a' >= p
	a = a % p
	
	while n > 0:
		
		# If n is odd, multiply 'a' with result
		if n % 2:
			result = (result * a) % p
			n = n - 1
		else:
			a = (a ** 2) % p
			
			# n must be even now
			n = n // 2
			
	return result % p
	
# If n is prime, then always returns true.
# If n is composite then return false.
# Higher value of k increases the probability of 
# correct results as the composite inputs become higher.
# For prime inputs, result is always correct.
def isPrime(n, k):
	
	# Edge cases
	if n == 1 or n == 4:
		return False
	elif n == 2 or n == 3:
		return True
	
	# Check k times
	else:
		for i in range(k):
			
			# Pick a random number in range (2, n - 2)	
			# Above edge cases, make sure that n > 4
			a = random.randint(2, n - 2)
			
			# Fermat's Little Theorem
			if power(a, n - 1, n) != 1:
				return False
	
	return True # # [probably prime]
			
# Driver code
k = 3
if isPrime(29, k):
	print("true")
else:
	print("false")

if isPrime(33, k):
	print("true")
else:
	print("false")	