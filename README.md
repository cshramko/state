# Python module: state

## Description
```
    A Python Class to contain state across
    multiple functions and modules.

    Initializes a Class Instance of dictionary object
    to contain the state of the importing Python script
    and its called functions and modules.

    In an assignment, sets the value of
    the attribute named <name> to <value>.
    Non-existant attribute will be created.

    In a reference, returns the value of
    the attribute named <name>. Raises 'AttributeError'
    if the attribute does not exist.
    
    state.toggle(<name>)
        Toggles the value of bool attribute named <name>
        (False becomes True, True becomes False).
        Returns 'AttributeError' if the attribute is not a bool.

    Instantiates the variable object which contains state via:
        state = State()
```

## Usage
```
    import state
    state.debug     =  False
    state.message   =  "Hello, world!"
    state.linecount = state.linecount + 1
```

## License.

See [License](LICENSE).
