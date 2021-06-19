from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin

from transfer.models import Category, Transfer, Images, Comment


class TransferImageInline(admin.TabularInline):
    model = Images
    extra = 5


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'image_tag']
    list_filter = ['status']
    readonly_fields = ('image_tag',)


class TransferAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image_tag', 'seat', 'price', 'status']
    list_filter = ['status', 'category']
    inlines = [TransferImageInline]
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('title',)}


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'transfer', 'image_tag']
    readonly_fields = ('image_tag',)


class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_transfers_count', 'related_transfers_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative travel count
        qs = Category.objects.add_related_count(
            qs,
            Transfer,
            'category',
            'transfers_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                                                Transfer,
                                                'category',
                                                'transfers_count',
                                                cumulative=False)
        return qs

    def related_transfers_count(self, instance):
        return instance.transfers_count

    related_transfers_count.short_description = 'Related transfers (for this specific category)'

    def related_transfers_cumulative_count(self, instance):
        return instance.transfers_cumulative_count

    related_transfers_cumulative_count.short_description = 'Related transfers (in tree)'


class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'comment', 'transfer', 'user', 'status']
    list_filter = ['status']


admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin2)
admin.site.register(Transfer, TransferAdmin)
admin.site.register(Images, ImagesAdmin)
