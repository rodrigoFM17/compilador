class Symbol:
    def __init__(self, name, symbol_type, is_constant=False, value=None, params=None):
        self.name = name
        self.type = symbol_type
        self.is_constant = is_constant
        self.value = value
        self.params = params  # Lista de tipos de parámetros para funciones

    def __str__(self):
        if self.params:
            params_str = ", ".join([f"{p[0]}: {p[1]}" for p in self.params])
            return f"Symbol(name={self.name}, type={self.type}, params=[{params_str}])"
        return f"Symbol(name={self.name}, type={self.type}, const={self.is_constant}, value={self.value})"


class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.scopes = [{}]  # El ámbito global
        self.current_scope = 0
        self.scope_history = []  # Historial de todos los ámbitos
        self.scope_names = []    # Nombres de los ámbitos (funciones, if, etc.)

    def enter_scope(self, name=None):
        """Create a new scope for local variables."""
        self.scopes.append({})
        self.current_scope += 1
        # Guardar nombre del ámbito
        scope_name = name if name else f"local_{self.current_scope}"
        self.scope_names.append(scope_name)

    def exit_scope(self):
        """Exit the current scope but keep it in history."""
        if self.current_scope > 0:
            # Guardar el ámbito actual en el historial antes de eliminarlo
            self.scope_history.append({
                'scope': self.scopes.pop(),
                'name': self.scope_names[self.current_scope - 1] if self.current_scope - 1 < len(self.scope_names) else f"local_{self.current_scope}"
            })
            self.current_scope -= 1

    def declare(self, name, symbol_type, is_constant=False, value=None, params=None):
        """Declare a new symbol in the current scope."""
        if name in self.scopes[self.current_scope]:
            return False  # Symbol already exists in current scope
        
        self.scopes[self.current_scope][name] = Symbol(name, symbol_type, is_constant, value, params)
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

    def get_all_symbols_with_scopes(self):
        """Return all symbols with their scope information (including history)."""
        result = []
        
        # Primero agregar los ámbitos actuales
        for scope_idx, scope in enumerate(self.scopes):
            scope_name = "global" if scope_idx == 0 else self.scope_names[scope_idx-1] if scope_idx-1 < len(self.scope_names) else f"local_{scope_idx}"
            for name, symbol in scope.items():
                result.append((scope_name, name, symbol))
        
        # Luego agregar los ámbitos históricos
        for scope_info in self.scope_history:
            for name, symbol in scope_info['scope'].items():
                result.append((scope_info['name'], name, symbol))
        
        return result


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