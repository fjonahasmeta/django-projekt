from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Post, Review
from .forms import PostForm, ReviewForm, BookingForm


# 🏠 HOME (LIST POSTS)
def home(request):
    query = request.GET.get('q')

    posts = Post.objects.all()

    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    posts = posts.order_by('-created_at')

    return render(request, 'agency/post_list.html', {'posts': posts})


# 📄 POST DETAIL + REVIEWS
def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    reviews = post.reviews.all()

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.post = post
            review.save()

            messages.success(request, "Review added successfully!")
            return redirect('detail', pk=post.id)
    else:
        form = ReviewForm()

    return render(request, 'agency/post_detail.html', {
        'post': post,
        'reviews': reviews,
        'form': form
    })


# ➕ CREATE POST
def create_post(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Post created successfully!")
        return redirect('home')

    return render(request, 'agency/post_form.html', {'form': form})


# ✏️ EDIT POST
def edit_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        messages.success(request, "Post updated!")
        return redirect('home')

    return render(request, 'agency/post_form.html', {'form': form})


# 🗑 DELETE POST
def delete_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.delete()
    messages.success(request, "Post deleted!")
    return redirect('home')


# 📅 BOOKING SYSTEM
def booking(request, pk):
    post = get_object_or_404(Post, id=pk)
    form = BookingForm(request.POST or None)

    if form.is_valid():
        book = form.save(commit=False)
        book.post = post
        book.save()

        messages.success(request, "Booking successful!")
        return redirect('detail', pk=post.id)

    return render(request, 'agency/booking.html', {
        'form': form,
        'post': post
    })


# ❤️ LIKE POST
def like_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.likes = (post.likes or 0) + 1
    post.save()
    return redirect('detail', pk=pk)


# 👎 DISLIKE POST
def dislike_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.dislikes = (post.dislikes or 0) + 1
    post.save()
    return redirect('detail', pk=pk)