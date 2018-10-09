import json

import sign_message

PUBLIC_KEY = 'tests/public.pem'
PRIVATE_KEY = 'tests/private.pem'


def test_verify_random_signature_fails():
    message = b'This is a message'
    signature = b'random_signature'
    assert not sign_message.verify(message, signature, PUBLIC_KEY)


def test_verify_signature_passes():
    message = b'This is a message'
    signature = b"\x89g\x9a6If\xa7\xe8\xd0\x13FQ\xefrJ\xc4m\xf42\x98\xa2\xf7\x9f\xa0\xae\x18\xd9\x9d\xc2\x9e\xc3?\xa0\xaa\x13\xcc\xc3\xd6\xc0=\x16\x8fe3}\x9b\xb1\xe9_+o\xdf\x82\xda\xd8\n7\xaez\x1c\xa7*\xfdh~\xac\xc2Ca\xbb\x80m\xc5\xff\xb7\x01B\xc6\xba\xb3.!\xc4\xd3\x1e\xc2i\x15)`5\x85\x91VOFo\xea\x0e\xe3\xe2Z\xc0\x133XB\xca_=:7\xad\xff\x91lps-B>\t\xeeH\x80\x8c\xf6\x9b\xf2\xeds\xdda>:t\xe2\x11N\xd6\xb7\\\x18\x0eZ\xc5j|\x8eP\xbf'\x03Gh\x98\xff\x9e\x1a\xb3\xf9=\x99\xbaF\xe7\x93\x9d\x8a\xc8\xe74\xf8\x14\x7f^/PE\xc8\x88\x1a\xe3\x1f\xf7\x0b\x85\x0f$\xd9g(\xd2\x98}\xf1\x10\xa5Kz3\x86\xc0\x15\x07'\xddp%9\xf7\x07A\xe3\xe3\x8fC\xeb\x85i;\x16\xf8\x89\xe4JB]\xf0\x93A\x94\xc3K\x8b\xfbP\xf8\xfbG\xdd\x9c\xb0\x88\xa3h\xd0\x9d\xa5\x17c&\x98\xbc|X"
    assert sign_message.verify(message, signature, PUBLIC_KEY)


def test_sign_simple_messge():
    message = b"This is a message"
    signature = sign_message.sign(message, PRIVATE_KEY)
    assert sign_message.verify(message, signature, PUBLIC_KEY)


def test_sign_message_sample():
    message = open('message_sample.txt', 'rb').read()
    signature = sign_message.sign(message, PRIVATE_KEY)
    assert sign_message.verify(message, signature, PUBLIC_KEY)


def test_verify_message_sample_signature():
    message = open('message_sample.txt', 'rb').read()
    signature = open('message_sample_signature.txt', 'rb').read()
    assert sign_message.verify(message, signature, PUBLIC_KEY)
