from pathlib import Path, PurePath
import shutil
import os


class App:
    def __init__(self):
        self.current_dir: str = Path.cwd()
        self.documents_folder: str = Path("documents")
        self.pictures_folder: str = Path("pictures")
        self.videos_folder: str = Path("videos")
        self.audios_folder: str = Path("audios")
        self.archives_folder: str = Path("archives")
        self.executables_folder: str = Path("executables")
        self.code_folder: str = Path("code/")

        self.folders_templates_advance: tuple = (self.documents_folder,
                                                 self.pictures_folder,
                                                 self.videos_folder,
                                                 self.audios_folder,
                                                 self.archives_folder,
                                                 self.executables_folder,
                                                 self.code_folder)

        self.folders_templates_normal: tuple = (self.documents_folder,
                                                self.pictures_folder,
                                                self.videos_folder,
                                                self.audios_folder,
                                                self.archives_folder)

        self.documents_suffixes: tuple = (
            ".txt", ".rtf", ".doc", ".odt", ".pdf", ".csv", ".json", ".xml",
            ".html", ".doc", "", ".docx", ".htm")

        self.pictures_suffixes: tuple = (".jpg", ".jpeg", ".jfif", ".png",
                                         ".gif", ".bmp", ".tif", ".tiff",
                                         ".svg", ".webp")

        self.videos_suffixes: tuple = (".mp4", ".m4v", ".mkv", ".avi", ".mov",
                                       ".wmv", ".flv", ".swf", ".webm", ".mpg",
                                       ".mpeg", ".mts", ".m2ts")

        self.audios_suffixes: tuple = (".mp3", ".wav", ".aac", ".m4a", ".flac",
                                       ".ogg", ".opus", ".wma", ".aiff")

        self.archievs_suffixes: tuple = (".zip", ".rar", ".7z", ".tar", ".gz",
                                         ".bz2", ".iso", ".torrent")

        self.executable_suffixes: tuple = (".exe", ".dll", ".sh", ".bat",
                                           ".cmd", ".app", ".dmg")

        self.code_suffixes: tuple = (".py", ".c", ".cpp", ".java", ".db",
                                     ".sqlite", ".xls", ".xlsx")

    def ask_user(self):
        operations: dict = {
            1: ("Normal mode(documents, audios, pictures, videos, archives)",
                self.normal_mode_sort),
            2: ("Advance mode(Normal mode + archives, code)",
                self.advance_mode_sort)
        }

        print("\n Availables operations:")
        for key, (text, _) in operations.items():
            print(f"{key}: {text}")

        user_answer: int = self.int_validator(
            input("\nWhat mode do you want to use? "),
            "What mode do you want to use? ")

        _, func = operations[user_answer]
        func()

    def int_validator(self, user_text: str, string: str) -> int:
        while True:
            if not user_text:
                print("Type the number!")
                user_text = input(string)
                continue
            elif not user_text.isdigit():
                print("Only numbers!")
                user_text = input(string)
                continue
            elif int(user_text) not in range(1, 3):
                print("Only 1 or 2!")
                user_text = input(string)
                continue
            else:
                return int(user_text)

    def normal_mode_sort(self) -> None:
        for i in self.folders_templates_normal:
            if not i.exists():
                i.mkdir()

        for i in self.current_dir.iterdir():
            if i.is_dir():
                continue
            else:
                if i.suffix in self.audios_suffixes:
                    destination = self.audios_folder / i.name
                    if destination.exists():
                        i.unlink()
                    else:
                        shutil.move(i, self.audios_folder)
                elif i.suffix in self.videos_suffixes:
                    destination = self.videos_folder / i.name
                    if destination.exists():
                        i.unlink()
                    else:
                        shutil.move(i, self.videos_folder)
                elif i.suffix in self.archievs_suffixes:
                    destination = self.archives_folder / i.name
                    if destination.exists():
                        i.unlink()
                    else:
                        shutil.move(i, self.archives_folder)
                elif i.suffix in self.pictures_suffixes:
                    destination = self.pictures_folder / i.name
                    if destination.exists():
                        i.unlink()
                    else:
                        shutil.move(i, self.pictures_folder)
                elif i.suffix in self.documents_suffixes:
                    destination = self.documents_folder / i.name
                    if destination.exists():
                        i.unlink()
                    else:
                        shutil.move(i, self.documents_folder)
                else:
                    continue
        print("Done!")

    def advance_mode_sort(self) -> None:
        for i in self.folders_templates_normal:
            if not i.exists():
                i.mkdir()

        for i in self.current_dir.iterdir():
            if i.is_dir():
                continue
            else:
                if i.suffix in self.audios_suffixes:
                    destination = self.audios_folder / i.name
                    if destination.exists():
                        i.unlink()
                    else:
                        shutil.move(i, self.audios_folder)
                elif i.suffix in self.videos_suffixes:
                    destination = self.videos_folder / i.name
                    if destination.exists():
                        i.unlink()
                    else:
                        shutil.move(i, self.videos_folder)
                elif i.suffix in self.archievs_suffixes:
                    destination = self.archives_folder / i.name
                    if destination.exists():
                        i.unlink()
                    else:
                        shutil.move(i, self.archives_folder)
                elif i.suffix in self.pictures_suffixes:
                    destination = self.pictures_folder / i.name
                    if destination.exists():
                        i.unlink()
                    else:
                        shutil.move(i, self.pictures_folder)
                elif i.suffix in self.documents_suffixes:
                    destination = self.documents_folder / i.name
                    if destination.exists():
                        i.unlink()
                    else:
                        shutil.move(i, self.documents_folder)
                elif PurePath(i).suffix in self.executable_suffixes:
                    destination = self.executables_folder / i.name
                    if destination.exists():
                        i.unlink()
                    else:
                        shutil.move(i, self.executables_folder)
                elif PurePath(i).suffix in self.code_suffixes:
                    shutil.move(i, self.code_folder)
                else:
                    continue
        print("Done!")

    def run(self):
        self.ask_user()


def main():
    app = App()
    app.run()


if __name__ == "__main__":
    main()
