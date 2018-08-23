from django.contrib import admin

from .models import Post, Paragraph



class ParagraphInline(admin.TabularInline):
    model = Paragraph


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['title']}),
        (None,  {'fields': ['summary']}),
        (None,  {'fields': ['pub_date']}),
        (None,  {'fields': ['header']})
    ]
    inlines = [ParagraphInline]
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title']


admin.site.register(Post, PostAdmin)
