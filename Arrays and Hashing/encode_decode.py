"""
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.
"""

def encode(strs):
    encoding_string = ""
    for i in range(len(strs)):
        if i != len(strs) - 1:
            encoding_string += (strs[i] + ":;")
        else:
            encoding_string += strs[i]
    return encoding_string
    
def decode(string):
    encode = []
    word = ""
    for i in range(len(string)):
        if string[i].isalpha():
            word += string[i]
        else:
            if word != "" :
                encode.append(word)
                word = ""
    encode.append(word)
    return encode
            


strs = ["lint","code","love","you"]
encoded_string = encode(strs)
print(encoded_string)
print("The decoded string is: ", decode(encoded_string))