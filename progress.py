import sys


def get_progress_bar_string(progress, total, length=20, prefix=""):
    filled = int(length * progress / total)
    bar = "#" * filled + " " * (length - filled)
    str_len = len(str(total))
    progress = str(progress).rjust(str_len)
    return f"{prefix} [{bar}] {progress}/{total}"


def print_double_progress(progress1, total1, progress2, total2, length=20, prefix1="", prefix2=""):
    progress_bar1 = get_progress_bar_string(progress1, total1, length, prefix1)
    progress_bar2 = get_progress_bar_string(progress2, total2, length, prefix2)
    sys.stdout.write(f"\r{progress_bar1} | {progress_bar2}")
    sys.stdout.flush()


def print_single_progress(progress, total, length=20, prefix=""):
    progress_bar1 = get_progress_bar_string(progress, total, length, prefix)
    sys.stdout.write(f"\r{progress_bar1}")
    sys.stdout.flush()
