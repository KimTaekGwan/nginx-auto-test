FROM python:3.12-slim

# uv 설치
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# 프로젝트 파일 복사
COPY pyproject.toml .
COPY app app/

# 의존성 설치
RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install --system .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]