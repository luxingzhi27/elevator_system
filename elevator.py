from enum import Enum
from add_passenger_ui import Ui_DialogAddPassenger
from PyQt5 import QtCore, QtGui, QtWidgets
from elevator_ui import Ui_MainWindow
from about_ui import Ui_Dialog
from threading import Thread


class Ui_UpdateAddPassengerDialog(Ui_DialogAddPassenger):
    def __init__(self, dialog: QtWidgets.QDialog) -> None:
        super().setupUi(dialog)
        self.currentFloor = 1
        self.direction = Direction.UP
        self.comboBox.currentIndexChanged.connect(
            self.handleCurrentFloorChanged)
        self.comboBox_2.currentIndexChanged.connect(
            self.handleDirectionChanged)

    def handleCurrentFloorChanged(self):
        self.currentFloor = int(self.comboBox.currentText())

    def handleDirectionChanged(self):
        if self.comboBox_2.currentText() == "up":
            self.direction = Direction.UP
        elif self.comboBox_2.currentText() == "down":
            self.direction = Direction.DOWN


class Direction(Enum):
    UP = 1
    DOWN = -1
    IDLE = 0


class Passenger():
    def __init__(self, id: int, currentFloor: int, direction: Direction) -> None:
        self.id = id
        self.currentFloor = currentFloor
        self.direction = direction
        self.aimFloor = 1


class Elevator():
    def __init__(self, id: int) -> None:
        self.id = id
        self.currentFloor = 1
        self.direction = Direction.UP
        from queue import PriorityQueue as pq
        self.stops = pq()
        self.passengers = []

    def reset(self):
        self.currentFloor = 1
        self.direction = Direction.UP
        self.stops = []
        self.passengers = []
        self.passengerID = 1

    def addPassenger(self, passenger: Passenger):
        self.passengers.append(passenger)
        self.stops.put(passenger.aimFloor)

    def getPassengerNum(self) -> int:
        return len(self.passengers)

    def up(self) -> bool:
        if self.currentFloor == 20:
            return False
        self.currentFloor += 1
        return True

    def down(self):
        if self.currentFloor == 1:
            return False
        self.currentFloor -= 1
        return True


class ElevatorSystem():
    def __init__(self) -> None:
        self.elevatorNum = 5
        self.elevators = [Elevator(1), Elevator(2),
                          Elevator(3), Elevator(4), Elevator(5)]
        self.elevatorCapacity = 10
        self.floorNum = 10
        self.passengerID = 1
        self.passengers = []
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mainWindow)
        self.reset()
        self.updateUi()

    def updateUi(self):
        self.listenResetButton()
        self.listenAddPassengerButton()
        self.listenAboutButton()

    def resetUi(self):
        self.ui.lcdNumber_1.setProperty(
            "value", 1)
        self.ui.lcdNumber_2.setProperty(
            "value", 1)
        self.ui.lcdNumber_3.setProperty(
            "value", 1)
        self.ui.lcdNumber_4.setProperty(
            "value", 1)
        self.ui.lcdNumber_5.setProperty(
            "value", 1)
        self.ui.elevator1EnterButton.setDisabled(True)
        self.ui.elevator2EnterButton.setDisabled(True)
        self.ui.elevator3EnterButton.setDisabled(True)
        self.ui.elevator4EnterButton.setDisabled(True)
        self.ui.elevator5EnterButton.setDisabled(True)

    def reset(self):
        for evevaltor in self.elevators:
            evevaltor.reset()
        self.passengers = []
        self.passengerID = 1
        self.resetUi()

    def chooseElevator(self, passenger: Passenger) -> int:
        """choose a elevator"""
        sameDirectionElevators = []
        for elevator in self.elevators:
            if (elevator.currentFloor-passenger.currentFloor)*elevator.direction.value <= 0:
                sameDirectionElevators.append(elevator)
        if not sameDirectionElevators:
            return self.elevators[0].id
        else:
            elevator = min(sameDirectionElevators, key=lambda x: abs(
                x.currentFloor-passenger.currentFloor))
            return elevator.id

    def addPassenger(self, currentFloor: int, direction: Direction.UP):
        passenger = Passenger(self.passengerID, currentFloor, direction)
        self.passengers.append(
            passenger)
        self.passengerID += 1
        eleID = self.chooseElevator(passenger)
        self.printPassengers()

    def listenResetButton(self):
        self.ui.resetButton.clicked.connect(self.reset)

    def listenAddPassengerButton(self):
        self.ui.addPassengerButton.clicked.connect(self.handleAddPassenger)

    def listenAboutButton(self):
        self.ui.aboutButton.clicked.connect(self.handleAbout)

    def handleAbout(self):
        aboutDialog = QtWidgets.QDialog()
        aboutUi = Ui_Dialog()
        aboutUi.setupUi(aboutDialog)
        aboutDialog.exec_()

    def handleAddPassenger(self):
        addPassengerDialog = QtWidgets.QDialog()
        addPassengerUi = Ui_UpdateAddPassengerDialog(addPassengerDialog)
        addPassengerDialog.exec_()
        # print(addPassengerUi.currentFloor, addPassengerUi.direction)
        self.addPassenger(addPassengerUi.currentFloor,
                          addPassengerUi.direction)

    def printPassengers(self):
        for passenger in self.passengers:
            print(passenger.currentFloor, passenger.direction)

    def testElevator(self):
        """test elevatpors running
        """
        while self.testElevatorRunning:
            while self.elevatorUp(1):
                import time
                time.sleep(1)

            while self.elevatorDown(1):
                import time
                time.sleep(1)

    def elevatorUp(self, eleID: int) -> bool:
        if self.elevators[eleID-1].up():   # id begin with 1
            if eleID == 1:
                self.ui.lcdNumber_1.setProperty(
                    "value", self.elevators[eleID-1].currentFloor)
                self.ui.elevator1DownButton.setStyleSheet(
                    "QPushButton{color: black}")
                self.ui.elevator1UpButton.setStyleSheet(
                    "QPushButton{color: green}")
                return True
            elif eleID == 2:
                self.ui.lcdNumber_2.setProperty(
                    "value", self.elevators[eleID-1].currentFloor)
                self.ui.elevator2DownButton.setStyleSheet(
                    "QPushButton{color: black}")
                self.ui.elevator2UpButton.setStyleSheet(
                    "QPushButton{color: green}")
                return True
            elif eleID == 3:
                self.ui.lcdNumber_3.setProperty(
                    "value", self.elevators[eleID-1].currentFloor)
                self.ui.elevator3DownButton.setStyleSheet(
                    "QPushButton{color: black}")
                self.ui.elevator3UpButton.setStyleSheet(
                    "QPushButton{color: green}")
                return True
            elif eleID == 4:
                self.ui.lcdNumber_4.setProperty(
                    "value", self.elevators[eleID-1].currentFloor)
                self.ui.elevator4DownButton.setStyleSheet(
                    "QPushButton{color: black}")
                self.ui.elevator4UpButton.setStyleSheet(
                    "QPushButton{color: green}")
                return True
            elif eleID == 5:
                self.ui.lcdNumber_5.setProperty(
                    "value", self.elevators[eleID-1].currentFloor)
                self.ui.elevator5DownButton.setStyleSheet(
                    "QPushButton{color: black}")
                self.ui.elevator5UpButton.setStyleSheet(
                    "QPushButton{color: green}")
                return True
        return False

    def elevatorDown(self, eleID: int) -> bool:
        if self.elevators[eleID-1].down():   # id begin with 1
            if eleID == 1:
                self.ui.lcdNumber_1.setProperty(
                    "value", self.elevators[eleID-1].currentFloor)
                self.ui.elevator1UpButton.setStyleSheet(
                    "QPushButton{color: black}")
                self.ui.elevator1DownButton.setStyleSheet(
                    "QPushButton{color: green}")
                return True
            elif eleID == 2:
                self.ui.lcdNumber_2.setProperty(
                    "value", self.elevators[eleID-1].currentFloor)
                self.ui.elevator2UpButton.setStyleSheet(
                    "QPushButton{color: black}")
                self.ui.elevator2DownButton.setStyleSheet(
                    "QPushButton{color: green}")
                return True
            elif eleID == 3:
                self.ui.lcdNumber_3.setProperty(
                    "value", self.elevators[eleID-1].currentFloor)
                self.ui.elevator3UpButton.setStyleSheet(
                    "QPushButton{color: black}")
                self.ui.elevator3DownButton.setStyleSheet(
                    "QPushButton{color: green}")
                return True
            elif eleID == 4:
                self.ui.lcdNumber_4.setProperty(
                    "value", self.elevators[eleID-1].currentFloor)
                self.ui.elevator4UpButton.setStyleSheet(
                    "QPushButton{color: black}")
                self.ui.elevator4DownButton.setStyleSheet(
                    "QPushButton{color: green}")
                return True
            elif eleID == 5:
                self.ui.lcdNumber_5.setProperty(
                    "value", self.elevators[eleID-1].currentFloor)
                self.ui.elevator5UpButton.setStyleSheet(
                    "QPushButton{color: black}")
                self.ui.elevator5DownButton.setStyleSheet(
                    "QPushButton{color: green}")
                return True
        return False


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    elevatorSystem = ElevatorSystem()
    elevatorSystem.mainWindow.show()
    sys.exit(app.exec_())
