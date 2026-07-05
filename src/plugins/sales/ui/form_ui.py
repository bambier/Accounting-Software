# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDateEdit, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTabWidget, QTableView, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1117, 877)
        self.Invoices = QWidget()
        self.Invoices.setObjectName(u"Invoices")
        self.vboxLayout = QVBoxLayout(self.Invoices)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.save_btn = QPushButton(self.Invoices)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMaximumSize(QSize(250, 16777215))

        self.vboxLayout.addWidget(self.save_btn)

        self.scrollArea = QScrollArea(self.Invoices)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollarea_qwidget = QWidget()
        self.scrollarea_qwidget.setObjectName(u"scrollarea_qwidget")
        self.scrollarea_qwidget.setGeometry(QRect(0, 0, 1079, 921))
        self.scrollarea_qwidget_layout = QVBoxLayout(self.scrollarea_qwidget)
        self.scrollarea_qwidget_layout.setObjectName(u"scrollarea_qwidget_layout")
        self.scrollarea_qwidget_layout.setContentsMargins(0, 0, 0, -1)
        self.frame = QWidget(self.scrollarea_qwidget)
        self.frame.setObjectName(u"frame")
        self.frame_verticalLayout = QVBoxLayout(self.frame)
        self.frame_verticalLayout.setObjectName(u"frame_verticalLayout")
        self.frame_invoice = QWidget(self.frame)
        self.frame_invoice.setObjectName(u"frame_invoice")
        self.frame_invoice_layout = QVBoxLayout(self.frame_invoice)
        self.frame_invoice_layout.setObjectName(u"frame_invoice_layout")
        self.label_new_invoice = QLabel(self.frame_invoice)
        self.label_new_invoice.setObjectName(u"label_new_invoice")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_new_invoice.setFont(font)
        self.label_new_invoice.setWordWrap(True)

        self.frame_invoice_layout.addWidget(self.label_new_invoice)

        self.label_company = QLabel(self.frame_invoice)
        self.label_company.setObjectName(u"label_company")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setWeight(QFont.DemiBold)
        self.label_company.setFont(font1)
        self.label_company.setWordWrap(True)

        self.frame_invoice_layout.addWidget(self.label_company)

        self.label_subtitle = QLabel(self.frame_invoice)
        self.label_subtitle.setObjectName(u"label_subtitle")
        font2 = QFont()
        font2.setPointSize(12)
        self.label_subtitle.setFont(font2)
        self.label_subtitle.setStyleSheet(u"color: rgb(154, 153, 150)")
        self.label_subtitle.setWordWrap(True)

        self.frame_invoice_layout.addWidget(self.label_subtitle)

        self.line = QFrame(self.frame_invoice)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.frame_invoice_layout.addWidget(self.line)

        self.widget = QWidget(self.frame_invoice)
        self.widget.setObjectName(u"widget")
        self._2 = QHBoxLayout(self.widget)
        self._2.setSpacing(6)
        self._2.setObjectName(u"_2")
        self._2.setContentsMargins(0, 0, 0, 0)
        self.frame_title_sub = QWidget(self.widget)
        self.frame_title_sub.setObjectName(u"frame_title_sub")
        self.verticalLayout = QVBoxLayout(self.frame_title_sub)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_input = QLineEdit(self.frame_title_sub)
        self.title_input.setObjectName(u"title_input")

        self.verticalLayout.addWidget(self.title_input)

        self.subheading_input = QLineEdit(self.frame_title_sub)
        self.subheading_input.setObjectName(u"subheading_input")

        self.verticalLayout.addWidget(self.subheading_input)


        self._2.addWidget(self.frame_title_sub)

        self.frame_btn_logo = QWidget(self.widget)
        self.frame_btn_logo.setObjectName(u"frame_btn_logo")
        self.horizontalLayout = QHBoxLayout(self.frame_btn_logo)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.select_logo_btn = QPushButton(self.frame_btn_logo)
        self.select_logo_btn.setObjectName(u"select_logo_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_logo_btn.sizePolicy().hasHeightForWidth())
        self.select_logo_btn.setSizePolicy(sizePolicy)
        self.select_logo_btn.setFont(font)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.InsertImage))
        self.select_logo_btn.setIcon(icon)
        self.select_logo_btn.setIconSize(QSize(128, 128))

        self.horizontalLayout.addWidget(self.select_logo_btn)


        self._2.addWidget(self.frame_btn_logo)

        self.frame_logo = QFrame(self.widget)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_logo.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame_logo)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.image_lable = QLabel(self.frame_logo)
        self.image_lable.setObjectName(u"image_lable")
        self.image_lable.setLineWidth(0)

        self.verticalLayout_2.addWidget(self.image_lable)


        self._2.addWidget(self.frame_logo)

        self.frame_address = QWidget(self.widget)
        self.frame_address.setObjectName(u"frame_address")
        self.verticalLayout_3 = QVBoxLayout(self.frame_address)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.name_input = QLineEdit(self.frame_address)
        self.name_input.setObjectName(u"name_input")

        self.verticalLayout_3.addWidget(self.name_input)

        self.email_input = QLineEdit(self.frame_address)
        self.email_input.setObjectName(u"email_input")

        self.verticalLayout_3.addWidget(self.email_input)

        self.tax_number_input = QLineEdit(self.frame_address)
        self.tax_number_input.setObjectName(u"tax_number_input")

        self.verticalLayout_3.addWidget(self.tax_number_input)

        self.phone_input = QLineEdit(self.frame_address)
        self.phone_input.setObjectName(u"phone_input")

        self.verticalLayout_3.addWidget(self.phone_input)

        self.address_input = QLineEdit(self.frame_address)
        self.address_input.setObjectName(u"address_input")

        self.verticalLayout_3.addWidget(self.address_input)

        self.country_input = QLineEdit(self.frame_address)
        self.country_input.setObjectName(u"country_input")

        self.verticalLayout_3.addWidget(self.country_input)


        self._2.addWidget(self.frame_address)

        self._2.setStretch(0, 4)
        self._2.setStretch(1, 1)
        self._2.setStretch(2, 3)
        self._2.setStretch(3, 4)

        self.frame_invoice_layout.addWidget(self.widget)


        self.frame_verticalLayout.addWidget(self.frame_invoice, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_billing = QWidget(self.frame)
        self.frame_billing.setObjectName(u"frame_billing")
        self.frame_billing_layout = QVBoxLayout(self.frame_billing)
        self.frame_billing_layout.setObjectName(u"frame_billing_layout")
        self.label_billing = QLabel(self.frame_billing)
        self.label_billing.setObjectName(u"label_billing")
        self.label_billing.setFont(font)
        self.label_billing.setWordWrap(True)

        self.frame_billing_layout.addWidget(self.label_billing)

        self.widget_2 = QWidget(self.frame_billing)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_btn_costumer_2 = QWidget(self.widget_4)
        self.frame_btn_costumer_2.setObjectName(u"frame_btn_costumer_2")
        self.verticalLayout_4 = QVBoxLayout(self.frame_btn_costumer_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.select_costumer_btn = QPushButton(self.frame_btn_costumer_2)
        self.select_costumer_btn.setObjectName(u"select_costumer_btn")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ContactNew))
        self.select_costumer_btn.setIcon(icon1)
        self.select_costumer_btn.setIconSize(QSize(64, 64))

        self.verticalLayout_4.addWidget(self.select_costumer_btn)

        self.label_3 = QLabel(self.frame_btn_costumer_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_4.addWidget(self.frame_btn_costumer_2, 0, Qt.AlignmentFlag.AlignVCenter)

        self.date_layout_widget = QWidget(self.widget_4)
        self.date_layout_widget.setObjectName(u"date_layout_widget")
        self.date_layout_widget.setMinimumSize(QSize(200, 0))
        self.date_layout = QVBoxLayout(self.date_layout_widget)
        self.date_layout.setSpacing(10)
        self.date_layout.setObjectName(u"date_layout")
        self.label = QLabel(self.date_layout_widget)
        self.label.setObjectName(u"label")

        self.date_layout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.date_layout.addItem(self.horizontalSpacer_2)

        self.dateEdit = QDateEdit(self.date_layout_widget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setTimeSpec(Qt.TimeSpec.LocalTime)
        self.dateEdit.setDate(QDate(2025, 6, 1))

        self.date_layout.addWidget(self.dateEdit)

        self.horizontalSpacer = QSpacerItem(40, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.date_layout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.date_layout_widget)
        self.label_2.setObjectName(u"label_2")

        self.date_layout.addWidget(self.label_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.date_layout.addItem(self.horizontalSpacer_3)

        self.dateEdit_2 = QDateEdit(self.date_layout_widget)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setDate(QDate(2025, 6, 30))

        self.date_layout.addWidget(self.dateEdit_2)


        self.horizontalLayout_4.addWidget(self.date_layout_widget)

        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(300, 0))
        self.verticalLayout_5 = QVBoxLayout(self.widget_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lineEdit = QLineEdit(self.widget_6)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_5.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.widget_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_5.addWidget(self.lineEdit_2)


        self.horizontalLayout_4.addWidget(self.widget_6)


        self.horizontalLayout_5.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")

        self.horizontalLayout_5.addWidget(self.widget_5)

        self.horizontalLayout_5.setStretch(0, 6)
        self.horizontalLayout_5.setStretch(1, 6)

        self.frame_billing_layout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.frame_billing)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.billing_name_input = QLineEdit(self.widget_3)
        self.billing_name_input.setObjectName(u"billing_name_input")

        self.horizontalLayout_3.addWidget(self.billing_name_input)

        self.price_input = QLineEdit(self.widget_3)
        self.price_input.setObjectName(u"price_input")

        self.horizontalLayout_3.addWidget(self.price_input)

        self.count_input = QLineEdit(self.widget_3)
        self.count_input.setObjectName(u"count_input")

        self.horizontalLayout_3.addWidget(self.count_input)

        self.add_to_record_btn = QPushButton(self.widget_3)
        self.add_to_record_btn.setObjectName(u"add_to_record_btn")

        self.horizontalLayout_3.addWidget(self.add_to_record_btn)

        self.horizontalLayout_3.setStretch(0, 4)
        self.horizontalLayout_3.setStretch(1, 3)
        self.horizontalLayout_3.setStretch(2, 3)
        self.horizontalLayout_3.setStretch(3, 1)

        self.frame_billing_layout.addWidget(self.widget_3)

        self.tableView = QTableView(self.frame_billing)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"")
        self.tableView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableView.setTabKeyNavigation(False)
        self.tableView.setDragDropOverwriteMode(False)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableView.setSortingEnabled(True)

        self.frame_billing_layout.addWidget(self.tableView)


        self.frame_verticalLayout.addWidget(self.frame_billing)

        self.frame_advanced = QWidget(self.frame)
        self.frame_advanced.setObjectName(u"frame_advanced")
        self.frame_advanced_layout = QVBoxLayout(self.frame_advanced)
        self.frame_advanced_layout.setObjectName(u"frame_advanced_layout")
        self.label_advanced = QLabel(self.frame_advanced)
        self.label_advanced.setObjectName(u"label_advanced")
        self.label_advanced.setFont(font)
        self.label_advanced.setWordWrap(True)

        self.frame_advanced_layout.addWidget(self.label_advanced)


        self.frame_verticalLayout.addWidget(self.frame_advanced, 0, Qt.AlignmentFlag.AlignTop)


        self.scrollarea_qwidget_layout.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignTop)

        self.scrollArea.setWidget(self.scrollarea_qwidget)

        self.vboxLayout.addWidget(self.scrollArea)

        Form.addTab(self.Invoices, "")
        self.Customers = QWidget()
        self.Customers.setObjectName(u"Customers")
        Form.addTab(self.Customers, "")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.save_btn.setText(QCoreApplication.translate("Form", u"Save", None))
        self.save_btn.setProperty(u"class", QCoreApplication.translate("Form", u"primary outlined", None))
        self.label_new_invoice.setText(QCoreApplication.translate("Form", u"New Invoice", None))
        self.label_company.setText(QCoreApplication.translate("Form", u"Company", None))
        self.label_subtitle.setText(QCoreApplication.translate("Form", u"Change the address, logo, and other information for your company.", None))
        self.title_input.setPlaceholderText(QCoreApplication.translate("Form", u"Title", None))
        self.subheading_input.setPlaceholderText(QCoreApplication.translate("Form", u"Subheading", None))
        self.select_logo_btn.setText("")
        self.image_lable.setText("")
        self.name_input.setPlaceholderText(QCoreApplication.translate("Form", u"Name", None))
        self.email_input.setPlaceholderText(QCoreApplication.translate("Form", u"Email", None))
        self.tax_number_input.setPlaceholderText(QCoreApplication.translate("Form", u"Tax Number", None))
        self.phone_input.setPlaceholderText(QCoreApplication.translate("Form", u"Phone", None))
        self.address_input.setPlaceholderText(QCoreApplication.translate("Form", u"Address", None))
        self.country_input.setPlaceholderText(QCoreApplication.translate("Form", u"Country", None))
        self.label_billing.setText(QCoreApplication.translate("Form", u"Billing", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Add Customer", None))
        self.label.setText(QCoreApplication.translate("Form", u" Invoice Date", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("Form", u"yyyy/MM/dd", None))
        self.label_2.setText(QCoreApplication.translate("Form", u" Due Date", None))
        self.dateEdit_2.setDisplayFormat(QCoreApplication.translate("Form", u"yyyy/MM/dd", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u" Invoice Number", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u" Order Number ", None))
        self.billing_name_input.setPlaceholderText(QCoreApplication.translate("Form", u"Name", None))
        self.price_input.setPlaceholderText(QCoreApplication.translate("Form", u"Price", None))
        self.count_input.setPlaceholderText(QCoreApplication.translate("Form", u"Count", None))
        self.add_to_record_btn.setText(QCoreApplication.translate("Form", u"Add to record", None))
        self.add_to_record_btn.setProperty(u"class", QCoreApplication.translate("Form", u"primary outlined", None))
        self.label_advanced.setText(QCoreApplication.translate("Form", u"Advanced", None))
        Form.setTabText(Form.indexOf(self.Invoices), QCoreApplication.translate("Form", u"Page", None))
        Form.setTabText(Form.indexOf(self.Customers), QCoreApplication.translate("Form", u"Page", None))
        pass
    # retranslateUi

