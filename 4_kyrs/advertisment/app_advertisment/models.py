from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()
class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length= 12 )
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('торг', help_text='Отметьте, если торг уместен')
    created_at= models.DateTimeField('Дата и время создания', auto_now_add=True)
    updatet_at = models.DateTimeField('Дата и время изменения', auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image = models.ImageField('Изображение',upload_to='advertisements/')
    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description='Дата обновления ')
    def updatet_date(self):
        if self.updatet_at.date() == timezone.now().date():
            updatet_time = self.updatet_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: red; font-weight: bold;">Сегодня в {}</span>', updatet_time
            )
        return self.updatet_at.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description='фото')
    def get_image(self):
        if self.image:
            return format_html(
            '<img src="{url}" style="max-width: 80px; max-height: 80px"', url = self.image.url)

    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'

    class Meta:
        db_table = 'advertisements'



