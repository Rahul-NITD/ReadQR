from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import ImageUpload

from .ReadQR.qr import decodeQR

@api_view(["POST"])
def api_home(req):
    if 'file' in req.data:
        file = req.data['file']
        try:
            img = ImageUpload.objects.create(image=file)
            return Response(readqr(img))
        except ValueError:
            return Response(data={"message": "No file Provided"})
    else:
        return Response(data={"message": "upload image with key 'file'"})

def readqr(img: ImageUpload):
    print(img.image.path)
    data = decodeQR(img.image.path)
    img.image.delete()
    img.delete()
    if data["error"]:
        return data
    return {
        "qr_codes": data["qr_codes"]
    }