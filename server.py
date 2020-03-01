import socket

from utils.network import proxy
from utils.protocol import PacketChunkData, auto_unpack_pack
from quarry.types.buffer.v1_7 import Buffer1_7

listen_ip = '127.0.0.1'
listen_port = 2000
dst_ip = '127.0.0.1'
dst_port = 25565


@auto_unpack_pack
def tweak(buff: Buffer1_7) -> bytes:
    packet_id = buff.unpack_varint()
    if packet_id == 0x22:
        packet_chunk_data = PacketChunkData(buff.buff[buff.pos:])
        return buff.pack_varint(packet_id) + packet_chunk_data.pack_packet_data()

    return buff.buff


if __name__ == '__main__':
    proxy(listen_ip, listen_port, dst_ip, dst_port, tweak)
