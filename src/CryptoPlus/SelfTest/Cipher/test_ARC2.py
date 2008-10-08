# -*- coding: utf-8 -*-
#
#  SelfTest/Cipher/ARC2.py: Self-test for the Alleged-RC2 cipher
#
# =======================================================================
# Copyright (C) 2008  Dwayne C. Litzenberger <dlitz@dlitz.net>
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# =======================================================================
#

"""Self-test suite for CryptoPlus.Cipher.ARC2"""

__revision__ = "$Id$"

from common import dict     # For compatibility with Python 2.1 and 2.2

# This is a list of (plaintext, ciphertext, key[, description[, extra_params]]) tuples.
test_data = [
    # Test vectors from RFC 2268

    # 63-bit effective key length
    ('0000000000000000', 'ebb773f993278eff', '0000000000000000',
        'RFC2268-1', dict(effective_keylen=63)),

    # 64-bit effective key length
    ('ffffffffffffffff', '278b27e42e2f0d49', 'ffffffffffffffff',
        'RFC2268-2', dict(effective_keylen=64)),
    ('1000000000000001', '30649edf9be7d2c2', '3000000000000000',
        'RFC2268-3', dict(effective_keylen=64)),
    ('0000000000000000', '61a8a244adacccf0', '88',
        'RFC2268-4', dict(effective_keylen=64)),
    ('0000000000000000', '6ccf4308974c267f', '88bca90e90875a',
        'RFC2268-5', dict(effective_keylen=64)),
    ('0000000000000000', '1a807d272bbe5db1', '88bca90e90875a7f0f79c384627bafb2',
        'RFC2268-6', dict(effective_keylen=64)),

    # 128-bit effective key length
    ('0000000000000000', '2269552ab0f85ca6', '88bca90e90875a7f0f79c384627bafb2',
        "RFC2268-7", dict(effective_keylen=128)),
    ('0000000000000000', '5b78d3a43dfff1f1',
        '88bca90e90875a7f0f79c384627bafb216f80a6f85920584c42fceb0be255daf1e',
        "RFC2268-8", dict(effective_keylen=129)),

    # Test vectors from PyCryptoPlus 2.0.1's testdata.py
    # 1024-bit effective key length
    ('0000000000000000', '624fb3e887419e48', '5068696c6970476c617373',
        'PCTv201-0',dict(effective_keylen=1024)),
    ('ffffffffffffffff', '79cadef44c4a5a85', '5068696c6970476c617373',
        'PCTv201-1',dict(effective_keylen=1024)),
    ('0001020304050607', '90411525b34e4c2c', '5068696c6970476c617373',
        'PCTv201-2',dict(effective_keylen=1024)),
    ('0011223344556677', '078656aaba61cbfb', '5068696c6970476c617373',
        'PCTv201-3',dict(effective_keylen=1024)),
    ('0000000000000000', 'd7bcc5dbb4d6e56a', 'ffffffffffffffff', 'PCTv201-4',dict(effective_keylen=1024)),
    ('ffffffffffffffff', '7259018ec557b357', 'ffffffffffffffff', 'PCTv201-5',dict(effective_keylen=1024)),
    ('0001020304050607', '93d20a497f2ccb62', 'ffffffffffffffff', 'PCTv201-6',dict(effective_keylen=1024)),
    ('0011223344556677', 'cb15a7f819c0014d', 'ffffffffffffffff', 'PCTv201-7',dict(effective_keylen=1024)),
    ('0000000000000000', '63ac98cdf3843a7a',
        'ffffffffffffffff5065746572477265656e6177617953e5ffe553',
        'PCTv201-8',dict(effective_keylen=1024)),
    ('ffffffffffffffff', '3fb49e2fa12371dd',
        'ffffffffffffffff5065746572477265656e6177617953e5ffe553',
        'PCTv201-9',dict(effective_keylen=1024)),
    ('0001020304050607', '46414781ab387d5f',
        'ffffffffffffffff5065746572477265656e6177617953e5ffe553',
        'PCTv201-10',dict(effective_keylen=1024)),
    ('0011223344556677', 'be09dc81feaca271',
        'ffffffffffffffff5065746572477265656e6177617953e5ffe553',
        'PCTv201-11',dict(effective_keylen=1024)),
    ('0000000000000000', 'e64221e608be30ab', '53e5ffe553', 'PCTv201-12',dict(effective_keylen=1024)),
    ('ffffffffffffffff', '862bc60fdcd4d9a9', '53e5ffe553', 'PCTv201-13',dict(effective_keylen=1024)),
    ('0001020304050607', '6a34da50fa5e47de', '53e5ffe553', 'PCTv201-14',dict(effective_keylen=1024)),
    ('0011223344556677', '584644c34503122c', '53e5ffe553', 'PCTv201-15',dict(effective_keylen=1024)),
]

def get_tests():
    from CryptoPlus.Cipher import ARC2
    from common import make_block_tests
    return make_block_tests(ARC2, "ARC2", test_data)

if __name__ == '__main__':
    import unittest
    suite = lambda: unittest.TestSuite(get_tests())
    unittest.main(defaultTest='suite')

# vim:set ts=4 sw=4 sts=4 expandtab: