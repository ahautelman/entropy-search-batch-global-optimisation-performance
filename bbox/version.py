
def _version_as_tuple(version_str: str) -> tuple:
    return tuple(int(i) for i in version_str.split(".") if i.isdigit())


__version__ = '0.1.0'
__version_info__ = _version_as_tuple(__version__)
