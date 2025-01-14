"""Only used for unit test."""
from __future__ import annotations

import datetime
import inspect
import os
from pathlib import Path


def print_function_args():
    """Prints name. parameter names and values of calling function.

    Mainly for test purpose.
    """
    frame = inspect.stack()[1].frame
    args, _, _, values = inspect.getargvalues(frame)
    func_info_list = [f"func={inspect.stack()[1].function}"]
    for arg in args:
        func_info_list.append(f"{arg}={values.get(arg)}")
    print(", ".join(func_info_list))


def time_stamp(separator: str = "_", utc: bool = True) -> str:
    """Returns a time stamp.

    format "YYYYmmdd<separator>HHMMSSsss"
    Args:
        separator (str, optional):Separator char. Defaults to "_".

    Returns:
        str: _description_
    """
    if utc:
        return _utcnow().strftime(f"%Y%m%d{separator}%H%M%S%f")[:-3]
    else:
        return _now().strftime(f"%Y%m%d{separator}%H%M%S%f")[:-3]


def _utcnow() -> datetime.datetime:
    return datetime.datetime.utcnow()


def _now() -> datetime.datetime:
    return datetime.datetime.now()


class DictUtils:
    """Utility class for dictionary related methods."""

    @staticmethod
    def merge_dicts(source: dict, destination: dict):
        """Merges source with destination dict.

        If corresponding key exist in both source and destination, destination will not be
        overwritten, unless the value is a list, then source list will be appended to exsting
        distination list.

        Args:
            source (dict): dict to be merge.
            destination (dict): dict to be merged into.
        """
        # pylint: disable=invalid-name
        for k, v in source.items():
            if (
                k in destination
                and isinstance(destination[k], dict)
                and isinstance(source[k], dict)
            ):
                DictUtils.merge_dicts(source[k], destination[k])
            # Only update destination if key does not exist
            elif k in destination and isinstance(destination[k], list):
                destination[k].extend(v)
            elif k not in destination:
                destination[k] = v


def yaml_files_in_directory(config: Path) -> list[str]:
    """List all yaml files in directory.

    Args:
        config (Path): the directory.

    Raises:
        FileNotFoundError: raised if source directory does not exist.

    Returns:
        list[str]: list of yaml files.
    """
    config_files = []
    if not os.path.exists(config):
        raise FileNotFoundError(f"Path {config!r} does not exist.")
    if os.path.isdir(config):
        yaml_files = [
            str(Path(config, file))
            for file in os.listdir(config)
            if file.endswith((".yaml", ".yml"))
        ]
        config_files.extend(yaml_files)
    else:
        config_files.append(str(config))
    return config_files


def is_windows() -> bool:
    """True if the host system is Windows.

    Returns:
        bool: the result.
    """
    return _os_name() == "nt"


def _os_name() -> str:
    return os.name


# TODO: Update disclaimer text
DISCLAIMER_TEXT = ""


def add_disclaimer_text(help_text: str) -> str:
    """Return disclaimer text + help text.

    Returns:
        str: Disclaimer + help_text.
    """
    return f"""{DISCLAIMER_TEXT}

    {help_text}
    """
