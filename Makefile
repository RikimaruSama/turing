main: main.py
  python3 main.py

unitest: unitest.py main.py
  python3 unitest.py
  
clean:
    rm -rf __pycache__