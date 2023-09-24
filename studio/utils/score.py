from studio import models


class Score(object):

    def __init__(self, request):
        info_dict = request.session.get("info")

        question_1 = models.ExamResult.objects.filter(username=info_dict.get("username"))
        self.result_1 = question_1[0].Result_1
        question_2 = models.ExamResult.objects.filter(username=info_dict.get("username"))
        self.result_2 = question_2[0].Result_2
        question_3 = models.ExamResult.objects.filter(username=info_dict.get("username"))
        self.result_3 = question_3[0].Result_3
        question_4 = models.ExamResult.objects.filter(username=info_dict.get("username"))
        self.result_4 = question_4[0].Result_4
        question_5 = models.ExamResult.objects.filter(username=info_dict.get("username"))
        self.result_5 = question_5[0].Result_5
        question_6 = models.ExamResult.objects.filter(username=info_dict.get("username"))
        self.result_6 = question_6[0].Result_6
        question_7 = models.ExamResult.objects.filter(username=info_dict.get("username"))
        self.result_7 = question_7[0].Result_7
        question_8 = models.ExamResult.objects.filter(username=info_dict.get("username"))
        self.result_8 = question_8[0].Result_8
        question_9 = models.ExamResult.objects.filter(username=info_dict.get("username"))
        self.result_9 = question_9[0].Result_9
        question_10 = models.ExamResult.objects.filter(username=info_dict.get("username"))
        self.result_10 = question_10[0].Result_10

        Q1 = models.QuestionObj.objects.filter(id=1)
        self.answer_1 = Q1[0].ans_1
        Q2 = models.QuestionObj.objects.filter(id=1)
        self.answer_2 = Q2[0].ans_2
        Q3 = models.QuestionObj.objects.filter(id=1)
        self.answer_3 = Q3[0].ans_3
        Q4 = models.QuestionObj.objects.filter(id=1)
        self.answer_4 = Q4[0].ans_4
        Q5 = models.QuestionObj.objects.filter(id=1)
        self.answer_5 = Q5[0].ans_5
        Q6 = models.QuestionObj.objects.filter(id=1)
        self.answer_6 = Q6[0].ans_6
        Q7 = models.QuestionObj.objects.filter(id=1)
        self.answer_7 = Q7[0].ans_7
        Q8 = models.QuestionObj.objects.filter(id=1)
        self.answer_8 = Q8[0].ans_8
        Q9 = models.QuestionObj.objects.filter(id=1)
        self.answer_9 = Q9[0].ans_9
        Q10 = models.QuestionObj.objects.filter(id=1)
        self.answer_10 = Q10[0].ans_10

    def score_obj_all(self):
        num = 6
        if self.result_1 == self.answer_1:
            score_1 = num
        else:
            score_1 = 0

        if self.result_2 == self.answer_2:
            score_2 = num
        else:
            score_2 = 0

        if self.result_3 == self.answer_3:
            score_3 = num
        else:
            score_3 = 0

        if self.result_4 == self.answer_4:
            score_4 = num
        else:
            score_4 = 0

        if self.result_5 == self.answer_5:
            score_5 = num
        else:
            score_5 = 0

        if self.result_6 == self.answer_6:
            score_6 = num
        else:
            score_6 = 0

        if self.result_7 == self.answer_7:
            score_7 = num
        else:
            score_7 = 0

        if self.result_8 == self.answer_8:
            score_8 = num
        else:
            score_8 = 0

        if self.result_9 == self.answer_9:
            score_9 = num
        else:
            score_9 = 0

        if self.result_10 == self.answer_10:
            score_10 = num
        else:
            score_10 = 0

        score = (score_1 + score_2 + score_3 + score_4 + score_5 + score_6 + score_7 + score_8 + score_9 + score_10)

        return score
