from django.contrib import admin
from .models import PurchaseOrder, FinancialInstrument, Broker, \
                        CotizationFinancialIntrument, TypeInstrument, \
                        IPC
from django.db import models
from django.forms.widgets import TextInput
from django.contrib import admin
from .helpers.CotizationHelper import SearchCotizationIntrument
from django.contrib import messages
from admincharts.admin import AdminChartMixin

from datetime import date
# Register your models here.

@admin.register(IPC)
class IPCAdmin(AdminChartMixin, admin.ModelAdmin):
    list_chart_type = "line"
    # list_chart_data = {}
    list_chart_options = {"aspectRatio": 2}
    # list_chart_config = None
    list_display = ('name', 'ytd', 'monthly_varation', 'period')    

    def get_list_chart_data(self, queryset):
        # import ipdb; ipdb.set_trace()
        if not queryset:
            return {}        

        labels = []
        totals = []
        for record in queryset:
            labels.append(record.name)
            totals.append(record.monthly_varation * 10)

        return {
            "labels": labels,
            "datasets": [
                {"label": "IPC", "data": totals, "backgroundColor": "#79aec8"},
            ],
        }
    
@admin.register(FinancialInstrument)
class FinancialInstrumentAdmin(admin.ModelAdmin):
    readonly_fields = ['last_cotization']
    list_display = ('id', 'name', 'description', 'type_id', 'last_cotization')
    search_fields = ('name',)
    list_filter = ['type_id']
    search_fields = ['name']
    list_editable = ['type_id']

    actions = ['update_cotization']

    @admin.action(description='Update Cotization')
    def update_cotization(self, request, queryset):
        searchs = {}
        type_instrument = TypeInstrument.objects.all()
        for typ in type_instrument:
            if typ.url is not None: 
                searchs[typ.name] = SearchCotizationIntrument(typ.url)

        for elem in queryset:   
            if elem.type_id.url is not None:         
                search = searchs[elem.type_id.name]
                cotiz = search.search(elem.name)
                CotizationFinancialIntrument.objects.create(fin_id=elem, date=date.today(), cotization=cotiz)                       

        self.message_user(request, f"Se han actualizado {queryset.count()} instrumentos", messages.SUCCESS)
    

@admin.register(TypeInstrument)
class TypeInstrumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')


@admin.register(Broker)
class BrokerAdmin(admin.ModelAdmin):
    readonly_fields = ['total_inversting']
    list_display = ('id', 'name', 'total_inversting')
    search_fields = ('name',)
    

@admin.register(CotizationFinancialIntrument)
class CotizationFinancialIntrumentAdmin(admin.ModelAdmin):
    list_display = ('id','fin_id', 'date', 'cotization')
    totalsum_list = ('cotization')
    unit_of_measure = '&euro;'

@admin.register(PurchaseOrder)
class PurcharseOrderAdmin(admin.ModelAdmin):
    readonly_fields = ('days_until_purchase', 'total', 'last_cotization_fn', 'total_today', 'benefit', 'percent', 'percent_estimate_mensual')
    list_display = ('number', 'date', 'fin_id', 'brk_id', 'total', 'days_until_purchase', 'last_cotization_fn', 'total_today', 'benefit', 'percent', 'percent_estimate_mensual')
    fields = (
        ('number', 'date', 'days_until_purchase'),
        ('brk_id', 'fin_id',),
        ('quantity', 'price',),
        ('total', 'last_cotization_fn'),
        ('total_today', 'benefit', 'percent', 'percent_estimate_mensual')       
    )    
    autocomplete_fields = ['fin_id', 'brk_id' ]
    list_filter = ['fin_id', 'brk_id' ]    

    formfield_overrides = {
        models.FloatField: {'widget': TextInput(attrs={'style': 'text-align:right;'})}
    }

    def suit_row_attributes(self, obj, request):
        import ipdb; ipdb.set_trace()
        return {'class': 'type-%s' % obj.type}

    
