import json
import os


class Frame(object):
    """This class include attributes and method of frames.

    Attributes:
        ack = An integer count of the eggs we have laid.
        seq = An integer count of the frame sequence desired/transferring.
        nak = A boolean indicating if the frame received succeed or not.
        data = A String include the original data.
    """

    def __init__(self, ack_in, seq_in, nak, data):
        """Inits Frame with its elements."""
        self.ack = ack_in
        self.seq = seq_in
        self.nak = nak
        self.data = data

    def to_bytes(self):
        """Pack Frames into dictionary and transform to bytes which is ready to sent.

        The Frame object will transform into bytes format and encode with CRC-CCITT

        Args:

        Returns:
            self: The frame constructed by this method
        """
        frame_dic = {
            'ack': self.ack,
            'seq': self.seq,
            'nak': self.nak,
            'data': self.data,
        }
        frame_json = json.dumps(frame_dic)
        frame_bytes = frame_json.encode('utf-8')
        return self._crc_encode(frame_bytes)

    def construct(self, frame_bytes):
        """Decode bytes and construct a Frame

        Args:
            frame_bytes (bytes): The bytes format of Frame(dictionary)

        Returns:
            self: The frame constructed by this method
        """

        if self._crc_decode(frame_bytes):
            frame_bytes = frame_bytes[:-2]
        print(frame_bytes)
        print(frame_bytes[:-2])

        frame_json = frame_bytes.decode('utf-8')
        frame_dic = json.loads(frame_json)
        self.ack = frame_dic['ack']
        self.seq = frame_dic['seq']
        self.nak = frame_dic['nak']
        self.data = frame_dic['data']
        return self

    def _crc_encode(self, source):
        """Calculate crc code of the Frame

        Args:
            source (bytes): The bytes format of Frame(dictionary)

        Returns:
            self: The frame constructed by this method
        """

        polynomial = 0x11021  # 1 0001 0000 0010 0001 (0, 5, 12) x^16+x^12+x^5+1
        dividend = 0
        for index in range(len(source)):
            b = source[index]
            for i in range(0, 8, 1):
                dividend = (dividend << 1) + (b >> (7 - i) & 1)

                if (dividend >> 16 & 1) == 1:
                    dividend ^= polynomial
        for i in range(0, 16, 1):
            dividend = (dividend << 1)

            if (dividend >> 16 & 1) == 1:
                dividend ^= polynomial
        source += bytes([dividend >> 8 & 255])
        source += bytes([dividend & 255])
        return source

    def _crc_decode(self, source):
        """Checksum of crc for the Frame

        Args:
            source (bytes): The bytes format of Frame(dictionary)

        Returns:
            self: The frame constructed by this method
        """

        # remainder = bytes([source >> 8 & 255])
        # remainder += bytes([source & 255])

        polynomial = 0x11021  # 1 0001 0000 0010 0001 (0, 5, 12) x^16+x^12+x^5+1
        dividend = 0
        for index in range(len(source)):
            b = source[index]
            for i in range(0, 8, 1):
                dividend = (dividend << 1) + (b >> (7 - i) & 1)

                if (dividend >> 16 & 1) == 1:
                    dividend ^= polynomial
                print(dividend)
        if dividend == 0:
            return True

        '''
        crc = 0xFFFF
        polynomial = 0x1021  # 0001 0000 0010 0001 (0, 5, 12)
        tmp = ""
        byte = bytes()
        for i in source:
            if i % 2 == 0:
                tmp = Source.Substring(i, 2)
                byte[i / 2] = (byte)
                Int16.Parse(tmp, System.Globalization.NumberStyles.HexNumber)

        for b in byte:
            for i in range[0,7,1]:
                bool
                bit = ((b >> (7 - i) & 1) == 1)
                bool
                c15 = ((crc >> 15 & 1) == 1)
                crc <<= 1
                if c15 ^ bit:
                    crc ^= polynomial
        crc &= 0xffff
        strDest = crc.ToString("X")
        return strDest'''
