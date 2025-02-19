from typing import Union
from direct.gui.DirectGui import DirectFrame, DirectLabel
from data.tiles.tile import Tile
from menus._base import BaseMenu


class Game(BaseMenu):
    def __init__(self, base):
        BaseMenu.__init__(self)

        # We'll store the frame and label references at class level.
        self.frame = None
        self.label = None
        self.base = base

    def register(self):
        self.base.accept("ui.update.user.tile_clicked", self.process_game_click)

    def show(self):
        # Example usage of some manager call, if needed
        from managers.ui import ui

        ui.get_instance().get_main_menu

        # Create your frame
        self.frame = DirectFrame(
            frameColor=(0.2, 0.2, 0.2, 1),
            frameSize=(-0.1, 0.5, -0.2, 0.4),  # width/height dimensions
            pos=(1.2, 0, 0.55),
        )

        # Add a label to the frame
        self.label = DirectLabel(
            parent=self.frame,
            text="Initial text",
            text_scale=0.05,  # Adjust to your preference
            text_align=1,  # 0=left, 1=center, 2=right
            pos=(0.2, 0, 0.15),  # Position relative to the frame
        )

        return self.frame

    def update_label_text(self, new_text: Union[list[str], str]):
        """
        Call this method whenever your model has new data
        that needs to be displayed in the frame.
        """
        if self.label:
            self.label["text"] = (
                new_text if isinstance(new_text, str) else "\n".join(new_text)
            )

    def process_game_click(self, tile: Union[list[str], str]):
        if isinstance(tile, str):
            tile = [tile]
        self.update_label_text(tile)
