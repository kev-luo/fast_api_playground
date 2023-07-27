run live server
```bash
uvicorn main:app --reload
```
    main: refers to main.py
    app: object created inside of main.py with line app = FastAPI()
    --reload: make the server restart after code changes, only used for dev

