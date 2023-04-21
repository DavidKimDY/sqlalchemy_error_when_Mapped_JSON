# Repo for reprocude the error sqlalchemy_error_when_Mapped_JSON
### Dependencies

Python 3.11.3

pytest==7.1.2

sqlalchemy==2.0.6

# Start

### git
```
git clone https://github.com/DavidKimDY/sqlalchemy_error_when_Mapped_JSON.git
```

### venv
```
python3 -m .venv venv
source .venv/bin/activate
```

### install
```
pip istall -r requirements.txt
```

### Reproduce
```
pytest test.py
```

### result
```
_________________________________________________________________________________________ ERROR collecting test.py _________________________________________________________________________________________
test.py:18: in <module>
    class Test(Base):
.venv/lib/python3.11/site-packages/sqlalchemy/orm/decl_api.py:838: in __init_subclass__
    _as_declarative(cls._sa_registry, cls, cls.__dict__)
.venv/lib/python3.11/site-packages/sqlalchemy/orm/decl_base.py:248: in _as_declarative
    return _MapperConfig.setup_mapping(registry, cls, dict_, None, {})
.venv/lib/python3.11/site-packages/sqlalchemy/orm/decl_base.py:329: in setup_mapping
    return _ClassScanMapperConfig(
.venv/lib/python3.11/site-packages/sqlalchemy/orm/decl_base.py:574: in __init__
    self._extract_mappable_attributes()
.venv/lib/python3.11/site-packages/sqlalchemy/orm/decl_base.py:1479: in _extract_mappable_attributes
    value.declarative_scan(
.venv/lib/python3.11/site-packages/sqlalchemy/orm/properties.py:684: in declarative_scan
    self._init_column_for_annotation(
.venv/lib/python3.11/site-packages/sqlalchemy/orm/properties.py:783: in _init_column_for_annotation
    raise sa_exc.ArgumentError(
E   sqlalchemy.exc.ArgumentError: The type provided inside the 'json' attribute Mapped annotation is the SQLAlchemy type <class 'sqlalchemy.sql.sqltypes.JSON'>. Expected a Python type instead
========================================================================================= short test summary info ==========================================================================================
ERROR test.py - sqlalchemy.exc.ArgumentError: The type provided inside the 'json' attribute Mapped annotation is the SQLAlchemy type <class 'sqlalchemy.sql.sqltypes.JSON'>. Expected a Python type instead
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
```
