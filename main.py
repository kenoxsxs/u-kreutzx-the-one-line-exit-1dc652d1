"""Entry program: write one one-line resignation letter to entry.txt.

The line is a single UTF-8 text of 1-140 characters; the grader runs this
program twice and the two runs must write identical bytes.
"""

import hashlib
import os

TEXT = "I hereby resign, effective immediately. My two weeks' notice is this sentence. Please water my desk plant."

# Gate contract: entry.txt must be UTF-8 text of 1 to 140 characters,
# not only white space, on a single line.
assert 1 <= len(TEXT) <= 140, "resignation line must be 1-140 characters"
assert TEXT.strip(), "resignation line must not be only white space"
assert "\n" not in TEXT and "\r" not in TEXT, "resignation line must be a single line"


def main():
    # An empty env value is as unusable as a missing one; fall back to
    # "output" in both cases so the program never tries to create "".
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = TEXT.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Read back and verify the written bytes match the intended text.
    with open(path, "rb") as f:
        written = f.read()
    assert written == data, "entry.txt content mismatch"
    print(path)
    print(len(data))
    print(hashlib.sha256(data).hexdigest())


if __name__ == "__main__":
    main()
