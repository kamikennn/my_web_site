from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

#新しいfieldを追加したカスタムユーザモデルを作成したので，adminを更新する
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    #/admin画面で表示させたいfields
    list_display = ['email','username','age','is_staff',]

admin.site.register(CustomUser, CustomUserAdmin)