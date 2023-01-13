from django.db import models


class UserInfo(models.Model):
    name=models.CharField(max_length=32)
    password=models.CharField(max_length=64)

class FileInfo(models.Model):
    name=models.CharField(max_length=32)
class ResultInfo(models.Model):
    result_id=models.IntegerField(default=12)
    inval=models.CharField(max_length=1000,default='abc')
    ouval=models.CharField(max_length=1000,default='abc')
    err=models.CharField(max_length=1000,default='abc')



"""
会自动帮我们创建表
create table electron_userinfo(
     id bigint auto_increment primary key,
     name varchar(32),
     password varchar(64),
     age int,
)
"""