```pseudocode
# Function 1: Transaction Aggregation
function aggregate_transactions(mempool):
    block = []
    # Select transactions based on fees and block size
    for transaction in mempool:
        if transaction.fee >= minimum_fee and block.size() < maximum_block_size:
            block.add(transaction)
    return block  # Output: Assembled block

# Function 2: Work Distribution
function distribute_work(block_header, difficulty):
    work_units = []
    # Divide the work into smaller tasks for miners
    for miner in miners:
        work = create_work(miner, block_header, difficulty)
        work_units.add(work)
    return work_units  # Output: Assigned work to miners

# Function 3: Receive Miner Results
function receive_results(miner_results):
    valid_results = []
    # Validate the results from miners
    for result in miner_results:
        if validate_hash(result.hash, result.difficulty):
            valid_results.add(result)
    return valid_results  # Output: Validated results (potential block solutions)

# Function 4: Block Validation
function validate_block(block_solution):
    # Check if the solution meets blockchain rules
    if block_solution.hash meets difficulty_target:
        return True  # Block is valid
    else:
        return False  # Block is invalid

# Function 5: Blockchain Communication
function submit_block_to_network(block):
    # Submit the valid block to the blockchain network
    network_response = blockchain_network.submit(block)
    if network_response == "success":
        return "Block added to blockchain"  # Output: Block added
    else:
        return "Block rejected"

# Function 6: Performance Tracking
function track_performance(miners):
    performance_stats = []
    # Track hashrate and contribution of each miner
    for miner in miners:
        performance_stats.add(miner.id, miner.hashrate)
    return performance_stats  # Output: Miner performance statistics

# Function 7: Reward Distribution
function distribute_rewards(valid_block, miner_stats):
    rewards = []
    total_reward = calculate_block_reward(valid_block)
    # Distribute rewards based on miner contribution (hashrate)
    for miner in miner_stats:
        miner_reward = (miner.hashrate / total_network_hashrate) * total_reward
        rewards.add(miner.id, miner_reward)
    return rewards  # Output: Distributed rewards

# Function 8: Miner Communication
function communicate_with_miners(miner_requests):
    miner_stats = []
    # Record miner identification and their work requests
    for miner in miner_requests:
        miner_stats.add(miner.id, miner.wallet_address)
    return miner_stats  # Output: Miner statistics and work assignment

# Main mining pool workflow
function mining_pool_workflow(mempool, block_header, difficulty):
    # Step 1: Aggregate transactions into a block
    block = aggregate_transactions(mempool)
    
    # Step 2: Distribute work to miners
    work_units = distribute_work(block_header, difficulty)
    
    # Step 3: Receive miner results
    miner_results = receive_results(work_units)
    
    # Step 4: Validate the block if a solution is found
    for result in miner_results:
        if validate_block(result):
            # Step 5: Submit the valid block to the blockchain
            network_response = submit_block_to_network(result)
            
            # Step 6: Track miner performance
            miner_stats = track_performance(miners)
            
            # Step 7: Distribute rewards to miners
            rewards = distribute_rewards(result, miner_stats)
            return network_response, rewards
    return "No valid block found in this round"
