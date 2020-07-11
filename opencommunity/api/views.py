
# Create your views here.
# views.py
from rest_framework import viewsets
from .serializers import HeroSerializer
from .models import Hero


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer



# def logout_request(request):
#     logout(request)
#     messages.info(request, "Logged out successfully!")
#     return redirect("main:homepage")


# @csrf_exempt
# def register(request):
#     form = UserCreationForm
#     return render(request=request,
#                   template_name="main/register.html",
#                   context={"form": form})
#

# @api_view(['POST'])
# # @csrf_exempt
# class UserCreateAPIView(viewsets.ModelViewSet):
#     # serialized = UserSerializer(data=request.data)
#     # if serialized.is_valid():
#     #     User.objects.create_user(
#     #         serialized.save()
#     #     )
#     #     return Response(serialized.data, status=status.HTTP_201_CREATED)
#     # else:
#     #     return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (AllowAny,)
