import sys
import types
import unittest
from unittest.mock import patch

sys.modules.setdefault('serial', types.SimpleNamespace(Serial=None))
from core.serial import ProcessorCIInterface


class FakeSerial:
    def __init__(self, chunks=()):
        self.writes = []
        self.chunks = list(chunks)
        self.timeout = 0.01

    def write(self, data):
        self.writes.append(data)

    def read(self, size):
        return self.chunks.pop(0)[:size] if self.chunks else b''


class SerialContractTests(unittest.TestCase):
    def interface(self, chunks=()):
        interface = ProcessorCIInterface.__new__(ProcessorCIInterface)
        interface.serial = FakeSerial(chunks)
        return interface

    def test_command_encoding_and_banks(self):
        interface = self.interface([b'\0\0\0\x01'])
        interface.write_memory(0x20, 0x11223344, second_memory=True)
        self.assertEqual(interface.serial.writes[:2], [bytes.fromhex('80000857'), bytes.fromhex('11223344')])
        interface.read_memory(0x20, second_memory=True)
        self.assertEqual(interface.serial.writes[2], bytes.fromhex('8000084c'))
        interface.read_accumulator()
        interface.read_from_accumulator(0)
        self.assertEqual(interface.serial.writes[-2:], [bytes.fromhex('00000061'), bytes.fromhex('0000004d')])

    def test_partial_response_and_deadline(self):
        interface = self.interface([b'luck', bytes.fromhex('00000014')])
        self.assertEqual(interface.execute_until_stop(host_timeout=1), b'luck\0\0\0\x14')
        interface = self.interface()
        with self.assertRaises(TimeoutError):
            interface.execute_until_stop(host_timeout=0.001)


if __name__ == '__main__':
    unittest.main()
