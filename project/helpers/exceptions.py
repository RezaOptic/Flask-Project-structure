"""

"""


class NotFoundError(Exception):
    """not found exception"""

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.field = None
        self.error = args[0] if args else None


class ForbiddenError(Exception):
    """Forbidden exception"""

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.field = None
        self.error = args[0] if args else None


class NetworkError(Exception):
    """Network exception"""

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.field = None
        self.error = args[0] if args else None
