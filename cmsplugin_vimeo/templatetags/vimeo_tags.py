from django import template
from cmsplugin_vimeo.models import Vimeo
import requests


register = template.Library()


class LatestVideosNode(template.Node):
    def __init__(self, count):
        self.count = count

    def render(self, context):
        videos = Vimeo.objects.order_by('-video_id').distinct(
            'video_id')[:self.count]

        s = requests.Session()
        a = requests.adapters.HTTPAdapter(max_retries=3)
        s.mount('https://', a)

        for v in videos:
            url = 'https://vimeo.com/api/v2/video/{0}.json'.format(v.video_id)
            r = s.get(url, timeout=5)

            if v.page:
                v.page_title = v.page.get_menu_title()
                v.page_link = v.page.get_absolute_url()
                try:
                    v.thumbnail = r.json()[0]['thumbnail_large']
                except ValueError:
                    v.thumbnail = ''

        context['videos'] = videos
        return ''


@register.tag
def get_latest_videos(parser, token):
    tag_name, count = token.split_contents()
    return LatestVideosNode(int(count))
