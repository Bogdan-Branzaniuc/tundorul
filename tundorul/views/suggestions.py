from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
import requests


class Suggestions(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'suggestions.html',
        )

    def post(self, request, *args, **kwargs):
        return render(
            request,
            'suggestions.html',
        )

