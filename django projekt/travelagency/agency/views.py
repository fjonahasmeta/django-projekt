from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Post, Review, HelpMessage
from .forms import PostForm, ReviewForm, BookingForm


# 🏠 HOME + SEARCH
def home(request):
    query = request.GET.get('q', '')

    posts = Post.objects.all().order_by('-created_at')

    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    return render(request, 'agency/post_list.html', {
        'posts': posts,
        'query': query
    })


# 📄 POST DETAIL + REVIEWS
def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    reviews = post.reviews.all()

    form = ReviewForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            review = form.save(commit=False)
            review.post = post
            review.save()

            messages.success(request, "Review added successfully!")
            return redirect('detail', pk=post.id)
        else:
            messages.error(request, "Review form is not valid!")

    return render(request, 'agency/post_detail.html', {
        'post': post,
        'reviews': reviews,
        'form': form
    })


# ➕ CREATE POST
def create_post(request):
    form = PostForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Post created successfully!")
            return redirect('home')
        else:
            messages.error(request, "Form is not valid!")

    return render(request, 'agency/post_form.html', {'form': form})


# ✏️ EDIT POST
def edit_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    form = PostForm(request.POST or None, instance=post)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully!")
            return redirect('home')
        else:
            messages.error(request, "Form is not valid!")

    return render(request, 'agency/post_form.html', {'form': form})


# 🗑 DELETE POST
def delete_post(request, pk):
    post = get_object_or_404(Post, id=pk)

    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted successfully!")
        return redirect('home')

    return render(request, 'agency/confirm_delete.html', {'post': post})


# 📅 BOOKING
def booking(request, pk):
    post = get_object_or_404(Post, id=pk)
    form = BookingForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            book = form.save(commit=False)
            book.post = post
            book.save()

            messages.success(request, "Booking successful!")
            return redirect('detail', pk=post.id)
        else:
            messages.error(request, "Booking form is not valid!")

    return render(request, 'agency/booking.html', {
        'form': form,
        'post': post
    })


# ❤️ LIKE
def like_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.likes = (post.likes or 0) + 1
    post.save()
    return redirect('detail', pk=pk)


# 👎 DISLIKE
def dislike_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.dislikes = (post.dislikes or 0) + 1
    post.save()
    return redirect('detail', pk=pk)


# ✨ ABOUT PAGE
def about(request):
    return render(request, 'agency/about.html')


# 💬 HELP PAGE (SAVE TO DATABASE)
def help_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if name and email and message:
            HelpMessage.objects.create(
                name=name,
                email=email,
                message=message
            )
            messages.success(request, "Mesazhi u dërgua me sukses!")
            return redirect('help')

        messages.error(request, "Ju lutem plotësoni të gjitha fushat!")

    return render(request, 'agency/help.html')