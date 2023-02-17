from turtle import update
from django.db import models
from decimal import Decimal

# Create your models here.

class User(models.Model):
    username = models.CharField('用户名', max_length=100, default='匿名用户')
    # avatar = models.ImageField('头像', upload_to='avatar/', default='avatar/default.png')
    avatar = models.CharField('头像', max_length=500, default='/media/avatar/default.png')
    gender = models.CharField('性别', max_length=10, default='未设置')
    phoneNumber = models.CharField('手机号码', max_length=11, default='')
    email = models.EmailField('邮箱', default='')
    registerDate = models.DateField('创建时间', auto_now_add=True)
    openid = models.CharField("微信ID", max_length=200, unique=True)
    class Meta:
        db_table = 'user'

    def info_json(self):
        return {
            'user_id': self.username,
            'avatar': self.avatar,
            'gender': self.gender,
            'phone_number': self.phoneNumber,
            'email': self.email,
            'register_date': self.registerDate
        }

# class Wrong(models.Model):
#     user_id = models.DecimalField('用户ID',max_digits=3, decimal_places=0, default=Decimal('0'))
#     question_id = models.DecimalField('题目ID',max_digits=3, decimal_places=0, default=Decimal('0'))
#     type = models.CharField('题型',max_length=10)
#     update_Date = models.DateField('加入时间', auto_now_add=True)

#     class Meta:
#         db_table = 'wrong'
    
#     def info_json(self):
#         return {
#             'user_id': self.user_id,
#             'question_id': self.question_id,
#             'type': self.type,
#             'update_date': self.update_Date
#         }
# class Collection(models.Model):
#     user_id = models.DecimalField('用户ID',max_digits=3, decimal_places=0, default=Decimal('0'))
#     question_id = models.DecimalField('题目ID',max_digits=3, decimal_places=0, default=Decimal('0'))
#     type = models.CharField('题型',max_length=10)
#     update_Date = models.DateField('加入时间', auto_now_add=True)   

#     class Meta:
#         db_table = 'collection'
    
#     def info_json(self):
#         return {
#             'user_id': self.user_id,
#             'question_id': self.question_id,
#             'type': self.type,
#             'update_date': self.update_Date
#         }

# class Record(models.Model):
#     user_id = models.DecimalField('用户ID',max_digits=3, decimal_places=0, default=Decimal('0'))
#     question_id = models.DecimalField('题目ID',max_digits=3, decimal_places=0, default=Decimal('0'))
#     state = models.CharField('回答状态',max_length=10)
#     type = models.CharField('题型',max_length=10)
#     record_Date = models.DateField('回答时间', auto_now_add=True)

#     class Meta:
#         db_table = 'record'
#     def info_json(self):
#         return {
#             'user_id': self.user_id,
#             'question_id': self.question_id,
#             'state': self.state,
#             'type': self.type,
#             'record_date': self.record_Date
#         }   
class Login_record(models.Model):
    user_id = models.DecimalField('用户ID',max_digits=3, decimal_places=0, default=Decimal('0'))
    login_time = models.CharField('登陆时间',max_length=50)
    record_Date = models.DateField('登录日期', auto_now_add=True)
    class Meta:
        db_table = 'login'
    def info_json(self):
        return {
            'user_id': self.user_id,
            'login_time': self.login_ltime,
            'record_date':self.record_Date
        }