from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
# from django.http import Http404
from django.urls import reverse

from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context=context)


# template = loader.get_template('polls/index.html')
#    return HttpResponse(template.render(context, request))
#    output = ', '.join([q.question_text for q in latest_question_list])
#    return HttpResponse(output)
#    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    template = loader.get_template('polls/detail.html')
    print(template.render({'question': question}, request))
    return render(request, 'polls/detail.html', {'question': question})

#    try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exist")
#    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
#    return HttpResponse("You're voting on question %s." % question_id)
