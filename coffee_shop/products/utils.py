from mongoengine import fields

def dozens_validator(value):
    if value < 0:
        raise fields.ValidationError(message='positive integer only')