import threading

from django.conf import settings

# リクエストグローバルに変数を保存したい場所
GLOBAL_REQUEST_CONTEXT = threading.local()


class Log:
    level = None
    triggered_by = None
    type = None
    user_ip_address = None
    user_email = None
    user_name = None
    server_ip_address = None
    endpoint = None
    http_method = None
    process_time_msec = None
    created_at = None
    page_name = None
    stay_time_sec = None
    data = None


def get_auth():
    # ##その他のコードからリクエストグローバルなauthを取得するためのメソッド
    # Django shell用のauth存在しないエラー回避策
    # デバッグ時にauthが設定されていない場合はシステムユーザアドレスを設定
    if settings.DEBUG:
        if hasattr(GLOBAL_REQUEST_CONTEXT, 'auth'):
            return GLOBAL_REQUEST_CONTEXT.auth
        else:
            class DummyUser:
                def __init__(self):
                    self.email = 'example@gmail.com'
                    # self.id = 'system_id'
                    self.last_name = 'システム'
                    self.first_name = 'ユーザー'

            class DummyAuth:
                def __init__(self):
                    self.user = DummyUser()

            return DummyAuth()
    else:
        return GLOBAL_REQUEST_CONTEXT.auth


def get_request():
    return GLOBAL_REQUEST_CONTEXT.request
