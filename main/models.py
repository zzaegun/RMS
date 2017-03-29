from django.db import models
from django.utils import timezone

class T_PROD_PROCESS(models.Model):
	PROCESS_ID = models.IntegerField(db_index=True, primary_key=True)
	SUBPROC_ORDER = models.TextField()
	PROCESS_NAME = models.CharField(max_length=10)
	class Meta:
		db_table = 'T_PROD_PROCESS'


class T_PROD_TYPE(models.Model):
	ITEM_ID = models.IntegerField(db_index=True, primary_key=True)
	ITEM_NAME = models.CharField(max_length=10)
	PROCESS_ID = models.ForeignKey(T_PROD_PROCESS, on_delete=models.CASCADE, default=1)
	class Meta:
		db_table = 'T_PROD_TYPE'

class T_SUB_PROCESS(models.Model):
	SUBPROC_ID = models.IntegerField(db_index=True, primary_key=True)
	SUBPROC_NAME = models.CharField(max_length=10)

	class Meta:
		db_table = 'T_SUB_PROCESS'

class T_ORDER_INFO(models.Model):
	ORDER_ID = models.IntegerField(db_index=True, primary_key=True)
	ORDER_DATE = models.DateTimeField(default = timezone.now)
	ITEM_ID = models.ForeignKey(T_PROD_TYPE, on_delete=models.CASCADE)
	ORDER_QTY = models.IntegerField(default = 0)
	ORDER_FIN = models.BooleanField(default = False)
	FIN_TIME = models.DateTimeField(null=True)
	
	class Meta:
		db_table = 'T_ORDER_INFO'


class T_MACHINE_STATUS(models.Model):
	MACHINE_ID = models.IntegerField(db_index=True, primary_key=True)
	MACHINE_MTR = models.DateTimeField(auto_now_add = False, null=True)
	MACHINE_LOAD = models.IntegerField(default=0)
	MACHINE_LT = models.IntegerField(default=0)
	MACHINE_CAPA = models.IntegerField(default=0)
	MACHINE_NAME = models.CharField(max_length=10)
	SUBPROC_ID = models.ForeignKey(T_SUB_PROCESS, on_delete=models.CASCADE, default=1)
	MACHINE_SCHED = models.DateTimeField(auto_now_add = False, null=True)
	MACHINE_ENABLED = models.BooleanField(default = False)

	class Meta:
		db_table = 'T_MACHINE_STATUS'

class T_PROD_SCHEDULE(models.Model):
	SCHEDULE_ID = models.IntegerField(db_index=True, primary_key=True)
	ORDER_ID = models.ForeignKey(T_ORDER_INFO, on_delete=models.CASCADE)
	UPDATE_TIME = models.DateTimeField(auto_now_add = True, null=True)
	PROD_START = models.DateTimeField(auto_now_add = False,null=True)
	PROD_END = models.DateTimeField(auto_now_add = False,null=True)
	PROCESS_ID = models.ForeignKey(T_PROD_PROCESS, on_delete=models.CASCADE)
	MACHINE_USE = models.TextField()
	MACHINE_QTY =models.IntegerField(default = 0)
	#url = models.EmailField()
	#email = models.TextField()

	class Meta:
		db_table = 'T_PROD_SCHEDULE'









