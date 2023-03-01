import pandas as pd
import random
from .models import Product
from django.http import HttpResponse, Http404
from rest_framework.views    import APIView
from . import serializers
from rest_framework.response import Response


class ProductsView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = serializers.ProductsSerializer(products, many=True)
        return Response(serializer.data)

class ProductView(APIView):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            serializer = serializers.ProductSerializer(product)
            
            return Response(serializer.data)
        except Product.DoesNotExist:
                raise Http404("product does not exist")
            


"""
db값 추가
"""
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
import os
ROOT_DIR = os.path.dirname(BASE_DIR)
SECRET_BASE_FILE = os.path.join(BASE_DIR, 'oround_data.csv')

def dbsaveView(request):

    db = pd.read_csv(SECRET_BASE_FILE,encoding='cp949' )

    for i in range(0,len(db)):
        name = db['name'][i].replace('#',',')
        category_id = 1
        theme_id=random.choice([1,2,3,4])
        artist_id = random.randrange(1,62)
        option_id = 1
        price = int(db['price'][i].replace('#',''))
        stock = random.randrange(1,101)
        hits = random.randrange(1,501)
        image1 = db['img1'][i].replace('#',',')
        image2 = db['img2'][i].replace('#',',')
        Product.objects.create(name=name , category_id=category_id, theme_id=theme_id, artist_id=artist_id,option_id=option_id,price=price,stock=stock,hits=hits,image1=image1,image2=image2)
    return HttpResponse('새로운 data가 저장되었습니다')  
     

def dbPkResetView(request):
    records = Product.objects.all()
    index = 1
    for record in records:
        old_record = Product.objects.get(id=record.id)
        record.id = index
        old_record.delete()
        record.save()        
        index = index + 1
    return HttpResponse('pk 값이 reset되었습니다.')