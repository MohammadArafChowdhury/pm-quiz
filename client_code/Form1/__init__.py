from ._anvil_designer import Form1Template
from anvil import *


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def alfred_deakin_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert('Incorrect. Please try again.')

  def edmund_barton_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert('Correct! Edmund Barton is the first prime minister of Australia.')

  def john_curtin_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert('Incorrect. Please try again.')

  def andrew_fisher_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert('Incorrect. Please try again.')
