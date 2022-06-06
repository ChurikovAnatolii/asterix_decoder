import socket
import keyboard


def cut_in_asterix(buf, above_buf):
    p_len = int(hex(int(buf[2:6], 16)), 16) * 2
    if buf[0:2] == '3e':
        cut_s = buf[0:p_len]
        if len(buf) != len(cut_s):
            above_buf = buf[buf.rfind('3e'):-1]
        return cut_s
    else:
        print(above_buf + buf[0:buf.find('3e')])
        #cut_s = above_buf + buf[buf.find('3e'):-1]
        #print(cut_s)
    return 0


cat62_pack = {}
index = 0
buf_ostatka = ''
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 4001))

while True:
    data = sock.recv(65556)
    str_buf = str(data.hex())
    index = index + 1
    if cut_in_asterix(str_buf, buf_ostatka) != 0:
        print(index, 'raw', str_buf)
        cat62_pack[index] = cut_in_asterix(str_buf, buf_ostatka)
        print(index, 'map',  cat62_pack[index])
    if keyboard.is_pressed('q'):
        print('q has pressed end of program')
        break



