from fastapi import FastAPI, HTTPException, Header
import time

app = FastAPI()

# Simulated mining data
miners = {}
pool_reward = 100.0  # Simulated total reward

@app.post("/connect")
async def connect(miner_id: str, hash_rate: float, authorization: str = Header(None)) -> dict:
    """
    Connect a miner to the mining pool.
    
    Args:
        miner_id (str): Unique identifier of the miner.
        hash_rate (float): Hash rate of the miner.
        authorization (str): Authorization token (Bearer token).

    Returns:
        dict: Status of the connection and task for the miner.
    """
    if authorization != "Bearer your_secure_api_key":
        raise HTTPException(status_code=403, detail="Invalid or missing API key.")
    
    if miner_id not in miners:
        miners[miner_id] = {"hash_rate": hash_rate, "total_shares": 0, "reward": 0.0, "active": True}
    return {"status": "connected", "task": "Mine for reward"}

@app.post("/submit_share")
async def submit_share(miner_id: str, share_data: str, timestamp: float, authorization: str = Header(None)) -> dict:
    """
    Submit a share for reward calculation.
    
    Args:
        miner_id (str): Unique identifier of the miner.
        share_data (str): Submitted mining share data.
        timestamp (float): Submission timestamp.
        authorization (str): Authorization token (Bearer token).

    Returns:
        dict: Status of share submission and reward amount.
    """
    if authorization != "Bearer your_secure_api_key":
        raise HTTPException(status_code=403, detail="Invalid or missing API key.")
    
    if miner_id not in miners or not miners[miner_id]["active"]:
        raise HTTPException(status_code=404, detail="Miner not found or inactive.")
    
    miners[miner_id]["total_shares"] += 1
    
    reward_for_share = 0.01
    miners[miner_id]["reward"] += reward_for_share
    
    return {"status": "accepted", "reward": reward_for_share}

@app.get("/reward_update")
async def reward_update(miner_id: str, authorization: str = Header(None)) -> dict:
    """
    Get the current reward status for a miner.
    
    Args:
        miner_id (str): Unique identifier of the miner.
        authorization (str): Authorization token (Bearer token).

    Returns:
        dict: Current reward information for the miner.
    """
    if authorization != "Bearer your_secure_api_key":
        raise HTTPException(status_code=403, detail="Invalid or missing API key.")
    
    if miner_id not in miners:
        raise HTTPException(status_code=404, detail="Miner not found.")
    
    return {"miner_id": miner_id, "reward": miners[miner_id]["reward"]}
