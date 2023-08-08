from django import template
from ..models import SlideShow

register = template.Library()

@register.inclusion_tag('SlideShow/slideshow.html')
def slideshow(self):
	return {
	'slides':SlideShow.objects.filter(status=True,article__status=True)
	}