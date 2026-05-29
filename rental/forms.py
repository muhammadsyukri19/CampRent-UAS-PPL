from django import forms
from .models import Equipment, Booking


class EquipmentForm(forms.ModelForm):
    """Form untuk menambah/mengedit data alat camping."""
    
    class Meta:
        model = Equipment
        fields = ['name', 'category', 'price_per_day', 'stock', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-gray-600 bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition',
                'placeholder': 'Masukkan nama alat'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-gray-600 bg-gray-700 text-white focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition'
            }),
            'price_per_day': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-gray-600 bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition',
                'placeholder': 'Masukkan harga per hari'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-gray-600 bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition',
                'placeholder': 'Masukkan jumlah stok'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-gray-600 bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition',
                'rows': 4,
                'placeholder': 'Masukkan deskripsi alat'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-gray-600 bg-gray-700 text-white file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:bg-emerald-600 file:text-white file:cursor-pointer hover:file:bg-emerald-700 transition'
            }),
        }


class BookingForm(forms.ModelForm):
    """Form untuk booking alat camping."""
    
    class Meta:
        model = Booking
        fields = ['customer_name', 'phone', 'equipment', 'start_date', 'end_date', 'note']
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-gray-300 bg-white text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition',
                'placeholder': 'Masukkan nama lengkap'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-gray-300 bg-white text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition',
                'placeholder': 'Contoh: 08123456789'
            }),
            'equipment': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-gray-300 bg-white text-gray-800 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-gray-300 bg-white text-gray-800 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition',
                'type': 'date'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-gray-300 bg-white text-gray-800 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition',
                'type': 'date'
            }),
            'note': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-gray-300 bg-white text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition',
                'rows': 3,
                'placeholder': 'Catatan tambahan (opsional)'
            }),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        
        if start_date and end_date:
            if end_date <= start_date:
                raise forms.ValidationError('Tanggal kembali harus setelah tanggal pinjam.')
        
        return cleaned_data


class LoginForm(forms.Form):
    """Form untuk login admin."""
    
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 rounded-xl border border-gray-600 bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition',
            'placeholder': 'Username',
            'autocomplete': 'username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 rounded-xl border border-gray-600 bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition',
            'placeholder': 'Password',
            'autocomplete': 'current-password'
        })
    )
