from django.db import models


class Equipment(models.Model):
    """Model untuk data alat camping."""
    
    CATEGORY_CHOICES = [
        ('Tenda', 'Tenda'),
        ('Carrier', 'Carrier'),
        ('Sleeping Bag', 'Sleeping Bag'),
        ('Matras', 'Matras'),
        ('Kompor', 'Kompor'),
        ('Perlengkapan Lain', 'Perlengkapan Lain'),
    ]
    
    name = models.CharField(max_length=200, verbose_name='Nama Alat')
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, verbose_name='Kategori')
    price_per_day = models.IntegerField(verbose_name='Harga Sewa/Hari')
    stock = models.IntegerField(default=0, verbose_name='Stok')
    description = models.TextField(blank=True, verbose_name='Deskripsi')
    image = models.ImageField(upload_to='equipments/', blank=True, null=True, verbose_name='Gambar')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Alat Camping'
        verbose_name_plural = 'Alat Camping'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name


class Booking(models.Model):
    """Model untuk data booking/penyewaan."""
    
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Dipinjam', 'Dipinjam'),
        ('Selesai', 'Selesai'),
    ]
    
    customer_name = models.CharField(max_length=200, verbose_name='Nama Penyewa')
    phone = models.CharField(max_length=20, verbose_name='No. Telepon')
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='bookings', verbose_name='Alat')
    start_date = models.DateField(verbose_name='Tanggal Pinjam')
    end_date = models.DateField(verbose_name='Tanggal Kembali')
    note = models.TextField(blank=True, verbose_name='Catatan')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending', verbose_name='Status')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Booking'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.customer_name} - {self.equipment.name}"
    
    @property
    def duration(self):
        """Hitung durasi sewa dalam hari."""
        return (self.end_date - self.start_date).days
    
    @property
    def total_price(self):
        """Hitung total harga sewa."""
        return self.duration * self.equipment.price_per_day
