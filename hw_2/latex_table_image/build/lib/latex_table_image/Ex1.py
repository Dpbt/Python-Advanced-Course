def latex_document(*args):
    latex_code = "\\documentclass{article}\n" + "\\usepackage{graphicx}\n" + "\\begin{document}\n"
    for arg in args:
        latex_code += arg
    latex_code += "\\end{document}"
    return latex_code


def latex_table(data: list):
    def longest_list(data: list):
        return max(len(lis) for lis in data)

    def fill_empty_elements(data: list):
        longest_l = longest_list(data)
        for i in range(len(data)):
            for j in range(longest_l - len(data[i])):
                data[i].append("")
        return data

    def list_to_table_string(data: list):
        string_code = "\hline\n"
        for element in data:
            string_code += (str(element) + " & ")
        string_code = string_code[:-2]
        string_code += ("\\" + "\\\n")
        return string_code

    data = fill_empty_elements(data)
    number_of_columns = len(data[0])

    latex_table_code = "\\begin{tabular}{ |" + "c|" * number_of_columns + " }\n"
    for line in data:
        latex_table_code += list_to_table_string(line)
    latex_table_code += ("\\hline\n" + "\\end{tabular}\n")
    return latex_table_code


if __name__ == "__main__":
    data = [[1, 5, 3, 23536], [2, 5], ["dgsvfv", 34.2345, "dfefeef", "sdgdfngf", 2345678, 34356],
            ["dfkgk", 1132, 2364, 981347, "eriu+30"]]
    print(latex_document(latex_table(data)))
