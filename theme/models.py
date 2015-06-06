from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to


class HomePage(Page, RichTextField):
    '''
    A page representing the format of the home page
    '''
    heading = models.CharField(max_length=200,
        help_text="The heading under the icon blurbs")
    subheading = models.CharField(max_length=200,
        help_text="The subheading just below the heading")
    featured_works_heading = models.CharField(max_length=200,
        default="Featured Works")
    featured_portfolio = models.ForeignKey("Portfolio", blank=True, null=True,
        help_text="If selected items from this portfolio will be featured "
                  "on the home page.")
    content_heading = models.CharField(max_length=200,
        default="About us!")
    news_heading = models.CharField(max_length=255,
        default="Latest News",
        help_text="Heading for the news slider")
    latest_posts_heading = models.CharField(max_length=200,
        default="Latest Posts")
    content = RichTextField()


    class Meta:
        verbose_name = _("Home page")
        verbose_name_plural = _("Home pages")

class TextSlider(Orderable):
    '''
    A slider for content section connected to a HomePage
    '''
    
    homepage = models.ForeignKey(HomePage, related_name="textslider")
    heading = models.CharField(max_length=200)
    content = RichTextField(blank=True)
    link = models.CharField(max_length=2000, blank=True, null=True,
        help_text="Optional, if provided clicking the blurb will go here.")
    
class Porter(Orderable):
    '''
    more portfolio's to the home page
    '''
    
    homepage = models.ForeignKey(HomePage, blank=True, null=True, related_name="porter")
    multiport = models.ForeignKey("Portfolio", blank=True, null=True,
        help_text="If selected items from this portfolio will be featured "
                  "on the home page.")

class Slide(Orderable):
    '''
    A slide in a slider connected to a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name="slides")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("theme.Slide.image", "slider"),
        format="Image", max_length=255, null=True, blank=True)


class IconBlurb(Orderable):
    '''
    An icon box on a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name="blurbs")
    icon = FileField(verbose_name=_("Image"),
        upload_to=upload_to("theme.IconBlurb.icon", "icons"),
        format="Image", max_length=255)
    title = models.CharField(max_length=200)
    content = models.TextField()
    link = models.CharField(max_length=2000, blank=True,
        help_text="Optional, if provided clicking the blurb will go here.")


COLUMNS_CHOICES = (
    ('6', 'Two Columns'), #span6
    ('4', 'Three columns'), #span4
    ('3', 'Four columns'), #span3
)

class Portfolio(Page):
    '''
    A collection of individual portfolio items
    '''
    portfolio_item = models.ForeignKey("PortfolioItem", blank=True, null=True)
    content = RichTextField(blank=True)
    columns = models.CharField(max_length=1, choices=COLUMNS_CHOICES,
        default='3')
    class Meta:
        verbose_name = _("Portfolio")
        verbose_name_plural = _("Portfolios")

class Item(Orderable):
    '''
    Items to feature apart of the portfolio page
    '''
    portfolio = models.ForeignKey(Portfolio, related_name="items")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("theme.Item.image", "items"),
        format="Image", max_length=255, null=True, blank=True)
    content = models.CharField(max_length=500, blank=True, null=True)

class PortfolioItem(Page, RichText):
    '''
    An individual portfolio item, should be nested under a Portfolio
    '''
    featured_image = FileField(verbose_name=_("Featured Image"),
        upload_to=upload_to("theme.PortfolioItem.featured_image", "portfolio"),
        format="Image", max_length=255, null=True, blank=True)
    short_description = RichTextField(blank=True)
    categories = models.ManyToManyField("PortfolioItemCategory",
                                        verbose_name=_("Categories"),
                                        blank=True,
                                        related_name="portfolioitems")
    href = models.CharField(max_length=2000, blank=True,
        help_text="A link to the finished project (optional)")

    class Meta:
        verbose_name = _("Portfolio item")
        verbose_name_plural = _("Portfolio items")


class PortfolioItemImage(Orderable):
    '''
    An image for a PortfolioItem
    '''
    portfolioitem = models.ForeignKey(PortfolioItem, related_name="images")
    file = FileField(_("File"), max_length=200, format="Image",
        upload_to=upload_to("theme.PortfolioItemImage.file", "portfolio items"))

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")


class PortfolioItemCategory(Slugged):
    """
    A category for grouping portfolio items into a series.
    """

    class Meta:
        verbose_name = _("Portfolio Item Category")
        verbose_name_plural = _("Portfolio Item Categories")
        ordering = ("title",)   

class DocumentList(Page, RichText):
    '''
    A collection of Document list items
    '''

    heading = models.CharField(max_length=250,
        help_text="The heading for the Document list")

class DocumentListItemCategory(Slugged):
    '''
    A category for grouping document items into categories
    '''
    
    class Meta:
        verbose_name = _("Document List Item Category")
        verbose_name_plural = _("Document List Item Categories")
        ordering = ("title",) 

class DocumentListItem(Orderable):
    '''
    Individual documents for document list
    '''

    documentlist = models.ForeignKey(DocumentList, related_name="documents", blank=True, null=True)
    files = FileField(verbose_name=_("File"), null=True, blank=True,
        upload_to=upload_to("theme.DocumentListItem.file", "documents"))
    title = models.CharField(max_length=200)
    category = models.ForeignKey(DocumentListItemCategory, related_name="category", blank=True, null=True)

  

