from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

MIN_FLOWRATE = 50
MAX_FLOWRATE = 500






class flow_rate_one_Sample_Flow_Sliders(QWidget):
    def __init__(self):
        super().__init__()

        self.flow_rate_one = MIN_FLOWRATE
        self.flow_rate_two = MAX_FLOWRATE - MIN_FLOWRATE

        self.real_conentration = 0

        self.molecular_weight = 48.11
        self.calibration_temperature = 40
        self.permeation_rate = 304
        self.split_flow = 0

        # Labels for General Info
        #self.molecular_weight_label  = QLabel('Molecular Weight: {}'.format(self.molecular_weight), self)
        #self.molecular_weight_label.show()

        form_layout = QFormLayout()

        self.min_flow_rate_text_edit = QLineEdit()
        self.min_flow_rate_text_edit.setValidator(QDoubleValidator())
        self.min_flow_rate_text_edit.setText('{}'.format(MIN_FLOWRATE))
        self.min_flow_rate_text_edit.textChanged.connect(self.process_min_flow_rate)
        self.min_flow_rate_text_edit.show()

        self.max_flow_rate_text_edit = QLineEdit()
        self.max_flow_rate_text_edit.setValidator(QDoubleValidator())
        self.max_flow_rate_text_edit.setText('{}'.format(MAX_FLOWRATE))
        self.max_flow_rate_text_edit.textChanged.connect(self.process_max_flow_rate)
        self.max_flow_rate_text_edit.show()

        self.molecular_weight_text_edit = QLineEdit()
        self.molecular_weight_text_edit.setValidator(QDoubleValidator())
        self.molecular_weight_text_edit.setText('{}'.format(self.molecular_weight))
        self.molecular_weight_text_edit.textChanged.connect(self.process_molecular_weight)
        self.molecular_weight_text_edit.show()

        self.calibration_temperature_text_edit = QLineEdit()
        self.calibration_temperature_text_edit.setValidator(QDoubleValidator())
        self.calibration_temperature_text_edit.setText('{}'.format(self.calibration_temperature))
        self.calibration_temperature_text_edit.textChanged.connect(self.process_calibration_temperature)
        self.calibration_temperature_text_edit.show()

        self.permeation_rate_text_edit = QLineEdit()
        self.permeation_rate_text_edit.setValidator(QDoubleValidator())
        self.permeation_rate_text_edit.setText('{}'.format(self.permeation_rate))
        self.permeation_rate_text_edit.textChanged.connect(self.process_permeation_rate)
        self.permeation_rate_text_edit.show()

        self.split_flow_text_edit = QLineEdit()
        self.split_flow_text_edit.setValidator(QDoubleValidator())
        self.split_flow_text_edit.setText('{}'.format(self.split_flow))
        self.split_flow_text_edit.textChanged.connect(self.process_split_flow)
        self.split_flow_text_edit.show()

        self.flow_rate_one_text_edit = QLineEdit()
        self.flow_rate_one_text_edit.setValidator(QDoubleValidator())
        self.flow_rate_one_text_edit.setText('{}'.format(self.flow_rate_one))
        self.flow_rate_one_text_edit.textChanged.connect(self.process_flow_rate_one)
        self.flow_rate_one_text_edit.show()

        self.flow_rate_two_text_edit = QLineEdit()
        self.flow_rate_two_text_edit.setValidator(QDoubleValidator())
        self.flow_rate_two_text_edit.setText('{}'.format(self.flow_rate_two))
        self.flow_rate_two_text_edit.textChanged.connect(self.process_flow_rate_two)
        self.flow_rate_two_text_edit.show()

        self.real_conentration_label = QLabel('', self)
        self.real_conentration_label.show()

        form_layout.addRow('Min Flow Rate', self.min_flow_rate_text_edit)
        form_layout.addRow('Max Flow Rate', self.max_flow_rate_text_edit)
        form_layout.addRow('Molecular Weight', self.molecular_weight_text_edit)
        form_layout.addRow('Calibration Temperature', self.calibration_temperature_text_edit)
        form_layout.addRow('Permeation Rate', self.permeation_rate_text_edit)
        form_layout.addRow('Split Flow', self.split_flow_text_edit)
        form_layout.addRow('Flow Rate One (air)', self.flow_rate_one_text_edit)
        form_layout.addRow('Flow Rate Two (gas)', self.flow_rate_two_text_edit)






        # flow_rate_one
        flow_rate_one_slider_box = QHBoxLayout()
        flow_rate_one_slider_box.addStretch(1)

        self.flow_rate_one_label = QLabel('Flow Rate One: {}'.format(self.flow_rate_one), self)
        self.flow_rate_one_slider = QSlider(Qt.Horizontal)
        self.flow_rate_one_slider.setMinimum(MIN_FLOWRATE)
        self.flow_rate_one_slider.setMaximum(MAX_FLOWRATE - MIN_FLOWRATE)
        self.flow_rate_one_slider.setValue(self.flow_rate_one)

        self.flow_rate_one_label.show()
        self.flow_rate_one_slider.show()

        self.flow_rate_one_slider.valueChanged.connect(self.flow_rate_one_change_ratio)

        flow_rate_one_slider_box.addWidget(self.flow_rate_one_label)
        flow_rate_one_slider_box.addWidget(self.flow_rate_one_slider)





        # Flow Rate two
        flow_rate_two_slider_box = QHBoxLayout()
        flow_rate_two_slider_box.addStretch(1)

        self.flow_rate_two_label = QLabel('Flow Rate Two: {}:'.format(self.flow_rate_two), self)
        self.flow_rate_two_slider = QSlider(Qt.Horizontal)


        self.flow_rate_two_slider.setMinimum(MIN_FLOWRATE)
        self.flow_rate_two_slider.setMaximum(MAX_FLOWRATE - MIN_FLOWRATE)
        self.flow_rate_two_slider.setValue(self.flow_rate_two)


        self.flow_rate_two_label.show()
        self.flow_rate_two_slider.show()

        self.flow_rate_two_slider.valueChanged.connect(self.flow_rate_two_change_ratio)

        flow_rate_two_slider_box.addWidget(self.flow_rate_two_label)
        flow_rate_two_slider_box.addWidget(self.flow_rate_two_slider)

        #self.concentration_flow_rate_one = 0
        #self.concentration_flow_rate_one_label = QLabel('Concentration Flow Rate One (air): {}'.format(self.concentration_flow_rate_one), self)
        #self.concentration_flow_rate_one_label.show()

        self.concentration_flow_rate_two = 0
        self.concentration_flow_rate_two_label = QLabel('Concentration Flow Rate Two (gas): {}'.format(self.concentration_flow_rate_two), self)
        self.concentration_flow_rate_two_label.show()

        # All boxes
        verticalbox = QVBoxLayout()
        verticalbox.addLayout(form_layout)
        verticalbox.addWidget(self.real_conentration_label)
        verticalbox.addWidget(self.concentration_flow_rate_two_label)
        verticalbox.addLayout(flow_rate_one_slider_box)
        verticalbox.addLayout(flow_rate_two_slider_box)

        self.setLayout(verticalbox)


        self.update_labels()

    def process_flow_rate_one(self, value):
        try:
            value = int(value)
            if MIN_FLOWRATE <= value and value <= MAX_FLOWRATE:
                self.flow_rate_one = int(value)
                self.flow_rate_one_slider.setValue(int(value))
            self.update_labels()
        except Exception:
            pass

    def process_flow_rate_two(self, value):
        try:
            value = int(value)
            if MIN_FLOWRATE <= value and value <= MAX_FLOWRATE:
                self.flow_rate_two = int(value)
                self.flow_rate_two_slider.setValue(int(value))
            self.update_labels()
        except Exception:
            pass

    def process_min_flow_rate(self, value):
        try:
            if not int(value) < MAX_FLOWRATE or int(value) == 0:
                return
            global MIN_FLOWRATE
            MIN_FLOWRATE = int(value)
            self.flow_rate_one_slider.setMinimum( MIN_FLOWRATE )
            self.flow_rate_two_slider.setMinimum( MIN_FLOWRATE )

            self.flow_rate_one_slider.setMaximum( MAX_FLOWRATE - MIN_FLOWRATE )
            self.flow_rate_two_slider.setMaximum( MAX_FLOWRATE - MIN_FLOWRATE )
            self.update_labels()
        except Exception:
            pass

    def process_max_flow_rate(self, value):
        try:
            if not int(value) > MIN_FLOWRATE:
                return
            global MAX_FLOWRATE
            MAX_FLOWRATE = int(value)
            self.flow_rate_one_slider.setMaximum( float(MAX_FLOWRATE - MIN_FLOWRATE) )
            self.flow_rate_two_slider.setMaximum( float(MAX_FLOWRATE - MIN_FLOWRATE) )
            self.update_labels()
        except Exception:
            pass

    def process_molecular_weight(self, value):
        try:
            self.molecular_weight = float(value)
            self.update_labels()
        except Exception:
            pass

    def process_calibration_temperature(self, value):
        try:
            self.calibration_temperature = float(value)
            self.update_labels()
        except Exception:
            pass

    def process_permeation_rate(self, value):
        try:
            self.permeation_rate = float(value)
            self.update_labels()
        except Exception:
            pass

    def process_split_flow(self, value):
        try:
            self.split_flow = float(value)
            self.update_labels()
        except Exception:
            pass

    def process_concentration(self):

        ###try:
        ###    # This is PPB
        ###    self.concentration_flow_rate_one =  1000 * (self.permeation_rate*(24.5 / self.molecular_weight) / self.flow_rate_one) * (self.flow_rate_one / (self.flow_rate_one + self.split_flow))

        ###    # Converting to PPM
        ###    self.concentration_flow_rate_one /= 1000
        ###except ZeroDivisionError:
        ###    self.concentration_flow_rate_one = None


        try:
            # This is PPB
            self.concentration_flow_rate_two =  1000 * (self.permeation_rate*(24.5 / self.molecular_weight) / self.flow_rate_two) * (self.flow_rate_two / (self.flow_rate_two + self.split_flow))

            # Converting to PPM
            self.concentration_flow_rate_two /= 1000
        except ZeroDivisionError:
            self.concentration_flow_rate_two = None


        self.real_conentration = (self.concentration_flow_rate_two * self.flow_rate_two) / MAX_FLOWRATE


    def update_labels(self):
        self.flow_rate_one_label.setText('Flow Rate One (air): {}'.format(self.flow_rate_one))
        self.flow_rate_two_label.setText('Flow Rate Two (gas): {}'.format(self.flow_rate_two))

        self.process_concentration()

        #### Update Concentration One
        ###if self.concentration_flow_rate_one is None:
        ###    self.concentration_flow_rate_one_label.setText('Concentration Flow Rate One (air): Divided By Zero')
        ###else:
        ###    self.concentration_flow_rate_one_label.setText('Concentration Flow Rate One (air): {0:0.4f}'.format(self.concentration_flow_rate_one))

        # Update Concentration Two
        if self.concentration_flow_rate_two is None:
            self.concentration_flow_rate_two_label.setText('Concentration Flow Rate Two (gas): Divided By Zero')
        else:
            self.concentration_flow_rate_two_label.setText('Concentration Flow Rate Two (gas): {0:0.4f}'.format(self.concentration_flow_rate_two))

        self.real_conentration_label.setText('Real Concentration: {0:0.4f}'.format(self.real_conentration))



    def flow_rate_one_change_ratio(self):
        self.flow_rate_one = self.flow_rate_one_slider.value()
        self.flow_rate_two = MAX_FLOWRATE - self.flow_rate_one
        self.flow_rate_two_slider.setValue(self.flow_rate_two)
        self.update_labels()

    def flow_rate_two_change_ratio(self):
        self.flow_rate_two = self.flow_rate_two_slider.value()
        self.flow_rate_one = MAX_FLOWRATE - self.flow_rate_two
        self.flow_rate_one_slider.setValue(self.flow_rate_one)
        self.update_labels()


class main_widget(QWidget):
    def __init__(self):
        super().__init__()

        vertical_box = QVBoxLayout()
        self.S1 = flow_rate_one_Sample_Flow_Sliders()
        vertical_box.addWidget(self.S1)

        self.setLayout(vertical_box)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = main_widget()
    widget.show()

    sys.exit(app.exec_())
