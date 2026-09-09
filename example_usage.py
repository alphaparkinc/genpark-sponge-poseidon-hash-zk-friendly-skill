from client import PoseidonHash

def main():
    print("=== Testing Poseidon ZK-Friendly Hash ===")
    pos = PoseidonHash(width=3)
    h1 = pos.hash([42, 99])
    h2 = pos.hash([42, 99])
    h3 = pos.hash([42, 100])

    print("Poseidon([42, 99]) =", h1)
    assert h1 == h2
    assert h1 != h3

    print("Poseidon Hash verified successfully!")

if __name__ == '__main__':
    main()
