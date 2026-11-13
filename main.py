"""Write the entry's picture to $MAKEFUN_OUTPUT_DIR (or /output) as entry.png."""
import hashlib, os, pathlib, shutil, sys

MAX_BYTES = 1048576
SRC = pathlib.Path(__file__).resolve().parent / "asset" / "entry.png"


def main() -> int:
    if not SRC.is_file():
        print(f"asset missing: {SRC}", file=sys.stderr)
        return 1
    payload = SRC.read_bytes()
    if not payload or len(payload) > MAX_BYTES:
        print(f"asset is {len(payload)} bytes, the gate allows {MAX_BYTES}", file=sys.stderr)
        return 1
    out_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SRC, target)
    print(f"wrote {target} ({len(payload)} bytes, sha256:{hashlib.sha256(payload).hexdigest()[:16]})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
