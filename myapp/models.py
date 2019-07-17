from django.db import models
from random import *
from datetime import datetime

class Bus(models.Model):
    
    category_choices=(
        ('AC sleeper','AC sleeper'),
        ('Non-AC sleeper','Non-AC sleeper'),
        ('AC Multi Axle Semi sleeper','AC Multi Axle Semi sleeper'),
        ('AC seater','AC seater'),
        ('Super Luxery','Super Luxery'),
        ('Deluxe','Deluxe')
    )

    source=models.CharField(max_length=30)
    category=models.CharField(max_length=30,choices=category_choices)
    bus_no=models.CharField(max_length=30)

    def __str__(self):
        return self.bus_no

class User(models.Model):
    category_choices=(
        ('Elite','Elite'),
        ('Premium','Premium'),
        ('Normal','Normal')
    )
    u=''
    for i in range(0,4):
        u=u+str(randint(0,9))
    Passenger_name=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    category=models.CharField(max_length=30,choices=category_choices)
    pid=models.IntegerField(default=u)

    def __str__(self):
        return self.Passenger_name

class Elite(models.Model):
    category_choices=(
        ('AC sleeper','AC sleeper'),
        ('Non-AC sleeper','Non-AC sleeper'),
        ('AC Multi Axle Semi sleeper','AC Multi Axle Semi sleeper'),
        ('AC seater','AC seater')
    )

    places=(
        ('HYDERABAD','HYDERABAD'),
        ('BANGOLORE','BANGOLORE'),
        ('VISAKHAPATNAM','VISAKHAPATNAM'),
        ('VIJAYAWADA','VIJAYAWADA'),
        ('GUNTUR','GUNTUR'),
        ('TIRUPATHI','TIRUPATHI')
    )

    low=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10')
    )

    up=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10')
    )

    seat=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10')
    )
    
    source=models.CharField(max_length=30,choices=places)
    destination=models.CharField(max_length=30,choices=places)
    depature=models.DateTimeField()
    category=models.CharField(max_length=30,choices=category_choices)
    bus_no=models.ForeignKey(Bus,on_delete=models.CASCADE,default='')
    seat_no=models.CharField(max_length=30,choices=seat,default='')
    Psname=models.ForeignKey(User,on_delete=models.CASCADE,default='')
    
class Pre(models.Model):
    category_choices=(
        ('Non-AC sleeper','Non-AC sleeper'),
        ('AC Multi Axle Semi sleeper','AC Multi Axle Semi sleeper'),
        ('AC seater','AC seater')
    )
    places=(
        ('HYDERABAD','HYDERABAD'),
        ('BANGOLORE','BANGOLORE'),
        ('VISAKHAPATNAM','VISAKHAPATNAM'),
        ('VIJAYAWADA','VIJAYAWADA'),
        ('GUNTUR','GUNTUR'),
        ('TIRUPATHI','TIRUPATHI')
    )
    seat=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10')
    )

    source=models.CharField(max_length=30,choices=places)
    destination=models.CharField(max_length=30,choices=places)
    depature=models.DateTimeField()
    category=models.CharField(max_length=30,choices=category_choices)
    bus_no=models.ForeignKey(Bus,on_delete=models.CASCADE,default='')
    seat_no=models.CharField(max_length=30,choices=seat,default='')
    Psname=models.ForeignKey(User,on_delete=models.CASCADE,default='')
    
class Nor(models.Model):

    category_choices=(
        ('Super Luxery','Super Luxery'),
        ('Deluxe','Deluxe'),
        ('AC seater','AC seater')
    )

    places=(
        ('HYDERABAD','HYDERABAD'),
        ('BANGOLORE','BANGOLORE'),
        ('VISAKHAPATNAM','VISAKHAPATNAM'),
        ('VIJAYAWADA','VIJAYAWADA'),
        ('GUNTUR','GUNTUR'),
        ('TIRUPATHI','TIRUPATHI')
    )

    seat=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10')
    )

    source=models.CharField(max_length=30,choices=places)
    destination=models.CharField(max_length=30,choices=places)
    depature=models.DateTimeField()
    category=models.CharField(max_length=30,choices=category_choices)
    bus_no=models.ForeignKey(Bus,on_delete=models.CASCADE,default='')
    seat_no=models.CharField(max_length=30,choices=seat,default='')
    Psname=models.ForeignKey(User,on_delete=models.CASCADE,default='')