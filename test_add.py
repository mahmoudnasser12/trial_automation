import ctypes
import sys

# Load the library (DLL on Windows, SO on Linux)
# to test new commit checking 5
lib_name = './add.dll' if sys.platform.startswith('win') else './add.so'
add_dll = ctypes.CDLL(lib_name)

# Define the function signature
add_dll.add.argtypes = [ctypes.c_int, ctypes.c_int]
add_dll.add.restype = ctypes.c_int

# Test the function
result1 = add_dll.add(2, 3)
print(f"add(2, 3) = {result1}")

result2 = add_dll.add(10, 20)
print(f"add(10, 20) = {result2}")

result3 = add_dll.add(-5, 5)
print(f"add(-5, 5) = {result3}")
