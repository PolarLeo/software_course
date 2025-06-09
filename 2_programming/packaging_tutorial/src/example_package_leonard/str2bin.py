# turn str 2 binary
def str2bin_function(input_string):
    input_string = ((input_string.encode(encoding="ascii",errors="namereplace")))
    with open("string.bin","wb") as file:
        file.write((input_string))
    return(input_string)

def bin2str_function(filename):
    with open(filename,"rb") as file:
        output_string = ((file.read()))
        output_string = output_string.decode(encoding="ascii",errors="namereplace")
    return output_string