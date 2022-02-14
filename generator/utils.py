import html


class Utilities(object):
    # If converting to TeX, set to False
    CONVERT_HTML_CHARACTERS: bool = True

    @classmethod
    def string_to_html_series(cls, text):
        """Convert HTML tags to human-readable version."""
        if cls.CONVERT_HTML_CHARACTERS:
            return html.escape(text)
        return text
