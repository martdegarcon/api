from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel.ext.asyncio.session import AsyncSession
from database.politician.schemes import Politician, PoliticianCreate
from database.politician.models import PoliticianOperations
from database_connection import get_session, init_db

# Create FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    await init_db()

# Endpoint for creating a new politician
@app.post("/politicians/", response_model=Politician, status_code=status.HTTP_201_CREATED)
async def create_politician_endpoint(
    politician_data: PoliticianCreate,
    session: AsyncSession = Depends(get_session)
):
    """
    Create a new politician.
    """
    politician = Politician(**politician_data.dict())
    operations = PoliticianOperations(session)
    status, message = await operations.create(politician)
    if not status:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT if "already exists" in message.lower() 
            else status.HTTP_400_BAD_REQUEST,
            detail=message
        )
    return politician

# Endpoint for getting list of politicians
@app.get("/politicians/", response_model=list[Politician], status_code=status.HTTP_200_OK)
async def read_politicians(
    skip: int = 0,
    limit: int = 10,
    session: AsyncSession = Depends(get_session)
):
    """
    Get list of politicians with pagination support.
    """
    operations = PoliticianOperations(session)
    return await operations.get_politicians(skip=skip, limit=limit)
