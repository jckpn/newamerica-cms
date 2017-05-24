import django_filters

from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.serializers import ListSerializer

from wagtail.wagtailcore.models import Page

from home.models import Post, HomePage
from person.models import Person
from serializers import PostSerializer, AuthorSerializer, ProgramSerializer, ProjectSerializer, HomeSerializer, TopicSerializer
from helpers import content_types, get_subpages
from programs.models import Program, Subprogram
from issue.models import IssueOrTopic
from event.models import Event
from rest_framework import mixins

class PostFilter(django_filters.rest_framework.FilterSet):
    id = django_filters.CharFilter(name='id', lookup_expr='iexact')
    program_id = django_filters.CharFilter(name='parent_programs__id', lookup_expr='iexact')
    project_id = django_filters.CharFilter(name='post_subprogram__id', lookup_expr='iexact')
    topic_id = django_filters.CharFilter(name='topic__id', lookup_expr='iexact')
    after = django_filters.DateFilter(name='date', lookup_expr='gte')
    before = django_filters.DateFilter(name='date', lookup_expr='lte')
    content_type = django_filters.CharFilter(name='content_type__model')

    class Meta:
        model = Post
        fields = ['id', 'program_id', 'project_id', 'before', 'after', 'content_type', 'topic_id']

class PostList(generics.ListAPIView):
    serializer_class = PostSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = PostFilter

    def get_queryset(self):
        ids = self.request.query_params.getlist('id[]', None)
        posts = Post.objects.live().order_by('-date').not_type(Event)
        if not ids:
            return posts

        return posts.filter(id__in=ids)


# class TopicFilter(django_filters.rest_framework.FilterSet):
#     id = django_filters.CharFilter(name='id', lookup_expr='iexact')
#     program_id = django_filters.CharFilter(name='parent_programs__id', lookup_expr='iexact')
#
#     class Meta:
#         model = IssueOrTopic
#         fields = ['id', 'program_id']

# class TopicList(generics.ListAPIView):
#     serializer_class = TopicSerializer
#     filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
#     filter_class = TopicFilter
#
#     def get_queryset(self):
#         ids = self.request.query_params.getlist('id[]', None)
#
#         if not ids:
#             return Post.objects.live()
#
#         return Post.objects.live().filter(id__in=ids)

class AuthorFilter(django_filters.rest_framework.FilterSet):
    id = django_filters.CharFilter(name='id', lookup_expr='iexact')
    program_id = django_filters.CharFilter(name='belongs_to_these_programs__id', lookup_expr='iexact')
    project_id = django_filters.CharFilter(name='belongs_to_these_subprograms__id', lookup_expr='iexact')
    topic_id = django_filters.CharFilter(name='topic__id', lookup_expr='iexact')
    name = django_filters.CharFilter(name='title', lookup_expr='icontains')

    class Meta:
        model = Person
        fields = ['id','program_id', 'project_id', 'topic_id', 'name']

class AuthorList(generics.ListAPIView):
    queryset = Person.objects.live().order_by('last_name')
    serializer_class = AuthorSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = AuthorFilter

class MetaList(APIView):
    def get(self, request, format=None):
        subpages = get_subpages(HomePage)
        programs = ProgramSerializer(Program.objects.live(), many=True).data
        projects = ProjectSerializer(Subprogram.objects.live(), many=True).data
        home = HomeSerializer(HomePage.objects.live().first()).data

        return Response({
            'count': None,
            'next': None,
            'previous': None,
            'results': {
                'subpages': subpages,
                'programs': programs,
                'projects': projects,
                'home': home
            }
        })

class ContentList(APIView):
    def get(self, request, format=None):
        types = content_types(request)
        return Response({
            'count': len(types),
            'next': None,
            'previous': None,
            'results': types
        })

class ProgramFilter(django_filters.rest_framework.FilterSet):
    id = django_filters.CharFilter(name='id', lookup_expr='iexact')

    class Meta:
        model = Program
        fields = ['id',]

class ProgramList(generics.ListAPIView):
    queryset = Program.objects.in_menu().live().order_by('title').exclude(location=True)
    serializer_class = ProgramSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = ProgramFilter

class ProjectFilter(django_filters.rest_framework.FilterSet):
    id = django_filters.CharFilter(name='id', lookup_expr='iexact')

    class Meta:
        model = Subprogram
        fields = ['id',]

class ProjectList(generics.ListAPIView):
    queryset = Subprogram.objects.live().order_by('title')
    serializer_class = ProjectSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = ProjectFilter
