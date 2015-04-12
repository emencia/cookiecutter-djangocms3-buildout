from socialaggregator.formatter import RessourceFormatterDefault

class RessourceFormatterCustom(RessourceFormatterDefault):
    size_classes = {
        'small': 'w-sizer-1 h-sizer-1',
        'default': 'w-sizer-2 h-sizer-1',
        'medium': 'w-sizer-2 h-sizer-1',
        'large': 'w-sizer-2 h-sizer-2',
    }
    # CSS classes linked to social content type key name
    type_classes = {
        'edsa_facebook_fanpage': 'facebook',
        'edsa_twitter': 'twitter',
        'edsa_instagram': 'instagram',
        'edsa_wordpress_rss': 'article-wordpress',
        'edsa_pinterest': 'pinterest',
        'edsa_youtube': 'youtube',
        'edsa_youtube_search': 'youtube',
        # Articles content types are not real feed content
        'edsa_article': 'article-event',
        'edsa_article-infos': 'article-infos',
        'edsa_article-facebook': 'article-facebook',
        'edsa_article-twitter': 'article-twitter',
        'edsa_article-youtube': 'article-youtube',
    }
    
    def render(self):
        return {
            "id": self.instance.pk,
            "slug": self.instance.slug,
            "css_classes": self.get_css_classes(),
            "title": self.get_title(),
            "intro": self.get_intro(),
            "description": self.get_description(),
            "button": self.get_button(),
            "has_subblock": self.has_subblock(),
            "author": self.instance.author,
            "date": self.get_date(),
            "image": self.get_image(),
            "media": self.get_content_media(),
            "url": self.get_content_url(),
        }
    
    def get_content_url(self):
        # Allways return the media_url if not empty, even if the button is active
        if self.instance.media_url:
            return self.instance.media_url;
        return None
    
    def get_intro(self):
        if self.get_type() == 'article-infos':
            return self.instance.short_description
        return None
    
    def get_description(self):
        if self.get_type() == 'article-infos':
            return self.instance.description
        return self.instance.description or self.instance.short_description
    
    def get_button(self):
        if self.instance.media_url:
            return {
                'label': self.instance.button_label or 'En savoir plus',
                'color': self.instance.button_color,
                'url': self.instance.media_url,
            }
        return None
