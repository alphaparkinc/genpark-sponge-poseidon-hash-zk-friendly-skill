import hashlib

PRIME = 21888242871839275222246405745257275088548364400416034343698204186575808495617

class PoseidonHash:
    """Poseidon ZK-friendly Algebraic Sponge Hash."""
    def __init__(self, width=3, rounds_f=4, rounds_p=8):
        self.width = width
        self.p = PRIME
        self.rounds_f = rounds_f
        self.rounds_p = rounds_p
        self.round_constants = [int(hashlib.sha256(f"C_{i}".encode()).hexdigest(), 16) % self.p for i in range(width * (rounds_f + rounds_p))]
        self.mds = [[(i + j + 1) for j in range(width)] for i in range(width)]

    def _sbox(self, x):
        return pow(x, 5, self.p)

    def hash(self, inputs):
        state = [0] * self.width
        for i, val in enumerate(inputs[:self.width]):
            state[i] = val % self.p

        rc_idx = 0
        total_rounds = self.rounds_f + self.rounds_p
        for r in range(total_rounds):
            for i in range(self.width):
                state[i] = (state[i] + self.round_constants[rc_idx]) % self.p
                rc_idx += 1

            if r < self.rounds_f // 2 or r >= self.rounds_f // 2 + self.rounds_p:
                state = [self._sbox(s) for s in state]
            else:
                state[0] = self._sbox(state[0])

            new_state = [0] * self.width
            for i in range(self.width):
                new_state[i] = sum(self.mds[i][j] * state[j] for j in range(self.width)) % self.p
            state = new_state

        return state[0]
