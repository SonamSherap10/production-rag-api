FROM python:3.12-slim

# curl is needed by the healthcheck
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Non-root user that owns /app
RUN useradd --create-home appuser && chown appuser:appuser /app

RUN pip install --no-cache-dir uv

# Dependency files first (so Docker can cache the install layer)
COPY --chown=appuser:appuser pyproject.toml uv.lock ./

USER appuser

# Install ONLY third-party dependencies, not the project itself
RUN uv sync --frozen --no-dev --no-install-project

# Now copy the application code
COPY --chown=appuser:appuser app/ app/

# Use the virtualenv's executables
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=20s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]