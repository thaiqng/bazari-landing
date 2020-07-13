from ._anvil_designer import LandingTemplate
from anvil import *
import anvil.server
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..Highlight import Highlight

class Landing(LandingTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.column_panel_content.add_component(Highlight())

  def link_click(self, **event_args):
    Notification("Contáctanos en WhatsApp para más información.", timeout=3).show()
