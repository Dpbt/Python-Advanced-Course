import click
import sys


@click.group()
def main():
    pass


@main.command()
@click.argument('in_file', nargs=1, default="sys.stdin")
def nl(in_file):
    if in_file != "sys.stdin":
        file = click.open_file(in_file, 'r')
        lines_orig = file.readlines()

        lines = [f"{i + 1} " + lines_orig[i].rstrip("\n") for i in range(0, len(lines_orig))]

        for line in lines:
            line = "     " + line
            click.echo(line)
    else:
        i = 1
        for line in sys.stdin:
            line = f"     {i}  " + line.rstrip("\n")
            click.echo(line)
            i += 1


@main.command()
@click.argument('in_files', nargs=-1)
def tail(in_files):
    if in_files:
        file_number = 0
        for in_file in in_files:
            file_number += 1
            file_name = in_file.split("\\")[-1]

            file = click.open_file(in_file, 'r')
            lines_orig = file.readlines()

            lines = list(map(lambda s: s.rstrip("\n"), lines_orig))

            if len(in_files) > 1:
                click.echo(f"==> {file_name} <==")
            for line in lines[-10::]:
                click.echo(line)
            if len(in_files) > 1 and file_number != len(in_files):
                click.echo()

    else:
        lines_orig = sys.stdin.readlines()
        lines = list(map(lambda s: s.rstrip("\n"), lines_orig))
        for line in lines[-17::]:
            click.echo(line)


@main.command()
@click.argument('in_files', nargs=-1)
def wc(in_files):
    stats = []
    if in_files:
        for in_file in in_files:
            file_name = in_file.split("\\")[-1]
            
            file = click.open_file(in_file, 'r')
            lines_orig = file.readlines()

            lines = list(map(lambda s: s.rstrip("\n"), lines_orig))

            words = []
            for line in lines:
                if line:
                    words += [i for i in line.split(" ") if i]

            num_of_strings = 0
            for i in range(len(lines_orig)):
                if lines_orig[i].endswith("\n"):
                    num_of_strings += 1

            num_of_words = len(words)
            num_of_symbols = sum([len(line) for line in lines_orig]) + num_of_strings

            stats.append([num_of_strings, num_of_words, num_of_symbols, file_name])

        for file_stats in stats:
            print(" ".join(str(i) for i in file_stats))

        total_strings, total_words, total_symbols = 0, 0, 0
        if len(in_files) > 1:
            for i in range(len(in_files)):
                total_strings += stats[i][0]
                total_words += stats[i][1]
                total_symbols += stats[i][2]
            print(total_strings, total_words, total_symbols, "total")

    else:
        lines_orig = sys.stdin.readlines()
        lines = list(map(lambda s: s.rstrip("\n"), lines_orig))

        words = []
        for line in lines:
            if line:
                words += [i for i in line.split(" ") if i]

        num_of_strings = 0
        for i in range(len(lines_orig)):
            if lines_orig[i].endswith("\n"):
                num_of_strings += 1

        num_of_words = len(words)
        num_of_symbols = sum([len(line) for line in lines_orig])

        print("     ", num_of_strings, "     ", num_of_words, "     ", num_of_symbols)


if __name__ == '__main__':
    main()
