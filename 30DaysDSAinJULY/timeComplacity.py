import math

"""
👉 PROBLEM STATEMENT / QUESTION:
"Aapko ek number 'N' diya gaya hai. Is 'N' ko process karne ke liye 
BEST se lekar WORST efficiency tak ke saare Time Complexity cases ko 
Python code ke sath samjhaiye, taaki growth rate ka farq saaf dikhe."
"""


# 1. 🟢 O(1) - Constant Time [SABSE BEST]
def constant_time_sol(n):
    # Input 'n' chahe 10 ho ya 10 Crore, ye hamesha CONSTANT (ek hi) step lega.
    # Isme koi loop nahi hota, direct formula se kaam hota hai.
    result = n * (n + 1) // 2
    return result  # Ek jhatke me khatam!


# 2. 🟢 O(log log n) - Log-Log Time [SUPER FAST]
def log_log_time_sol(n):
    # Isme loop variable har step me Square Root (√) hota jata hai.
    # Agar N = 16 hai -> toh √16 = 4 -> √4 = 2 (Sirf 2 steps me loop khatam!).
    count = 0
    i = n
    while i > 1.1:
        i = math.sqrt(i)
        count += 1
    return count


# 3. 🟡 O(log n) - Logarithmic Time [EXCELLENT]
def logarithmic_time_sol(n):
    # Isme input har step me Seedha AADHA (Divide by 2) ho jata hai.
    # Jaise Binary Search! Agar N = 16 hai -> 16 -> 8 -> 4 -> 2 -> 1 (Sirf 4 steps).
    count = 0
    while n > 0:
        n = n // 2
        count += 1
    return count


# 4. 🟡 O(n) - Linear Time [GOOD / FAIR]
def linear_time_sol(n):
    # Jitna bada 'n', utne hi zyada steps. Direct relation hai!
    # Agar N = 100 hai, toh loop poori imandari se 100 baar chalega.
    count = 0
    for i in range(n):
        count += 1
    return count


# 5. 🟠 O(n log n) - Linearithmic Time [AVERAGE]
def n_log_n_time_sol(n):
    # Ek O(n) ka baahar wala loop, aur uske andar ek O(log n) ka loop.
    # Sorting algorithms jaise Merge Sort aur Quick Sort iska sabse bada example hain.
    count = 0
    for i in range(n):  # Yeh n baar chalega
        j = n
        while j > 0:  # Yeh log(n) baar chalega
            j = j // 2
            count += 1
    return count


# 6. 🔴 O(n^2) - Quadratic Time [BAD / SLOW]
def quadratic_time_sol(n):
    # NESTED LOOPS! Baahar wala loop bhi 'n' baar aur andar wala loop bhi 'n' baar.
    # Agar N = 100 hai, toh total steps 100 * 100 = 10,000 ho jayenge! (Jaise Bubble Sort).
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count


# 7. 💀 O(2^n) - Exponential Time [SABSE BEKAR / DANGER ZONE]
def exponential_time_sol(n):
    # Har ek step par 2 nayi branches (recursive calls) khulti hain, yaani kaam double hota jata hai.
    # Agar N = 40-50 bhi ho gaya, toh aapka computer hang ya crash ho sakta hai! (Jaise Naive Fibonacci).
    if n <= 1:
        return n
    return exponential_time_sol(n - 1) + exponential_time_sol(n - 2)
