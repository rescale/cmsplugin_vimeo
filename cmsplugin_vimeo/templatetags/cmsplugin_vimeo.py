from django import template
from cmsplugin_vimeo.models import Vimeo


register = template.Library()


class LatestVideosNode(template.Node):
    def __init__(self, count):
        self.count = count

    def render(self, context):
        videos = Vimeo.objects.order_by('-id')[:self.count]
        context['videos'] = videos
    return ''


@register.tag
def get_latest_videos(parser, token):
    tag_name, count = token.split_contents()
    return LatestVideosNode(int(count))
