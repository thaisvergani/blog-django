from django.test import TestCase
from django.contrib.auth.models import User
from .models import Comment, Post


class CommentModelTests(TestCase):
    def setUp(self):
        default_user = User.objects.create(username='admin')
        post = Post.objects.create(title="Post de teste", text="lorem ipsun", author=default_user)
        Comment.objects.create(post=post, text="top", author=default_user)

    def test_upvote(self):
        """
        upvote() increases Comment.vote by 1 and returns None
        """
        comment = Comment.objects.first()
        comment.upvote()
        self.assertEqual(comment.votes, 1)
