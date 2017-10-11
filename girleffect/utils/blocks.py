from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailsnippets.blocks import SnippetChooserBlock

from .models import CallToActionSnippet


class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "blocks/image_block.html"


class QuoteBlock(blocks.StructBlock):
    quote = blocks.CharBlock(classname="title")
    citation_link = blocks.URLBlock(required=False)

    class Meta:
        icon = "openquote"
        template = "blocks/quote_block.html"


class LinkBlock(blocks.StructBlock):
    external_link = blocks.URLBlock(required=False, label="External Link")
    internal_link = blocks.PageChooserBlock(required=False, label="Internal Link")
    link_text = blocks.CharBlock(max_length=255)

    def get_context(self, value):
        link = value['internal_link'].url if value.get('internal_link') else value['external_link']

        context = super(LinkBlock, self).get_context(value)
        context.update({
            'link': link,
        })
        return context

    class Meta:
        template = "blocks/link_block.html"


class CarouselItemBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    label = blocks.CharBlock(max_length=255)
    text = blocks.RichTextBlock(required=False)

    class Meta:
        template = "blocks/carousel_item_block.html"

# Main streamfield block to be inherited by Pages


class StoryBlock(blocks.StreamBlock):
    heading = blocks.CharBlock(classname="full title")
    paragraph = blocks.RichTextBlock()
    image = ImageBlock()
    quote = QuoteBlock()
    embed = EmbedBlock()
    call_to_action = SnippetChooserBlock(CallToActionSnippet, template="includes/call_to_action.html")

    class Meta:
        template = "blocks/stream_block.html"
