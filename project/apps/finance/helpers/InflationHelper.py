import ipdb
from .helper_base import HelperBase
from apps.finance.models import IPC

class InflationHelper(HelperBase):

    def update_table_ipc(self):        
        arr = self.df.to_numpy()  
        cnt = 0    
        for record in arr[0:-1]:
            name = record[0]
            increment = record[5]
            ytd = record[3]
            created = IPC.objects.create_if_not_exits(name, increment, ytd)
            if created:
                cnt += 1
