from django.contrib import admin


from users.models import User

#admin.site.register(User)

#class UserAdmin(admin.ModelAdmin):
 #   list_display = ('email', 'phone', 'avatar', 'country', 'is_block')
 #   list_filter = ('country', 'is_block')
   # search_fields = ('title', 'body', 'setting',)
   # filter_horizontal = ['clients']

 #   def get_form(self, request, obj=None, **kwargs):
#        form = super().get_form(request, obj, **kwargs)
#        if request.user.is_superuser:
#            return form

 #       elif request.user.is_staff:
  #          form.base_fields['email'].disabled = True
  #          form.base_fields['phone'].disabled = True
  #          form.base_fields['avatar'].disabled = True
  #          form.base_fields['country'].disabled = True
  #          return form