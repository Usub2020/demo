from django.db import models
from django.db.models.base import Model
from django.template.defaultfilters import slugify, title
from unidecode import unidecode
# import datetime

# Create your models here.
class Student_comment(models.Model):
    student = models.CharField(max_length=250,null=False,verbose_name='Telebe Adi')
    title = models.CharField(max_length=1000 , null=False,verbose_name='Telebenin reyi')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % (self.student)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = "Student"
        ordering = ['-date']

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    head = models.CharField(max_length=250,null=True,verbose_name="Baslig")
    title = models.TextField()
    image = models.ImageField(upload_to='polls/%Y/%M/%D/%H/%M/%S',null=False,blank=True,verbose_name='Image')
    category = models.CharField(max_length=1000,null=True,verbose_name="Kategoriya",help_text="Her Categoryden sonra - qoyun")
    date = models.DateTimeField(auto_now_add=True)
    click = models.IntegerField(null=True,editable=False,default=0)

    def __str__(self):
        return "%s" % (self.head)

    def category_split(self):
        split = str(self.category).split('-')
        return split
    
    def image_(self):
        return "/media/%s" % (self.image)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = "Blog"
        ordering = ['-date']
    
class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=False,unique=True,verbose_name='Course Name')
    slug = models.SlugField(max_length=50 , unique=True ,editable=False, null=True)

    mentor = models.CharField(max_length=100,null=False,unique=True,verbose_name='Mentor')
    course_day = models.IntegerField(verbose_name='Duration of education',null=True)
    courses_hours = models.IntegerField(verbose_name='Hourse education',null=True)
    student_price = models.IntegerField(verbose_name='Student Price',null=True)
    standart_price = models.IntegerField(verbose_name='Standart Price',null=True)

    category = models.CharField(max_length=250, null=True ,verbose_name='Category',help_text='Her Categoryden sonra - qoyun')
    image = models.ImageField(upload_to='Courses_image/%Y/%M/%D/%H/%M/%S',null=False,blank=True,verbose_name='Course Image')
    information = models.TextField(blank=True,unique=False)
    price = models.IntegerField(verbose_name='Course Price',null=True)
    create_date = models.DateTimeField(auto_now_add=True,verbose_name="Created Date")
    update_date = models.DateTimeField(auto_now=True,verbose_name='Update Date')
    available = models.BooleanField(default=True,verbose_name='if you are sure')

    def category_split(self):
        split = str(self.category).split('-')
        return split

    def __str__(self):
        return "%s" % (self.name)

    def melumat(self):
        return self.bolgu.all()

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = "Courses"
        ordering = ['-create_date']


    # def stop (self):
    #     start = 0
    #     stop = 0
    #     start_ = str(str(datetime.datetime.now()).split()[0]).split('-') 
    #     stop_ = str(str(self.end_day).split()[0]).split('-')
    #     for i , k in zip(start_,stop_):
    #         start = start + int(i)
    #         stop = stop + int(k)
    #     print(start,stop)
    #     if start >= stop :
    #         self.available = False

    def save(self,*args , **kwargs) :
        if self.id is None :
            name = self.name
            self.slug = slugify(unidecode(name))
        super(Courses,self).save(*args,**kwargs)

class text_multi (models.Model):
    connect = models.ForeignKey(Courses,on_delete=models.CASCADE,related_name="bolgu")
    grup = models.CharField(max_length=250,null=False,verbose_name='Text Head')
    text = models.TextField()

class contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=False,unique=False)
    email = models.EmailField(max_length=150,null=False,unique=False)
    phone = models.CharField(max_length=100,null=False,unique=False)
    subject = models.CharField(max_length=100,null=False,unique=False)
    mesage = models.TextField()
    date = models.DateTimeField(auto_now=True,verbose_name="Send Date")

    def __str__(self):
       return self.email

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = "Contact"
