Makefile example:
  1. ```bash make etc.```
  2. main: dependances + exectutables
  3. 

- Rajouter tests unitaires pour tester les questions
- Parler des packages

```bash
main: main.py
  python3 main.py

unitest: unitest.py main.py
  python3 unitest.py
  
clean:
    rm -rf __pycache__
```