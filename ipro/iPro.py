#!/usr/bin/env python
# scripts/examples/simple_tcp_server.py

import moduleModbusTCP
import payload
from struct import pack, unpack
import sys

# -----------------------------------------------------------------------------
def readData(ip, port, unit, ids):
    # prinpy t "Attemping to connect", ip, port
    print("start")

    modbus = moduleModbusTCP.moduleModbusTCP(ip, port)

    print("Connected")

    for id in ids:
        # print "Acquiring", unit, id
        success, data = modbus.ReadHoldingRegistersRTU(unit, int(id) * 10, 10, payload.Big)

        if success == True:
            # print "Payload:", modbus.Hex(data)
            index = 2
            start = 4 * index
            data1 = data[start + 2: start + 4] + data[start: start + 2] # Swap modbus words
            print "%3d %f" % (int(id), unpack(payload.Big + 'f', data1)[0])


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    name = "RFID"
    name = sys.argv[1]
    ip = sys.argv[2]
    port = int(sys.argv[3])
    unit = int(sys.argv[4])
    sensors = sys.argv[5].split(',')

    dict_iPro = { "Shawn"   : ('166.253.148.213', 12345, 232, [105]),
                  "RFID"    : ('166.254.243.215', 12345, 232, [2,101,102,105]),
                  "Ryan"    : ('166.254.119.138', 12345, 232, [105]),
                  "Leal"    : ('166.254.119.140', 12345, 232, [2, 101, 102, 105]),
                  "Brannon" : ('166.254.243.215', 12345, 232, [105, 111]),
                  "Walt"    : ('166.254.119.143', 12345, 232, [105]),
                  "Tyson"   : ('166.254.119.144', 12345, 232, [101, 102, 105]),
                  "Royal"   : ('166.246.206.125', 12345, 232, [105]),
                  "Martine" : ('166.254.119.141', 12345, 232, [105]),
                  "Benny"   : ('166.253.148.214', 12345, 232, [105]) }

    # print (name, dict_iPro[name])

    # ip, port, unit, sensors = dict_iPro[name]

    # print(ip, port, unit, sensors)

    readData(ip, port, unit, sensors)
