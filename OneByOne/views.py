from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import *
from validate_email import *
from django.core.exceptions import ValidationError
import random
# Create your views here.


def register(request):
    return render(request,'OneByOne/register.html')

def register_done(request):

    if request.method=="POST":
        if request.POST['firstname'] and request.POST['lastname'] and request.POST['email'] and request.POST['city'] and request.POST['country'] and request.POST['age']:
            # print('Hello')
            user=UserDetails()
            try:
                # check if email is valid or not
                email = request.POST['email']
                try:
                    validate_email(email)
                except ValidationError as e:
                    return render(request,'OneByOne/register.html',{'error':'Please verify your email.'})
                user.email=email
                user.first_name = request.POST['firstname']
                user.last_name = request.POST['lastname']
                user.age = request.POST['age']

                option = request.POST.get("option",None)
                if option in ["Male","Female","Other"]:
                    if option=="Male":
                        user.gender="Male"
                    elif option=="Female":
                        user.gender="Female"
                    elif option=="Other":
                        user.gender="Other"
                else:
                    return render(request, 'OneByOne/register.html',
                                      {'error': 'All fields are required.'})

                user.city = request.POST['city']
                user.country = request.POST['country']

                if 'terms' not in request.POST:
                    return render(request, 'OneByOne/register.html', {'error': 'Please accept the terms and conditions.'})

                user.save()
                request.session['user_id'] = user.id
                request.session['iteration'] = 1
                request.session['list_of_stimuli'] = []
                request.session['list_of_questions'] = []
                request.session['flag'] = True
            except ValueError as e:
                return render(request,'OneByOne/register.html',{'error':'Incorrect values.Please try again.'})

            return render(request,'OneByOne/display_stimuli_instruction.html')
        else:
            return render(request,'OneByOne/register.html',{'error':'All fields are required.'})
    else:
        return render(request,'OneByOne/register.html')



def show_stimuli_one_by_one(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
    #What to do if the session expires?
    user = get_object_or_404(UserDetails,pk=user_id)
    if request.session['iteration']==1:
        # print("In iteration 1")
        request.session['list_of_stimuli'] = list(Stimuli.objects.all().values_list('id', flat=True))
        # print("declared list")
        # print(request.session['list_of_stimuli'])
        id = request.session['list_of_stimuli'][request.session['iteration']-1]
        # helper = request.session['list_of_stimuli'][0].id
        helper=Stimuli.objects.get(pk=id)
        # print("ID",helper)
        # print("declared helper")
        # request.session['list_of
        # _stimuli'] = request.session['list_of_stimuli'][1:]
        # print("reinitializing list")
    else:
        # helper = request.session['list_of_stimuli'][0].id
        id = request.session['list_of_stimuli'][request.session['iteration']-1]
        helper = Stimuli.objects.get(pk=id)
    # helper = Stimuli.objects.first().id
    if request.method=='POST':
        num1 = random.randrange(2, 12, 1)
        num2 = random.randrange(2, 12, 1)
        num3 = random.randrange(2, 12, 1)
        num4 = random.randrange(2, 12, 1)
        num5 = random.randrange(2, 12, 1)
        num6 = random.randrange(2, 12, 1)
        num7 = random.randrange(2, 12, 1)
        num8 = random.randrange(2, 12, 1)
        context = {'num1': num1, 'num2': num2, 'num3': num3, 'num4': num4, 'num5': num5, 'num6': num6, 'num7': num7,
                   'num8': num8}
        request.session['context'] = context
        return render(request,'OneByOne/distractor.html',context)

    context = {
        'picture':helper,
    }

    return render(request, 'OneByOne/stimuli_display.html',context)



def save_responses(request):

    if request.method == "POST":
        user_response = UserResponses()
        try:
            option = request.POST.get("category",None)
            if option=='A':
                user_response.choice = 'A'
            else:
                user_response.choice = 'B'
            uid = request.session['user_id']
            user_response.user_id = UserDetails.objects.get(pk=uid)
            qid=request.session['question_id']
            user_response.choice_corr = Question.objects.get(pk=qid)
            user_response.iteration=request.session['iteration']
            user_response.save()


        except ValueError as e:
            return render(request,'OneByOne/question.html',{'error':'Please select either one of the categories.Go back to do so.'})


    if 'user_id' in request.session:
        user_id = request.session['user_id']
    #What to do if the session expires?
    user = get_object_or_404(UserDetails,pk=user_id)
    user_attended_questions = user.question_attended.all()
    helper = list(Question.objects.exclude(id__in=user_attended_questions))
    if (len(helper)==0 and request.session['iteration']==4):
        question_features = QuestionFeatures.objects.first()
        qid = QuestionFeatures.objects.first().id
        choice_features = ChoiceFeatures.objects.select_related().filter(question_rel=qid)

        context = {
            'question':question_features,
            'options': choice_features
        }
        return render(request,'OneByOne/question_feature.html',context)
    if (len(helper)==0 and request.session['iteration']<4):
        user.question_attended.set([])
        request.session['iteration']+=1
        context = {'iteration_done':request.session['iteration']-1,'iteration_left':5-request.session['iteration']}
        return render(request,'OneByOne/redo_quiz.html',context)
    random.shuffle(helper)
    helper = helper[0].id


    context = {
        'question':Question.objects.get(pk=helper),
        'options':Choice.objects.select_related().filter(question=helper)
    }
    request.session['question_id']=helper
    helper=Question.objects.get(pk=helper)
    user.question_attended.add(helper)

    return render(request, 'OneByOne/question.html',context)

def save_responses_features(request):
    if request.method=="POST":
        try:
            feature = request.POST.getlist("feature", None)
            if feature !=[]:
                user_response = UserResponsesForFeatures()
                if 'feature1' in feature:
                    print("I am here")
                    user_response.choice_1 = True
                if 'feature2' in feature:
                    user_response.choice_2 = True
                if 'feature3' in feature:
                    user_response.choice_3 = True
                if 'feature4' in feature:
                    user_response.choice_4 = True
                if 'feature5' in feature:
                    user_response.choice_5 = True
                if 'Color for classification' in feature:
                    user_response.choice_6 = True
                if 'None of the above' in feature:
                    user_response.choice_7 = True
                uid = request.session['user_id']
                user_response.user_id = UserDetails.objects.get(pk=uid)
                user_response.choice_corr = QuestionFeatures.objects.first()
                user_response.save()

            else:
                return render(request, 'OneByOne/question_feature.html', {'error': 'Please select atleast one option from the following'})

        except ValueError as e:
            return render(request,'OneByOne/question_feature.html.html',{'error':'Please select atleast one option from the following'})

    # return render(request,'OneByOne/thankyou.html')
    return render(request, 'OneByOne/description.html')

def save_responses_description(request):
    if request.method=="POST":
        try:
            desc = request.POST.get('description',None)
            print(desc)
            if len(desc)!=0:
                user_response = UserResponsesForDescription()
                user_response.description=desc
                uid = request.session['user_id']
                user_response.user_id = UserDetails.objects.get(pk=uid)
                user_response.save()

            else:
                return render(request, 'OneByOne/description.html', {'error': 'Please fill in the description'})

        except ValueError as e:
            return render(request,'OneByOne/question_feature.html',{'error':'Please fill in the description'})

    return render(request,'OneByOne/thankyou.html')

def contact(request):
    return render(request,'OneByOne/contact.html')

def about(request):
    return render(request,'OneByOne/about.html')

def terms(request):
    return render(request,'OneByOne/terms.html')


def instructions(request):
    if request.method=="POST":
        prod1 = request.session['context']['num1']*request.session['context']['num2']
        prod2 = request.session['context']['num3']*request.session['context']['num4']
        prod3 = request.session['context']['num5']*request.session['context']['num6']
        prod4 = request.session['context']['num7']*request.session['context']['num8']
        if request.POST['quantity1']!=str(prod1):
            return render(request,'OneByOne/distractor.html',{'error':'Please get the right answer for the first question.','num1': request.session['context']['num1'], 'num2': request.session['context']['num2'], 'num3': request.session['context']['num3'], 'num4': request.session['context']['num4'], 'num5': request.session['context']['num5'], 'num6': request.session['context']['num6'], 'num7': request.session['context']['num7'],
                   'num8': request.session['context']['num8']})
        elif request.POST['quantity2']!=str(prod2):
            return render(request, 'OneByOne/distractor.html',{'error': 'Please get the right answer for the second question.','num1': request.session['context']['num1'], 'num2': request.session['context']['num2'], 'num3': request.session['context']['num3'], 'num4': request.session['context']['num4'], 'num5': request.session['context']['num5'], 'num6': request.session['context']['num6'], 'num7': request.session['context']['num7'],
                   'num8': request.session['context']['num8']})
        elif request.POST['quantity3']!=str(prod3):
            return render(request, 'OneByOne/distractor.html',{'error': 'Please get the right answer for the third question.','num1': request.session['context']['num1'], 'num2': request.session['context']['num2'], 'num3': request.session['context']['num3'], 'num4': request.session['context']['num4'], 'num5': request.session['context']['num5'], 'num6': request.session['context']['num6'], 'num7': request.session['context']['num7'],
                   'num8': request.session['context']['num8']})
        elif request.POST['quantity4']!=str(prod4):
            return render(request, 'OneByOne/distractor.html',{'error': 'Please get the right answer for the fourth question.','num1': request.session['context']['num1'], 'num2': request.session['context']['num2'], 'num3': request.session['context']['num3'], 'num4': request.session['context']['num4'], 'num5': request.session['context']['num5'], 'num6': request.session['context']['num6'], 'num7': request.session['context']['num7'],
                   'num8': request.session['context']['num8']})
    return render(request,'OneByOne/instructions.html')

