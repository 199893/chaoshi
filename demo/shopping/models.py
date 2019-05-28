from django.db import models

# Create your models here.
#用户表
class User(models.Model):
    #用户名
    username=models.CharField(max_length=20)
    #邮箱
    eml=models.EmailField()
    #密码
    password=models.CharField(max_length=50)
    # 激活状态
    activate=models.BooleanField(default=False)
    #注册时间
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

#分类表
class Classify(models.Model):
    #大分类
    classb=models.CharField(max_length=30)
    #小分类
    classs=models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.classb


#商品表
class Commodity(models.Model):
    #图片
    img=models.ImageField(upload_to='goodsimg')
    #商品名
    name=models.CharField(max_length=40)
    #原价格
    price=models.CharField(max_length=30)
    #折扣后价
    discount=models.CharField(max_length=30)
    #上架时间
    date=models.DateTimeField(auto_now_add=True)
    #简介头
    title=models.CharField(max_length=10)
    #简介内容
    describe=models.CharField(max_length=150)
    #关联分类表
    classid=models.ForeignKey(Classify,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

