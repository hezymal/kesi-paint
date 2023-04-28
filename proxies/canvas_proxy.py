from tkinter import *
from tkinter.filedialog import asksaveasfile
from PIL import Image


class CanvasProxy:
    def __init__(self, tk: Tk):
        self._canvas = self._create_canvas(tk)

    def bind(self, event_name: str, handler) -> None:
        self._canvas.bind(event_name, handler)

    def create_line(self, x1: int, y1: int, x2: int, y2: int, fill: str = '#000000', width: int = 1) -> int:
        return self._canvas.create_line(x1, y1, x2, y2, fill=fill, width=width)

    def create_oval(self, x1: int, y1: int, x2: int, y2: int, fill: str = '#000000', outline: str = '') -> int:
        return self._canvas.create_oval(x1, y1, x2, y2, fill=fill, outline=outline)

    def set_position(self, _id: int, x1: int, y1: int, x2: int, y2: int) -> None:
        self._canvas.coords(_id, x1, y1, x2, y2)

    def save_to_png(self):
        file = asksaveasfile(
            initialfile='Untitled.png',
            defaultextension=".png",
            filetypes=[("All Files", "*.*"), ("Portal Network Graphics", "*.png")]
        )
        if file is None:
            return

        self._canvas.postscript(file=file.name, colormode="color")
        with Image.open(file.name) as image:
            image.save(file.name, 'png')

    @staticmethod
    def _create_canvas(tk: Tk) -> Canvas:
        canvas = Canvas(tk, bg='white')
        canvas.pack(expand=1, fill=BOTH)
        return canvas
