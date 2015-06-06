from django.contrib import admin
from .models import HomePage, Slide, IconBlurb, Portfolio, PortfolioItemImage, PortfolioItem, PortfolioItemCategory, TextSlider, DocumentListItem, DocumentList, DocumentListItemCategory, Item, Porter
from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin

class ItemInline(TabularDynamicInlineAdmin):
    model = Item

class PorterInline(TabularDynamicInlineAdmin):
    model = Porter

class SlideInline(TabularDynamicInlineAdmin):
    model = Slide

class IconBlurbInline(TabularDynamicInlineAdmin):
    model = IconBlurb

class PortfolioItemImageInline(TabularDynamicInlineAdmin):
    model = PortfolioItemImage

class TextSliderInline(TabularDynamicInlineAdmin):
    model = TextSlider

class HomePageAdmin(PageAdmin):
    inlines = (SlideInline, IconBlurbInline, TextSliderInline, PorterInline)

class PortfolioItemAdmin(PageAdmin):
    inlines = (PortfolioItemImageInline,)

class DocumentListItemInline(TabularDynamicInlineAdmin):
    model = DocumentListItem

class DocumentListAdmin(PageAdmin):
    inlines = (DocumentListItemInline,)

class PortfolioAdmin(PageAdmin):
    inlines = (ItemInline,)

admin.site.register(HomePage, HomePageAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(PortfolioItem, PortfolioItemAdmin)
admin.site.register(PortfolioItemCategory)
admin.site.register(DocumentList, DocumentListAdmin)
admin.site.register(DocumentListItemCategory)
