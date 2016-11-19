from kivy.garden.mapview import MapView
from kivy.garden.mapview import MapMarker
from kivy.core.image import Image
from kivy.app import App

#img =Image('med.png')
#img.size(10,10)
class MapViewApp(App):
    def build(self):

        mapa = MapView(zoom=11, lat=21.161908, lon=-86.851528)
        m1 = MapMarker(lat=21.161900, lon=-86.851528, source=img, anchor_x=0.5, anchor_y=0.5)
        mapa.add_marker(m1)
        return mapa

MapViewApp().run()
