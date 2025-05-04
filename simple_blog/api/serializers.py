from rest_framework import serializers

from blog.models import Article, ArticleTag, Tag, User


AT_LEAST_ONE_TEG_REQUIRED = 'Необходимо указать хотя бы 1 тег.'
TAG_LIST_CONTAINS_DUPLICATE_TAGS = 'Список тегов содержит повторяющиеся теги.'


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')


class UserReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class ArticleBaseSerializer(serializers.ModelSerializer):
    author = UserReadSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('id', 'created_at')


class ArticleReadSerializer(ArticleBaseSerializer):
    tags = TagSerializer(many=True)


class ArticleWriteSerializer(ArticleBaseSerializer):
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    def to_representation(self, instance):
        return ArticleReadSerializer(
            context=self.context
        ).to_representation(
            instance
        )

    def validate_tags(self, tags):
        if not tags:
            raise serializers.ValidationError(
                AT_LEAST_ONE_TEG_REQUIRED
            )
        if len(tags) != len(set(tags)):
            raise serializers.ValidationError(
                TAG_LIST_CONTAINS_DUPLICATE_TAGS
            )
        return tags

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        article = Article.objects.create(**validated_data)
        ArticleTag.objects.bulk_create(
            ArticleTag(article=article, tag=tag_id) for tag_id in tags
        )
        return article

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags', None)
        for field, value in validated_data.items():
            setattr(instance, field, value)
        if tags is not None:
            instance.tags.set(tags)
        instance.save()
        return instance
