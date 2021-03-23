# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(490, 694)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_3.sizePolicy().hasHeightForWidth())
        self.tab_3.setSizePolicy(sizePolicy)
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setLineWidth(1)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.people_count = QtWidgets.QSpinBox(self.tab_3)
        self.people_count.setObjectName("people_count")
        self.gridLayout_2.addWidget(self.people_count, 0, 1, 1, 1)
        self.bridness = QtWidgets.QProgressBar(self.tab_3)
        self.bridness.setMaximum(300)
        self.bridness.setProperty("value", 0)
        self.bridness.setTextVisible(True)
        self.bridness.setInvertedAppearance(False)
        self.bridness.setObjectName("bridness")
        self.gridLayout_2.addWidget(self.bridness, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.light1 = QtWidgets.QPushButton(self.tab_3)
        self.light1.setMinimumSize(QtCore.QSize(0, 100))
        self.light1.setCheckable(True)
        self.light1.setChecked(False)
        self.light1.setAutoDefault(False)
        self.light1.setDefault(False)
        self.light1.setFlat(False)
        self.light1.setObjectName("light1")
        self.horizontalLayout_2.addWidget(self.light1)
        self.light2 = QtWidgets.QPushButton(self.tab_3)
        self.light2.setMinimumSize(QtCore.QSize(0, 100))
        self.light2.setCheckable(True)
        self.light2.setObjectName("light2")
        self.horizontalLayout_2.addWidget(self.light2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.camera_view_main = QtWidgets.QLabel(self.tab_3)
        self.camera_view_main.setObjectName("camera_view_main")
        self.verticalLayout.addWidget(self.camera_view_main)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.reset_base_frame = QtWidgets.QPushButton(self.tab_3)
        self.reset_base_frame.setObjectName("reset_base_frame")
        self.verticalLayout.addWidget(self.reset_base_frame)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout.setObjectName("gridLayout")
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 13, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 20, 0, 1, 3)
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 19, 0, 1, 1)
        self.time_to_off_field = QtWidgets.QSpinBox(self.tab_4)
        self.time_to_off_field.setProperty("value", 5)
        self.time_to_off_field.setObjectName("time_to_off_field")
        self.gridLayout.addWidget(self.time_to_off_field, 16, 2, 1, 1)
        self.contr_ip_2_field = QtWidgets.QLineEdit(self.tab_4)
        self.contr_ip_2_field.setObjectName("contr_ip_2_field")
        self.gridLayout.addWidget(self.contr_ip_2_field, 19, 2, 1, 1)
        self.cam_view_field = QtWidgets.QCheckBox(self.tab_4)
        self.cam_view_field.setChecked(True)
        self.cam_view_field.setObjectName("cam_view_field")
        self.gridLayout.addWidget(self.cam_view_field, 7, 0, 1, 3)
        self.center_offset_filed = QtWidgets.QSlider(self.tab_4)
        self.center_offset_filed.setMinimum(-120)
        self.center_offset_filed.setMaximum(120)
        self.center_offset_filed.setProperty("value", 0)
        self.center_offset_filed.setOrientation(QtCore.Qt.Horizontal)
        self.center_offset_filed.setObjectName("center_offset_filed")
        self.gridLayout.addWidget(self.center_offset_filed, 15, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 10, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.tab_4)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 9, 0, 1, 3)
        self.select_video_path = QtWidgets.QPushButton(self.tab_4)
        self.select_video_path.setObjectName("select_video_path")
        self.gridLayout.addWidget(self.select_video_path, 2, 0, 1, 1)
        self.cameras_list = QtWidgets.QListWidget(self.tab_4)
        self.cameras_list.setObjectName("cameras_list")
        self.gridLayout.addWidget(self.cameras_list, 8, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 16, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.tab_4)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 14, 0, 1, 3)
        self.label_6 = QtWidgets.QLabel(self.tab_4)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 15, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.tab_4)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 5, 0, 1, 3)
        self.ar_cam_field = QtWidgets.QCheckBox(self.tab_4)
        self.ar_cam_field.setChecked(True)
        self.ar_cam_field.setObjectName("ar_cam_field")
        self.gridLayout.addWidget(self.ar_cam_field, 6, 0, 1, 3)
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 11, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_4)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 18, 0, 1, 1)
        self.vidio_path_field = QtWidgets.QLineEdit(self.tab_4)
        self.vidio_path_field.setReadOnly(True)
        self.vidio_path_field.setObjectName("vidio_path_field")
        self.gridLayout.addWidget(self.vidio_path_field, 2, 2, 1, 1)
        self.contr_ip_field = QtWidgets.QLineEdit(self.tab_4)
        self.contr_ip_field.setObjectName("contr_ip_field")
        self.gridLayout.addWidget(self.contr_ip_field, 18, 2, 1, 1)
        self.reset_area_field = QtWidgets.QSpinBox(self.tab_4)
        self.reset_area_field.setMaximum(999999999)
        self.reset_area_field.setSingleStep(1000)
        self.reset_area_field.setProperty("value", 0)
        self.reset_area_field.setObjectName("reset_area_field")
        self.gridLayout.addWidget(self.reset_area_field, 11, 2, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.tab_4)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 17, 0, 1, 3)
        self.is_video_recording_field = QtWidgets.QCheckBox(self.tab_4)
        self.is_video_recording_field.setChecked(True)
        self.is_video_recording_field.setObjectName("is_video_recording_field")
        self.gridLayout.addWidget(self.is_video_recording_field, 0, 0, 1, 3)
        self.min_area_field = QtWidgets.QSpinBox(self.tab_4)
        self.min_area_field.setMinimum(1)
        self.min_area_field.setMaximum(99999999)
        self.min_area_field.setSingleStep(100)
        self.min_area_field.setProperty("value", 500)
        self.min_area_field.setObjectName("min_area_field")
        self.gridLayout.addWidget(self.min_area_field, 10, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 8, 0, 1, 1)
        self.save = QtWidgets.QPushButton(self.tab_4)
        self.save.setObjectName("save")
        self.gridLayout.addWidget(self.save, 21, 0, 1, 3)
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 12, 0, 1, 1)
        self.frame_to_delete_field = QtWidgets.QSpinBox(self.tab_4)
        self.frame_to_delete_field.setMaximum(10000)
        self.frame_to_delete_field.setSingleStep(10)
        self.frame_to_delete_field.setProperty("value", 300)
        self.frame_to_delete_field.setObjectName("frame_to_delete_field")
        self.gridLayout.addWidget(self.frame_to_delete_field, 12, 2, 1, 1)
        self.static_offset_field = QtWidgets.QSpinBox(self.tab_4)
        self.static_offset_field.setProperty("value", 5)
        self.static_offset_field.setObjectName("static_offset_field")
        self.gridLayout.addWidget(self.static_offset_field, 13, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 0, 1, 3)
        self.tabWidget.addTab(self.tab_4, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BloomLight"))
        self.label_2.setText(_translate("MainWindow", "Освещённость"))
        self.label.setText(_translate("MainWindow", "Объектов в помещении"))
        self.bridness.setFormat(_translate("MainWindow", "%p"))
        self.light1.setText(_translate("MainWindow", "Свет 1"))
        self.light2.setText(_translate("MainWindow", "Свет 2"))
        self.camera_view_main.setText(_translate("MainWindow", "Инициализация камеры..."))
        self.reset_base_frame.setToolTip(_translate("MainWindow", "Необходимо сбрасывать только в отсуствии людей"))
        self.reset_base_frame.setText(_translate("MainWindow", "Сбросить базовый кадр"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Панель управления"))
        self.label_11.setText(_translate("MainWindow", "Максимальное смещение статики"))
        self.label_9.setText(_translate("MainWindow", "IP контролера №2"))
        self.contr_ip_2_field.setText(_translate("MainWindow", "localhost:4210"))
        self.cam_view_field.setText(_translate("MainWindow", "Просмотр дополнительных камер"))
        self.label_4.setText(_translate("MainWindow", "Минимальный размер объекта"))
        self.select_video_path.setText(_translate("MainWindow", "Выбрать"))
        self.label_7.setText(_translate("MainWindow", "Время отключения света"))
        self.label_6.setText(_translate("MainWindow", "Смещение центра"))
        self.ar_cam_field.setText(_translate("MainWindow", "Доп. графика на камере"))
        self.label_5.setText(_translate("MainWindow", "Максимальный размер объекта"))
        self.label_8.setText(_translate("MainWindow", "IP контролера №1"))
        self.vidio_path_field.setText(_translate("MainWindow", "out/"))
        self.contr_ip_field.setText(_translate("MainWindow", "192.168.137.32:4210"))
        self.is_video_recording_field.setText(_translate("MainWindow", "Запись видео"))
        self.label_3.setText(_translate("MainWindow", "Камера"))
        self.save.setText(_translate("MainWindow", "Сохранить"))
        self.label_10.setText(_translate("MainWindow", "Кадров до удаления статики"))
        self.label_12.setText(_translate("MainWindow", "Место сохранения видео"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Настройки"))
