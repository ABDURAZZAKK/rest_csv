import csv
import io

from django.db.utils import IntegrityError
from django.forms import model_to_dict

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from .models import Customer, Deal, Gem



class DealsCSVParseAPIView(APIView):
    parser_classes = (MultiPartParser, )

    def get(self, request): 
        try:
            customers = Customer.objects.all().order_by('-spent_money')[:5]
            result = []
            for cust in customers:
                cust_j = model_to_dict(cust)
                cust_j['gems'] = [model_to_dict(x) for x in cust_j['gems']]
                result.append(cust_j)
            return Response({'response':result,'status': 'OK'}) 
        except Exception as e:
            return Response({'status': f'Error, Desc: <{e}>'}) 

    def post(self, request, format='csv'):
        try:
            with io.TextIOWrapper(request.FILES['file'], encoding="utf-8", newline='\n') as file:
                csv_r = csv.reader(file)
                next(csv_r)
                deals_count = 0
                for row in csv_r:
                    try:
                        Deal.objects.create(
                                customer=row[0],
                                item = row[1],
                                total = row[2],
                                quantity = row[3],
                                date = row[4],
                            )
                    except IntegrityError:
                        continue
                    
                    deals_count+=1
                    gem = Gem.objects.get_or_create(name=row[1])[0]
                    customer = Customer.objects.get_or_create(username=row[0])[0]
                    customer.spent_money+=int(row[2])
                    customer.gems.add(gem)
                    customer.save()

            return Response({'status': f'OK - файл был обработан без ошибок, {deals_count} сделок добавленно;'})
        except Exception as e:
                    print(e)
                    return Response({'status': f'Error, Desc: <{e}> - в процессе обработки файла произошла ошибка.'})