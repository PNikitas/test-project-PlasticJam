import os
import json

from django.core.management.base import BaseCommand
from datetime import datetime
from test_project_PlasticJam.settings import BASE_DIR

from users.models import Statistic


class Command(BaseCommand):
    def json_to_db(self):
        data_folder = os.path.join(BASE_DIR, 'users', 'data')
        
        for data_file in os.listdir(data_folder):
            with open(os.path.join(data_folder, data_file), encoding='utf-8') as data_file:
                data = json.loads(data_file.read())

                for data_object in data:
                    user_id = data_object.get('user_id', None)
                    date = data_object.get('date', None)
                    page_views = data_object.get('page_views', None)
                    clicks = data_object.get('clicks', None)

                    try:
                        statistic, created = Statistic.objects.get_or_create(
                            user_id=user_id,
                            date=date,
                            page_views=page_views,
                            clicks=clicks,
                        )

                        if created:
                            statistic.save()
                            print(f'\nStatistic {statistic} has been already saved.')
                    
                    except Exception as ex:
                        print(f'\n\nSomething went wrong saving this statistic: {user_id}\n{str(ex)}')

    def handle(self, *args, **kwargs):
        self.json_to_db()