#!/usr/bin/env python3
from insecure_hash import hash_string
from Crypto.Cipher import AES


# This function finds a message that collids with the given message in the
# hash_string function.
def find_collision(message):
    block = message[:16]
    block = block + (" " * (16-len(block))).encode()
    key = (" " * 16).encode()
    cipher = AES.new(key)
    encrypted = cipher.encrypt(block)
    message_rest = message[16:]
    message_rest = message_rest + (" " * (16-len(message_rest))).encode()
    collision = encrypted + key + message_rest
    return collision


if __name__ == '__main__':
    message = "abcdef".encode()
    print("Hash of %s is %s" % (message, hash_string(message)))
    collision = find_collision(message)
    print("Hash of %s is %s" % (collision, hash_string(collision)))
