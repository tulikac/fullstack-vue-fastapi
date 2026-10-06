# Vue and FastAPI Full-Stack Sample

A Vite Vue SPA and FastAPI backend deployed as separate components behind one
public hostname.

## Structure

```text
web/  Vue 3 and Vite 8 static frontend
api/  FastAPI and Uvicorn web API
```

## Run locally

Prepare the API:

```powershell
Set-Location .\api
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements-dev.txt
$env:PORT = "18091"
.\.venv\Scripts\python main.py
```

In another terminal, prepare and start the frontend:

```powershell
Set-Location .\web
npm install
npm run dev
```

Vite proxies `/api` to `http://127.0.0.1:18091`, matching the deployed
same-origin route shape.

## Build and verify

```powershell
Set-Location .\api
.\.venv\Scripts\python -m pytest

Set-Location ..\web
npm run build
npm run preview -- --host 127.0.0.1 --port 8080

Set-Location ..
.\scripts\verify.ps1 -BaseUrl http://127.0.0.1:8080
```

## Builder Apps configuration

The root `builder.yaml` declares:

- A Vite-detected static `web` component at `/`
- An explicit Python `api` component at `/api`

The route split keeps SPA fallback behavior out of the API prefix and allows
the browser to call FastAPI without CORS configuration.
