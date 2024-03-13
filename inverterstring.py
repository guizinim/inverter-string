def reverse_string(s):
    reversed_str = ""
    
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str

input_string = input("Digite uma string para reverter: ")
reversed_string = reverse_string(input_string)
print("String revertida:", reversed_string)
