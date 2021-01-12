from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

User = settings.AUTH_USER_MODEL


class Post(models.Model):
    title = models.CharField('タイトル', max_length=100)
    content = models.TextField('本文')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', verbose_name='画像', blank=True, null=True)
    pub_date = models.DateTimeField('公開日', default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
