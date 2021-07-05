from django.db import models


class IPCManager(models.Manager):

    def create_if_not_exits(self, name, increment, ytd):
        print(f'Create new element {name} {increment}')
        obj = self.filter(name=name)        
        if obj.count() == 0:
            self.create(name=name, monthly_varation=self.format_float(increment), ytd=self.format_float(ytd))
            return True
        
        return False
    
    def format_float(self, value:str):
        return float(value.replace('%', '').replace(',', '.'))        
