import argparse
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA
from Crypto import Random
from Crypto.PublicKey import RSA


def generate_keys(private_key_file, public_key_file):
    key = RSA.generate(2048)
    with open(private_key_file,'wb') as f:
        f.write(key.exportKey('PEM'))
    public_key = key.publickey()
    with open(public_key_file,'wb') as f:
        f.write(public_key.exportKey('PEM'))


def message_hash(message):
    h = SHA.new()
    h.update(message)
    return h    


def sign(message, private_key):
    key = RSA.importKey(open(private_key).read())
    signer = PKCS1_PSS.new(key)
    return signer.sign(message_hash(message))


def verify(message, signature, public_key):
    key = RSA.importKey(open(public_key).read())
    verifier = PKCS1_PSS.new(key)
    return verifier.verify(message_hash(message), signature)


def create_keys(args):
    generate_keys(args.private, args.public)


def sign_message(args):
    message = open(args.message, 'rb').read()
    signature = sign(message, args.key)
    if args.signature is not None:
        open(args.signature, 'wb').write(signature)
    else:
        print(signature)


def verify_message(args):
    message = open(args.message, 'rb').read()
    signature = open(args.signature, 'rb').read()
    print("Verified!" if verify(message, signature, args.key) else "Failed!")


def main():
    '''
    Main entry point, handle argument parsing
    '''
    parser = argparse.ArgumentParser(
        description='Sign Burn message.')
    subparsers = parser.add_subparsers(help='sub-command help')

    parser_create_keys = subparsers.add_parser('create_keys', help='Create new keys')
    parser_create_keys.add_argument('--public', help='File to store the public key.', required=True)
    parser_create_keys.add_argument('--private', help='File to store the private key.', required=True)
    parser_create_keys.set_defaults(func=create_keys)

    parser_sign_message = subparsers.add_parser('sign', help='Sign message file')
    parser_sign_message.add_argument('-m', '--message', help='Message to sign', required=True)
    parser_sign_message.add_argument('-k', '--key', help='Private key to use', required=True)
    parser_sign_message.add_argument('-s', '--signature', help='File to store signature (Optional)')
    parser_sign_message.set_defaults(func=sign_message)

    parser_verify_message = subparsers.add_parser('verify', help='Verify signature file')
    parser_verify_message.add_argument('-m', '--message', help='Message signed', required=True)
    parser_verify_message.add_argument('-k', '--key', help='Public key to use', required=True)
    parser_verify_message.add_argument('-s', '--signature', help='Signature', required=True)
    parser_verify_message.set_defaults(func=verify_message)

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
