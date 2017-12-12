# from django.conf.urls import (url, include)
# from snippet3 import views
#
# from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework import renderers
#
# user_list = views.UserViewSet.as_view({
#     'get': 'list',
# })
# user_detail = views.UserViewSet.as_view({
#     'get': 'retrieve',
# })
#
# snippet_list = views.SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = views.SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = views.SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
#
# urlpatterns = [
#     url(r'^users/$',
#         user_list,
#         name="user-list"),
#     url(r'^users/(?P<pk>[0-9]+)/$',
#         user_detail,
#         name="user-detail"),
#
#     url(r"^$", views.api_root),
#
#     url(r'^snippets/$',
#         snippet_list,
#         name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$',
#         snippet_detail,
#         name='snippet-detail'),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
#         snippet_highlight,
#         name='snippet-highlight'),
#
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)

# add urls.py more code,

from django.conf.urls import url, include
from snippet3 import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
