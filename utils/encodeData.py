import base64


def encodeStr(str):
    str_bytes = str.encode("ascii")

    base64_bytes = base64.b64encode(str_bytes)
    base64_string = base64_bytes.decode("ascii")

    print(base64_string)

    return base64_string


encodeStr("5e54a6da-d4f8-3fee-a749-430ea39ec848:9f038bb12a293ca9")
