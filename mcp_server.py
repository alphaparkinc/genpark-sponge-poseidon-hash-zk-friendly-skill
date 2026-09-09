import sys
import json
from client import PoseidonHash

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "hash":
        pos = PoseidonHash(params.get("width", 3))
        return {"digest": str(pos.hash(params.get("inputs", [0])))}
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == '__main__':
    main()
