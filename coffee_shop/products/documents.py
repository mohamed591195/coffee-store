from mongoengine import Document, fields
from .utils import dozens_validator

TYPES = (
    ('LRG', 'Large'),
    ('SML', 'Small'),
    ('ESP', 'ESPRESSO')
)


class CoffeeMachine(Document):

    CLASSIFICATION_TYPES = (
        ('BAS', 'Base'),
        ('PRM', 'Premium'),
        ('DLX', 'Deluxe'),
    )
    type_ = fields.StringField(max_length=3, choices=TYPES)
    water_compatible = fields.BooleanField()
    classification = fields.StringField(max_length=3, choices=CLASSIFICATION_TYPES)
    sku_code = fields.StringField()

    def save(self, *args, **kwargs):

        if not self.sku_code:
            switcher = {
                'LRG': 'CM10',
                'SML': 'CM00',
                'ESP': 'EM00',
                'BAS': '1',
                'PRM': '2',
                'DLX': '3',
            }
            self.sku_code = f'{switcher[self.type_]}{switcher[self.classification]}'
        return super().save(*args, **kwargs)
            


class CoffeePod(Document):
    FLAVORS = (
        ('VAN', 'Vanilla'),
        ('CAR', 'CARAMEL'),
        ('PSL', 'PSL'),
        ('MOC', 'Mocha'),
        ('HAZ', 'Hazelnut')
    )
    type_ = fields.StringField(max_length=3, choices=TYPES)
    flavor = fields.StringField(max_length=3, choices=FLAVORS)
    dozen_count = fields.IntField(validation=dozens_validator)
    sku_code = fields.StringField()

    def save(self, *args, **kwargs):

        if not self.sku_code:
            switcher = {
                'LRG': 'CP1',
                'SML': 'CP0',
                'ESP': 'EP0',
                'VAN': '0',
                'CAR': '1',
                'PSL': '2',
                'MOC': '3',
                'HAZ': '4'
            }
            self.sku_code = f'{switcher[self.type_]}{switcher[self.flavor]}{self.dozen_count}'
        return super().save(*args, **kwargs)

