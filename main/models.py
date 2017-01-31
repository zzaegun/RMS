from django.db import models
from django.utils import timezone

class T_PROD_TYPE(models.Model):
	ITEM_ID = models.IntegerField(db_index=True, primary_key=True)
	ITEM_NAME = models.CharField(max_length=10)

	class Meta:
		db_table = 'T_PROD_TYPE'

class T_PROD_MACHINE(models.Model):
	MACHINE_ID = models.IntegerField(db_index=True, primary_key=True)
	MACHINE_NAME = models.CharField(max_length=10)

	class Meta:
		db_table = 'T_PROD_MACHINE'

class T_ORDER_INFO(models.Model):
	ORDER_ID = models.IntegerField(db_index=True, primary_key=True)
	ORDER_DATE = models.IntegerField(default = 0)
	ITEM_ID = models.ForeignKey(T_PROD_TYPE, on_delete=models.CASCADE)
	ORDER_QTY = models.IntegerField(default = 0)
	ORDER_FIN = models.BooleanField(default = True)
	
	class Meta:
		db_table = 'T_ORDER_INFO'

class T_PROD_PROCESS(models.Model):
	PROCESS_ID = models.IntegerField(db_index=True, primary_key=True)
	PROCESS_ORDER = models.IntegerField(default=0)
	PROCESS_NAME = models.CharField(max_length=10)
	ITEM_ID = models.ForeignKey(T_PROD_TYPE, on_delete=models.CASCADE)

	class Meta:
		db_table = 'T_PROD_PROCESS'

class T_MACHINE_STATUS(models.Model):
	MACHINE_ID = models.OneToOneField(T_PROD_MACHINE, primary_key=True, on_delete=models.CASCADE)
	MACHINE_MTR = models.DateTimeField(auto_now_add = False, null=True)
	MACIHNE_LOAD = models.IntegerField(default=0)
	MACHINE_LT = models.IntegerField(default=0)
	MACHINE_CAPA = models.IntegerField(default=0)
	MCAHINE_SCHED = models.DateTimeField(auto_now_add = False, null=True)
	
	class Meta:
		db_table = 'T_MACHINE_STATUS'

class T_PROD_SCHEDULE(models.Model):
	SCHEDULE_ID = models.IntegerField(db_index=True, primary_key=True)
	ORDER_ID = models.ForeignKey(T_ORDER_INFO, on_delete=models.CASCADE)
	UPDATE_TIME = models.DateTimeField(auto_now_add = True, null=True)
	PROD_SCHED = models.DateTimeField(auto_now_add = False,null=True)
	PROCESS_ID = models.ForeignKey(T_PROD_PROCESS, on_delete=models.CASCADE)
	MACHINE_ID = models.ForeignKey(T_PROD_MACHINE, on_delete=models.CASCADE)
	MACHINE_QTY =models.IntegerField(default = 0)
	#url = models.EmailField()
	#email = models.TextField()

	class Meta:
		db_table = 'T_PROD_SCHEDULE'









