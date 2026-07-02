"""QUESTION: Python me O(1), O(log n), O(n), O(n^2), O(n^3) aur O(2^n) complexities ko live code se samjhao."""


def master_complexity_hub(n):
    # 1. Constant Time -> O(1)
    result = n * 5  # Koi loop nahi, input chahe 1 ho ya 10L, time fixed rahega # O(1)

    # 2. Logarithmic Time -> O(log n)
    i = 1
    while i < n:
        i = i * 2  # Value step-by-step nahi balki har baar double (*2) ho rahi hai # O(log n)

    # 3. Linear Time -> O(n)
    for x in range(n):
        pass  # Ek single loop jo seedhe 0 se n tak barabar chalta hai # O(n)

    # 4. Quadratic Time -> O(n^2)
    for x in range(n):
        for y in range(n):
            pass  # Nested loop: Loop ke andar loop chalne se n*n ho gaya # O(n^2)

    # 5. Cubic Time -> O(n^3)
    for x in range(n):
        for y in range(n):
            for z in range(n):
                pass  # 3 Nested loops: Loop ke andar loop ke andar loop (n*n*n) # O(n^3)

    # 6. Exponential Time -> O(2^n)
    for x in range(2**n):
        pass  # Input thoda sa badhte hi operations seedha double ho jaate hain # O(2^n)


""" 
SUMMARY:
1. Speed Order: O(1) > O(log n) > O(n) > O(n^2) > O(n^3) > O(2^n) (Sabse slow).
2. Best Performance: O(1) aur O(log n) super fast hain aur bade data ke liye best hain.
3. Average Performance: O(n) bilkul normal aur decent maana jata hai.
4. Worst Performance: O(n^2) aur O(n^3) loops ki nesting badhne se heavy ho jaate hain.
5. Danger Zone: O(2^n) recursion ya brute force me aata hai jo program ko crash kar sakta hai.
"""