# Mining Pool API Endpoints

## List of API Endpoints

| **Endpoint**                     | **HTTP Method**  | **Description**                                                                                                                                                  |
|-----------------------------------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `/api/auth/login`                 | `POST`           | Authenticates miners using credentials (e.g., API keys or tokens). Input: miner credentials, Output: access token.                                                |
| `/api/auth/logout`                | `POST`           | Logs out the miner and invalidates the access token. Input: access token, Output: confirmation of logout.                                                         |
| `/api/transactions/aggregate`     | `POST`           | Aggregates transactions from the mempool and creates a block. Input: transactions, Output: assembled block.                                                       |
| `/api/work/distribute`            | `POST`           | Distributes work (block header and difficulty) to miners. Input: block header, difficulty, Output: assigned work for miners.                                       |
| `/api/work/submit`                | `POST`           | Receives mining results (hashes) from miners. Input: hash values from miners, Output: validated results and potential block solution.                              |
| `/api/block/validate`             | `POST`           | Validates a proposed block solution from miners. Input: block solution, Output: confirmation of whether the block meets the blockchain rules.                      |
| `/api/block/submit`               | `POST`           | Submits a validated block to the blockchain network. Input: valid block, Output: confirmation of block added to the blockchain.                                    |
| `/api/performance/track`          | `GET`            | Tracks the performance of miners (e.g., hashrate). Output: performance statistics for miners.                                                                     |
| `/api/rewards/distribute`         | `POST`           | Distributes mining rewards based on miner contributions. Input: valid block and miner performance stats, Output: distributed rewards.                              |
| `/api/miners/register`            | `POST`           | Registers miners in the pool (providing wallet addresses and identification). Input: miner details, Output: registration confirmation and assigned work.           |
| `/api/miners/stats`               | `GET`            | Retrieves miner performance statistics. Output: miner information about performance and contribution to mining.                                                   |

## API Endpoint Details

### 1. `/api/auth/login`
- **Method**: `POST`
- **Description**: Authenticates miners using their credentials. Miners submit their credentials (e.g., API key or username/password) and receive an access token.
- **Input**: Miner credentials (e.g., API key, username/password).
- **Output**: Access token for authenticated session.

### 2. `/api/auth/logout`
- **Method**: `POST`
- **Description**: Logs out the authenticated miner by invalidating their access token.
- **Input**: Access token.
- **Output**: Confirmation of logout.

### 3. `/api/transactions/aggregate`
- **Method**: `POST`
- **Description**: Aggregates pending transactions from the mempool and selects them to form a block. This block is prepared for miners to begin mining.
- **Input**: Transactions from mempool.
- **Output**: Assembled block.

### 4. `/api/work/distribute`
- **Method**: `POST`
- **Description**: Distributes work to miners, including block header, nonce, and difficulty target. The work is divided among miners to calculate the hash for solving the block.
- **Input**: Block header, difficulty target.
- **Output**: Work assigned to miners.

### 5. `/api/work/submit`
- **Method**: `POST`
- **Description**: Receives results (hash values) from miners. The pool validates these results to determine if the miner has successfully solved the block.
- **Input**: Hash values from miners.
- **Output**: Validated hash results and potential block solution.

### 6. `/api/block/validate`
- **Method**: `POST`
- **Description**: Validates whether the block solution meets the blockchain's difficulty target and is compliant with the rules of the network.
- **Input**: Proposed block solution.
- **Output**: Validation result (valid or invalid block).

### 7. `/api/block/submit`
- **Method**: `POST`
- **Description**: Submits a validated block to the blockchain network to be added to the blockchain. If successful, the block is added to the blockchain.
- **Input**: Valid block.
- **Output**: Confirmation that the block has been added to the blockchain.

### 8. `/api/performance/track`
- **Method**: `GET`
- **Description**: Tracks the hashrate and performance of miners in the pool. This endpoint provides information on each miner’s contribution to the pool.
- **Output**: Miner performance statistics (hashrate, contribution).

### 9. `/api/rewards/distribute`
- **Method**: `POST`
- **Description**: Distributes rewards to miners based on their contribution (hashrate) to the mining of a validated block.
- **Input**: Valid block, miner performance statistics.
- **Output**: Distributed rewards to miners.

### 10. `/api/miners/register`
- **Method**: `POST`
- **Description**: Registers new miners to the pool. Miners provide identification details, including wallet addresses and possibly an API key for authorization.
- **Input**: Miner identification details (wallet address, etc.).
- **Output**: Registration confirmation and assignment of mining work.

### 11. `/api/miners/stats`
- **Method**: `GET`
- **Description**: Provides statistics about individual miners, such as their hashrate, contribution to mining efforts, and their earnings from mining rewards.
- **Output**: Miner performance statistics.

