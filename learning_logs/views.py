from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    """The home page for learning_log"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """show all topics"""

    # query db
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') # query db & sort result by date_added
    # build dictionary
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    '''Show a single topic and all its entries'''
    # query db
    topic = get_object_or_404(Topic,  id=topic_id)

    # Make sure the topic belongs to the current User
    check_topic_owner(topic, request)

    # build dictionary of entries
    entries = topic.entry_set.order_by('-date_added') # sort by date_added in reverse due to the minus sign
    context = {'topic': topic, 'entries': entries}

    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    '''Add a new topic'''
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = TopicForm()
    else:
        # POST data submitted; process data
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    '''Add a new entry for a particular topic'''
    # topic = Topic.objects.get(id=topic_id)
    topic = get_object_or_404(Topic, id=topic_id)

    # Make sure the topic belongs to the current User
    check_topic_owner(topic, request)

    if request.method != 'POST':
        # No data submitted create a blank form
        form = EntryForm()
    else:
        # POST data submitted; process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic

            new_entry.save()
            print("REGEX ERROR!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    # entry = Entry.objects.get(id=entry_id)
    entry = get_object_or_404(Entry, id=entry_id)
    topic =  entry.topic

    # Make sure the topic belongs to the current User
    check_topic_owner(topic, request)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                        args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

# refactor
def check_topic_owner(topic, request):
    '''check if the user trying to acess a topic is logged in'''
    if topic.owner != request.user:
        raise Http404

# for cutom error pages
def handler404(request, exception):
    '''Show 404 cutom error page'''
    return render(request, 'learning_log/404.html', status=404)

def handler500(request):
    '''Show 500 error page'''
    return render(request, 'learning_log/500.html', status=500)
