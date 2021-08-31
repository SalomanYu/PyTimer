from playsound import playsound
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys
import time


class App(QWidget):
    def __init__(self):
        super().__init__()

        
    def initGUI(self):
        
        self.HMaket = QHBoxLayout()
        self.HMaket2 = QHBoxLayout()
        
        self.VMaket = QVBoxLayout()

        self.hour_label = QLabel('Часы',self)
        self.minute_label = QLabel('Минуты',self)
        self.second_label = QLabel('Секунды',self)

        self.hour_box = QComboBox(self)
        self.hour_box.addItems([str(hour) for hour in range(60)])

        self.minute_box = QComboBox(self)
        self.minute_box.addItems([str(minute) for minute in range(60)])
        
        self.second_box = QComboBox(self)
        self.second_box.addItems([str(second) for second in range(60)])

        self.start_btn = QPushButton('Запуск', self)
        self.start_btn.clicked.connect(self.startARaport)
        

        self.HMaket.addWidget(self.hour_box)
        self.HMaket.addWidget(self.minute_box)
        self.HMaket.addWidget(self.second_box)

        self.HMaket2.addWidget(self.hour_label)
        self.HMaket2.addWidget(self.minute_label)
        self.HMaket2.addWidget(self.second_label)

        self.VMaket.addStretch(1)
        self.VMaket.addLayout(self.HMaket)
        self.VMaket.addLayout(self.HMaket2)
        self.VMaket.addStretch(1)
        self.VMaket.addWidget(self.start_btn)
        self.setLayout(self.VMaket)      

        self.setGeometry(400,500,500,300)
        self.setWindowTitle('Таймер')
        self.show()
        
    def startARaport(self):
        hour = int(self.hour_box.currentText())
        minute = int(self.minute_box.currentText())
        second = int(self.second_box.currentText())

        if hour or minute or second > 0:

            self.close()
            self.test = Timer(hour, minute, second)
            
            


class Timer(QMainWindow):
    def __init__(self, hours, minutes, seconds):
        super().__init__()

        self.create_new_window(hours, minutes, seconds)
        
    
    def closeEvent(self, event):
        event.accept()
        sys.exit()
        
    
    def create_new_window(self, hours, minutes, seconds):
        HLayout = QHBoxLayout()
        VLayout = QVBoxLayout()

        self.timer_is_run = True
            
        def stop_timer():
            sys.exit()

        self.count_hour = QLabel(str(hours))
        self.count_minute = QLabel(str(minutes))
        self.count_second = QLabel(str(seconds))
        self.all_time = QLabel(f'Всего {hours} ч. {minutes} мин. {seconds} сек.')
        self.all_time.setObjectName('all_time')

        self.stop_btn = QPushButton('Стоп', self)
        self.stop_btn.clicked.connect(stop_timer)
    

        HLayout.addWidget(self.count_hour)
        HLayout.addWidget(self.count_minute)
        HLayout.addWidget(self.count_second)
        HLayout.addStretch(3)
        
        VLayout.addLayout(HLayout)
        VLayout.addWidget(self.all_time)
        VLayout.addStretch(1)
        VLayout.addWidget(self.stop_btn)     
        widget = QWidget()
        
        widget.setLayout(VLayout)
        
        
        self.setCentralWidget(widget)
        self.setGeometry(400,500,500,300)
        
        style = ' '
        with open('style_timer.css', 'r') as file:
            for line in file:
                style += line

        self.setStyleSheet(style)

        self.show()

        time.sleep(1)
        self.counter()
        


    def counter(self):
        hour, minute, second, = map(int, (self.count_hour.text(), self.count_minute.text(), self.count_second.text()))
        len_sec = second + minute * 60 + hour * 3600

        for sec in range(len_sec):
            while self.timer_is_run:
                self.update()
                QApplication.processEvents()
                if second > 0:
                    second -= 1
                    self.count_second.setText(str(second))
                    time.sleep(1)
                else:
                    if minute > 0:
                        second = 59
                        minute -= 1
                        self.count_second.setText(str(second))
                        self.count_minute.setText(str(minute))
                        time.sleep(1)
                    else:
                        if hour > 0:
                            minute = second = 59
                            hour -= 1
                            self.count_minute.setText(str(minute))
                            self.count_second.setText(str(second))
                            self.count_hour.setText(str(hour))
                            time.sleep(1)
                        else:
                            self.timer_is_run = False
                            self.stop_btn.setText('Выйти')
                            playsound('media/Mellen Gi Remix .mp3', True)
    

if __name__ == '__main__':
    run_app = QApplication(sys.argv)
    style = ' '
    with open('style.css', 'r') as file:
        for line in file:
            style += line
    main = App()
    main.setStyleSheet(style)
    main.initGUI()
    sys.exit(run_app.exec_())
