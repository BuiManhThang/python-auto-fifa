import cv2 as cv


class TemplateMatching:
    def __init__(self) -> None:
        pass

    @staticmethod
    def matchTemplage(image: cv.typing.MatLike, template: cv.typing.MatLike, threshold=0.8):
        (h, w, z) = image.shape
        res = cv.matchTemplate(image, template, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

        if max_val < threshold:
            return None

        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        return (top_left[0], top_left[1], bottom_right[0], bottom_right[1])
