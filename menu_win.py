from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QLineEdit, QFormLayout)

from app import app

txt_question = QLineEdit("")
txt_ans = QLineEdit("")
txt_wrong1 = QLineEdit("")
txt_wrong2 = QLineEdit("")
txt_wrong3 = QLineEdit("")

layout_form = QFormLayout()

layout_form.addRow("Питання: ", txt_question)
layout_form.addRow("Правильна відповідь: ", txt_ans)
layout_form.addRow("Невірна відповідь 1: ", txt_wrong1)
layout_form.addRow("Невірна відповідь 2: ", txt_wrong2)
layout_form.addRow("Невірна відповідь 3: ", txt_wrong3)
