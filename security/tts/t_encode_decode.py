import json
from security.dff_security_engine import SecurityEngine as DFF_Security

#from security.dff_security_engine import DFF_Security as DFF_Security




def t1():
    ds = DFF_Security()

    jwt_info = {

            "sub": "1234567890",
            "name": "Muchen",
            "intelligence": "unbelievably high",
            "iat": 1516239022

    }

    token = ds.encode_token(jwt_info)
    print("t1: Encoded token = ", token)


def t2():
    ds = DFF_Security()

    # Used JWT.io to encode using secret.

    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6Ik11Y2hlbiIsImludGVsbGlnZW5jZSI6InVuYmVsaWV2YWJseSBoaWdoIiwiaWF0IjoxNTE2MjM5MDIyfQ.5zwtjvG_EMlos4qOvAXIMHrnqQ1VTj6SqBIqWH_sA6s"

    d = ds.decode_token(token)

    print("t2 decode = \n", json.dumps(d, indent=2))


if __name__ == "__main__":
    t1()
    t2()
