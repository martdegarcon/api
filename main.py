from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel.ext.asyncio.session import AsyncSession
from database.politician.schemes import Politician, PoliticianCreate
from database.politician.models import PoliticianOperations
from database_connection import get_session, init_db
from routers.user import router as user_router
from routers.user_group import router as user_group_router
from routers.political_party import router as political_party_router
from routers.political_party_position import router as political_party_position_router
from routers.political_party_member import router as political_party_member_router
from routers.ministry import router as ministry_router
from routers.ministry_position import router as ministry_position_router
from routers.ministry_member import router as ministry_member_router
from routers.politician_education import router as politician_education_router
from routers.dataset_university import router as dataset_university_router
from routers.dataset_province import router as dataset_province_router
from routers.government import router as government_router
from routers.government_position import router as government_position_router
from routers.dataset_gender import router as dataset_gender_router
from routers.politician import router as politician_router

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

# Register routers
app.include_router(user_router)
app.include_router(user_group_router)
app.include_router(political_party_router)
app.include_router(political_party_position_router)
app.include_router(political_party_member_router)
app.include_router(ministry_router)
app.include_router(ministry_position_router)
app.include_router(ministry_member_router)
app.include_router(politician_education_router)
app.include_router(dataset_university_router)
app.include_router(dataset_province_router)
app.include_router(government_router)
app.include_router(government_position_router)
app.include_router(dataset_gender_router)
app.include_router(politician_router)

# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    await init_db()
