from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    header = models.ImageField(upload_to='headers/%Y/%m/%d/')

    def __str__(self):
        return self.title

class Paragraph(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(blank=True, default="default_content")
    main_image = models.ImageField(upload_to='post_images', blank=True)
    caption = models.CharField(max_length=300, blank=True)
