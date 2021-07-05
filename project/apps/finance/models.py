from django.db import models
from datetime import date
from .managers import IPCManager
# Create your models here.

class IPC(models.Model):
    name = models.CharField('Name', max_length=100, unique=True)
    ytd = models.FloatField()
    monthly_varation = models.FloatField()
    period = models.DateField(null=True, blank=True)

    objects = IPCManager()

    def __str__(self) -> str:
        return self.name

class Broker(models.Model):
    name = models.CharField('Name', max_length=100, unique=True)

    @property
    def total_inversting(self):
        all = [obj.total_today for obj in self.purchaseorder_set.all()]
        return sum(all)

    def __str__(self) -> str:
        return self.name

class TypeInstrument(models.Model):
    name = models.CharField('Name', max_length=50, unique=True)
    url = models.CharField('URL', max_length=1000, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.name}'

class FinancialInstrument(models.Model):    
    name = models.CharField('Name', max_length=100, unique=True)
    description = models.CharField("Description", max_length=200)
    type_id = models.ForeignKey(TypeInstrument, on_delete=models.RESTRICT, null=True)

    @property
    def last_cotization(self):
        lst = CotizationFinancialIntrument.objects.filter(fin_id=self.id).last()
        return lst.cotization if lst is not None else 0

    def __str__(self) -> str:
        return self.name

class CotizationFinancialIntrument(models.Model):
    cotization = models.FloatField()
    date = models.DateField()
    fin_id = models.ForeignKey(FinancialInstrument, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{ self.fin_id.name }: { self.date } | { self.cotization }"

class PurchaseOrder(models.Model):
    number = models.CharField('Nro', max_length=10)
    date = models.DateField('Purchase Date')
    fin_id = models.ForeignKey( FinancialInstrument, on_delete=models.RESTRICT)
    quantity = models.FloatField('Qnt', default=0)
    price = models.FloatField('Price', default=0)
    brk_id = models.ForeignKey(Broker, on_delete=models.RESTRICT, null=True)    

    @property
    def days_until_purchase(self):
        if self.date is None:
            return 0

        dif = date.today() - self.date
        return dif.days
    
    @property
    def total(self):
        return round(self.quantity * self.price, 2)        
    
    @property
    def last_cotization_fn(self):        
        return self.fin_id.last_cotization
    
    @property
    def total_today(self):
        return round(self.last_cotization_fn * self.quantity)
    
    @property
    def benefit(self):
        return round(self.total_today - self.total, 2)

    @property
    def percent(self):
        return round( (self.benefit / self.total) * 100 ,2)
    
    @property
    def percent_estimate_mensual(self):
        if self.days_until_purchase == 0:
            return 0
            
        percent_day = self.percent / (self.days_until_purchase / 30)
        return round(percent_day, 2)
        
    def __str__(self) -> str:
        return self.number
