from django.core.urlresolvers import reverse
from django.test.testcases import SimpleTestCase

from .urls import urlpatterns


class TemplateRenderTestCase(SimpleTestCase):
    def test_all_views_should_render_template_on_get(self):
        self._run_tests_on_a_group_of_urls(urlpatterns, '')

    def _test_view_should_render_template_on_get(self, url):
        response = self.client.get(url)
        response.render()

        print(url)
        assert response.status_code == 200
        assert 'INVALID'.encode('utf-8') not in response.content

    def _run_tests_on_a_group_of_urls(self, urls, namespace):
        for url in urls:
            if hasattr(url, 'url_patterns'):
                joined_namespace = join_namespaces(namespace, url.namespace)
                self._run_tests_on_a_group_of_urls(url.url_patterns, joined_namespace)
            else:
                self._test_view_should_render_template_on_get(build_url(namespace, url))


def format_namespace(namespace):
    return '' if not namespace else '{}:'.format(namespace)


def join_namespaces(outer, inner):
    return '{outer}{inner}'.format(outer=format_namespace(outer), inner=inner)


def build_url(namespace, url):
    return reverse('{namespace}{url}'.format(
        namespace=format_namespace(namespace),
        url=url.name
    ))
