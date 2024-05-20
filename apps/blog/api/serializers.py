from rest_framework import serializers
from apps.blog.models import Blog, Blog_comment, LikeDislike
from django.utils.timesince import timesince
from django.contrib.auth import get_user_model



User = get_user_model()

class BlogSerializer(serializers.ModelSerializer):

    blog_comments_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Blog
        fields = (
            'id',
            'blog_title',
            'blog_image',
            'slug',
            'status',
            'published_date',
            'blog_user',
            'published_blog_count',
            'blog_comments_count'
            )

    def get_blog_comments_count(self, obj):
        return obj.blog_comments.count()


class BlogCreateSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    blog_author = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Blog
        fields = (
            'id',
            'blog_title',
            'blog_image',
            'blog_content',
            'slug',
            'blog_author'
            )
    
    def validate(self, attrs):
            request = self.context.get('request')

            # if not request or not request.user.is_authenticated:
            #     raise serializers.ValidationError('You have to log in')

            attrs['blog_author'] = User.objects.first()
            return attrs
      

class BlogCommentSerializer(serializers.ModelSerializer):
    
    comment_author = serializers.SerializerMethodField()
    days_since_created = serializers.SerializerMethodField()

    
    class Meta:
        model = Blog_comment
        fields = (
        'id',
        'comment_author',
        'comment_text',
        'days_since_created',
        'like_count',
        'dislike_count'

        )
        
    def get_days_since_created(self, obj):
        timesince_str = timesince(obj.published_at)
        if 'day' in timesince_str:
            days = timesince_str.split()[0]
            return f'{days} days ago'
        return 0
   
    def get_comment_author(self, obj):
        return f'{obj.comment_author.first_name} {obj.comment_author.last_name}'
       
        
class BlogDetailSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField(read_only=True)
    blog_comments = BlogCommentSerializer(many=True)
    blog_comments_count = serializers.SerializerMethodField()
    published_date = serializers.SerializerMethodField()
    class Meta:
        model = Blog
        fields = (
            "id",
            "slug",
            "blog_title",
            'blog_content',
            "blog_user",
            "blog_image",
            'published_date',
            "blog_comments",
            'blog_comments_count',
            'view_count'
        )

    def get_blog_comments_count(self, obj):
        return obj.blog_comments.count()
    
    def get_published_date(self, obj):
        return obj.published_at.strftime('%b %d, %Y at %I:%M %p')
        
    def get_slug(self, obj):
        return obj.slug
            
        
class BlogCommentCreateSerializer(serializers.ModelSerializer):
    comment_author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Blog_comment
        fields = (
        'id',
        'blog',
        'comment_text',
        'comment_author'
        )            
    
    def validate(self, attrs):
        request = self.context.get('request')

        if not request or not request.user.is_authenticated:
            raise serializers.ValidationError('You have to log in')

        attrs['comment_author'] = request.user
        return attrs
    
    
class LikeDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeDislike
        fields = ['id', 'user', 'comment', 'action']



