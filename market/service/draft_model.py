import os
import random
import time
import uuid

from django.core.files.base import ContentFile

from draft.utils.exception_util import BusinessException
from draft.utils.log_util import get_logger
from draft import settings
from market.models import User, Draft

logger = get_logger("draft")


class DraftModel(object):

    def publish(self, title, description, image, price, category_id, username):
        user = User.objects.get(username=username)
        user_id = user.id

        # 保存画稿图片
        image_name = image.name
        image_suffix = image_name.split('.')[-1]
        if image_suffix not in ["png", "jpg"]:
            raise BusinessException("图片格式不支持，请上传png或jpg格式图片")
        new_image_name = "{}.{}".format(str(uuid.uuid4()), image_suffix)
        image_url = os.path.join(settings.design_images_dir, new_image_name)
        with open(os.path.join(settings.design_images_dir, new_image_name), "wb") as f:
            for chunk in ContentFile(image.read()).chunks():
                f.write(chunk)
        logger.info("图片已保存至{}".format(image_url))
        params = {
            "title": title,
            "description": description,
            "image_url": image_url,
            "price": price,
            "category_id": category_id,
            "designer_id": user_id,
            "online_time": int(time.time())
        }
        draft = Draft.objects.create(**params)
        logger.info("画稿已发布")
        return {"id": draft.id}

