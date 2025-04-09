class Symbol:
    def __init__(self, name, symbol_type, is_constant=False, value=None):
        self.name = name
        self.type = symbol_type
        self.is_constant = is_constant
        self.value = value

    def __str__(self):
        value_str = str(self.value) if self.value is not None else "None"
        return f"Symbol(name={self.name}, type={self.type}, const={self.is_constant}, value={value_str})"


class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.scopes = [{}]
        self.current_scope = 0

    def enter_scope(self):
        """Create a new scope for local variables."""
        self.scopes.append({})
        self.current_scope += 1

    def exit_scope(self):
        """Exit the current scope."""
        if self.current_scope > 0:
            self.scopes.pop()
            self.current_scope -= 1

    def declare(self, name, symbol_type, is_constant=False, value=None):
        """Declare a new symbol in the current scope."""
        if name in self.scopes[self.current_scope]:
            return False  # Symbol already exists in current scope
        
        self.scopes[self.current_scope][name] = Symbol(name, symbol_type, is_constant, value)
        return True

    def lookup(self, name):
        """Look up a symbol in all scopes, from innermost to outermost."""
        for i in range(self.current_scope, -1, -1):
            if name in self.scopes[i]:
                return self.scopes[i][name]
        return None

    def update(self, name, value):
        """Update a symbol's value."""
        for i in range(self.current_scope, -1, -1):
            if name in self.scopes[i]:
                if self.scopes[i][name].is_constant:
                    return False  # Cannot modify a constant
                self.scopes[i][name].value = value
                return True
        return False  # Symbol not found

    def get_current_scope_symbols(self):
        """Return all symbols in the current scope."""
        return self.scopes[self.current_scope]

    def get_all_symbols(self):
        """Return all symbols from all scopes."""
        all_symbols = {}
        for scope in self.scopes:
            all_symbols.update(scope)
        return all_symbols


class SemanticError(Exception):
    """Exception raised for semantic errors during analysis."""
    def __init__(self, message, line=None, column=None):
        self.message = message
        self.line = line
        self.column = column
        super().__init__(self.message)

    def __str__(self):
        if self.line and self.column:
            return f"Error semántico en línea {self.line}, columna {self.column}: {self.message}"
        return f"Error semántico: {self.message}"