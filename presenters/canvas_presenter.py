from models.tool_model import ToolModel
from utils.vector2 import Vector2
from views.canvas_view import CanvasView


class CanvasPresenter:
    def __init__(self, canvas_view: CanvasView, tool_model: ToolModel):
        self.canvas_view = canvas_view
        self.canvas_view.event_bus.subscribe(CanvasView.EVENT_CHANNEL_START_DRAW, self.start_draw)
        self.canvas_view.event_bus.subscribe(CanvasView.EVENT_CHANNEL_MOVE_DRAW, self.move_draw)
        self.canvas_view.event_bus.subscribe(CanvasView.EVENT_CHANNEL_END_DRAW, self.end_draw)
        self.tool_model = tool_model

    def start_draw(self, position: Vector2):
        self.tool_model.start_draw(position)
        shape_id = self.canvas_view.draw(self.tool_model)
        self.tool_model.start_draw_end(shape_id)

    def move_draw(self, position: Vector2):
        self.tool_model.move_draw(position)
        self.canvas_view.draw(self.tool_model)

    def end_draw(self, position):
        self.tool_model.end_draw(position)
        self.canvas_view.draw(self.tool_model)
        self.tool_model.end_draw_end()
