import uuid
from typing import Optional

import arrow
from pydantic import BaseModel, Field, StrictStr

class RawPrediction(BaseModel):
    selfie_score: Optional[float] 
    document_score: Optional[float] 

class ProbabilitiesPrediction(BaseModel):
    selfie_probability: Optional[float] 
    document_probability: Optional[float] 

class Prediction(BaseModel):
    raw_prediction: Optional[RawPrediction] =None
    probabilities: Optional[ProbabilitiesPrediction] =None
    class_predicted: Optional[StrictStr] = ""

class OutputPrediction(BaseModel):
    leadId: Optional[StrictStr]
    photoHash: Optional[StrictStr] = ""
    prediction: Optional[Prediction] = None
    requestId: Optional[str] = Field(default_factory=uuid.uuid4)
    timestamp: Optional[str] = Field(default_factory=arrow.now)
