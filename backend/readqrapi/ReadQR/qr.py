from pyzbar.pyzbar import decode, Decoded
from PIL import Image, UnidentifiedImageError

def decodeQR(imgPath: str):
    try:
        img = Image.open(imgPath)
        res = decode(img)
        return {
            "qr_codes": extractData(res),
            "error": False
        }
    except FileNotFoundError:
        return {"error": True, "errorData": "FileNotFound"}
    except UnidentifiedImageError:
        return {"error": True, "errorData": "Cannot Identify Image. Possible Incorrect type."}

def extractData(data):
    l = []
    for d in data:
        p = d.polygon[0]
        l.append({
            "content": d.data.decode(),
            "x": p.x,
            "y": p.y
        })
    return l