from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=64, required=True, help_text="用户名")
    password1 = serializers.CharField(max_length=32, required=True, help_text="密码1")
    password2 = serializers.CharField(max_length=32, required=True, help_text="密码2")
    gander = serializers.ChoiceField(choices=[(1, "男"), (0, "女")], help_text="1男，0女")
    phone = serializers.CharField(max_length=32, required=True, help_text="手机号")
    nickname = serializers.CharField(max_length=64, required=True, help_text="昵称")
