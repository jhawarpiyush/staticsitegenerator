from pathlib import Path
import os
import shutil


def main():
    project_root = Path(__file__).parent.parent
    static_dir_path = project_root / "static"
    public_dir_path = project_root / "public"

    if os.path.exists(public_dir_path):
        shutil.rmtree(public_dir_path)
    copy_directory_recursive(static_dir_path, public_dir_path)


def copy_directory_recursive(src, dst):
    if not dst.exists():
        dst.mkdir()

    for f in src.iterdir():
        new_f = dst / f.name
        if f.is_dir():
            copy_directory_recursive(f, new_f)
        else:
            print(f"Copying {f} to {new_f}")
            shutil.copy(f, new_f)



if __name__ == "__main__":
    main()
