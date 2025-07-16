from django.db.models import Q
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated

from fleamarket.models import FleaItem
from fleamarket.serializers import FleaItemSerializer


# Create your views here.
class FleaItemView(APIView):
    permission_classes = [IsAuthenticated]
    # 가져오기
    def get(self, request):
        id = request.query_params.get('id')
        if id: results = FleaItem.objects.filter(pk=id)
        else:
            q = request.query_params.get('q')
            s = request.query_params.get('s')
            if s == 'sold': results = FleaItem.objects.filter(
                (Q(name__icontains=q) | Q(description__icontains=q))
            ).exclude(is_sold__exact=False) if q else FleaItem.objects.all().exclude(is_sold__exact=False)
            elif s == 'selling': results = FleaItem.objects.filter(
                (Q(name__icontains=q) | Q(description__icontains=q))
            ).exclude(is_sold__exact=True) if q else FleaItem.objects.all().exclude(is_sold__exact=True)
            else: results = FleaItem.objects.filter(
                Q(name__icontains=q) | Q(description__icontains=q)
            ) if q else FleaItem.objects.all()

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
    def post(self, request):
        id = request.query_params.get('q')
        item = FleaItem.objects.get(pk=id)
        if not item or item.is_sold: return Response(status=404)
        item.is_sold = True
        item.save()
        return Response(status=200)

    # 삭제
    def delete(self, request):
        id = request.query_params.get('q')
        item = FleaItem.objects.get(pk=id)
        if not item: return Response(status=404)
        item.delete()
        return Response(status=200)