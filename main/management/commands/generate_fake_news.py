from django.core.management.base import BaseCommand
from django.core.files import File
from main.models import News
from django.utils import timezone
from faker import Faker
import requests
import tempfile
import os
from datetime import timedelta

class Command(BaseCommand):
    help = 'Generates fake news entries'

    def transliterate_to_kazakh(self, text):
        # Простая транслитерация с русского на казахский
        # Это очень упрощенная версия, для демо-данных
        replacements = {
            'а': 'ә', 'и': 'і', 'у': 'ұ', 'о': 'ө',
            'А': 'Ә', 'И': 'І', 'У': 'Ұ', 'О': 'Ө',
        }
        for rus, kaz in replacements.items():
            text = text.replace(rus, kaz)
        return text

    def handle(self, *args, **options):
        fake_ru = Faker('ru_RU')
        fake_en = Faker('en_US')
        
        # Список URL изображений для новостей
        image_urls = [
            'https://picsum.photos/800/600',  # Случайные изображения с picsum
            'https://source.unsplash.com/800x600/?history',
            'https://source.unsplash.com/800x600/?museum',
            'https://source.unsplash.com/800x600/?archive',
            'https://source.unsplash.com/800x600/?library'
        ]

        self.stdout.write('Начинаю генерацию новостей...')

        for i in range(10):
            # Создаем временный файл для изображения
            img_temp = tempfile.NamedTemporaryFile(delete=True)
            
            # Получаем случайное изображение
            img_url = fake_ru.random_element(image_urls)
            response = requests.get(img_url, stream=True)
            
            if response.status_code == 200:
                # Записываем изображение во временный файл
                for block in response.iter_content(1024 * 8):
                    if not block:
                        break
                    img_temp.write(block)
                
                # Генерируем случайную дату в пределах последних 6 месяцев
                created_at = timezone.now() - timedelta(days=fake_ru.random_int(min=0, max=180))
                
                # Создаем новость
                news = News()
                news.created_at = created_at
                news.is_featured = fake_ru.boolean(chance_of_getting_true=20)
                
                # Русский контент
                news.title_ru = fake_ru.sentence(nb_words=6, variable_nb_words=True)
                news.preview_ru = fake_ru.paragraph(nb_sentences=3)
                news.content_ru = '\n\n'.join(fake_ru.paragraphs(nb=5))
                
                # Казахский контент (транслитерация с русского)
                news.title_kk = self.transliterate_to_kazakh(news.title_ru)
                news.preview_kk = self.transliterate_to_kazakh(news.preview_ru)
                news.content_kk = self.transliterate_to_kazakh(news.content_ru)
                
                # Английский контент
                news.title_en = fake_en.sentence(nb_words=6, variable_nb_words=True)
                news.preview_en = fake_en.paragraph(nb_sentences=3)
                news.content_en = '\n\n'.join(fake_en.paragraphs(nb=5))
                
                # Сохраняем новость
                news.save()
                
                # Добавляем изображение
                img_temp.flush()
                filename = f'news_image_{i+1}.jpg'
                news.image.save(filename, File(img_temp))
                
                self.stdout.write(self.style.SUCCESS(f'Создана новость: {news.title_ru}'))
            
            img_temp.close()

        self.stdout.write(self.style.SUCCESS('Успешно создано 10 новостей!')) 