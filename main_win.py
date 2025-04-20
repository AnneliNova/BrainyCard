from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QButtonGroup, QRadioButton, 
       QPushButton, QLabel, QSpinBox)

from app import app

btn_menu = QPushButton('Меню')
btn_rest = QPushButton('Відпочити')
btn_next = QPushButton('Відповісти')
sp_rest = QSpinBox()
sp_rest.setValue(30)

lb_question = QLabel("")

RadioGroupBox = QGroupBox("Варіанти відповідей")

RadioGroup = QButtonGroup()

rbtn_ans1 = QRadioButton('1')
rbtn_ans2 = QRadioButton('2')
rbtn_ans3 = QRadioButton('3')
rbtn_ans4 = QRadioButton('4')

RadioGroup.addButton(rbtn_ans1)
RadioGroup.addButton(rbtn_ans2)
RadioGroup.addButton(rbtn_ans3)
RadioGroup.addButton(rbtn_ans4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_ans1)
layout_ans2.addWidget(rbtn_ans2)
layout_ans3.addWidget(rbtn_ans3)
layout_ans3.addWidget(rbtn_ans4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox("Результат тесту")
lb_Result = QLabel("")
lb_Correct = QLabel("")

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment = (Qt.AlignHCenter))
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_menu)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_rest)
layout_line1.addWidget(sp_rest)
layout_line1.addWidget(QLabel("хвилин"))

layout_line2.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)

layout_line4.addWidget(btn_next, stretch=2, alignment=Qt.AlignHCenter)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
 