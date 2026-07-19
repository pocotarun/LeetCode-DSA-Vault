"""Q: Create an array, search X with O(N) & O(log N) complexities, and analyze a 2x3 Matrix."""

from array import array as arr  # Array module import kiya short name ke sath
import numpy as np  # NumPy import kiya multi-dimension aur automatic shape ke liye

# --- 1. ARRAY MODULE & OPERATIONS ---
a = arr("i", [1, 2, 3])  # 'i' typecode se signed int array bana, homogeneous data rule
a.append(4)  # append() se array ke bilkul end me 4 add ho gaya
a.insert(1, 5)  # insert() se index 1 pr 5 aaya, baki elements right side khisak gaye
a.pop()  # pop() bina index ke hamesha last element ko delete karta hai
a.remove(5)  # remove() se direct value 5 delete hui, index na pata ho tab best h
a.reverse()  # reverse() pure array को बिना किसी एक्स्ट्रा लूप के तुरंत उल्टा कर देता है
sub = a[0:2]  # slicing se index 0 se 1 tak ka tukda mila, end index (2) excluded hai
rev_arr = a[::-1]  # [::-1] slicing ka short trick hai array ko double reverse karne ke liye
for x in a:
    print(x, end=" ")  # Enhanced loop bina index jhanjhat ke saare elements print karega

# --- 2. SEARCHING WITH DIFFERENT TIME COMPLEXITIES ---
# Approach 1: Linear Search -> Time Complexity: O(N), Space: O(1)
arr_linear = np.arange(10, 20, 2)  # arange se [10,12,14,16,18] bana, end (20) excluded h
idx = -1  # Default index -1 set kiya agar target na mile to
for i in range(len(arr_linear)):  # len() dynamic size batata h, range se loop index mila
    if arr_linear[i] == 14:
        idx = i
        break  # Element 14 milte hi index save kiya aur loop break kiya
print(f"\nO(N) Index: {idx}")  # Linear search ka normal output print kiya

# Approach 2: Binary Search (Optimized) -> Time Complexity: O(log N), Space: O(1)
low, high, target, b_idx = 0, len(arr_linear) - 1, 16, -1  # Pointers set kiye target 16 ke liye
while low <= high:  # Jab tak low pointer high se chota ya barabar h tab tak chalega
    mid = (low + high) // 2  # Mid index nikala records ko do bhaago me divide karne ke liye
    if arr_linear[mid] == target:
        b_idx = mid
        break  # Mid par hi target mil gaya, binary search complete
    elif arr_linear[mid] < target:
        low = mid + 1  # Target bada hai to array ke right side shift ho jao
    else:
        high = mid - 1  # Target chota hai to array ke left side shift ho jao
print(f"O(log N) Index: {b_idx}")  # Binary search ka fast output print kiya

# --- 3. NUMPY SHORTCUT METHODS ---
lin = np.linspace(1, 5, 5)  # [1,2,3,4,5] bana, linspace me start aur end dono included hote hain
z = np.zeros(3)  # zeros() se [0., 0., 0.] float array mila (by default data type float)
o = np.ones(3)  # ones() se [1., 1., 1.] mila, full(3, 7) use karne par [7, 7, 7] milta
lg = np.logspace(1, 2, 3)  # log scale array mila, heterogeneous support karta h numpy

# --- 4. MULTI-DIMENSIONAL ARRAYS & SHAPE (N x M) ---
mat_2x3 = np.array([[1, 2, 3], [4, 5, 6]])  # 2D Array bana, rule: saare sub-lists ka size hamesha same ho
print("Shape (N, M):", mat_2x3.shape)  # .shape se (2, 3) mila. RC Rule: R=Row (Soti), C=Column (Khadi)
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # 3D Array, brackets ke levels dekhkar dimension pehchano

""" 
QUICK SUMMARY:
1. Array module same data-type ('i','d') ka 1D continuous memory allocation array banata hai.
2. NumPy advanced hai, isme bina typecode ke 1D, 2D, 3D (Heterogeneous) arrays auto-cast ke sath bante hain.
3. arange() aur range() me end value include nahi hoti, par linspace() me end value include hoti hai.
4. Matrix size n x m me RC Rule chalta hai: n = Rows (Soti hui lines) aur m = Columns (Khadi hui lines/Pillars).
5. Search complexity ko poor O(N) Linear se optimize karke ultra-fast O(log N) Binary Search me badla jata hai.
"""
