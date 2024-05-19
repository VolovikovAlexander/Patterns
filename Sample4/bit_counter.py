#! encoding: utf8


def main():
    filename = '/usr/share/dict/words'
    bit_1_cnt = bit_0_cnt = 0
    with open(filename) as fh:
        for line in fh.readlines():
            bytes_str = bytearray(line, 'UTF-8')
            for single_byte in bytes_str:
                mask_bit = 0b00000001
                for i in range(8):
                    if single_byte & mask_bit:
                        bit_1_cnt += 1
                    else:
                        bit_0_cnt += 1
                    mask_bit <<= 1
    print("Total 1 count:{}, Total 0 count:{}, Ratio: {:.5f}".format(bit_1_cnt,bit_0_cnt,float(bit_1_cnt)/bit_0_cnt))


if __name__ == '__main__':
    main()

