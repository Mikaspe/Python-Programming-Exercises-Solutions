import zlib

str = 'hello world!hello world!hello world!hello world!'
str8 = bytes(str, 'utf-8')

str_compressed = zlib.compress(str8)
str_decompressed = zlib.decompress(str_compressed)

print(len(str_compressed), '\n', len(str_decompressed))

