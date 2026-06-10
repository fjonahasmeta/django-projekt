from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)

    image = models.ImageField(upload_to='images/', blank=True, null=True)

    # ❤️ LIKE SYSTEM
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']  # newest posts first


class Review(models.Model):

    STAR_CHOICES = [
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    ]

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    name = models.CharField(max_length=100)
    comment = models.TextField()

    # ⭐ STAR RATING (PRO LEVEL)
    rating = models.IntegerField(choices=STAR_CHOICES, default=5)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating}⭐"

    class Meta:
        ordering = ['-created_at']


class Booking(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} booking → {self.post.title}"

    class Meta:
        ordering = ['-created_at']