from django import template
from cmsplugin_vimeo.models import Vimeo
import requests


register = template.Library()


class LatestVideosNode(template.Node):
    def __init__(self, count):
        self.count = count

    def render(self, context):
        videos = list(Vimeo.objects.order_by('-id')[:self.count])

        for v in videos:
            r = requests.get('https://vimeo.com/api/v2/video/%s.json'
                             % v.video_id)
            v.page_title = v.page.get_menu_title()
            v.page_link = v.page.get_absolute_url()
            v.thumbnail = r.json()[0]['thumbnail_large']

        context['videos'] = videos
        return ''


@register.tag
def get_latest_videos(parser, token):
    tag_name, count = token.split_contents()
    return LatestVideosNode(int(count))
