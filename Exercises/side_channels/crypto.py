mem_size = 2048
cache_lines = 32
cache_line_size = 32
class Cache():
    def __init__(self):
        self.cache = [{"tag":None, "value":None} for line in range(cache_lines)]
        self.memory = [0 for i in range(mem_size)]
    def line_from_address(self, address):
        return (address//cache_line_size)%cache_lines
    def tag_from_address(self, address):
        return (address//cache_line_size)
    def read_address(self, address):
        miss = False
        l = self.line_from_address(address)
        tag = self.tag_from_address(address)
        if self.cache[l]["tag"] != tag:
            miss = True
            v = [self.memory[tag*cache_line_size + offset] for offset in range(cache_line_size)]
            self.cache[l]["value"] = v
            self.cache[l]["tag"] = tag
        return (self.cache[l]["value"][address % cache_line_size], 20 if miss else 1)
    def write_address(self, address, value):
        l = self.line_from_address(address)
        self.cache[l]["value"] = None
        self.cache[l]["tag"] = None
        self.memory[address]=value
        self.read_address(address)

T = [57, 78, 232, 141, 132, 252, 34, 13, 184, 92, 144, 45, 133, 44, 151, 219, 182, 14, 80, 206, 88, 99, 230, 52, 155, 127, 50, 185, 243, 165, 179, 245, 93, 130, 54, 1, 117, 96, 143, 79, 106, 7, 118, 156, 43, 171, 177, 196, 229, 175, 221, 203, 111, 213, 84, 150, 61, 218, 139, 201, 124, 223, 250, 53, 112, 180, 9, 244, 131, 109, 136, 178, 159, 142, 81, 194, 238, 119, 105, 89, 125, 114, 157, 49, 91, 8, 25, 103, 26, 220, 69, 100, 153, 129, 205, 195, 67, 188, 164, 10, 170, 17, 163, 197, 101, 65, 42, 241, 60, 254, 137, 86, 59, 235, 192, 227, 183, 85, 97, 123, 135, 226, 64, 204, 225, 146, 134, 38, 128, 209, 87, 32, 166, 193, 46, 30, 40, 120, 47, 210, 249, 173, 191, 28, 23, 207, 71, 248, 39, 5, 20, 74, 55, 63, 24, 21, 208, 27, 116, 95, 75, 121, 58, 168, 242, 29, 187, 98, 31, 236, 12, 3, 239, 224, 2, 94, 190, 82, 22, 246, 217, 231, 102, 6, 222, 18, 83, 251, 16, 51, 113, 149, 126, 174, 162, 11, 234, 62, 104, 77, 41, 90, 200, 161, 115, 240, 0, 68, 19, 181, 169, 152, 172, 37, 108, 214, 140, 110, 72, 4, 215, 158, 186, 198, 33, 154, 202, 160, 107, 15, 148, 147, 56, 216, 176, 73, 122, 189, 35, 212, 167, 70, 199, 211, 36, 233, 237, 138, 253, 76, 247, 228, 145, 66, 48]
T_address = 0
class Crypto():
    def load_table(self, cache):
        for a in range(len(T)):
            cache.write_address(T_address+a, T[a])
    
    def feistel_encrypt(self, cache, msg, key):
        l0 = ord(msg[0])
        r0 = ord(msg[1])
        r1 = cache.read_address(r0)
        r1 = l0 ^ ord(key[0]) ^ r1[0]
        l1 = r0
        r2 = cache.read_address(r1)
        r2 = l1 ^ ord(key[1]) ^ r2[0]
        l2 = l1
        return chr(l2)+chr(r2)
