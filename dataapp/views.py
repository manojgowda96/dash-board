from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Data
from .serializers import DataSerializer

class DataList(generics.ListAPIView):
    serializer_class = DataSerializer
    

    def get_queryset(self):
        queryset = Data.objects.all()
        end_year = self.request.query_params.get('end_year')
        topic = self.request.query_params.get('topic')
        sector = self.request.query_params.get('sector')
        region = self.request.query_params.get('region')
        pestle = self.request.query_params.get('pestle')
        source = self.request.query_params.get('source')
        swot = self.request.query_params.get('swot')
        country = self.request.query_params.get('country')
        city = self.request.query_params.get('city')

        if end_year:
            queryset = queryset.filter(end_year=end_year)
        if topic:
            queryset = queryset.filter(topic_icontains=topic)
        if sector:
            queryset = queryset.filter(sector__icontains=sector)
        if region:
            queryset = queryset.filter(region__icontains=region)
        if pestle:
            queryset = queryset.filter(pest__icontains=pestle)
        if source:
            queryset = queryset.filter(source__icontains=source)
        if swot:
            queryset = queryset.filter(swot__icontains=swot)
        if country:
            queryset = queryset.filter(country__icontains=country)
        if city:
            queryset = queryset.filter(city_iconatins=city)
        
        return queryset

def index(request):
    return render(request, 'dataapp/index.html')