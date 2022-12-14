class SymbolMapper:
    __symbols__: dict[str, str] = {
        '\"': '$double_quote$',
        '\n': '$new_line$',
        '\t': '$tab$',
        '\\': '$backslash$',
        ':': '$colon$',
        ',': '$comma$',
    }

    @staticmethod
    def symbol_to_export(s: str) -> str:
        if s in SymbolMapper.__symbols__:
            return SymbolMapper.__symbols__[s]
        return s

    @staticmethod
    def symbol_to_import(s: str) -> str:
        for key in SymbolMapper.__symbols__:
            if SymbolMapper.__symbols__[key] == s:
                return key
        return s

    @staticmethod
    def word_to_export(symbols: str) -> str:
        symbols_export = ''
        for s in symbols:
            symbols_export += SymbolMapper.symbol_to_export(s)
        return symbols_export
