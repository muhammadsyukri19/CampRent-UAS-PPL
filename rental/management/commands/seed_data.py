import os
import shutil
from django.core.management.base import BaseCommand
from django.conf import settings
from rental.models import Equipment


class Command(BaseCommand):
    help = 'Seed database dengan data alat camping awal'
    
    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')
        
        # Copy images from static to media
        static_images_dir = os.path.join(
            settings.BASE_DIR, 'rental', 'static', 'rental', 'images'
        )
        media_dir = os.path.join(settings.MEDIA_ROOT, 'equipments')
        os.makedirs(media_dir, exist_ok=True)
        
        equipments_data = [
            {
                'name': 'Tenda Dome 4 Orang',
                'category': 'Tenda',
                'price_per_day': 75000,
                'stock': 5,
                'description': 'Tenda dome kapasitas 4 orang dengan bahan waterproof yang cocok untuk camping di berbagai medan. Dilengkapi dengan tiang aluminium yang ringan dan kuat, serta ventilasi yang baik untuk kenyamanan saat tidur. Mudah dipasang dan dibongkar, ideal untuk pemula maupun camper berpengalaman.',
                'image_file': 'tent.png',
            },
            {
                'name': 'Carrier 60L Expedition',
                'category': 'Carrier',
                'price_per_day': 50000,
                'stock': 8,
                'description': 'Carrier berkapasitas 60 liter dengan desain ergonomis dan sistem back support yang nyaman untuk perjalanan panjang. Dilengkapi dengan rain cover, compartment terpisah, dan banyak kantong untuk organisasi barang. Cocok untuk hiking dan trekking multi-hari.',
                'image_file': 'carrier.png',
            },
            {
                'name': 'Sleeping Bag Polar',
                'category': 'Sleeping Bag',
                'price_per_day': 30000,
                'stock': 10,
                'description': 'Sleeping bag berbahan polar yang hangat dan nyaman, mampu menahan suhu hingga 5°C. Ringan dan mudah dilipat sehingga tidak memakan banyak tempat di carrier. Cocok untuk camping di dataran tinggi atau pegunungan.',
                'image_file': 'sleeping_bag.png',
            },
            {
                'name': 'Matras Camping Ultralight',
                'category': 'Matras',
                'price_per_day': 20000,
                'stock': 12,
                'description': 'Matras camping ultralight dengan bahan foam berkualitas tinggi yang memberikan isolasi dari tanah dan kenyamanan ekstra saat tidur. Sangat ringan dan compact saat dilipat, mudah dibawa kemana saja.',
                'image_file': 'matras.png',
            },
            {
                'name': 'Kompor Portable Gas',
                'category': 'Kompor',
                'price_per_day': 25000,
                'stock': 7,
                'description': 'Kompor portable bertenaga gas butane dengan pengapian piezo otomatis. Kompak dan ringan, ideal untuk memasak di outdoor. Dilengkapi dengan windscreen untuk perlindungan angin dan pengaturan api yang presisi.',
                'image_file': 'kompor.png',
            },
        ]
        
        for data in equipments_data:
            image_file = data.pop('image_file')
            src_path = os.path.join(static_images_dir, image_file)
            dst_path = os.path.join(media_dir, image_file)
            
            if os.path.exists(src_path):
                shutil.copy2(src_path, dst_path)
                data['image'] = f'equipments/{image_file}'
            
            equipment, created = Equipment.objects.update_or_create(
                name=data['name'],
                defaults=data
            )
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'  + Created: {equipment.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'  ~ Updated: {equipment.name}'))
        
        self.stdout.write(self.style.SUCCESS(f'\nSeeding selesai! {Equipment.objects.count()} alat camping tersedia.'))
