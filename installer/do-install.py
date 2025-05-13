# coding=utf-8
from __future__ import annotations

from zipfile import ZipFile
from base64 import decode
from tkinter.filedialog import askdirectory as _askdir, askopenfile as _askreadfile
from tkinter.messagebox import *
from core_base64 import core_base64
from jbk import jbk_base64
from mysql import mysql
from tqdm.rich import tqdm
from traceback import print_exc
from typing import *
from os import PathLike


def _file_helper(func: Callable[[], []]):
    return_val = func()
    if return_val is None:
        raise WindowsError(f"call of {func}(), failed")
    else:
        return return_val


askdirectory = lambda: _file_helper(_askdir)
askopenfile = lambda: _file_helper(_askreadfile)

if __name__ == "__main__":
    print("Loading...")


def system(cmd: str | bytes | PathLike[str] | PathLike[bytes]):
    from os import system as f
    result_code = f(cmd)
    if result_code:
        raise WindowsError(f"when ran command [{cmd}], failed! exit code is {result_code}")
    else:
        return None


def do_part(where: str | bytes | PathLike[str] | PathLike[bytes],
            base64_code: str | bytes | PathLike[str] | PathLike[bytes]):
    try:
        try:
            with open("do-install-read", "w") as f:
                for i in tqdm(base64_code.split("\n")):
                    f.write(i + "\n")
        except Exception:
            print_exc()
        try:
            with open("do-install.zip", "wb") as f:
                decode(open("do-install-read", "rb"), f)
        except Exception:
            print_exc()
        try:
            with ZipFile("do-install.zip", "r") as zzip:
                zzip.extractall(where + "/timemachineplus")
        except Exception:
            print_exc()
        from os import remove
        try:
            for i in ("do-install-read", "do-install.zip"):
                remove(i)
        except Exception:
            print_exc()
    except Exception:
        print_exc()


def install_part(base64_code: str | bytes | PathLike[str] | PathLike[bytes],
                 suffix: str | bytes | PathLike[str] | PathLike[bytes],
                 back_cmd: tuple[str | bytes | PathLike[str] | PathLike[bytes]]
                 = ()):
    try:
        try:
            with open("do-install-read", "w") as f:
                for i in tqdm(base64_code.split("\n")):
                    f.write(i + "\n")
        except Exception:
            print_exc()
        try:
            with open("do-install-installer." + suffix, "wb") as f:
                print("Decoding...")
                decode(open("do-install-read", "rb"), f)
            print("Installing...")
            system(f"do-install-installer.{suffix} {' '.join(back_cmd)}")
        except Exception:
            print_exc()
        from os import remove
        try:
            for i in ("do-install-read", "do-install-installer." + suffix):
                remove(i)
        except Exception:
            print_exc()
    except Exception:
        print_exc()


if __name__ == "__main__":
    where = None
    try:
        print("Select install directory")
        where = askdirectory()
        do_part(where, core_base64)
        print("Finished: timemachineplus")
    except Exception:
        print_exc()
    try:
        pass
    except Exception:
        print_exc()
    try:
        pass
    except Exception:
        print_exc()
    try:
        print("[timemachineplus] Please note the license shown in the popup window:")
        s = open(where + "/timemachineplus/LICENSE", encoding="utf-8").read().split("\n")
        from math import ceil

        total = ceil(len(s) / 40)
        cnt = 1
        import time

        begin = time.time()
        early_leave = True
        while s:
            spent = time.time() - begin
            more = spent / (cnt / total) - spent
            if not askyesno("timemachineplus/LICENSE GPL license information, "
                            "NO to stop showing",
                            "\n".join(s[:40]) +
                            f"\nShowing progress: {cnt}/{total} {cnt * 100 / total:.2f}% "
                            f"spent {round(spent) // 60}:{round(spent) % 60}"
                            f" remaining {round(more) // 60}:{round(more) % 60}"):
                break
            s = s[40:]
            cnt += 1
        else:
            early_leave = False
        if not askyesno("agreement of timemachineplus/LICENSE GPL"
                        f" {'(early leave)' if early_leave else ''}",
                        "Do you agree with the LICENSE (no to exit)"):
            raise KeyboardInterrupt("since you don't agree with the GPL license, you cannot "
                                    "finish the installation progress")
    except Exception:
        print_exc()
    try:
        print("[timemachineplus] It is also recommended to read the README.md, at popup window")
        showinfo("README.md", open(where + "/timemachineplus/README.md", encoding="utf-8").read())
        print("Finished: timemachineplus LICENSE")
    except Exception:
        print_exc()
    try:
        install_part(jbk_base64, "exe")
        print("Finish: jbk")
    except Exception:
        print_exc()
    try:
        install_part(mysql, "exe")
        print("Finish: mysql")
    except Exception:
        print_exc()
else:
    raise RuntimeError("this module must not be imported")
