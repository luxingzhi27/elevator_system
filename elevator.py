import threading
from enum import Enum
from add_passenger_ui import Ui_DialogAddPassenger
from PyQt5 import QtCore, QtGui, QtWidgets
from elevator_ui import Ui_MainWindow
from about_ui import Ui_Dialog
from threading import Thread
from queue import PriorityQueue as pq
import queue
from get_aim_floor_ui import Ui_DialogGetAimFloor


class Direction(Enum):
    UP = 1
    DOWN = -1
    IDLE = 0


class ChooseELevatorThread(Thread):
    def __init__(self, func, queue:queue.Queue, args=()) -> None:
        super(ChooseELevatorThread,self).__init__()
        self.func = func
        self.args = args
        self.queue = queue

    def run(self) -> None:
        self.result = self.func(*self.args)
        self.queue.put(self.result)



class Passenger(object):
    def __init__(self, id: int, currentFloor: int, direction: Direction) -> None:
        self.id = id
        self.currentFloor = currentFloor
        self.direction = direction
        self.aimFloor = 1


class Elevator(object):
    def __init__(self, id: int) -> None:
        self.id = id
        self.currentFloor = 1
        self.stops = pq()
        self.passengers = []
        self.nextPassengers = [] # passengers who will get on the elevator
        self.direction = Direction.IDLE


    def reset(self):
        self.currentFloor = 1
        self.direction = Direction.IDLE
        self.stops = pq()
        self.passengers = []
        self.nextPassengers = []

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





class ElevatorSystem(object):
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
        chooseElevatorThread = ChooseELevatorThread(self.chooseElevator, args=(
            passenger,), queue=queue.Queue())
        chooseElevatorThread.start()
        chooseElevatorThread.join()
        elevatorID = chooseElevatorThread.queue.get()
        self.elevators[elevatorID-1].stops.put(passenger.aimFloor)
        self.elevators[elevatorID-1].nextPassengers.append(passenger)

    def listenResetButton(self):
        self.ui.resetButton.clicked.connect(self.reset)

    def listenAddPassengerButton(self):
        self.ui.addPassengerButton.clicked.connect(self.handleAddPassenger)

    def listenAboutButton(self):
        self.ui.aboutButton.clicked.connect(self.handleAbout)

    def listenEnterButton(self):
        self.ui.elevator1EnterButton.clicked.connect(lambda: self.handleEnterButton(1))
        self.ui.elevator2EnterButton.clicked.connect(lambda:self.handleEnterButton(2))
        self.ui.elevator3EnterButton.clicked.connect(lambda: self.handleEnterButton(3))
        self.ui.elevator4EnterButton.clicked.connect(lambda: self.handleEnterButton(4))
        self.ui.elevator5EnterButton.clicked.connect(lambda:self.handleEnterButton(5))

    def handleAbout(self):
        aboutDialog = QtWidgets.QDialog()
        aboutUi = Ui_Dialog()
        aboutUi.setupUi(aboutDialog)
        aboutDialog.exec_()

    def handleAddPassenger(self):
        addPassengerDialog = QtWidgets.QDialog()
        addPassengerUi = Ui_DialogAddPassenger()
        addPassengerUi.setupUi(addPassengerDialog)
        addPassengerDialog.exec_()
        # print(addPassengerUi.currentFloor, addPassengerUi.direction)
        currentFloor=int(addPassengerUi.comboBox.currentText())
        direction=Direction.IDLE
        if addPassengerUi.comboBox_2.currentText() == "up":
            direction = Direction.UP
        elif addPassengerUi.comboBox_2.currentText()== "down":
            direction = Direction.DOWN
        print(currentFloor, direction)
        self.addPassenger(currentFloor , direction)


    def printPassengers(self):
        for passenger in self.passengers:
            print(passenger.currentFloor, passenger.direction)

    def testElevator(self):
        """test elevatpors running
        """
        for i in range(1,2):
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

    def elevatorOpen(self,eleID:int):
        if eleID == 1:
            self.ui.elevator1OpenButton.setStyleSheet(
                "QPushButton{color: green}")
            self.ui.elevator1EnterButton.setDisabled(False)
        elif eleID ==2:
            self.ui.elevator2OpenButton.setStyleSheet("QPushButton{color: green}")
            self.ui.elevator2EnterButton.setDisabled(False)
        elif eleID ==3:
            self.ui.elevator3OpenButton.setStyleSheet("QPushButton{color: green}")
            self.ui.elevator3EnterButton.setDisabled(False)
        elif eleID ==4:
            self.ui.elevator4OpenButton.setStyleSheet("QPushButton{color: green}")
            self.ui.elevator4EnterButton.setDisabled(False)
        elif eleID ==5:
            self.ui.elevator5OpenButton.setStyleSheet("QPushButton{color: green}")
            self.ui.elevator5EnterButton.setDisabled(False)
        else:
            print("elevatorOpen error")

    def handleEnterButton(self, eleID:int):
        getAimFloorDialog = QtWidgets.QDialog()
        ui = Ui_DialogGetAimFloor()
        ui.setupUi(getAimFloorDialog)
        getAimFloorDialog.exec_()
        elevator=self.elevators[eleID-1]
        for passenger in elevator.nextPassengers:
            if passenger.currentFloor==elevator.currentFloor:
                elevator.nextPassengers.remove(passenger)
                passenger.aimFloor=int(ui.comboBox.currentText())
                elevator.addPassenger(passenger)
                elevator.passengers = list(
                    filter(lambda x: x.aimFloor != elevator.currentFloor, elevator.passengers))


    def autoRun(self):
        for elevator in self.elevators:
            if elevator.stops.empty():
                elevator.direction = Direction.IDLE
                return
            if elevator.direction == Direction.IDLE:
                if elevator.stops.queue[0] >= elevator.currentFloor:
                    elevator.direction = Direction.UP
                elif elevator.stops.queue[len(elevator.stops.queue)-1] <= elevator.currentFloor:
                    elevator.direction = Direction.DOWN
                elif elevator.stops.queue[0] <elevator.currentFloor<elevator.stops.queue[len(elevator.stops.queue)-1]:
                    elevator.direction= Direction.UP if (elevator.currentFloor-elevator.stops.queue[0])>=elevator.stops.queue[len(elevator.stops.queue)-1]-elevator.currentFloor else Direction.DOWN
            if elevator.direction == Direction.UP and elevator.currentFloor <= elevator.stops.queue[len(elevator.stops.queue)-1]:
                self.elevatorUp(elevator.id)
            if elevator.direction == Direction.DOWN and elevator.currentFloor >= elevator.stops.queue[0]:
                self.elevatorDown(elevator.id)



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    elevatorSystem = ElevatorSystem()
    elevatorSystem.mainWindow.show()
    sys.exit(app.exec_())
