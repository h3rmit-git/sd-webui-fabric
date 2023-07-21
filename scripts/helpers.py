
class WebUiComponents:
    txt2img_gallery = None
    txt2img_callbacks = []

    @staticmethod
    def on_txt2img_gallery(callback):
        if WebUiComponents.txt2img_gallery is not None:
            callback(WebUiComponents.txt2img_gallery)
        else:
            WebUiComponents.txt2img_callbacks.append(callback)

    @staticmethod
    def register_component(component, **kwargs):
        elem_id = getattr(component, "elem_id", None)
        if elem_id == "txt2img_gallery":
            print("Registering txt2img_gallery")
            WebUiComponents.txt2img_gallery = component
            for callback in WebUiComponents.txt2img_callbacks:
                callback(component)
