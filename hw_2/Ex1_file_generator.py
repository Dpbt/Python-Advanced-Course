import latex_table_image.Ex1 as Ex1


if __name__ == "__main__":
    data = [[1, 5, 3, 23536], [2, 5], ["dgsvfv", 34.2345, "dfefeef", "sdgdfngf", 2345678, 34356],
            ["dfkgk", 1132, 2364, 981347, "eriu+30"]]
    latex_tab = Ex1.latex_document(Ex1.latex_table(data))
    with open("example_table.tex", "w") as file:
        file.write(latex_tab)
