from tkinter import *
from tkinter import colorchooser
from tkinter import ttk

from services.tkinter_service import TkinterService


class MenuService:
    def __init__(self, tkinter_service: TkinterService):
        self._create_tabs(tkinter_service)

    def choose_color(self) -> str:
        (rgb_color, hex_color) = colorchooser.askcolor(title="Choose color")
        return hex_color

    def set_color_1(self, color: str) -> None:
        self._color_button_1.config(bg=color)

    def set_color_2(self, color: str) -> None:
        self._color_button_2.config(bg=color)

    def bind_new_file_button_click(self, handler) -> None:
        self._new_file_button.config(command=handler)

    def bind_open_file_button_click(self, handler) -> None:
        self._open_file_button.config(command=handler)

    def bind_save_file_button_click(self, handler) -> None:
        self._save_file_button.config(command=handler)

    def bind_exit_button_click(self, handler) -> None:
        self._exit_button.config(command=handler)

    def bind_pencil_tool_button_click(self, handler) -> None:
        self._pencil_tool_button.config(command=handler)

    def bind_brush_tool_button_click(self, handler) -> None:
        self._brush_tool_button.config(command=handler)

    def bind_eraser_tool_button_click(self, handler) -> None:
        self._eraser_tool_button.config(command=handler)

    def bind_line_primitive_button_click(self, handler) -> None:
        self._line_primitive_button.config(command=handler)

    def bind_rectangle_primitive_button_click(self, handler) -> None:
        self._rectangle_primitive_button.config(command=handler)

    def bind_oval_primitive_button_click(self, handler) -> None:
        self._oval_primitive_button.config(command=handler)

    def bind_size_scale_change(self, handler) -> None:
        self._size_scale.config(command=handler)

    def bind_choose_color_button_1_click(self, handler) -> None:
        self._color_button_1.config(command=handler)

    def bind_choose_color_button_2_click(self, handler) -> None:
        self._color_button_2.config(command=handler)

    def _create_tabs(self, tkinter_service: TkinterService) -> None:
        self._tabs = tkinter_service.create_frame()

        self._file_frame = self._create_frame(self._tabs, "File")
        self._new_file_button = Button(self._file_frame, text='New', width=5)
        self._new_file_button.pack(side=LEFT, padx=4)
        self._open_file_button = Button(self._file_frame, text='Open', width=5)
        self._open_file_button.pack(side=LEFT, padx=4)
        self._save_file_button = Button(self._file_frame, text='Save', width=5)
        self._save_file_button.pack(side=LEFT, padx=4)
        self._exit_button = Button(self._file_frame, text='Exit', width=5)
        self._exit_button.pack(side=LEFT, padx=4)

        self._tools_frame = self._create_frame(self._tabs, "Tools")
        self._pencil_tool_button = Button(self._tools_frame, text='Pencil', width=5)
        self._pencil_tool_button.pack(side=LEFT, padx=4)
        self._brush_tool_button = Button(self._tools_frame, text='Brush', width=5)
        self._brush_tool_button.pack(side=LEFT, padx=4)
        self._eraser_tool_button = Button(self._tools_frame, text='Eraser', width=5)
        self._eraser_tool_button.pack(side=LEFT, padx=4)

        self._primitives_frame = self._create_frame(self._tabs, "Primitives")
        self._line_primitive_button = Button(self._primitives_frame, text='Line', width=5)
        self._line_primitive_button.pack(side=LEFT, padx=4)
        self._rectangle_primitive_button = Button(self._primitives_frame, text='Rectangle')
        self._rectangle_primitive_button.pack(side=LEFT, padx=4)
        self._oval_primitive_button = Button(self._primitives_frame, text='Oval', width=5)
        self._oval_primitive_button.pack(side=LEFT, padx=4)

        self._size_frame = self._create_frame(self._tabs, "Size")
        self._size_scale = Scale(self._size_frame, from_=1, to=100, orient=HORIZONTAL)
        self._size_scale.pack(side=LEFT)

        self._color_frame = self._create_frame(self._tabs, "Color")
        self._color_button_1 = Button(self._color_frame, bg='black', width=5)
        self._color_button_1.pack(side=LEFT, padx=4)
        self._color_button_2 = Button(self._color_frame, bg='white', width=5)
        self._color_button_2.pack(side=LEFT, padx=4)

        self._tabs.pack(fill=BOTH)

    @staticmethod
    def _create_frame(tab: ttk.Frame, text: str) -> ttk.Frame:
        frame = ttk.LabelFrame(tab, relief=SOLID, borderwidth=1, text=text)
        inner = ttk.Frame(frame, padding=[2, 4, 4, 4])
        inner.pack(side=LEFT)
        frame.pack(side=LEFT, padx=(4, 0), pady=(2, 4), expand=0, fill=Y, anchor=NW)
        return inner
