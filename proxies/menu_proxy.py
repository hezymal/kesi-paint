from tkinter import *
from tkinter import colorchooser
from tkinter import ttk


class MenuProxy:
    def __init__(self, tk: Tk):
        self._create_tabs(tk)

    def choose_color(self) -> str:
        (rgb_color, hex_color) = colorchooser.askcolor(title="Choose color")
        return hex_color

    def set_current_color(self, color: str) -> None:
        self._current_color_label.config(bg=color)

    def bind_save_to_png_button_click(self, handler) -> None:
        self._save_to_png_button.config(command=handler)

    def bind_point_shape_button_click(self, handler) -> None:
        self._point_shape_button.config(command=handler)

    def bind_line_shape_button_click(self, handler) -> None:
        self._line_shape_button.config(command=handler)

    def bind_size_scale_change(self, handler) -> None:
        self._size_scale.config(command=handler)

    def bind_choose_color_button_click(self, handler) -> None:
        self._choose_color_button.config(command=handler)

    def _create_tabs(self, tk: Tk) -> None:
        self._tabs = ttk.Notebook(tk)
        self._create_file_tab()
        self._create_edit_tab()
        self._tabs.pack(fill=BOTH)
        self._tabs.select(1)

    def _create_file_tab(self) -> None:
        self._file_tab = self._create_tab(self._tabs, 'File')

        self._save_frame = self._create_frame(self._file_tab, "Save")
        self._save_to_png_button = Button(self._save_frame, text='Save as PNG')
        self._save_to_png_button.pack(side=LEFT, padx=4)

    def _create_edit_tab(self) -> None:
        self._edit_tab = self._create_tab(self._tabs, 'Edit')

        self._shape_frame = self._create_frame(self._edit_tab, "Brush")
        self._point_shape_button = Button(self._shape_frame, text='Point')
        self._point_shape_button.pack(side=LEFT, padx=4)
        self._line_shape_button = Button(self._shape_frame, text='Line')
        self._line_shape_button.pack(side=LEFT, padx=4)

        self._size_frame = self._create_frame(self._edit_tab, "Size")
        self._size_scale = Scale(self._size_frame, from_=1, to=100, orient=HORIZONTAL)
        self._size_scale.pack(side=LEFT)

        self._color_frame = self._create_frame(self._edit_tab, "Color")
        self._choose_color_button = Button(self._color_frame, text='Choose color')
        self._choose_color_button.pack(side=LEFT, padx=4)
        self._current_color_label = Label(self._color_frame, bg='red', width=5)
        self._current_color_label.pack(side=LEFT, padx=4)

    @staticmethod
    def _create_tab(tabs: ttk.Notebook, text: str) -> ttk.Frame:
        tab = ttk.Frame(tabs)
        tab.pack(side=LEFT)
        tabs.add(tab, text=text)
        return tab

    @staticmethod
    def _create_frame(tab: ttk.Frame, text: str) -> ttk.Frame:
        frame = ttk.LabelFrame(tab, relief=SOLID, borderwidth=1, text=text)
        inner = ttk.Frame(frame, padding=[2, 4, 4, 4])
        inner.pack(side=LEFT)
        frame.pack(side=LEFT, padx=(4, 0), pady=(2, 4), expand=0, fill=Y, anchor=NW)
        return inner
