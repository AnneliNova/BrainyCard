from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt

from main_win import *
from random import shuffle, randint

class Question():
    def __init__ (self, question = "", answer = "", wrong_ans1 = "", wrong_ans2 = "", wrong_ans3 = ""):
        self.question = question
        self.answer = answer
        self.wrong_ans1 = wrong_ans1
        self.wrong_ans2 = wrong_ans2
        self.wrong_ans3 = wrong_ans3
        self.is_active = True
        self.attempts = 0
        self.correct = 0
    
    def got_right(self):
        self.attempts += 1
        self.correct += 1

    def got_wrong(self):
        self.attempts += 1

class QuestionView():
    def __init__ (self, frm_model, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.frm_model = frm_model
        self.question = question
        self.answer = answer
        self.wrong_ans1 = wrong_ans1
        self.wrong_ans2 = wrong_ans2
        self.wrong_ans3 = wrong_ans3

    def show(self):
        self.question.setText(self.frm_model.question)
        self.answer.setText(self.frm_model.answer)
        self.wrong_ans1.setText(self.frm_model.wrong_ans1)
        self.wrong_ans2.setText(self.frm_model.wrong_ans2)
        self.wrong_ans3.setText(self.frm_model.wrong_ans3)

    def change(self, frm_model):
        self.frm_model = frm_model

class QuestionEdit(QuestionView):
    def save_question(self):
        self.frm_model.question = self.question.text()

    def save_answer(self):
        self.frm_model.answer = self.answer.text()

    def save_wrong(self):
        self.frm_model.wrong_ans1 = self.wrong_ans1.text()
        self.frm_model.wrong_ans2 = self.wrong_ans2.text()
        self.frm_model.wrong_ans3 = self.wrong_ans3.text()
    
    def set_connects(self):
        self.question.editingFinished.connect(self.save_question)
        self.answer.editingFinished.connect(self.save_answer)
        self.wrong_ans1.editingFinished.connect(self.save_wrong)
        self.wrong_ans2.editingFinished.connect(self.save_wrong)
        self.wrong_ans3.editingFinished.connect(self.save_wrong)

    def __init__ (self, frm_model, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        super().__init__(frm_model, question, answer, wrong_ans1, wrong_ans2, wrong_ans3)
        self.set_connects()
    
class AnswerCheck(QuestionView):
    def __init__ (self, frm_model, question, answer, wrong_ans1, wrong_ans2, wrong_ans3, showed_ans, result):
        super().__init__(frm_model, question, answer, wrong_ans1, wrong_ans2, wrong_ans3)
        self.showed_ans = showed_ans
        self.result = result

    def check(self):
        if self.answer.isChecked():
            self.result.setText("Правильно")
            self.showed_ans.setText(self.frm_model.answer)
            self.frm_model.got_right()
        else:
            self.result.setText("Неправильно")
            self.showed_ans.setText(self.frm_model.answer)
            self.frm_model.got_wrong()

class QuestionListModel(QAbstractListModel):
    def __init__ (self, parent = None):
        super().__init__(parent)
        self.form_list = []
    
    def rowCount (self, index):
        return len(self.form_list)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            form = self.form_list[index.row()]
            return form.question
        
    def insertRows (self, parent = QModelIndex()):
        position = len(self.form_list)
        self.beginInsertRows(parent, position, position)
        self.form_list.append(Question())
        self.endInsertRows()
        QModelIndex()
    
    def removeRows(self, position, parent = QModelIndex()):
        self.beginRemoveRows(parent, position, position)
        self.form_list.pop(position)
        self.endRemoveRows()
        return True

    def random_question(self):
        total = len(self.form_list)
        current = randint(0, total - 1)
        return self.form_list[current]
    
def random_AnswerCheck(list_model, w_question, widget_list, w_showed_answer, w_result):
    frm = list_model.random_question()
    shuffle(widget_list)
    frm_card = AnswerCheck(frm, w_question, widget_list[0], widget_list[1], 
                           widget_list[2], widget_list[3], w_showed_answer, w_result)
    return frm_card