"""
Create or customize your page models here.
"""

from aratinga.models import AratingaArticlePage, AratingaArticleIndexPage, AratingaWebPage
from django.utils.translation import gettext_lazy as _
from wagtail.models import Site


class ArticlePage(AratingaArticlePage):
    """
    Article, suitable for news or blog content.
    """

    class Meta:
        verbose_name = _("Article")
        ordering = ["-first_published_at"]

    # Only allow this page to be created beneath an ArticleIndexPage.
    parent_page_types = ["website.ArticleIndexPage"]

    template = "pages/article_page.html"
    search_template = "pages/article_page.search.html"


class ArticleIndexPage(AratingaArticleIndexPage):
    """
    Shows a list of article sub-pages.
    """

    class Meta:
        verbose_name = _("Article Landing Page")

    # Override to specify custom index ordering choice/default.
    index_query_pagemodel = "website.ArticlePage"

    # Only allow ArticlePages beneath this page.
    subpage_types = ["website.ArticlePage"]

    template = "pages/article_index_page.html"


class WebPage(AratingaWebPage):
    """
    General use page with featureful streamfield.
    """

    class Meta:
        verbose_name = _("Web Page")

    template = "pages/web_page.html"

    def get_context(self, request):
        context = super().get_context(request)
        site = Site.find_for_request(request)  # acessa o site da requisição
        context['site_name'] = site.site_name       # adiciona o nome ao contexto
        return context
