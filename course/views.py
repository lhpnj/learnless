from django.shortcuts import render
from django.views import generic
from .models import Subject, Course
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'course/index.html'
    context_object_name = 'latest_course_list'

    def get_queryset(self):
        """
        Return the last five published courses (not including those set to be
        published in the future).
        """
        return Course.objects.filter(
            mod_date__lte=timezone.now()
        ).order_by('-mod_date')[:5]


class DetailView(generic.DetailView):
    model = Course
    template_name = 'course/detail.html'
