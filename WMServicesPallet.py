from forklift.models import Pallet
from os import path

class WMServicesPallet(Pallet):
  def __init__(self):
     #: this is required to initialize the Pallet base class properties
     super(WMServicesPallet, self).__init__()

     self.arcgis_services = [('plat/UT_SITLA_CoalPlat', 'MapServer'),
                             ('plat/UT_SITLA_GeneralMap', 'MapServer'),
                             ('plat/UT_SITLA_OilGasPlat', 'MapServer'),
                             ('plat/UT_SITLA_OtherMineralPlat', 'MapServer'),
                             ('plat/UT_SITLA_SurfacePlat', 'MapServer'),]

     self.webmercservices = '\\\\tlwslms.utah.utad.state.ut.us\\map-share\\GISServices\\WebMercator\\WebMercatorServices.gdb'
     #//HOST/share/path/to/file

     self.copy_data = [self.webmercservices]

  def build(self, configuration):
     #destination_workspace = path.join(r'W:\\GISServices\\WebMercator', 'WebMercatorServices.gdb')
     source_workspace = path.join(self.garage, 'Viewer_TrustPub@tla-gis.sde')

     self.add_crates(['Contract_Esmt','Contract_Grazing','Owner_Coal','Owner_OilGas','Owner_OtherMin',
                      'Owner_Surface','Trans_Completed'], {'source_workspace': source_workspace,
                              'destination_workspace': self.webmercservices})
