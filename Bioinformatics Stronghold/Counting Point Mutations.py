s = input("Enter the first sequence: ")
t = input("Enter the second sequence: ")

def hammingDistance(s, t):
    mutation = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            mutation += 1
            
    return mutation

print(hammingDistance(s, t))
