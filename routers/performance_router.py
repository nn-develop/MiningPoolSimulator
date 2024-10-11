from fastapi import APIRouter

router = APIRouter()

@router.get("/track")
async def track_performance():
    """
    Track the performance of miners (e.g., hashrate).
    
    Returns:
        dict: Message confirming performance tracking.
    """
    return {"message": "Track miner performance"}
