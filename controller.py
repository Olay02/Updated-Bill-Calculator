from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    """
    Grabs the information from the pyqt
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.button_submit.clicked.connect(lambda: self.submit())
        self.button_clear.clicked.connect(lambda: self.clear())

    def submit(self):
        """
        outputs the data onto the gui when the submit button is clicked
        :return:
        """
        try:
            food_name = float(self.line_food.text())
            food_drink = float(self.line_drink.text())
            food_dessert = float(self.line_dessert.text())
            food_split = int(self.line_split.text())
            cash_amount = float(self.line_cash.text())

            total_food = food_name + food_drink + food_dessert
            tax = total_food * .10

            # Checks to see what radiobutton is checked and assigns the given amount to the tip_amount var
            if self.radioButton_10.isChecked():
                tip_amount = .10 * (total_food + tax)
            elif self.radioButton_15.isChecked():
                tip_amount = .15 * (total_food + tax)
            elif self.radioButton_20.isChecked():
                tip_amount = .20 * (total_food + tax)

            total = total_food + tax + tip_amount

            # Grabs the change if cash_amount is more than the total, throws error if it's below
            if cash_amount > total:
                change = cash_amount - total
            elif cash_amount == total:
                change = 0


            if food_split > 0:  # Checks to see how much the bill is split by
                split_amount = total / food_split
                self.label_msg.setText(f'\tSummary\n'
                                       f'Food:\t\t${food_name:.2f}\n'
                                       f'Drink:\t\t${food_drink:.2f}\n'
                                       f'Dessert:\t${food_dessert:.2f}\n'
                                       f'Tax:\t\t${tax:.2f}\n'
                                       f'Tip:\t\t${tip_amount:.2f}\n\n'
                                       f'TOTAL:\t\t${total:.2f}\n'
                                       f'----------------------------\n'
                                       f'Total Split {food_split} ways ${split_amount:.2f}')
            elif food_split <= 0:  # if the split amount is 0 or less, it will not print out the Total split
                self.label_msg.setText(f'\tSummary\n'
                                       f'Food:\t\t${food_name:.2f}\n'
                                       f'Drink:\t\t${food_drink:.2f}\n'
                                       f'Dessert:\t${food_dessert:.2f}\n'
                                       f'Tax:\t\t${tax:.2f}\n'
                                       f'Tip:\t\t${tip_amount:.2f}\n\n'
                                       f'TOTAL:\t\t${total:.2f}\n'
                                       f'Cash:\t\t${cash_amount:.2f}\n'
                                       f'Change:\t\t${change:.2f}\n'  # returns the change amount 
                                       f'----------------------------')
        except:
            self.label_msg.setText("Food, drink, dessert, split, and cash\nneed to be numeric\ne. g. 10.25 not $10.25")

    def clear(self):
        """
        clears on the data from the GUI when the clear button is clicked
        :return:
        """
        self.line_food.clear()
        self.line_drink.clear()
        self.line_dessert.clear()
        self.line_split.clear()
        self.line_cash.clear()

        self.radioButton_10.setChecked(True)
