import napari
from napari import Viewer as NapariViewer, layers
from vispy.util import keys

from dataset_viewer.dataset import Dataset


class Viewer():
    dataset = Dataset()

    def __init__(self):
        self.viewer = NapariViewer()
        self.__set_bindings()

    def start(self):
        napari.run()

    def __set_bindings(self):
        self.__bind_key('h', self.__hello)
        self.__bind_key('l', self.__current_label_name)
        self.__bind_key('Escape', self.__exit)

    def __bind_key(self, key, func):
        self.viewer.bind_key(key, func)

    def __current_label_name(self, viewer: NapariViewer):
        active_layer = viewer.layers.selection.active

        if active_layer is not None:
            print(viewer.layers.selection.active.name)

    def __hello(self, viewer: NapariViewer):
        print('Hello World!')
        yield
        print('Bye World!')

    def __exit(self, viewer: NapariViewer):
        viewer.close()


Viewer().start()
