from django.contrib import admin
from django.http import HttpResponseRedirect
from django.utils.http import is_safe_url

class ModelAdmin(admin.ModelAdmin):
    def response_change(self, request, obj):
        res = super(ModelAdmin, self).response_change(request, obj)
        next_url = request.GET.get('next','')
        if next_url and is_safe_url(next_url):
            return HttpResponseRedirect(next_url)
        else:
            return res

    def response_add(self, request, obj, post_url_continue=None):
        res = super(ModelAdmin, self).response_add(request, obj, post_url_continue)
        next_url = request.GET.get('next','')
        if next_url and is_safe_url(next_url):
            return HttpResponseRedirect(next_url)
        else:
            return res
