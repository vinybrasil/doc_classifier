import uuid
from typing import Optional

import arrow
from pydantic import BaseModel, Field, StrictStr


class OutputPrediction(BaseModel):
    leadId: Optional[StrictStr]
    photoHash: Optional[StrictStr] = ""
    prediction: Optional[dict] = None
    requestId: Optional[str] = Field(default_factory=uuid.uuid4)
    timestamp: Optional[str] = Field(default_factory=arrow.now)
