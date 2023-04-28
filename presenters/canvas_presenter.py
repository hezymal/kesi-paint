from models.brush_model import BrushModel
from utils.vector2 import Vector2
from views.canvas_view import CanvasView


class CanvasPresenter:
    def __init__(self, canvas_view: CanvasView, brush_model: BrushModel):
        self.canvas_view = canvas_view
        self.canvas_view.event_bus.subscribe(CanvasView.EVENT_CHANNEL_START_DRAW, self.start_draw)
        self.canvas_view.event_bus.subscribe(CanvasView.EVENT_CHANNEL_MOVE_DRAW, self.move_draw)
        self.canvas_view.event_bus.subscribe(CanvasView.EVENT_CHANNEL_END_DRAW, self.end_draw)

        self.brush_model = brush_model

    def start_draw(self, position: Vector2):
        self.brush_model.start_draw(position)
        brush_id = self.canvas_view.draw_brush(self.brush_model)
        self.brush_model.set_id(brush_id)

    def move_draw(self, position: Vector2):
        self.brush_model.move_draw(position)
        self.canvas_view.draw_brush(self.brush_model)

    def end_draw(self, position):
        self.brush_model.end_draw(position)
        self.canvas_view.draw_brush(self.brush_model)
        self.brush_model.set_id(None)
