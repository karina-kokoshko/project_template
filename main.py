from app.io.input import input_from_console, read_from_file_builtin, read_from_file_pandas
from app.io.output import output_to_console, write_to_file_builtin

def main():
    text_from_user = input_from_console()
    text_from_file = read_from_file_builtin("data.txt")
    text_from_pandas = read_from_file_pandas("data.csv")

    output_to_console("Результати: ")
    output_to_console(f"З консолі: {text_from_user}")
    output_to_console(f"З файлу (builtin): {text_from_file}")
    output_to_console(f"З файлу (pandas): \n{text_from_pandas}")

    final_result = f"{text_from_user}\n{text_from_file}\n{text_from_pandas}"
    write_to_file_builtin(final_result, "output_result.txt")


if __name__ == '__main__':
    main()