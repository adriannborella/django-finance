from django.core.management.base import BaseCommand, CommandError
from apps.finance.helpers.InflationHelper import InflationHelper
from apps.finance.models import IPC

class Command(BaseCommand):
    help = "Search the information in web and update the IPC's table"

    def handle(self, *args, **options):
        url = 'https://datosmacro.expansion.com/ipc-paises/argentina?sc=IPC-IG'
        helper = InflationHelper(url)
        cnt_new = helper.update_table_ipc() or 0
        self.stdout.write(self.style.SUCCESS(f"It's load {cnt_new} new register"))      
