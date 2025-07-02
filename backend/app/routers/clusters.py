from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .. import schemas, models
from ..db.session import get_db

router = APIRouter(tags=["clusters"])


@router.get("/clusters", response_model=list[schemas.Cluster])
def read_clusters(db: Session = Depends(get_db)):
    return db.query(models.Cluster).all()


@router.post("/clusters", response_model=schemas.Cluster)
def create_cluster(cluster: schemas.ClusterCreate, db: Session = Depends(get_db)):
    db_cluster = models.Cluster(name=cluster.name, description=cluster.description)
    db.add(db_cluster)
    db.commit()
    db.refresh(db_cluster)
    return db_cluster


@router.get("/clusters/{cluster_id}", response_model=schemas.Cluster)
def get_cluster(cluster_id: str, db: Session = Depends(get_db)):
    cluster = db.get(models.Cluster, cluster_id)
    if not cluster:
        raise HTTPException(status_code=404, detail="Cluster not found")
    return cluster


@router.delete("/clusters/{cluster_id}")
def delete_cluster(cluster_id: str, db: Session = Depends(get_db)):
    cluster = db.get(models.Cluster, cluster_id)
    if not cluster:
        raise HTTPException(status_code=404, detail="Cluster not found")
    db.delete(cluster)
    db.commit()
    return {"ok": True}
