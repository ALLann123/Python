import base64

# List of Base64-encoded strings
encoded_strings = {
    "random": "KCAkU0hFTExpRFsxXSskc0hFTExJRFsxM10rJ1gnKQ==",
    "another_one": "KCAoIFtjSEFSW11dICg4NywgOTEsMjQsOTQgLCA2NSw4OSAsIDkyLDExNSwgMzggLCA4OCAsIDI4ICwyOCAsMTE1LCAxMDUgLCAyNCAsIDk1LCA4NSwgMTE1LCAzOCAsIDI5ICwgNzQsMTE1LCA4NSAsMjgsIDg5ICwgMTE1ICwgMTA5LCA5NSw3MSwxMTUgLCAzOCw2NSAsIDMxLCAxMTU=",
    "too_much": "LDIwICw3OCAsMjUsIDc5ICwgMjYsIDI0LCAyNSAsIDMwLDc4ICwgMjcgLCAzMSwyNCAsMjAsNzgsIDIxLDI1LDc5LDczLCA3MiAsNzMgLCAyNSwgMjgsMjQsIDc3LDc0ICw3NCwgMjQgLCAyMCAsMjggLCAyOSwgNzQsMjEsIDgxKSAK",
    "getting_boring": "fCBGb1JFYWNILW9CakVDdCB7IFtjSEFSXSgkXyAtQnhvUiAiMHgyQyIgKSB9ICkgLUpPaW4nJyAp"
}

# Decode each string
for key, encoded in encoded_strings.items():
    try:
        decoded = base64.b64decode(encoded).decode('utf-8')
        print(f"{key}:\n{decoded}\n")
    except Exception as e:
        print(f"Error decoding {key}: {e}\n")
