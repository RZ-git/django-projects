import uuid

from django.db import models
from django_currentuser.middleware import get_current_authenticated_user


class BaseModel(models.Model):
    """ 抽象ベースクラス
        全てのモデルに適用させる共通のカラムを定義 """
    # ID （プライマリキー）
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 削除フラグ
    is_deleted = models.BooleanField(default=False)
    # 作成者
    create_user = models.SlugField(default=None, max_length=50)
    # 作成日時
    created_at = models.DateTimeField(auto_now_add=True)
    # 更新者
    update_user = models.SlugField(default=None, max_length=50)
    # 更新日時
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    # def create(self, *args):
    #     self.update_user = get_current_authenticated_user()
    #
    # def update(self, *args):
    #     self.update_user = get_current_authenticated_user()
    #
    # def save(self, *args):
    #     self.update_user = get_current_authenticated_user()
    #
    # def __init__(self, *args, **kwargs):
    #     from config.middleware import get_auth
    #
    #     super(BaseModel, self).__init__(*args, **kwargs)
    #     # 新規作成時は認証ユーザID、更新時は元々のIDを指定
    #     self.created_user_id = self.created_user_id if self.created_user_id else get_auth().user.id
    #
    # def save(self, *args, **kwargs):
    #     from config.middleware import get_auth
    #     # update時にユーザのアドレスを指定
    #     self.update_user_id = get_auth().user.id
    #     super(BaseModel, self).save(*args, **kwargs)
