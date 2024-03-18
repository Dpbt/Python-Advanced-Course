from PIL import Image
from .Ex1 import latex_document


def latex_image(image_path):
    latex_image_code = "\\begin{figure}[h]\n" + "\\centering\n"
    image = Image.open(image_path)
    image_width = image.size[0]
    image_scale = min(300 / image_width, 1.0)
    latex_image_code += f"\\includegraphics[scale={image_scale}]{{{image_path}}}\n"
    latex_image_code += "\\end{figure}\n"
    return latex_image_code


if __name__ == "__main__":
    example_image_path = "example_image.png"
    print(latex_document(latex_image(example_image_path)))
