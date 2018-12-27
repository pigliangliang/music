from rest_framework import serializers
from .models import Product, Type
# 定义Serializer类
# 设置下拉内容
# 模型Type的__str__函数返回什么字段，type_name就要查询对应的字段
type_name = Type.objects.values('type_name').all()
TYPE_CHOICES = [item['type_name'] for item in type_name]
class MySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    weight = serializers.CharField(required=True, allow_blank=False, max_length=100)
    size = serializers.CharField(required=True, allow_blank=False, max_length=100)
    type = serializers.ChoiceField(choices=TYPE_CHOICES, default=1)
    # 如果使用MySerializer加载模型Product
	# 也可以改用PrimaryKeyRelatedField指定模型Type的外键
    # type = serializers.PrimaryKeyRelatedField(queryset=type_name, required=True)

    # 重写create函数，将API数据保存到数据表index_product
    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    # 重写update函数，将API数据更新到数据表index_product
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.size = validated_data.get('size', instance.size)
        instance.type = validated_data.get('type', instance.type)
        instance.save()
        return instance

# 定义ModelSerializer类
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('id', 'name', 'weight', 'size', 'type')