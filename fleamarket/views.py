from django.db.models import Q
from rest_framework.views import APIView, Response

from fleamarket.models import FleaItem
from fleamarket.serializers import FleaItemSerializer


# Create your views here.
class FleaItemView(APIView):
    # 가져오기
    def get(self, request):
        q = request.query_params.get('q')
        if not q: return Response(status=400)
        results = FleaItem.objects.filter(
            Q(name__icontains=q) | Q(description__icontains=q)
        )
        serializer = FleaItemSerializer(results, many=True)
        return Response(serializer.data)

    # 등록
    def put(self, request):
        serializer = FleaItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    # 구매
    def post(self, request, pk):
        id = request.query_params.get('q')
        item = FleaItem.objects.get(pk=pk)