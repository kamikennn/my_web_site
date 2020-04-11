from django.contrib import admin

from .models import Inquiry,Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class InquiryAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Inquiry,InquiryAdmin)
admin.site.register(Comment)