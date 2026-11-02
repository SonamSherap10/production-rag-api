"""API Requests and Responses models.
Pydantic models are used for request validation and response structure.
"""

from pydantic import BaseModel, Field
from datetime import datetime, timezone

class ChatRequest(BaseModel):
    message:str = Field(
        ...,   # The ellipsis indicates that this field is required.
        min_length=1,
        max_length=10000,
        description="The message to be sent to the chat API."
    )

    thread_id: str =Field(
        default="default",
        description="The thread ID for the chat session. If not provided, a default thread will be used."
    )

class ChatResponse(BaseModel):
    response :str 
    thread_id: str
    model_used: str
    cached: bool = False
    processing_time_ms: float
    timestamp: datetime = Field(default_factory=lambda : datetime.now(timezone.utc), description="The timestamp when the response was generated.")


class HealthResponse(BaseModel):
    """Health check response model."""
    status: str = "Healthy"
    environment: str
    version : str = "1.0.0"
    checks:dict = {}


class MetricsResponse(BaseModel):
    """Metrics response model."""
    total_requests: int
    total_errors: int
    error_rate: float
    avg_latency_ms: float
    cache_hit_rate: str
    cache_miss_rate: str
    total_cache_hits: int
    total_input_tokens: int
    total_output_tokens: int


class ErrorResponse(BaseModel):
    """Error response model."""
    error: str
    details: str | None = None
    request_id: str | None = None