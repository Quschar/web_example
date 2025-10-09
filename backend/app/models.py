from django.db import models

class Item(models.Model):
    # author, type, create_date, update_date, title, description, pictures
    author = models.CharField(max_length=100, verbose_name="作者")
    type = models.CharField(max_length=20, verbose_name="类型")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_date = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    title = models.CharField(max_length=500, verbose_name="标题")
    description = models.TextField(blank=True, verbose_name="描述")
    pictures = models.CharField(max_length=100, verbose_name="图片")

    class Meta:
        verbose_name = "条目"
        verbose_name_plural = "条目列表"
        ordering = ['-create_date']

    def __str__(self):
        return self.title
    