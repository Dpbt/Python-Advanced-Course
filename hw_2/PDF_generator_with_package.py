from latex_table_image import latex_document, latex_table, latex_image
import os


data = [[1, 5, 3, 23536], [2, 5], ["dgsvfv", 34.2345, "dfefeef", "sdgdfngf", 2345678, 34356],
        ["dfkgk", 1132, 2364, 981347, "eriu+30"]]
image_path = "example_image.png"

latex_code = latex_document(latex_table(data), latex_image(image_path))

with open("example_table_and_image.tex", "w") as file:
    file.write(latex_code)

os.system(r"pdflatex C:/Users/denis/PycharmProjects/PHW2_F/example_table_and_image.tex")
