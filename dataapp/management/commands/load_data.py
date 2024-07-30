import json
from django.core.management.base import BaseCommand
from dataapp.models import Data
from datetime import datetime

class Command(BaseCommand):
    help = 'Load data from JSON file'

    def handle(self, *args, **kwargs):
        
        def safe_int(value,default=None):
             try:
                  return int(value)
             except(TypeError,ValueError):
                  return default

        with open('/Users/manojgowda/Desktop/blackcoffer/mydashboard/jsondata.json',encoding='utf8') as file:
            data = json.load(file)
            # print(data)

            for item in data:
                    try:
                        data=Data(
                            intensity=safe_int(int(item.get('intensity',0))),
                            likelihood=safe_int(int(item.get('likelihood',0))),
                            relevance=safe_int(int(item.get('relevance',0))),
                            end_year=safe_int(item.get('end_year',)), 
                            country=item.get('country',""),
                            topic=item.get('topic',""),
                            region=item.get('region'),
                            # city = item.get('city'),
                            sector = item.get('sector',""),
                            insight = item.get('insight',""),
                            url = item.get('url',""),
                            start_year = safe_int(item.get('start_year')),
                            impact = item.get('impact',""),
                            pestle = item.get('pestle',"") ,
                            source = item.get('source',"") ,
                            title = item.get('title',"") ,
                            # Convert date strings to datetime objects
                            added = datetime.strptime(item['added'], '%B, %d %Y %H:%M:%S'),
                            published = datetime.strptime(item['published'],'%B, %d %Y %H:%M:%S'),
                        )
                         
                    
                        data.save()
                        self.stdout.write(self.style.SUCCESS(f'Data "{data.title}" loaded successfully'))
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'Errorloadingdata:{e}'))
                         
                
                        


                
                

                    # intensity = int(intensity) if isinstance(intensity, (int, float)) or str(intensity).isdigit() else 0
                    # likelihood = int(likelihood) if isinstance(likelihood, (int, float)) or str(likelihood).isdigit() else 0
                    # relevance = int(relevance) if isinstance(relevance, (int, float)) or str(relevance).isdigit() else 0
                    # year = int(year) if isinstance(year, (int, float)) or str(year).isdigit() else year

                    # Data.objects.create(
                         
                    #     intensity=intensity,
                    #     likelihood=likelihood,
                    #     relevance=relevance,
                    #     year=year,
                    #     country=country,
                    #     topic=topics,
                    #     region=region,
                    # )
                    # Create the Data object
                #     Data.objects.create(
                #     intensity=intensity,
                #     likelihood=likelihood,
                #     relevance=relevance,
                #     year=year,
                #     country=country,
                #     topic=topics,
                #     region=region,
                #     city=city,
                #     end_year=end_year,
                #     sector=sector,
                #     insight=insight,
                #     url=url,
                #     start_year=start_year,
                #     impact=impact,
                #     added=added,
                #     published=published,
                #     pestle=pestle,
                #     source=source,
                #     title=title
                # )

        
        