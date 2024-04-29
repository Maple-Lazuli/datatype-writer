from data_simulator.link import Link, HexLink, ByteLink


def hex_dump(byte_array, endianess='big'):
    str_array = [hex(b)[2:].zfill(2).upper() for b in byte_array]
    if endianess == 'little':
        str_array = str_array[::-1]
    return " ".join(str_array)


class Format:
    def __init__(self, data, endianess='big'):
        self.data = data
        self.endianess = endianess
        self.bytes_buffer = None
        self.str_buffer = None

    def get_bytes(self):
        return bytes(self.data, 'utf-8')

    def get_hex_dump(self):
        byte_array = bytes(self.data, 'utf-8')
        return hex_dump(byte_array, self.endianess)

    def __and__(self, other):
        return HexLink(self.get_hex_dump() + other.get_hex_dump())

    def __or__(self, other):
        return ByteLink(self.get_bytes() + other.get_bytes())

    def __add__(self, other):
        return Link(self.get_hex_dump() + other.get_hex_dump(), self.get_bytes() + self.get_bytes())

    def __str__(self):
        return self.get_hex_dump()