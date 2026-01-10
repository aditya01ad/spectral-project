# decode_ggb_fix.py
# Paste your Base64 string into the variable 'b64' below.
# Then run: python3 decode_ggb_fix.py

import base64, sys, zipfile
from pathlib import Path

# --------- PASTE YOUR BASE64 STRING HERE (keep triple quotes) ----------
b64 = """
UEsDBBQAAAAIAPV2els70Z9tAwEAAIMFAAAMAAAAZ2VvZ2VicmEueG1srdRbisMwEAbgX8Fz
7yH2kE7QJp2lC8R2tBEbiYpIJE2m4j997JdJWAlLKy99/H3k1Vt8klrQvjeE9D5YHKmSTuN3r
tLLR5dnqTWX1GPPLy9r3yOz4yV1WKaMqK5bFxjJLGlcpUxSBpT3O1xlkqyyEVcaYinFstVEs
pzrTbst6lsxJtZp1H6wHhpw42WxwPBFQn78FhBMNZ5bxEe6ozRPKXyFlMmSvnCMJHLHgnua+
0oVq+W4zzL5DZGU9xUBD8kUyXebLCBn52eH9z9+nlPpuglwzQYStffevvXlRuuCpbET4cB6b
tMCU37aZKAJEUUVS8TeRspp1BJ6ZZHdZpZ7TrCkVLNLEtLHCUjp1hxJxUZczkFcWs0cUZeJ
6nRDT8/nbdyH6WdT6PFCsp1mPs6C5TQ2TmzMajRqs7TqN+jlC7LNlT4Ciiu/wWgAQkYlxKxB
SwMEFAAAAAgA9XZ6WymVy8uHAQAAEQIAAAoAAABtZXRhLnhtbI2RwWrDMBBE7/uKec8y9GSc
QG3aBtIutgRbtpLY4BASpVv+/RZJ2ECFNTpj5sw5M7Ozsz+X2UIr6OZXqXm2OIzbvJr7uUj+
FKl1rsrUFSZTqC7plPz7kqcxgjXC7lyF3qmpwNTbNWoVqbzT4f4hIuGqF5tEENlIKhz2dWLK
ZKpFEsnMnqapExZSUaLN1F0YRRpUuKSK9UuChNIknbaUOaUOShtIW48GKlPclvtvrbgYFl/r
gOUfGG+PukQOuCwdZZU6yhCGGXBQ2QTNCx34KCijyBTvjjlBqvZks9z8nqu2g9Bq8W1A1BLB
QYAAAAAAQABADoAAAC9AQAAAAA=
"""  # replace with your Base64 string if different
# ---------------------------------------------------------------------

out_path = Path("K5_fixed_decoded.ggb")

def sanitize_and_fix_padding(s):
    # remove whitespace/newlines
    s = "".join(s.split())
    # switch URL-safe characters to standard base64 if present
    s = s.replace('-', '+').replace('_', '/')
    # pad with '=' to multiple of 4
    rem = len(s) % 4
    if rem:
        s += '=' * (4 - rem)
    return s

def try_decode(s):
    try:
        return base64.b64decode(s, validate=False)
    except Exception as e:
        raise RuntimeError(f"Base64 decode failed: {e}")

def main():
    s = sanitize_and_fix_padding(b64)
    try:
        binary = try_decode(s)
    except RuntimeError as e:
        print("Error:", e)
        sys.exit(1)

    try:
        out_path.write_bytes(binary)
        print(f"Written file: {out_path.resolve()}")
    except Exception as e:
        print("Error writing file:", e)
        sys.exit(1)

    # Validate as zip and show contents
    try:
        with zipfile.ZipFile(out_path, 'r') as z:
            names = z.namelist()
            print("GeoGebra (.ggb) archive contents (first 20 entries):")
            for n in names[:20]:
                print(" -", n)
            # Optional: extract geogebra.xml to inspect
            if "geogebra.xml" in names:
                print("\nPreview of geogebra.xml (first 400 chars):")
                with z.open("geogebra.xml") as g:
                    content = g.read(400).decode(errors='replace')
                    print(content)
            print("\nOK: file appears to be a valid ZIP/GeoGebra file.")
    except zipfile.BadZipFile:
        print("\nWarning: the file is NOT a valid ZIP archive. The Base64 may still be truncated or corrupted.")
    except Exception as e:
        print("Warning while validating ZIP:", e)

if __name__ == "__main__":
    main()
