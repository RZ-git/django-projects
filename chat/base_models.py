import uuid

from django.db import models
from django_currentuser.middleware import get_current_user, get_current_authenticated_user


class BaseModel(models.Model):
    """ 抽象ベースクラス
        全てのモデルに適用させる共通のカラムを定義 """
    # ID （プライマリキー）
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 削除フラグ
    is_deleted = models.BooleanField(default=False)
    # 作成日時
    created_at = models.DateTimeField(auto_now_add=True)
    # 更新日時
    updated_at = models.DateTimeField(auto_now=True)

    # 作成者
    # create_user
    # 更新者
    # update_user

    class Meta:
        abstract = True

    # def create(self, *args):
    #     TODO ログインユーザーで作成
    #     self.update_user = get_current_authenticated_user()

    # def update(self, *args):
    #     TODO ログインユーザーで更新
    #     self.update_user = get_current_authenticated_user()

    # def save(self, *args):
    #     TODO ログインユーザーで作成と更新
    #     self.update_user = get_current_authenticated_user()
