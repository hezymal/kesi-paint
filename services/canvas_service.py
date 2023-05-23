from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfilename
from PIL import Image, ImageTk

from services.tkinter_service import TkinterService


class CanvasService:
    DEFAULT_EXTENSION = ".png"
    SUPPORTED_FILE_TYPES = [("Portal Network Graphics", "*.png")]

    def __init__(self, tkinter_service: TkinterService):
        self._canvas = self._create_canvas(tkinter_service)
        self._opened_image_reference = None  # https://www.c-sharpcorner.com/blogs/basics-for-displaying-image-in-tkinter-python

    def bind(self, event_name: str, handler) -> None:
        self._canvas.bind(event_name, handler)

    def create_line(self, x1: int, y1: int, x2: int, y2: int, fill: str = '#000000', width: int = 1,
                    smooth: bool = True, spline_steps: int = 36, cap_style=ROUND) -> int:
        return self._canvas.create_line(x1, y1, x2, y2, fill=fill, width=width, smooth=smooth, splinesteps=spline_steps,
                                        capstyle=cap_style)

    def create_rectangle(self, x1: int, y1: int, x2: int, y2: int, fill: str = '#000000', outline: str = '',
                         width: int = 1) -> int:
        return self._canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline=outline, width=width)

    def create_oval(self, x1: int, y1: int, x2: int, y2: int, fill: str = '#000000', outline: str = '',
                    width: int = 1) -> int:
        return self._canvas.create_oval(x1, y1, x2, y2, fill=fill, outline=outline, width=width)

    def create_polygon(self, points: [int], fill: str = '#000000', outline: str = '',
                       width: int = 1, smooth: bool = False) -> int:
        return self._canvas.create_polygon(points, fill=fill, outline=outline, width=width, smooth=smooth)

    def set_position(self, _id: int, x1: int, y1: int, x2: int, y2: int) -> None:
        self._canvas.coords(_id, x1, y1, x2, y2)

    def new_file(self) -> None:
        self._clear_canvas()

    def open_file(self) -> None:
        file_name = askopenfilename(
            defaultextension=self.DEFAULT_EXTENSION,
            filetypes=self.SUPPORTED_FILE_TYPES
        )
        if file_name == '':
            return

        tk_image = ImageTk.PhotoImage(Image.open(file_name))
        self._clear_canvas()
        self._opened_image_reference = tk_image
        self._canvas.create_image(0, 0, image=tk_image, anchor=NW)

    def save_file(self) -> None:
        file = asksaveasfile(
            initialfile='Untitled.png',
            defaultextension=self.DEFAULT_EXTENSION,
            filetypes=self.SUPPORTED_FILE_TYPES
        )
        if file is None:
            return

        self._canvas.postscript(file=file.name, colormode="color")
        with Image.open(file.name) as image:
            image.save(file.name, 'png')

    def _clear_canvas(self) -> None:
        self._canvas.delete("all")
        self._opened_image_reference = None

    @staticmethod
    def _create_canvas(tkinter_service: TkinterService) -> Canvas:
        canvas = tkinter_service.create_canvas(bg='white')
        canvas.pack(expand=1, fill=BOTH)
        return canvas
