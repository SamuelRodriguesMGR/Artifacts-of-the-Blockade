import re


class ConverterTextRenPy:

    TEXT_PATTERN = re.compile(r'[A-Za-zА-Яа-яЁё]')
    BRACKETS_PATTERN = re.compile(r'\([^()]*\)')
    
    @staticmethod
    def _clean_text(text: str) -> str:
        text = text.rstrip("\n")
        text = re.sub(r'\([^()]*\)', '', text)
        return ' '.join(text.split())
    
    def _get_brackets_content(self, text: str) -> list[str]:
        return re.findall(r'\(([^()]*)\)', text)


    def _get_text_lines(self, path: str):
        with open(path, encoding="utf-8") as file:
            for line in file:
                if self.TEXT_PATTERN.search(line):
                    yield line


    def _write_output(self, path : str, text : list) -> None:
        with open(path, encoding="utf-8", mode="w") as file: 
            file.write("\n" * 3)
            file.write("label bread:\n\n")
            for line in text:
                brackets_content = self._get_brackets_content(line)

                for i in brackets_content:
                    file.write(f'    #{i}\n')

                if brackets_content:
                    file.write(f'    scene \n')
                    
                percon = ("«" in line) or ("—" in line[0:2])
                print(("—" in line[0:2]))

                file.write(f'    {"metka " if percon else ""}"{self._clean_text(line)}"\n\n')
            file.write("    return")


    def run(self, input_file : str, output_file : str):
        filtered : list = self._get_text_lines(input_file)
        self._write_output(output_file, filtered)


if __name__ == "__main__":
    conv = ConverterTextRenPy()
    conv.run("input_file.txt", "output_file.txt")
