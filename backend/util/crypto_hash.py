import hashlib
import json

def crypto_hash(*args):
    """
    Return SHA256 has of the given arguements
    """
    stringified_args = sorted(map(lambda data: json.dumps(data), args))
    joined_data = ''.join(stringified_args)

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f"crypto_hash('one', 2, [3]): {crypto_hash('one', 2, [3])}")
    print(f"crypto_hash(2, [3], 'one'): {crypto_hash(2, [3], 'one')}")

if __name__ == '__main__':
    main()