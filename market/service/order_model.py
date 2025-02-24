import os
import random
import time
import uuid

from django.core.files.base import ContentFile
from django.core.paginator import Paginator
from django.forms import model_to_dict

from draft.utils.constants_util import OrderStatus
from draft.utils.exception_util import BusinessException
from draft.utils.log_util import get_logger
from draft import settings
from market.models import User, Draft, Order
from market.service.draft_model import DraftModel
from market.service.user_model import UserModel

logger = get_logger("draft")


class OrderModel(object):

    def create_order(self, username, draft_id):
        user = User.objects.get(username=username)
        user_id = user.id

        draft = Draft.objects.get(id=draft_id)
        params = {
            "user_id": user_id,
            "amount": draft.price,
            "status": OrderStatus.PENDING.value,
            "draft_id": draft_id,
            "create_time": int(time.time()),
            "is_cancel": 0,
        }
        order = Order.objects.create(**params)
        return {"id": order.id}

    def order_list(self, page, size, **kwargs):
        order_list = Order.objects.filter().order_by("-id")
        if kwargs.get("status"):
            order_list = order_list.filter(status=kwargs.get("status"))
        if kwargs.get("draft_id"):
            order_list = order_list.filter(draft_id=kwargs.get("draft_id"))
        if kwargs.get("username"):
            user = User.objects.get(username=kwargs.get("username"))
            user_id = user.id
            order_list = order_list.filter(user_id=user_id)
        count = order_list.count()
        paginator = Paginator(order_list, size)
        order_list = paginator.get_page(page)

        # 获取用户列表
        res = UserModel().user_list(1, 9999)
        user_list = res.get("list", [])
        user_map = {}
        for user in user_list:
            user_map[str(user.get("id"))] = user.get("username")

        data_list = []
        for item in order_list:
            info = model_to_dict(item)
            info["buyer"] = user_map.get(str(info.get("user_id")))
            data_list.append(info)
        return {"count": count, "list": data_list}

    def pay(self, order_id):
        order = Order.objects.get(id=order_id)
        # 查询画稿详情
        draft_id = order.draft_id
        draft = Draft.objects.get(id=draft_id)

        # 查询买方详情
        user_id = order.user_id
        user = User.objects.get(id=user_id)
        logger.info("user:{}".format(user.username))

        # 如果买方的余额小于画稿的价格，则交易失败
        if user.balance < draft.price:
            raise BusinessException("余额不足")

        user.balance -= draft.price
        user.save()

        # 查询设计师详情，并将amount的金额转入设计师的余额中
        designer_id = draft.designer_id
        designer = User.objects.get(id=designer_id)
        designer.balance += draft.price
        designer.save()

        # 修改订单状态为“已支付”
        order.status = OrderStatus.PAID.value
        order.save()


