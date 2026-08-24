encrypted = "2d041e1807120e0010"
key = b"Earth"

encrypted = input("plz input encrypted message: ")
key = bytes(input("plz input Encryption key: ").encode())

bytes_converted = bytes.fromhex(encrypted)

dec = bytes(
    bytes_converted[i] ^ key[i%len(key)]
    for i in range(len(bytes_converted))
)

print(dec.decode())