#coding=utf-8
from django.db import models
from datetime import datetime

class USER(models.Model):
	# name_ID = models.AutoField(max_length=11)
	name = models.CharField(max_length=20)
	password = models.IntegerField(max_length=20)
	email = models.CharField(max_length=20)

class GOODS(models.Model):
	# Goods_ID = models.AutoField(max_length=10)
	Goods_Name = models.CharField(max_length=20)
	Goods_Type = models.CharField(max_length=20)
	Goods_Price = models.FloatField()
	Goods_Units = models.CharField(max_length=20)
	Goods_Content = models.CharField(max_length=50)
	Goods_num = models.IntegerField(max_length=10)
	Goods_url = models.CharField(max_length=100)

class CAR(models.Model):
	# Car_ID = models.IntegerField(max_length=10)
	goods_id = models.ForeignKey('GOODS')
	Car_CountNum = models.IntegerField(max_length=10)

class BALANCE(models.Model):
	# Balance_ID = models.AutoField()
	address_ID = models.ForeignKey('ADDRESS')
	car_id = models.ForeignKey('CAR')
	Balance_SumNum = models.IntegerField(max_length=10)
	Balance_SumPrice = models.FloatField()
	Balance_PayPrice = models.FloatField()



class ADDRESS(models.Model):
	# Detail_ID = models.AutoField()
	Detail_Introduce = models.CharField(max_length=50)
	Detail_Comment = models.CharField(max_length=50)
	Detail_love = models.IntegerField(max_length=10)

class ORDERS(models.Model):
	# Orders_ID = models.AutoField()
	Orders_CreateTime = models.DateTimeField()
	Orders_Num = models.IntegerField(max_length=10)
	Orders_Pay = models.BooleanField(default=False)
	Orders_SumPrice = models.FloatField()
	car_id = models.ForeignKey('CAR')
	balance_id = models.ForeignKey('BALANCE')

# class DETAIL(models.Model):
# 	Detail_ID = models.AutoField()
# 	Detail_Introduce = models.CharField(max_length=50)
# 	Detail_Comment = models.CharField(max_length=50)
	# Detail_love = models.IntegerField(max_length=10)


