from fastapi import APIRouter

router = APIRouter()

@router.post("/aggregate")
async def aggregate_transactions():
    """
    Aggregate transactions from the mempool and create a block.
    
    Returns:
        dict: Message confirming transaction aggregation.
    """
    return {"message": "Aggregate transactions"}
