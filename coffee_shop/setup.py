import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coffee_shop.settings')
django.setup()


def main():
    from products.documents import CoffeeMachine, CoffeePod
    CoffeeMachine.objects.create(type_='LRG', classification='BAS', water_compatible=True)
    CoffeeMachine.objects.create(type_='LRG', classification='PRM', water_compatible=True)
    CoffeeMachine.objects.create(type_='SML', classification='BAS', water_compatible=False)
    CoffeeMachine.objects.create(type_='SML', classification='PRM', water_compatible=False)
    CoffeeMachine.objects.create(type_='SML', classification='DLX', water_compatible=False)
    CoffeeMachine.objects.create(type_='ESP', classification='BAS', water_compatible=True)
    CoffeeMachine.objects.create(type_='ESP', classification='DLX', water_compatible=True)

    CoffeePod.objects.create(type_='LRG', flavor="VAN", dozen_count=5)
    CoffeePod.objects.create(type_='LRG', flavor="CAR", dozen_count=3)
    CoffeePod.objects.create(type_='LRG', flavor="MOC", dozen_count=1)
    CoffeePod.objects.create(type_='SML', flavor="PSL", dozen_count=3)
    CoffeePod.objects.create(type_='SML', flavor="HAZ", dozen_count=5)
    CoffeePod.objects.create(type_='SML', flavor="CAR", dozen_count=5)
    CoffeePod.objects.create(type_='ESP', flavor="VAN", dozen_count=9)
    CoffeePod.objects.create(type_='ESP', flavor="MOC", dozen_count=5)
    CoffeePod.objects.create(type_='ESP', flavor="HAZ", dozen_count=1)


if __name__ == '__main__':
    main()
