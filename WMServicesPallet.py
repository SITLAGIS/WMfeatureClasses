from forklift.models import Pallet
from os import path

class WMServicesPallet(Pallet):
  def __init__(self):
     #: this is required to initialize the Pallet base class properties
     super(WMServicesPallet, self).__init__()

  def build(self, configuration):
     destination_workspace = path.join(r'W:\\GISServices\\test', 'ForkliftTest.gdb')
     source_workspace = path.join(self.garage, 'Viewer_TrustPub@tla-gis.sde')

     self.add_crate('Contract_OilShale', {'source_workspace': source_workspace,
                              'destination_workspace': destination_workspace})
