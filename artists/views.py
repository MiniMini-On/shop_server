import pandas as pd
import random
import string
from .models import Artist
from django.http import HttpResponse

"""
db값 추가
"""

def dbsaveView(request):

    db = pd.read_csv('../oround_data.csv',encoding='cp949' )

    temp = []
    for i in range(0,120):
        temp.append(db['artist'][i])
    print(temp)
    
    last=['김','이','박','최']
    first=['미','성','다','경', '은', '빈', '인', '섭', '훈', '양', '예', '림']     

        
    for i in list(set(temp)):
        name = f'{random.choice(last)}{random.choice(first)}{random.choice(first)}'
        phone = '010'

        for j in range(8) :
            phone += random.choice(string.digits)
            
        email = ''
        for k in range(8) :
            email += random.choice(string.ascii_lowercase)
        email += random.choice(['@naver.com','@gmail.com','@hanmail.net'])
        Artist.objects.create(name=name , nickname=i, phone=phone, email=email)
    return HttpResponse('새로운 data가 저장되었습니다')   

    
def dbPkResetView(request):
    records = Artist.objects.all()
    index = 1
    for record in records:
        old_record = Artist.objects.get(id=record.id)
        record.id = index
        old_record.delete()
        record.save()        
        index = index + 1
    return HttpResponse('pk 값이 reset되었습니다.')