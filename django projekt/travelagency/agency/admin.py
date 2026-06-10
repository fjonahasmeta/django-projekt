from django.contrib import admin
from .models import Post, Review, Booking, HelpMessage


# 🏠 POSTS
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'likes', 'dislikes', 'created_at')
    search_fields = ('title', 'content', 'author')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


# ⭐ REVIEWS
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'rating', 'created_at')
    search_fields = ('name', 'comment')
    list_filter = ('rating', 'created_at')
    ordering = ('-created_at',)


# 📅 BOOKINGS
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'date', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('date', 'created_at')
    ordering = ('-created_at',)


# 💬 HELP / SUPPORT SYSTEM (NEW)
@admin.register(HelpMessage)
class HelpMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_read', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('is_read', 'created_at')
    ordering = ('-created_at',)

    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)