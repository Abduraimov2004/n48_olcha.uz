from rest_framework import serializers
from .models import Category, Group, Product


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    full_image_url = serializers.SerializerMethodField()
    count = serializers.SerializerMethodField(method_name='groups_count')

    def groups_count(self, obj):
        count = obj.groups.count()
        return count

    def get_full_image_url(self, instance):

        if instance.image:
            image_url = instance.image.url
            request = self.context.get('request')
            return request.build_absolute_uri(image_url)
        else:
            return None

    class Meta:
        model = Category
        fields = ['id', 'title', 'full_image_url', 'slug', 'count','groups']


class ProductSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    full_image_url = serializers.SerializerMethodField()

    def get_full_image_url(self, instance):
        if instance.image:
            image_url = instance.image.url
            request = self.context.get('request')
            return request.build_absolute_uri(image_url)
        return None

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'full_image_url', 'slug', 'category', 'groups']
