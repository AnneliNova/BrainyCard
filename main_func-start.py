from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget

from app import app
from main import *
from main_layout import *
from main_win import *
from menu_win import txt_ans, txt_question, txt_wrong1, txt_wrong2, txt_wrong3

main_width, main_height = 1000, 450
card_width, card_height = 600, 500
time_unit = 10

question_listmodel = QuestionListModel()
frm_edit = QuestionEdit(0, txt_question, txt_ans, txt_wrong1, txt_wrong2, txt_wrong3)
radio_list = [rbtn_ans1, rbtn_ans2, rbtn_ans3, rbtn_ans4]
frm_card = 0 
timer = QTimer()
win_card = QWidget()
win_main = QWidget()

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_next.setText("Наступне питання")

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_next.setText("Відповісти")
    RadioGroup.setExclusive(False)
    rbtn_ans1.setChecked(False)
    rbtn_ans2.setChecked(False)
    rbtn_ans3.setChecked(False)
    rbtn_ans4.setChecked(False)
    RadioGroup.setExclusive(True)

def test_list():
    frm = Question("Яблуко", "apple", "banana", "frog", "dog")
    question_listmodel.form_list.append(frm)
    frm = Question("Кіт", "cat", "dog", "goose", "chuck")
    question_listmodel.form_list.append(frm)
    frm = Question("Мавпа", "monkey", "doggo", "roof", "pigeon")
    question_listmodel.form_list.append(frm)
    frm = Question("Жаба", "frog", "dog", "goat", "roof")
    question_listmodel.form_list.append(frm)

def set_card():
    win_card.resize(card_width, card_height)
    win_card.move(300, 300)
    win_card.setWindowTitle('BrainyCard')
    win_card.setLayout(layout_card)

def sleep_card():
    win_card.hide()
    timer.setInterval(time_unit * sp_rest.value())
    timer.start()

def show_card():
    win_card.show()
    timer.stop()

def show_random():
    global frm_card
    frm_card = random_AnswerCheck(question_listmodel, lb_question, radio_list, lb_Correct, lb_Result)
    frm_card.show()
    show_question()

def click_OK():
    if btn_next.text() != "Наступне питання":
        frm_card.check()
        show_result()
    else:
        show_random()

def back_to_menu():
    win_card.hide()
    win_main.show()

def set_main():
    win_main.resize(main_width, main_height)
    win_main.move(300, 300)
    win_main.setWindowTitle("Перелік питань")
    win_main.setLayout(layout_main)

def edit_question(index):
    if index.isValid():
        i = index.row()
        frm = question_listmodel.form_list[i]
        frm_edit.change(frm)
        frm_edit.show()
    
def add_form():
    question_listmodel.insertRows()
    last = question_listmodel.rowCount(0) - 1
    index = question_listmodel.index(last)
    list_question.setCurrentIndex(index)
    edit_question(index)
    txt_question.setFocus(Qt.TabFocusReason)

def del_form():
    question_listmodel.removeRows(list_question.currentIndex().row())
    edit_question(list_question.currentIndex())

def start_test():
    show_random()
    win_card.show()
    win_main.showMinimized()

def connects():
    list_question.setModel(question_listmodel)
    list_question.clicked.connect(edit_question)
    btn_add.clicked.connect(add_form)
    btn_delete.clicked.connect(del_form)
    btn_start.clicked.connect(start_test)
    btn_next.clicked.connect(click_OK)
    btn_menu.clicked.connect(back_to_menu)
    timer.timeout.connect(show_card)
    btn_rest.clicked.connect(sleep_card)

test_list()
set_card()
set_main()
connects()
win_main.show()
app.exec_()