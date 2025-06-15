# string slicing
text = "PythonProgramming"
# 1. Get the first 6 characters
print(text[0:6])  # Output: Python
# 2. Get the substring "Program"
print(text[6:13])  # Output: Program
#3. Get all characters from index 6 till end
print(text[6:])  # Output: Programming
# 4. Get every second character from index 0 to 10
print(text[0:11:2])  # Output: Pto rg
# 5. Get the string in reverse order using slicing
print(text[::-1])  # Output: gnimmargorPnohtyP
# 6. Get the last 3 characters
print(text[-3:])  # Output: ing
# 7. Get all characters except the last 5
print(text[:-5])  # Output: PythonProgra
# 8. Get characters from -11 to -6
print(text[-11:-6])  # Output: Progr
# 9. Get characters from -1 to -7 in reverse
print(text[-1:-8:-1])  # Output: gnimmar
# 10. Get characters from -6 to -1 (excluding -1)
print(text[-6:-1])  # Output: ammin
#11. Slice from index 3 to -3
print(text[3:-3])  # Output: honProgrammi
# 12. Get every third character from the string
print(text[::3])  # Output: PhPgai
# 13. 13. Get the middle 5 characters 
mid = len(text) // 2
print(text[mid-2:mid+3])  # Output: ogram
 #14. Remove first and last character using slicing
 print(text[1:-1])  # Output: ythonProgrammin
# 15. Reverse only the substring "Programming"
part = text[6:]  # 'Programming'
print(part[::-1])  # Output: gnimmargorP
