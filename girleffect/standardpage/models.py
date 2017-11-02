from django.db import models
from django.conf import settings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, MultiFieldPanel,
    StreamFieldPanel
)

from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel

from girleffect.utils.blocks import StoryBlock
from girleffect.utils.models import (
    ListingFields,
    SocialFields
)


class StandardPage(Page, SocialFields, ListingFields):
    hero_image = models.ForeignKey(
        'images.CustomImage',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.SET_NULL
    )
    hero_heading = models.CharField(
        max_length=80,
        blank=True,
        help_text="Heading that will appear over the hero image."
    )
    introduction = models.TextField(blank=True)
    body = StreamField(StoryBlock())
    call_to_action = models.ForeignKey(
        'utils.CallToActionSnippet',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('hero_heading'),
        index.SearchField('introduction'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                ImageChooserPanel('hero_image'),
                FieldPanel('hero_heading'),
            ],
            heading="Hero"
        ),
        FieldPanel('introduction'),
        StreamFieldPanel('body'),
        SnippetChooserPanel('call_to_action'),

    ]

    promote_panels = Page.promote_panels + SocialFields.promote_panels + ListingFields.promote_panels


class ParentPage(Page, SocialFields):
    hero_image = models.ForeignKey(
        'images.CustomImage',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.SET_NULL
    )
    hero_heading = models.CharField(
        max_length=80,
        blank=True,
        help_text="Heading that will appear over the hero image."
    )
    body = StreamField(StoryBlock())

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                ImageChooserPanel('hero_image'),
                FieldPanel('hero_heading'),
            ],
            heading="Hero"
        ),
        StreamFieldPanel('body'),

    ]

    search_fields = Page.search_fields + [
        index.SearchField('hero_heading'),
    ]

    promote_panels = Page.promote_panels + SocialFields.promote_panels
    subpage_types = ['solutions.SolutionPage', 'countries.CountryPage']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        subpages = self.get_children().live()
        per_page = settings.DEFAULT_PER_PAGE
        page_number = request.GET.get('page')
        paginator = Paginator(subpages, per_page)

        try:
            subpages = paginator.page(page_number)
        except PageNotAnInteger:
            subpages = paginator.page(1)
        except EmptyPage:
            subpages = paginator.page(paginator.num_pages)

        context['subpages'] = subpages

        return context
