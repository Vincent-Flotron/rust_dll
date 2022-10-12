# Load a DLL into memory and use its functions.
from ctypes import *


def main():
    # give location of dll
    dll_relative_path = r".\target\debug\rust_dll.dll".replace('\\', '/')

    # Load the dll on memory
    rust_dll = CDLL(dll_relative_path)

    # Call the function "Return111()" which return the number 111 using an integer
    print('Return 111: ')
    print(rust_dll.Return111())

    # Set the return type of the dll's function "ReturnTheString(str)". It's a string represented as an i8 array.
    rust_dll.ReturnTheString.restype = c_char_p

    # Call the function "ReturnTheString(str)" with jimmy as argument passing a byte array.
    print('\nReturn the string from dll:')
    print(rust_dll.ReturnTheString(b'jimmy').decode())

if __name__ == '__main__':
    main()