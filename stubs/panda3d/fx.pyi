import dtoolconfig
import panda3d.core
from typing import Any, ClassVar, overload

Dtool_PyNativeInterface: int

class CylindricalLens(panda3d.core.Lens):
    DtoolClassDict: ClassVar[dict] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    @staticmethod
    def getClassType(*args, **kwargs): ...
    @staticmethod
    def get_class_type() -> Any: ...

class FisheyeLens(panda3d.core.Lens):
    DtoolClassDict: ClassVar[dict] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    @staticmethod
    def getClassType(*args, **kwargs): ...
    @staticmethod
    def get_class_type() -> Any: ...

class NonlinearImager(dtoolconfig.DTOOL_SUPER_BASE):
    DtoolClassDict: ClassVar[dict] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def addScreen(self, *args, **kwargs): ...
    def addViewer(self, *args, **kwargs): ...
    @overload
    def add_screen(self, constNonlinearImagerself, ProjectionScreenscreen) -> Any: ...
    @overload
    def add_screen(self, constNonlinearImagerself, constNodePathscreen, strname) -> Any: ...
    @overload
    def add_viewer(self, constNonlinearImagerself, DisplayRegiondr) -> Any: ...
    @overload
    def add_viewer(self) -> Any: ...
    def findScreen(self, *args, **kwargs): ...
    def findViewer(self, *args, **kwargs): ...
    def find_screen(self, NonlinearImagerself, constNodePathscreen) -> Any: ...
    def find_viewer(self, NonlinearImagerself, DisplayRegiondr) -> Any: ...
    def getBuffer(self, *args, **kwargs): ...
    def getBuffers(self, *args, **kwargs): ...
    def getDarkRoom(self, *args, **kwargs): ...
    def getGraphicsEngine(self, *args, **kwargs): ...
    def getNumScreens(self, *args, **kwargs): ...
    def getNumViewers(self, *args, **kwargs): ...
    def getScreen(self, *args, **kwargs): ...
    def getScreenActive(self, *args, **kwargs): ...
    def getScreens(self, *args, **kwargs): ...
    def getViewer(self, *args, **kwargs): ...
    def getViewerCamera(self, *args, **kwargs): ...
    def getViewerScene(self, *args, **kwargs): ...
    def getViewers(self, *args, **kwargs): ...
    def get_buffer(self, NonlinearImagerself, intindex) -> Any: ...
    def get_buffers(self, *args, **kwargs): ...
    def get_dark_room(self, NonlinearImagerself) -> Any: ...
    def get_graphics_engine(self, NonlinearImagerself) -> Any: ...
    def get_num_screens(self, NonlinearImagerself) -> Any: ...
    def get_num_viewers(self, NonlinearImagerself) -> Any: ...
    def get_screen(self, NonlinearImagerself, intindex) -> Any: ...
    def get_screen_active(self, NonlinearImagerself, intindex) -> Any: ...
    def get_screens(self, *args, **kwargs): ...
    def get_viewer(self, NonlinearImagerself, intindex) -> Any: ...
    def get_viewer_camera(self, NonlinearImagerself, intindex) -> Any: ...
    def get_viewer_scene(self, NonlinearImagerself, intindex) -> Any: ...
    def get_viewers(self, *args, **kwargs): ...
    def recompute(self, constNonlinearImagerself) -> Any: ...
    def removeAllScreens(self, *args, **kwargs): ...
    def removeAllViewers(self, *args, **kwargs): ...
    def removeScreen(self, *args, **kwargs): ...
    def removeViewer(self, *args, **kwargs): ...
    def remove_all_screens(self, constNonlinearImagerself) -> Any: ...
    def remove_all_viewers(self, constNonlinearImagerself) -> Any: ...
    def remove_screen(self, constNonlinearImagerself, intindex) -> Any: ...
    def remove_viewer(self, constNonlinearImagerself, intindex) -> Any: ...
    def setScreenActive(self, *args, **kwargs): ...
    def setSourceCamera(self, *args, **kwargs): ...
    def setTextureSize(self, *args, **kwargs): ...
    def setViewerCamera(self, *args, **kwargs): ...
    def set_screen_active(self, constNonlinearImagerself, intindex, boolactive) -> Any: ...
    def set_source_camera(self, constNonlinearImagerself, intindex, constNodePathsource_camera) -> Any: ...
    def set_texture_size(self, constNonlinearImagerself, intindex, intwidth, intheight) -> Any: ...
    def set_viewer_camera(self, constNonlinearImagerself, intindex, constNodePathviewer_camera) -> Any: ...
    def __copy__(self): ...
    def __deepcopy__(self): ...

class OSphereLens(panda3d.core.Lens):
    DtoolClassDict: ClassVar[dict] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    @staticmethod
    def getClassType(*args, **kwargs): ...
    @staticmethod
    def get_class_type() -> Any: ...

class PSphereLens(panda3d.core.Lens):
    DtoolClassDict: ClassVar[dict] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    @staticmethod
    def getClassType(*args, **kwargs): ...
    @staticmethod
    def get_class_type() -> Any: ...

class ProjectionScreen(panda3d.core.PandaNode):
    DtoolClassDict: ClassVar[dict] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def clearUndistLut(self, *args, **kwargs): ...
    def clear_undist_lut(self, constProjectionScreenself) -> Any: ...
    def generateScreen(self, *args, **kwargs): ...
    def generate_screen(self, constProjectionScreenself, constNodePathprojector, strscreen_name, intnum_x_verts, intnum_y_verts, floatdistance, floatfill_ratio) -> Any: ...
    def getAutoRecompute(self, *args, **kwargs): ...
    @staticmethod
    def getClassType(*args, **kwargs): ...
    def getFrameColor(self, *args, **kwargs): ...
    def getInvertUvs(self, *args, **kwargs): ...
    def getLastScreen(self, *args, **kwargs): ...
    def getProjector(self, *args, **kwargs): ...
    def getTexcoord3d(self, *args, **kwargs): ...
    def getTexcoordName(self, *args, **kwargs): ...
    def getUndistLut(self, *args, **kwargs): ...
    def getVignetteColor(self, *args, **kwargs): ...
    def getVignetteOn(self, *args, **kwargs): ...
    def get_auto_recompute(self, ProjectionScreenself) -> Any: ...
    @staticmethod
    def get_class_type() -> Any: ...
    def get_frame_color(self, ProjectionScreenself) -> Any: ...
    def get_invert_uvs(self, ProjectionScreenself) -> Any: ...
    def get_last_screen(self, ProjectionScreenself) -> Any: ...
    def get_projector(self, ProjectionScreenself) -> Any: ...
    def get_texcoord_3d(self, ProjectionScreenself) -> Any: ...
    def get_texcoord_name(self, ProjectionScreenself) -> Any: ...
    def get_undist_lut(self, ProjectionScreenself) -> Any: ...
    def get_vignette_color(self, ProjectionScreenself) -> Any: ...
    def get_vignette_on(self, ProjectionScreenself) -> Any: ...
    def hasUndistLut(self, *args, **kwargs): ...
    def has_undist_lut(self, ProjectionScreenself) -> Any: ...
    def makeFlatMesh(self, *args, **kwargs): ...
    def make_flat_mesh(self, constProjectionScreenself, constNodePaththis_np, constNodePathcamera) -> Any: ...
    def recompute(self, constProjectionScreenself) -> Any: ...
    def recomputeIfStale(self, *args, **kwargs): ...
    @overload
    def recompute_if_stale(self, constProjectionScreenself) -> Any: ...
    @overload
    def recompute_if_stale(self, constProjectionScreenself, constNodePaththis_np) -> Any: ...
    def regenerateScreen(self, *args, **kwargs): ...
    def regenerate_screen(self, constProjectionScreenself, constNodePathprojector, strscreen_name, intnum_x_verts, intnum_y_verts, floatdistance, floatfill_ratio) -> Any: ...
    def setAutoRecompute(self, *args, **kwargs): ...
    def setFrameColor(self, *args, **kwargs): ...
    def setInvertUvs(self, *args, **kwargs): ...
    def setProjector(self, *args, **kwargs): ...
    def setTexcoord3d(self, *args, **kwargs): ...
    def setTexcoordName(self, *args, **kwargs): ...
    def setUndistLut(self, *args, **kwargs): ...
    def setVignetteColor(self, *args, **kwargs): ...
    def setVignetteOn(self, *args, **kwargs): ...
    def set_auto_recompute(self, constProjectionScreenself, boolauto_recompute) -> Any: ...
    def set_frame_color(self, constProjectionScreenself, constLVecBase4fframe_color) -> Any: ...
    def set_invert_uvs(self, constProjectionScreenself, boolinvert_uvs) -> Any: ...
    def set_projector(self, constProjectionScreenself, constNodePathprojector) -> Any: ...
    def set_texcoord_3d(self, constProjectionScreenself, booltexcoord_3d) -> Any: ...
    def set_texcoord_name(self, constProjectionScreenself, strtexcoord_name) -> Any: ...
    def set_undist_lut(self, constProjectionScreenself, constPfmFileundist_lut) -> Any: ...
    def set_vignette_color(self, constProjectionScreenself, constLVecBase4fvignette_color) -> Any: ...
    def set_vignette_on(self, constProjectionScreenself, boolvignette_on) -> Any: ...

def Dtool_BorrowThisReference(*args, **kwargs): ...
