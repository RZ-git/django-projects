from django.db import models

from chat.base_models import BaseModel

""" 
モデル規約（仮）
1. テーブル及びカラムの論理名をそれぞれ、DocString
2. id(pk)は小文字ハイフン無しUUIDで統一（DBMSによる）（例：530a4eac2c1845d6a9968d0055b7df4a）
    UUID生成ツール https://hogehoge.tk/guid/ 
3. 新規作成・更新したモデルをマージした場合は、全体に変更箇所とマイグレーションが必要な胸を周知する事

"""


class Authority(BaseModel):
    """ 権限 """
    # 名称
    name = models.CharField(max_length=20, default='')
    # レベル
    level = models.IntegerField()

    class Meta:
        db_table = 'authority'


class User(BaseModel):
    """ ユーザー """
    create_user = models.ForeignKey('self', on_delete=models.PROTECT)
    # 性
    last_name = models.CharField(max_length=50, default='')
    # 名
    first_name = models.CharField(max_length=50, default='')
    # 権限
    authority = models.ForeignKey(Authority, on_delete=models.PROTECT)
    # メールアドレス
    email = models.CharField(max_length=200, default='')
    # GitHubアカウント名
    github_account_name = models.CharField(max_length=50, default='')

    class Meta:
        db_table = 'user'

    # def save(self, *args, **kwargs):
    #     super(User, self).save(*args, **kwargs)
