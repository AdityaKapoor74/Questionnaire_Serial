from django.db import models

# Question
class Question (models.Model):

    class Meta:
        verbose_name_plural="Questions"

    def __str__(self):
        return self.question_text_for_real_test

    question_text_for_real_test = models.CharField(max_length=300)


#Choice
class Choice(models.Model):

    class Meta:
        verbose_name_plural="Choice"

    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None, blank=True)

    sample1_A = models.ImageField(upload_to='images/')

class Stimuli(models.Model):

    class Meta:
        verbose_name_plural = "Stimuli"
    stimuli_1 = models.ImageField(upload_to='images/',default='Contrast00.png')
    stimuli_2 = models.ImageField(upload_to='images/',default='Contrast00.png')
    stimuli_3 = models.ImageField(upload_to='images/',default='Contrast00.png')
    stimuli_4 = models.ImageField(upload_to='images/',default='Contrast00.png')
    stimuli_5 = models.ImageField(upload_to='images/',default='Contrast00.png')
    stimuli_6 = models.ImageField(upload_to='images/',default='Contrast00.png')
    stimuli_7 = models.ImageField(upload_to='images/',default='Contrast00.png')
    stimuli_8 = models.ImageField(upload_to='images/',default='Contrast00.png')
    stimuli_9 = models.ImageField(upload_to='images/',default='Contrast00.png')
    stimuli_10 = models.ImageField(upload_to='images/',default='Contrast00.png')


#User Details for Registeration
class UserDetails(models.Model):

    class Meta:
        verbose_name_plural = "User Details"

    question_attended = models.ManyToManyField(Question)

    first_name = models.CharField(max_length=100,blank=True,null=True,default=None)
    last_name = models.CharField(max_length=100,blank=True,null=True,default=None)
    email = models.EmailField()
    gender = models.CharField(max_length=10,blank=True,null=True,default=None)
    city = models.CharField(max_length=100,blank=True,null=True,default=None)
    country = models.CharField(max_length=100,blank=True,null=True,default=None)
    age = models.IntegerField(blank=True, null=True, default=None)

    def __str__(self):
        return self.first_name+' '+self.last_name

class UserResponses (models.Model):

    class Meta:
        verbose_name_plural = "User Responses"

    choice = models.CharField(max_length=10, blank=True, null=True, default=None)
    user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    choice_corr = models.ForeignKey(Question, on_delete=models.CASCADE, default=None, blank=True)
    iteration = models.IntegerField(default=1)


class QuestionFeatures(models.Model):

    class Meta:
        verbose_name_plural="Feature Questions"

    def __str__(self):
        return self.question_text

    question_text = models.CharField(max_length=200)


class ChoiceFeatures(models.Model):

    class Meta:
        verbose_name_plural="Feature Choice"
    question_rel = models.ForeignKey(QuestionFeatures, on_delete=models.CASCADE, default=None, blank=True)
    feature1_A = models.ImageField(upload_to='images/')
    feature2_A = models.ImageField(upload_to='images/')
    feature1_B = models.ImageField(upload_to='images/')
    feature2_B = models.ImageField(upload_to='images/')
    feature1_C = models.ImageField(upload_to='images/')
    feature2_C = models.ImageField(upload_to='images/')
    feature1_D = models.ImageField(upload_to='images/')
    feature2_D = models.ImageField(upload_to='images/')
    feature1_E = models.ImageField(upload_to='images/')
    feature2_E = models.ImageField(upload_to='images/')


class UserResponsesForFeatures(models.Model):

    class Meta:
        verbose_name_plural = "User Responses for Features"

    choice_1 = models.BooleanField(default=False, verbose_name='Lower Fin')
    choice_2 = models.BooleanField(default=False, verbose_name='Tail')
    choice_3 = models.BooleanField(default=False, verbose_name='Upper Fin')
    choice_4 = models.BooleanField(default=False, verbose_name='Body Fin')
    choice_5 = models.BooleanField(default=False, verbose_name='Mouth')
    choice_6 = models.BooleanField(default=False, verbose_name='Color for classification')
    choice_7 = models.BooleanField(default=False, verbose_name='None of the above')

    user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE, default=None, blank=True)
    choice_corr = models.ForeignKey(QuestionFeatures,on_delete=models.CASCADE, default=None, blank=True)

class UserResponsesForDescription(models.Model):

    class Meta:
        verbose_name_plural = "User Responses for Description"

    description = models.TextField(default=None, null=True, blank=True)

    user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE, default=None, blank=True)