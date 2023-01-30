from PyQt5.Qt import QGraphicsPixmapItem, QPixmap
import os


class CardGraphic(QGraphicsPixmapItem):
    def __init__(self, card, scene):
        super().__init__()
        self.suit = card.suit
        self.value = card.value
        self.set_image()
        self.scene = scene
        self.selected = False

    def set_image(self):
        f = str(self.suit) + str(self.value) + ".png"
        fn = os.path.join("png", f)
        pixmap = QPixmap(fn)
        self.setPixmap(pixmap.scaledToWidth(100))

    def mousePressEvent(self, *args, **kwargs):
        if self.selected:
            self.setOpacity(0.6)
            self.selected = False
        else:
            self.setOpacity(1)
            self.selected = True
