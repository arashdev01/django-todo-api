
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    اجازه می‌دهد کاربر فقط تسک‌هایی که خودش مالک آن‌هاست را ویرایش/حذف کند.
    بقیه کاربران فقط می‌توانند بخوانند (ReadOnly).
    """
    
    def has_object_permission(self, request, view, obj):
        # اگر درخواست فقط خواندن (GET, HEAD, OPTIONS) است، اجازه دسترسی بده.
        if request.method in permissions.SAFE_METHODS:
            return True

        # اگر درخواست ویرایش یا حذف (PUT, DELETE) است، فقط در صورتی اجازه بده
        # که مالک (owner) آبجکت با کاربر فعلی یکی باشد.
        return obj.owner == request.user