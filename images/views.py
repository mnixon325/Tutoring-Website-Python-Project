import imghdr
from uuid import uuid4
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView

from images.models import UploadedImage
from images.serializers import UploadedImageSerializer


class UploadedImagesView(APIView):
    queryset = UploadedImage.objects.all()
    serializer_class = UploadedImageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request):
        file = request.FILES.get('imagefile', False)
        if file:
            if imghdr.what(file) == 'jpeg':
                filename = random_name_jpg()
                file.name = filename

                upload = UploadedImage.objects.create(
                    user=request.user,
                    path_to_image=filename,
                    imagefile=file)
                upload.save()
                return Response({"filename": filename}, status=status.HTTP_201_CREATED)

            return Response({"details": "File has to be in jpeg (.jpg, .JPG)"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"details": "No file received"}, status=status.HTTP_400_BAD_REQUEST)


def random_name_jpg():
    return "{}.{}".format(uuid4(), 'jpg')