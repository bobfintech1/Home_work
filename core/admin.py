from django.contrib import admin
from core.models import home, portfolio, services, vacancy

admin.site.register(home.InfoPageModel)
admin.site.register(home.StatsModel)
admin.site.register(home.CarouselModel)

admin.site.register(portfolio.PortfolioModel)
admin.site.register(services.ServicesModel)
#nur
admin.site.register(vacancy.VacancyModel)
