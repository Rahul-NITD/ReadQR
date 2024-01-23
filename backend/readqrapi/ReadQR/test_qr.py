from pyzbar.pyzbar import decode
from qr import decodeQR 


def test_OneQR():
    path = "./test_images/qr.png"
    res = decodeQR(path)
    assert res == {
        "error": False,
        "qr_codes": [
            {
                "content": "http://en.m.wikipedia.org",
                "x": 29,
                "y": 25
            }
        ]
    }

def test_TwoQR():
    path = "./test_images/qr_2.png"
    res = decodeQR(path)
    assert res == {
        "error": False,
        "qr_codes": [
            {
                'content': 'Thalassiodracon', 
                'x': 173, 
                'y': 113
            }, 
            {
                'content': 'Thalassiodracon', 
                'x': 31, 
                'y': 354
            }
        ]
    }

def test_NoQR():
    path = "./test_images/noqr.png"
    res = decodeQR(path)
    assert res == {
        "error": False,
        "qr_codes": []
    }

def test_IncorrectType():
    path = "./test_images/qr-test.svg"
    res = decodeQR(path)
    assert res == {
        "error": True, 
        "errorData": "Cannot Identify Image. Possible Incorrect type."
    }