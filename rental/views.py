from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Sum, Q
from .models import Equipment, Booking
from .forms import EquipmentForm, BookingForm, LoginForm


# ==========================================
# PUBLIC VIEWS
# ==========================================

def landing_page(request):
    """Halaman utama / landing page."""
    popular_equipments = Equipment.objects.filter(stock__gt=0).order_by('-created_at')[:6]
    total_equipments = Equipment.objects.count()
    total_bookings = Booking.objects.count()
    
    context = {
        'popular_equipments': popular_equipments,
        'total_equipments': total_equipments,
        'total_bookings': total_bookings,
    }
    return render(request, 'rental/landing.html', context)


def catalog(request):
    """Halaman katalog alat camping."""
    equipments = Equipment.objects.all()
    
    # Filter by category
    category = request.GET.get('category', '')
    if category:
        equipments = equipments.filter(category=category)
    
    # Search
    search = request.GET.get('search', '')
    if search:
        equipments = equipments.filter(
            Q(name__icontains=search) | Q(description__icontains=search)
        )
    
    categories = Equipment.CATEGORY_CHOICES
    
    context = {
        'equipments': equipments,
        'categories': categories,
        'selected_category': category,
        'search_query': search,
    }
    return render(request, 'rental/catalog.html', context)


def equipment_detail(request, pk):
    """Halaman detail alat camping."""
    equipment = get_object_or_404(Equipment, pk=pk)
    related_equipments = Equipment.objects.filter(
        category=equipment.category
    ).exclude(pk=pk)[:4]
    
    context = {
        'equipment': equipment,
        'related_equipments': related_equipments,
    }
    return render(request, 'rental/equipment_detail.html', context)


def booking_form(request):
    """Halaman form booking."""
    equipment_id = request.GET.get('equipment')
    initial_data = {}
    
    if equipment_id:
        try:
            equipment = Equipment.objects.get(pk=equipment_id)
            initial_data['equipment'] = equipment
        except Equipment.DoesNotExist:
            pass
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            messages.success(request, f'Booking berhasil! Nomor booking Anda: #{booking.id}')
            return redirect('rental:booking_success')
    else:
        form = BookingForm(initial=initial_data)
    
    # Only show equipment with stock > 0
    form.fields['equipment'].queryset = Equipment.objects.filter(stock__gt=0)
    
    context = {
        'form': form,
    }
    return render(request, 'rental/booking_form.html', context)


def booking_success(request):
    """Halaman sukses booking."""
    return render(request, 'rental/booking_success.html')


# ==========================================
# ADMIN AUTH VIEWS
# ==========================================

def admin_login(request):
    """Halaman login admin."""
    if request.user.is_authenticated:
        return redirect('rental:dashboard')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'Selamat datang, {user.username}!')
                return redirect('rental:dashboard')
            else:
                messages.error(request, 'Username atau password salah.')
    else:
        form = LoginForm()
    
    context = {
        'form': form,
    }
    return render(request, 'rental/admin/login.html', context)


def admin_logout(request):
    """Logout admin."""
    logout(request)
    messages.success(request, 'Berhasil logout.')
    return redirect('rental:landing')


# ==========================================
# ADMIN DASHBOARD VIEWS
# ==========================================

@login_required
def dashboard(request):
    """Halaman dashboard admin."""
    total_equipments = Equipment.objects.count()
    total_bookings = Booking.objects.count()
    pending_bookings = Booking.objects.filter(status='Pending').count()
    active_bookings = Booking.objects.filter(status='Dipinjam').count()
    recent_bookings = Booking.objects.select_related('equipment').order_by('-created_at')[:5]
    
    context = {
        'total_equipments': total_equipments,
        'total_bookings': total_bookings,
        'pending_bookings': pending_bookings,
        'active_bookings': active_bookings,
        'recent_bookings': recent_bookings,
    }
    return render(request, 'rental/admin/dashboard.html', context)


# ==========================================
# ADMIN EQUIPMENT CRUD VIEWS
# ==========================================

@login_required
def equipment_list(request):
    """Daftar alat camping (admin)."""
    equipments = Equipment.objects.all()
    context = {
        'equipments': equipments,
    }
    return render(request, 'rental/admin/equipment_list.html', context)


@login_required
def equipment_create(request):
    """Tambah alat camping baru."""
    if request.method == 'POST':
        form = EquipmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Alat camping berhasil ditambahkan!')
            return redirect('rental:equipment_list')
    else:
        form = EquipmentForm()
    
    context = {
        'form': form,
        'title': 'Tambah Alat Camping',
    }
    return render(request, 'rental/admin/equipment_form.html', context)


@login_required
def equipment_edit(request, pk):
    """Edit data alat camping."""
    equipment = get_object_or_404(Equipment, pk=pk)
    
    if request.method == 'POST':
        form = EquipmentForm(request.POST, request.FILES, instance=equipment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data alat camping berhasil diperbarui!')
            return redirect('rental:equipment_list')
    else:
        form = EquipmentForm(instance=equipment)
    
    context = {
        'form': form,
        'title': 'Edit Alat Camping',
        'equipment': equipment,
    }
    return render(request, 'rental/admin/equipment_form.html', context)


@login_required
def equipment_delete(request, pk):
    """Hapus data alat camping."""
    equipment = get_object_or_404(Equipment, pk=pk)
    
    if request.method == 'POST':
        equipment.delete()
        messages.success(request, 'Alat camping berhasil dihapus!')
        return redirect('rental:equipment_list')
    
    context = {
        'equipment': equipment,
    }
    return render(request, 'rental/admin/equipment_delete.html', context)


# ==========================================
# ADMIN BOOKING MANAGEMENT VIEWS
# ==========================================

@login_required
def booking_list(request):
    """Daftar booking (admin)."""
    bookings = Booking.objects.select_related('equipment').all()
    
    # Filter by status
    status = request.GET.get('status', '')
    if status:
        bookings = bookings.filter(status=status)
    
    context = {
        'bookings': bookings,
        'selected_status': status,
    }
    return render(request, 'rental/admin/booking_list.html', context)


@login_required
def booking_update_status(request, pk):
    """Update status booking."""
    booking = get_object_or_404(Booking, pk=pk)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in ['Pending', 'Dipinjam', 'Selesai']:
            booking.status = new_status
            booking.save()
            messages.success(request, f'Status booking #{booking.id} berhasil diperbarui menjadi {new_status}!')
    
    return redirect('rental:booking_list')


@login_required
def booking_delete(request, pk):
    """Hapus data booking."""
    booking = get_object_or_404(Booking, pk=pk)
    
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking berhasil dihapus!')
        return redirect('rental:booking_list')
    
    context = {
        'booking': booking,
    }
    return render(request, 'rental/admin/booking_delete.html', context)
