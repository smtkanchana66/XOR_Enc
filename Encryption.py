data = bytes(input("Plz input data you want to encrypt: ").encode())
key  = bytes(input("plz input encryption key: ").encode())

enc = bytes(
    data[i] ^ key[i%len(key)]
    for i in range(len(data))
)

hex_coded = enc.hex()

print("Encrypted message: ", hex_coded)