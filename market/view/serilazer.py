from rest_framework import serializers

from market.models import User


class RegisterSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=64, required=True, help_text="用户名")
    password = serializers.CharField(max_length=32, required=True, help_text="密码")
    confirm_password = serializers.CharField(max_length=32, required=True, help_text="确认密码")
    gender = serializers.ChoiceField(choices=[(1, "男"), (0, "女")], help_text="1男，0女")
    phone = serializers.CharField(max_length=32, required=True, help_text="手机号")
    nickname = serializers.CharField(max_length=64, required=True, help_text="昵称")


class UserModifySerializer(serializers.Serializer):

    username = serializers.CharField(max_length=64, required=False, help_text="用户名")
    gender = serializers.ChoiceField(choices=[(1, "男"), (0, "女")], help_text="1男，0女")
    phone = serializers.CharField(max_length=32, required=False, help_text="手机号")
    nickname = serializers.CharField(max_length=64, required=True, help_text="昵称")


class ApplyAsDesignerSerializer(serializers.Serializer):

    reason = serializers.CharField(max_length=512, required=True, help_text="申请理由")


class RechargeSerializer(serializers.Serializer):

    amount = serializers.FloatField(required=True, help_text="充值金额")
