from rest_framework.views import APIView
import requests
from .detail import *
from rest_framework.response import Response

from .dictrict_code_info import *


class VahanView(APIView):

    def post(self, request, *args, **kwargs):
        print(request.FILES, request.POST)
        img_file = request.FILES['file']
        # print(type(img_file))
        # serializer = CarInfoSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #
        # b =serializer.data['number_photo']
        # #print(serializer.data)
        #
        regions = ['in']
        # #with open('1.jpg', 'rb') as fp:
        response = requests.post(
            'https://api.platerecognizer.com/v1/plate-reader/',
            data=dict(regions=regions),  # Optional
            files={'upload': img_file.read()},

            headers={'Authorization': 'Token xyz'})

        data = response.json()

        results = data.get('results')

        y = results[0]

        z = y.get('candidates')

        for temp in z:
            info = temp.get('plate')
            info2 = info.upper()
            # print(temp)

            state = info[0] + info[1]
            district = info[2] + info[3]
            x = district_code.get(state)
            if x:
                y = x
                state_name = y.get('name')
                t = y.get('no')
                y = t
                ex = y.get(district)
                if ex:
                    t = state_name, ex, info2
                    break
                elif ex is None:
                    t = state_name, "Nothing Found", info2
                    break
            else:
                t = "Nothing Found", "Nothing Found", info2

        return Response(t)


class VahanDetailView(APIView):

    def post(self, request, pk):
        
        return Response("sdsdsd")
