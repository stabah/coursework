from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from gistogramm.models import Gistogramm,Choice
from django.template import Context, loader

def index(request):
    question = Gistogramm.objects.all().order_by('-pub_date')[0]
    return render_to_response('question.html', {'question': question})


def answer(request):
    #question = Gistogramm.objects.all().order_by('-pub_date')[0]
    #print request.GET['G_ID']
    
    question = get_object_or_404(Gistogramm, pk=request.GET['G_ID'])
    try:
        print request.GET['Answer']
        mychoice = question.choice_set.get(pk=request.GET['Answer'])
        
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('', {
            'question': question,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        mychoice.votes += 1
        mychoice.save()
        
    return render_to_response('result.html', {'question': question})
