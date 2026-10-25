
import os
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# 1. Configuration de la connexion PostgreSQL
# Il lit la variable d'environnement DATABASE_URL, ou utilise une valeur par défaut en local
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://admin:secretpassword@db:5432/shopflow_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 2. Modèle de la table de base de données (SQLAlchemy)
class OrderDB(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    product = Column(String, index=True)
    quantity = Column(Integer)
    price = Column(Float)

# 3. Création automatique de la table "orders" au démarrage de l'API
Base.metadata.create_all(bind=engine)

app = FastAPI()

# 4. Modèles Pydantic (Validation des données entrantes/sortantes)
class OrderCreate(BaseModel):
    product: str
    quantity: int
    price: float

class OrderResponse(OrderCreate):
    id: int
    class Config:
        from_attributes = True

# 5. Dépendance pour ouvrir/fermer une session DB proprement à chaque requête
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 6. Les routes de l'API
@app.post("/api/orders", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    db_order = OrderDB(**order.model_dump())
    db.add(db_order)
    db.commit()
    db.refresh(db_order) # Récupère l'ID généré par PostgreSQL
    return db_order

@app.get("/api/orders", response_model=list[OrderResponse])
def get_orders(db: Session = Depends(get_db)):
    return db.query(OrderDB).all()
