from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

'''
forms.py file is for interacting with new custom user model(reference: guests/models.py).
ユーザ情報の操作は/adminで行うか，作成したwebサイト上で行うかの二通り．
カスタムユーザモデルを作成して，'age'というfieldを追加したが，
この変更が/adminとwebサイトで整合が取れるようにforms.pyを作成．
'''

#Meta class でデフォルトのfieldをオーバーライドしている
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserChangeForm):
        model = CustomUser

        #with defaul fields
        # fields = UserCreationForm.Meta.fields + ('age','country',)
        #without default fields
        fields = ('username','age','country',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        #'age'fieldは変更することは無いので，追加しない．(歳はとるが，ここでは無視)
        #with defaul fields
        # fields = UserChangeForm.Meta.fields
        #without default fields
        fields = ('username','age','country',)