'''
Modbus Payload Builders
------------------------

A collection of utilities for building and decoding
modbus messages payloads.
'''
from struct import pack, unpack

Little = '<'
Big    = '>'

class BinaryPayloadBuilder(object):
    '''
    A utility that helps build payload messages to be
    written with the various modbus messages. It really is just
    a simple wrapper around the struct module, however it saves
    time looking up the format strings. What follows is a simple
    example::

        builder = BinaryPayloadBuilder(endian=Endian.Little)
        builder.add_8bit_uint(1)
        builder.add_16bit_uint(2)
        payload = builder.build()
    '''

    def __init__(self, payload = None, endian = Big):
        ''' Initialize a new instance of the payload builder

        :param payload: Raw payload data to initialize with
        :param endian: The endianess of the payload
        '''
        self._payload = payload or []
        self._endian  = endian

    def __str__(self):
        ''' Return the payload buffer as a string

        :returns: The payload buffer as a string
        '''
        return ''.join(self._payload)

    def build(self):
        return self.__str__()

    def reset(self):
        ''' Reset the payload buffer
        '''
        self._payload = []

    def add_8bit_uint(self, value):
        ''' Adds a 8 bit unsigned int to the buffer

        :param value: The value to add to the buffer
        '''
        fstring = self._endian + 'B'
        self._payload.append(pack(fstring, value))

    def add_16bit_uint(self, value):
        ''' Adds a 16 bit unsigned int to the buffer

        :param value: The value to add to the buffer
        '''
        fstring = self._endian + 'H'
        self._payload.append(pack(fstring, value))

    def add_32bit_uint(self, value):
        ''' Adds a 32 bit unsigned int to the buffer

        :param value: The value to add to the buffer
        '''
        fstring = self._endian + 'I'
        self._payload.append(pack(fstring, value))

    def add_64bit_uint(self, value):
        ''' Adds a 64 bit unsigned int to the buffer

        :param value: The value to add to the buffer
        '''
        fstring = self._endian + 'Q'
        self._payload.append(pack(fstring, value))

    def add_8bit_int(self, value):
        ''' Adds a 8 bit signed int to the buffer

        :param value: The value to add to the buffer
        '''
        fstring = self._endian + 'b'
        self._payload.append(pack(fstring, value))

    def add_16bit_int(self, value):
        ''' Adds a 16 bit signed int to the buffer

        :param value: The value to add to the buffer
        '''
        fstring = self._endian + 'h'
        self._payload.append(pack(fstring, value))

    def add_32bit_int(self, value):
        ''' Adds a 32 bit signed int to the buffer

        :param value: The value to add to the buffer
        '''
        fstring = self._endian + 'i'
        self._payload.append(pack(fstring, value))

    def add_64bit_int(self, value):
        ''' Adds a 64 bit signed int to the buffer

        :param value: The value to add to the buffer
        '''
        fstring = self._endian + 'q'
        self._payload.append(pack(fstring, value))

    def add_32bit_float(self, value):
        ''' Adds a 32 bit float to the buffer

        :param value: The value to add to the buffer
        '''
        fstring = self._endian + 'f'
        self._payload.append(pack(fstring, value))

    def add_64bit_float(self, value):
        ''' Adds a 64 bit float(double) to the buffer

        :param value: The value to add to the buffer
        '''
        fstring = self._endian + 'd'
        self._payload.append(pack(fstring, value))

    def add_string(self, value):
        ''' Adds a string to the buffer

        :param value: The value to add to the buffer
        '''
        fstring = self._endian + 's'
        for c in value:
            self._payload.append(pack(fstring, c))


class BinaryPayloadDecoder(object):
    '''
    A utility that helps decode payload messages from a modbus
    reponse message.  It really is just a simple wrapper around
    the struct module, however it saves time looking up the format
    strings. What follows is a simple example::

        decoder = BinaryPayloadDecoder(payload)
        first   = decoder.decode_8bit_uint()
        second  = decoder.decode_16bit_uint()
    '''

    def __init__(self, payload, endian = Big):
        ''' Initialize a new payload decoder

        :param payload: The payload to decode with
        :param endian: The endianess of the payload
        '''
        self._payload = payload
        self._pointer = 0x00
        self._endian  = endian

    def reset(self):
        ''' Reset the decoder pointer back to the start
        '''
        self._pointer = 0x00

    def decode_8bit_uint(self):
        ''' Decodes a 8 bit unsigned int from the buffer
        '''
        self._pointer += 1
        fstring = self._endian + 'B'
        handle = self._payload[self._pointer - 1:self._pointer]
        return unpack(fstring, handle)[0]

    def decode_16bit_uint(self):
        ''' Decodes a 16 bit unsigned int from the buffer
        '''
        self._pointer += 2
        fstring = self._endian + 'H'
        handle = self._payload[self._pointer - 2:self._pointer]
        return unpack(fstring, handle)[0]

    def decode_32bit_uint(self):
        ''' Decodes a 32 bit unsigned int from the buffer
        '''
        self._pointer += 4
        fstring = self._endian + 'I'
        handle = self._payload[self._pointer - 4:self._pointer]
        return unpack(fstring, handle)[0]

    def decode_64bit_uint(self):
        ''' Decodes a 64 bit unsigned int from the buffer
        '''
        self._pointer += 8
        fstring = self._endian + 'Q'
        handle = self._payload[self._pointer - 8:self._pointer]
        return unpack(fstring, handle)[0]

    def decode_8bit_int(self):
        ''' Decodes a 8 bit signed int from the buffer
        '''
        self._pointer += 1
        fstring = self._endian + 'b'
        handle = self._payload[self._pointer - 1:self._pointer]
        return unpack(fstring, handle)[0]

    def decode_16bit_int(self):
        ''' Decodes a 16 bit signed int from the buffer
        '''
        self._pointer += 2
        fstring = self._endian + 'h'
        handle = self._payload[self._pointer - 2:self._pointer]
        return unpack(fstring, handle)[0]

    def decode_32bit_int(self):
        ''' Decodes a 32 bit signed int from the buffer
        '''
        self._pointer += 4
        fstring = self._endian + 'i'
        handle = self._payload[self._pointer - 4:self._pointer]
        return unpack(fstring, handle)[0]

    def decode_64bit_int(self):
        ''' Decodes a 64 bit signed int from the buffer
        '''
        self._pointer += 8
        fstring = self._endian + 'q'
        handle = self._payload[self._pointer - 8:self._pointer]
        return unpack(fstring, handle)[0]

    def decode_32bit_float(self):
        ''' Decodes a 32 bit float from the buffer
        '''
        self._pointer += 4
        fstring = self._endian + 'f'
        handle = self._payload[self._pointer - 4:self._pointer]
        return unpack(fstring, handle)[0]

    def decode_64bit_float(self):
        ''' Decodes a 64 bit float(double) from the buffer
        '''
        self._pointer += 8
        fstring = self._endian + 'd'
        handle = self._payload[self._pointer - 8:self._pointer]
        return unpack(fstring, handle)[0]

    def decode_string(self, size=1):
        ''' Decodes a string from the buffer

        :param size: The size of the string to decode
        '''
        self._pointer += size
        return self._payload[self._pointer - size:self._pointer]
