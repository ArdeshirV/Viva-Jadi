#!/usr/bin/env python
#  viva-jadi.py - Draw a lovely heart 4 dear Jadi, Version 1.0
#  Copyright (c) 2019 ArdeshirV@protonmail.com, Licensed under GPLv3+
import base64


def main(args):
    encoded_heart = b'cHJpbnQoJ1xuJy5qb2luKFsnJy5qb2luKFsnXDAzM1sxOzMxbScrKCdKYWRpTG92ZSdbKHgteSklOF1pZigoeCowLjA1KSoqMisoeSowLjEpKioyLTEpKiozLSh4KjAuMDUpKioyKih5KjAuMSkqKjM8PTAgZWxzZSdcMDMzWzBtICcpZm9yIHggaW4gcmFuZ2UoLTMwLDMwKV0pZm9yIHkgaW4gcmFuZ2UoMTUsLTE1LC0xKV0pKQ=='
    heart = base64.b64decode(encoded_heart)
    print('Code:\n{}\n'.format(encoded_heart))
    print('Decode:\n{}\n'.format(heart))
    exec(heart)
    return 0


if __name__ == '__main__':
    from sys import exit, argv
    exit(main(argv))
