from django import template
from cmsplugin_vimeo.models import Vimeo


register = template.Library()


class LatestVideosNode(template.Node):
    def __init__(self, count):
        self.count = count

    def render(self, context):
        videos = []
        for i in range(0, self.count):
            videos.push(Vimeo.objects.order_by('cmsplugin_ptr_id').last())
        context['videos'] = videos
    return ''


@register.tag
def get_latest_videos(parser, token):
    tag_name, count = token.split_contents()
    return LatestVideosNode(int(count))
