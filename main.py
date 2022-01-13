import sys
from PyQt5.QtWidgets import QApplication
from model.sokobanModel import SokobanModel
from view.sokobanView import SokobanView
from controller.sokobanController import SokobanController

app = QApplication(sys.argv)

model = SokobanModel()
view = SokobanView()
controller = SokobanController()

model.addView(view)
view.setModel(model)
view.setController(controller)
controller.setModel(model)
controller.setView(view)

view.show()

sys.exit(app.exec_())
